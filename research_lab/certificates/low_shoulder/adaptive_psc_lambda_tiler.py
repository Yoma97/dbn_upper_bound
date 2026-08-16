from decimal import Decimal,getcontext
import subprocess,re,json,time,sys,csv,hashlib
from concurrent.futures import ThreadPoolExecutor
getcontext().prec=80
if len(sys.argv)<8:
    print('usage: tiler EXE t0 t1 lam0 lam1 max_depth K prefix [workers]',file=sys.stderr);sys.exit(2)
EXE=sys.argv[1]; T0=Decimal(sys.argv[2]);T1=Decimal(sys.argv[3]);L0=Decimal(sys.argv[4]);L1=Decimal(sys.argv[5]);MAX=int(sys.argv[6]);K=sys.argv[7];PREFIX=sys.argv[8] if len(sys.argv)>8 else 'psc';WORKERS=int(sys.argv[9]) if len(sys.argv)>9 else 16
def s(x): return format(x,'f')
def sha(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()
def run(b):
    t0,t1,l0,l1,d=b
    p=subprocess.run([EXE,s(t0),s(t1),s(l0),s(l1),'0.1',K],text=True,capture_output=True)
    out=p.stdout
    m=re.search(r'RESULT status=([A-Z_]+)(?: pass=(\d))?',out)
    status=m.group(1) if m else 'PARSE'
    def field(name):
        z=re.search(r'^'+re.escape(name)+r'\s+([^\s]+)',out,re.M)
        return Decimal(z.group(1)) if z else None
    return status,{k:field(k) for k in ['A0_upper','A1_upper','S0_lower','phi_lower','d_upper','eAB_upper','eC_upper','jump_upper','E0_upper','ratio_upper','E1_upper','Y_lower','lhs_lower','margin_lower']},out,p.returncode
def split4(b):
    t0,t1,l0,l1,d=b;tm=(t0+t1)/2;lm=(l0+l1)/2;nd=d+1
    return [(t0,tm,l0,lm,nd),(t0,tm,lm,l1,nd),(tm,t1,l0,lm,nd),(tm,t1,lm,l1,nd)]
cur=[(T0,T1,L0,L1,0)];cert=[];un=[];levels=[];start=time.time()
for level in range(MAX+1):
    nxt=[];counts={};minm=None
    with ThreadPoolExecutor(max_workers=WORKERS) as ex: outs=list(ex.map(run,cur))
    for b,(st,vals,out,rc) in zip(cur,outs):
        counts[st]=counts.get(st,0)+1
        if st=='CERTIFIED':
            cert.append((b,vals));ma=vals['margin_lower'];minm=ma if minm is None or ma<minm else minm
        elif level<MAX: nxt.extend(split4(b))
        else: un.append((b,st,vals,out,rc))
    levels.append({'level':level,'tested':len(cur),'certified':counts.get('CERTIFIED',0),'statuses':counts,'min_margin_this_level':None if minm is None else str(minm)})
    print(levels[-1],flush=True)
    if not nxt: break
    cur=nxt
area=(T1-T0)*(L1-L0);ca=sum((b[1]-b[0])*(b[3]-b[2]) for b,v in cert);ua=sum((b[1]-b[0])*(b[3]-b[2]) for b,st,v,o,rc in un)
assert ca+ua==area,(ca,ua,area)
cert_path=PREFIX+'_certified.csv';un_path=PREFIX+'_unresolved.csv';sum_path=PREFIX+'_summary.json'
fields=['A0_upper','A1_upper','S0_lower','phi_lower','d_upper','eAB_upper','eC_upper','jump_upper','E0_upper','ratio_upper','E1_upper','Y_lower','lhs_lower','margin_lower']
with open(cert_path,'w',newline='') as f:
    w=csv.writer(f);w.writerow(['tlo','thi','lamlo','lamhi','depth']+fields)
    for b,v in cert:w.writerow([s(z) if isinstance(z,Decimal) else z for z in b]+[str(v[k]) for k in fields])
with open(un_path,'w',newline='') as f:
    w=csv.writer(f);w.writerow(['tlo','thi','lamlo','lamhi','depth','status','returncode','margin'])
    for b,st,v,o,rc in un:w.writerow([s(z) if isinstance(z,Decimal) else z for z in b]+[st,rc,'' if v['margin_lower'] is None else str(v['margin_lower'])])
res={'domain':{'t':[s(T0),s(T1)],'lambda':[s(L0),s(L1)],'rho':'0.1'},'max_depth':MAX,'K':K,'levels':levels,'certified_leaves':len(cert),'unresolved':len(un),'area_exact':str(area),'cert_area_exact':str(ca),'un_area_exact':str(ua),'fraction_exact':str(ca/area),'min_margin_projection':str(min((v['margin_lower'] for b,v in cert),default=Decimal('NaN'))),'elapsed_seconds':time.time()-start,'executable':EXE}
with open(sum_path,'w') as f:json.dump(res,f,indent=2)
res['certified_csv_sha256']=sha(cert_path);res['unresolved_csv_sha256']=sha(un_path)
with open(sum_path,'w') as f:json.dump(res,f,indent=2)
print(json.dumps(res,indent=2))
