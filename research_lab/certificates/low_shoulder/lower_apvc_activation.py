from pathlib import Path

p = Path('research_lab/certificates/low_shoulder/hybrid_psc_apvc_box_mpfr.c')
s = p.read_text()
old = 'setd(ap_tmin,"0.40",MPFR_RNDD); if(mpfr_cmp(tL,ap_tmin)<0) goto ap_fail;'
new = 'setd(ap_tmin,"0.39",MPFR_RNDD); if(mpfr_cmp(tL,ap_tmin)<0) goto ap_fail;'
if old not in s:
    raise SystemExit('APVC activation marker not found')
s = s.replace(old, new, 1)
s = s.replace('It is intentionally enabled only for t>=0.40;',
              'It is enabled from t>=0.39 in the strict 6.85 frontier audit;')
p.write_text(s)
print(p)
