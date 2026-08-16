from pathlib import Path

p=Path('research_lab/certificates/low_shoulder/hybrid_psc_apvc_box_mpfr.c')
s=p.read_text()
old="mpfr_log(logN,nN,MPFR_RNDU);mpfr_mul(tmp,Tup,logN,MPFR_RNDU); if(mpfr_cmp(phi,tmp)<0) goto ap_fail; /* Phi >= T log N */"
new="mpfr_log(logN,nN,MPFR_RNDU);mpfr_mul(tmp,Tup,logN,MPFR_RNDU);mpfr_sub(oldmargin,tmp,phi,MPFR_RNDU);if(mpfr_sgn(oldmargin)<0)zero(oldmargin); /* delta_U=max(T_U log N_U-Phi_L,0) */"
if old not in s:
    raise SystemExit('hard slope marker not found')
s=s.replace(old,new,1)
old2="mpfr_mul(apcore,phi,Qap,MPFR_RNDD);mpfr_mul(tmp,PhiU,A0,MPFR_RNDU);mpfr_sub(apcore,apcore,tmp,MPFR_RNDD);mpfr_mul(tmp,cL,A1L,MPFR_RNDD);"
new2="mpfr_mul(apcore,phi,Qap,MPFR_RNDD);mpfr_mul_ui(tmp,oldmargin,2,MPFR_RNDU);mpfr_add(tmp,tmp,PhiU,MPFR_RNDU);mpfr_mul(tmp,tmp,A0,MPFR_RNDU);mpfr_sub(apcore,apcore,tmp,MPFR_RNDD);mpfr_mul(tmp,cL,A1L,MPFR_RNDD);"
if old2 not in s:
    raise SystemExit('APVC core marker not found')
s=s.replace(old2,new2,1)
p.write_text(s)
print(p)
