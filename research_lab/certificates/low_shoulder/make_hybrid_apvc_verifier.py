from pathlib import Path

src_path = Path('research_lab/certificates/low_shoulder/convex_tail_psc_box_mpfr.c')
out_path = Path('research_lab/certificates/low_shoulder/hybrid_psc_apvc_box_mpfr.c')
s = src_path.read_text()

marker = 'int main(int argc,char**argv){'
if marker not in s:
    raise SystemExit('main marker not found')

helper = r'''
extern unsigned long mpfr_get_ui(mpfr_srcptr,mpfr_rnd_t);

/* Directed lower enclosure for one true heat amplitude on a parameter box.
   tL is a lower bound for t and sigmaU an upper bound for sigma. */
static void F_lower(mpfr_t out, unsigned long n, mpfr_srcptr tL, mpfr_srcptr sigmaU){
 mpfr_t nn,lL,lU,pos,prod,expo; ini(nn);ini(lL);ini(lU);ini(pos);ini(prod);ini(expo);
 mpfr_set_ui(nn,n,MPFR_RNDN); mpfr_log(lL,nn,MPFR_RNDD); mpfr_log(lU,nn,MPFR_RNDU);
 mpfr_sqr(pos,lL,MPFR_RNDD); mpfr_mul(pos,pos,tL,MPFR_RNDD); mpfr_div_ui(pos,pos,4,MPFR_RNDD);
 mpfr_mul(prod,sigmaU,lU,MPFR_RNDU); mpfr_sub(expo,pos,prod,MPFR_RNDD); mpfr_exp(out,expo,MPFR_RNDD);
 mpfr_clear(nn);mpfr_clear(lL);mpfr_clear(lU);mpfr_clear(pos);mpfr_clear(prod);mpfr_clear(expo);
}

/* Lower bound for A1 from a finite head known to be present for every point
   in the box.  The omitted positive tail only strengthens the lower bound. */
static int A1_head_lower(mpfr_t out, mpfr_srcptr tL, mpfr_srcptr sigmaU,
                         mpfr_srcptr nlow, unsigned long K){
 if(mpfr_cmp_ui(nlow,K)<=0) return 0;
 mpfr_t a,nn,lL,term; ini(a);ini(nn);ini(lL);ini(term); zero(out);
 for(unsigned long n=2;n<=K;n++){
   F_lower(a,n,tL,sigmaU); mpfr_set_ui(nn,n,MPFR_RNDN); mpfr_log(lL,nn,MPFR_RNDD);
   mpfr_mul(term,a,lL,MPFR_RNDD); mpfr_add(out,out,term,MPFR_RNDD);
 }
 mpfr_clear(a);mpfr_clear(nn);mpfr_clear(lL);mpfr_clear(term); return 1;
}

'''
s = s.replace(marker, helper + marker, 1)

start = s.find(' if(mpfr_cmp_ui(S0,0)<=0){printf("RESULT status=TRIANGLE_SIGN')
if start < 0:
    raise SystemExit('old PSC tail marker not found')

new_tail = r''' /* First gate: the previously certified scalar PSC. */
 int psc_valid=1,psc_pass=0;
 if(mpfr_cmp_ui(S0,0)<=0) psc_valid=0;
 if(psc_valid){
   mpfr_div_ui(halfE,E0,2,MPFR_RNDU); mpfr_sqr(rad,S0,MPFR_RNDD); mpfr_sqr(tmp,halfE,MPFR_RNDU); mpfr_sub(rad,rad,tmp,MPFR_RNDD);
   if(mpfr_cmp_ui(rad,0)<=0) psc_valid=0;
 }
 if(psc_valid){
   mpfr_sqrt(Y,rad,MPFR_RNDD); mpfr_mul(core,phi,Y,MPFR_RNDD); mpfr_mul(tmp,d,A1,MPFR_RNDU); mpfr_sub(core,core,tmp,MPFR_RNDD); mpfr_mul_ui(lhs,core,2,MPFR_RNDD); mpfr_sub(margin,lhs,E1,MPFR_RNDD);
   psc_pass=mpfr_cmp_ui(margin,0)>0;
 }
 if(psc_pass){
   printf("HYBRID PSC/APVC BOX PREC=%d K=%lu\n",PREC,K);pr("A0_upper",A0,MPFR_RNDU);pr("A1_upper",A1,MPFR_RNDU);pr("S0_lower",S0,MPFR_RNDD);pr("phi_lower",phi,MPFR_RNDD);pr("d_upper",d,MPFR_RNDU);pr("eAB_upper",eAB,MPFR_RNDU);pr("eC_upper",eC,MPFR_RNDU);pr("jump_upper",jump,MPFR_RNDU);pr("E0_upper",E0,MPFR_RNDU);pr("ratio_upper",R,MPFR_RNDU);pr("E1_upper",E1,MPFR_RNDU);pr("Y_lower",Y,MPFR_RNDD);pr("lhs_lower",lhs,MPFR_RNDD);pr("margin_lower",margin,MPFR_RNDD);printf("RESULT status=CERTIFIED pass=1 mechanism=PSC\n");return 0;
 }

 /* Second gate: Round-74 n=1 anchored phase-velocity certificate.
    It is intentionally enabled only for t>=0.40; the old PSC handles the
    singular small-time region more naturally and this also keeps the cutoff
    integer safely moderate. */
 mpfr_t ap_tmin,sigmaU,A1L,PhiU,Tup,Tlo,sigxU,nroot,nN,logN,Uap,Qap,cL,apcore,apmargin,oldmargin;
 ini(ap_tmin);ini(sigmaU);ini(A1L);ini(PhiU);ini(Tup);ini(Tlo);ini(sigxU);ini(nroot);ini(nN);ini(logN);ini(Uap);ini(Qap);ini(cL);ini(apcore);ini(apmargin);ini(oldmargin);
 setd(ap_tmin,"0.40",MPFR_RNDD); if(mpfr_cmp(tL,ap_tmin)<0) goto ap_fail;

 /* sigma <= 1/2 + lambda/4 because delta_A(x)<=0. */
 mpfr_div_ui(sigmaU,lbU,4,MPFR_RNDU);setd(tmp,"0.5",MPFR_RNDU);mpfr_add(sigmaU,sigmaU,tmp,MPFR_RNDU);
 if(!A1_head_lower(A1L,tL,sigmaU,nlow,K)) goto ap_fail;

 /* sigma_x upper and T=-tau_x bounds.  Cbd,Dbd are already rigorous
    positive upper enclosures from the old verifier. */
 mpfr_mul(sigxU,tU,Dbd,MPFR_RNDU);mpfr_div_ui(sigxU,sigxU,4,MPFR_RNDU);
 setd(Tlo,"0.5",MPFR_RNDD);mpfr_mul(Tup,tU,Cbd,MPFR_RNDU);mpfr_div_ui(Tup,Tup,4,MPFR_RNDU);setd(tmp,"0.5",MPFR_RNDU);mpfr_add(Tup,Tup,tmp,MPFR_RNDU);
 mpfr_sub(cL,Tlo,sigxU,MPFR_RNDD); if(mpfr_cmp_ui(cL,0)<=0) goto ap_fail;

 /* Phi upper: A/2 <= L/4 and (t/4)(A C - B D) is bounded using
    A<=L/2, C<=Cbd, |B|<=pi/4+3/x, D<=Dbd. */
 mpfr_div_ui(PhiU,Lmax,4,MPFR_RNDU);
 mpfr_div_ui(tmp,Lmax,2,MPFR_RNDU);mpfr_mul(tmp,tmp,Cbd,MPFR_RNDU);
 mpfr_div_ui(tmp2,piU,4,MPFR_RNDU);setd(tmp3,"3",MPFR_RNDU);mpfr_div(tmp3,tmp3,xcmin,MPFR_RNDU);mpfr_add(tmp2,tmp2,tmp3,MPFR_RNDU);mpfr_mul(tmp2,tmp2,Dbd,MPFR_RNDU);mpfr_add(tmp,tmp,tmp2,MPFR_RNDU);mpfr_mul(tmp,tmp,tU,MPFR_RNDU);mpfr_div_ui(tmp,tmp,4,MPFR_RNDU);mpfr_add(PhiU,PhiU,tmp,MPFR_RNDU);

 /* Exact integer upper bound for the moving cutoff over the box. */
 mpfr_exp(nroot,Lmax,MPFR_RNDU);mpfr_div_ui(tmp,tU,16,MPFR_RNDU);mpfr_add(nroot,nroot,tmp,MPFR_RNDU);mpfr_sqrt(nroot,nroot,MPFR_RNDU);
 { unsigned long Nmax=mpfr_get_ui(nroot,MPFR_RNDD); if(Nmax<2) goto ap_fail; mpfr_set_ui(nN,Nmax,MPFR_RNDN); }
 mpfr_log(logN,nN,MPFR_RNDU);mpfr_mul(tmp,Tup,logN,MPFR_RNDU); if(mpfr_cmp(phi,tmp)<0) goto ap_fail; /* Phi >= T log N */

 /* U=A0+E0/2 <1 and Q=sqrt(1-U^2). */
 mpfr_div_ui(tmp,E0,2,MPFR_RNDU);mpfr_add(Uap,A0,tmp,MPFR_RNDU); if(mpfr_cmp_ui(Uap,1)>=0) goto ap_fail;
 mpfr_sqr(tmp,Uap,MPFR_RNDU);one(tmp2);mpfr_sub(tmp2,tmp2,tmp,MPFR_RNDD); if(mpfr_cmp_ui(tmp2,0)<=0) goto ap_fail;mpfr_sqrt(Qap,tmp2,MPFR_RNDD);

 /* APVC-linear lower margin:
      2[Phi_L Q - Phi_U A0_U + (T_L-sigmax_U) A1_L] - E1_U. */
 mpfr_mul(apcore,phi,Qap,MPFR_RNDD);mpfr_mul(tmp,PhiU,A0,MPFR_RNDU);mpfr_sub(apcore,apcore,tmp,MPFR_RNDD);mpfr_mul(tmp,cL,A1L,MPFR_RNDD);mpfr_add(apcore,apcore,tmp,MPFR_RNDD);mpfr_mul_ui(apmargin,apcore,2,MPFR_RNDD);mpfr_sub(apmargin,apmargin,E1,MPFR_RNDD);
 if(mpfr_cmp_ui(apmargin,0)>0){
   mpfr_set(margin,apmargin,MPFR_RNDD);mpfr_add(lhs,apmargin,E1,MPFR_RNDD);
   printf("HYBRID PSC/APVC BOX PREC=%d K=%lu\n",PREC,K);pr("A0_upper",A0,MPFR_RNDU);pr("A1_upper",A1,MPFR_RNDU);pr("A1_lower",A1L,MPFR_RNDD);pr("S0_lower",S0,MPFR_RNDD);pr("phi_lower",phi,MPFR_RNDD);pr("phi_upper",PhiU,MPFR_RNDU);pr("d_upper",d,MPFR_RNDU);pr("eAB_upper",eAB,MPFR_RNDU);pr("eC_upper",eC,MPFR_RNDU);pr("jump_upper",jump,MPFR_RNDU);pr("E0_upper",E0,MPFR_RNDU);pr("ratio_upper",R,MPFR_RNDU);pr("E1_upper",E1,MPFR_RNDU);pr("Y_lower",Qap,MPFR_RNDD);pr("lhs_lower",lhs,MPFR_RNDD);pr("margin_lower",margin,MPFR_RNDD);printf("RESULT status=CERTIFIED pass=1 mechanism=APVC\n");return 0;
 }

ap_fail:
 /* For unresolved diagnostics retain the better of the two available lower
    margins when APVC was actually evaluated; otherwise preserve PSC output. */
 if(!psc_valid){zero(Y);zero(lhs);setd(margin,"-1e100",MPFR_RNDD);} 
 printf("HYBRID PSC/APVC BOX PREC=%d K=%lu\n",PREC,K);pr("A0_upper",A0,MPFR_RNDU);pr("A1_upper",A1,MPFR_RNDU);pr("S0_lower",S0,MPFR_RNDD);pr("phi_lower",phi,MPFR_RNDD);pr("d_upper",d,MPFR_RNDU);pr("eAB_upper",eAB,MPFR_RNDU);pr("eC_upper",eC,MPFR_RNDU);pr("jump_upper",jump,MPFR_RNDU);pr("E0_upper",E0,MPFR_RNDU);pr("ratio_upper",R,MPFR_RNDU);pr("E1_upper",E1,MPFR_RNDU);pr("Y_lower",Y,MPFR_RNDD);pr("lhs_lower",lhs,MPFR_RNDD);pr("margin_lower",margin,MPFR_RNDD);printf("RESULT status=PSC_CORE pass=0 mechanism=NONE\n");return 1;
}
'''

s = s[:start] + new_tail
out_path.write_text(s)
print(out_path)
