from pathlib import Path

p=Path('research_lab/certificates/low_shoulder/hybrid_psc_apvc_box_mpfr.c')
s=p.read_text()

old = '''mpfr_log(logN,nN,MPFR_RNDU);mpfr_mul(tmp,Tup,logN,MPFR_RNDU);mpfr_sub(oldmargin,tmp,phi,MPFR_RNDU);if(mpfr_sgn(oldmargin)<0)zero(oldmargin); /* delta_U=max(T_U log N_U-Phi_L,0) */'''
new = '''mpfr_log(logN,nN,MPFR_RNDU);
 /* Round-75 common convex secant endpoint defect.
    D_U=max(T_U L_U-Phi_L, Phi_U-T_L L_U, 0). */
 mpfr_mul(tmp,Tup,logN,MPFR_RNDU);mpfr_sub(oldmargin,tmp,phi,MPFR_RNDU);if(mpfr_sgn(oldmargin)<0)zero(oldmargin);
 mpfr_mul(tmp,Tlo,logN,MPFR_RNDD);mpfr_sub(tmp,PhiU,tmp,MPFR_RNDU);if(mpfr_sgn(tmp)<0)zero(tmp);if(mpfr_cmp(tmp,oldmargin)>0)mpfr_mul_ui(oldmargin,tmp,1,MPFR_RNDU);
 /* Omega_U=sqrt((sigx_U L_U)^2+D_U^2). */
 mpfr_mul(tmp,sigxU,logN,MPFR_RNDU);mpfr_sqr(tmp,tmp,MPFR_RNDU);mpfr_sqr(tmp2,oldmargin,MPFR_RNDU);mpfr_add(tmp,tmp,tmp2,MPFR_RNDU);mpfr_sqrt(oldmargin,tmp,MPFR_RNDU);
 /* This frontier uses the favorable negative-slope secant. If the certified
    endpoint norm is not below Phi_U, leave the leaf to subdivision/PSC. */
 if(mpfr_cmp(oldmargin,PhiU)>=0) goto ap_fail;
 /* m_U=(Omega_U-Phi_U)/L_U <0.  Division by the upper L_U rounds upward
    (less negative), hence preserves a common upper secant slope. */
 mpfr_sub(tmp,oldmargin,PhiU,MPFR_RNDU);mpfr_div(oldmargin,tmp,logN,MPFR_RNDU);'''
if old not in s:
    raise SystemExit('soft defect block not found')
s=s.replace(old,new,1)

old2 = '''mpfr_mul(apcore,phi,Qap,MPFR_RNDD);mpfr_mul_ui(tmp,oldmargin,2,MPFR_RNDU);mpfr_add(tmp,tmp,PhiU,MPFR_RNDU);mpfr_mul(tmp,tmp,A0,MPFR_RNDU);mpfr_sub(apcore,apcore,tmp,MPFR_RNDD);mpfr_mul(tmp,cL,A1L,MPFR_RNDD);mpfr_add(apcore,apcore,tmp,MPFR_RNDD);mpfr_mul_ui(apmargin,apcore,2,MPFR_RNDD);mpfr_sub(apmargin,apmargin,E1,MPFR_RNDD);'''
new2 = '''/* Round-75 secant tail: B1 <= Phi_U A0_U + m_U A1_L because m_U<0. */
 mpfr_mul(apcore,phi,Qap,MPFR_RNDD);
 mpfr_mul(tmp,PhiU,A0,MPFR_RNDU);mpfr_mul(tmp2,oldmargin,A1L,MPFR_RNDU);mpfr_add(tmp,tmp,tmp2,MPFR_RNDU);
 mpfr_sub(apcore,apcore,tmp,MPFR_RNDD);mpfr_mul_ui(apmargin,apcore,2,MPFR_RNDD);mpfr_sub(apmargin,apmargin,E1,MPFR_RNDD);'''
if old2 not in s:
    raise SystemExit('soft APVC core block not found')
s=s.replace(old2,new2,1)
p.write_text(s)
print(p)
