from pathlib import Path

src_path=Path('research_lab/certificates/low_shoulder/convex_tail_psc_box_mpfr.c')
out_path=Path('research_lab/certificates/low_shoulder/joint_ellipse_psc_box_mpfr.c')
s=src_path.read_text()

start=s.find(' if(mpfr_cmp_ui(S0,0)<=0){printf("RESULT status=TRIANGLE_SIGN')
if start<0:
    raise SystemExit('old PSC tail marker not found')

new_tail=r''' /* Gate 1: the established scalar PSC. */
 int psc_valid=1,psc_pass=0;
 if(mpfr_cmp_ui(S0,0)<=0) psc_valid=0;
 if(psc_valid){
   mpfr_div_ui(halfE,E0,2,MPFR_RNDU);mpfr_sqr(rad,S0,MPFR_RNDD);mpfr_sqr(tmp,halfE,MPFR_RNDU);mpfr_sub(rad,rad,tmp,MPFR_RNDD);
   if(mpfr_cmp_ui(rad,0)<=0) psc_valid=0;
 }
 if(psc_valid){
   mpfr_sqrt(Y,rad,MPFR_RNDD);mpfr_mul(core,phi,Y,MPFR_RNDD);mpfr_mul(tmp,d,A1,MPFR_RNDU);mpfr_sub(core,core,tmp,MPFR_RNDD);mpfr_mul_ui(lhs,core,2,MPFR_RNDD);mpfr_sub(margin,lhs,E1,MPFR_RNDD);psc_pass=mpfr_cmp_ui(margin,0)>0;
 }
 if(psc_pass){
   printf("JOINT-ELLIPSE PSC BOX PREC=%d K=%lu\n",PREC,K);pr("A0_upper",A0,MPFR_RNDU);pr("A1_upper",A1,MPFR_RNDU);pr("phi_lower",phi,MPFR_RNDD);pr("E0_upper",E0,MPFR_RNDU);pr("E1_upper",E1,MPFR_RNDU);pr("margin_lower",margin,MPFR_RNDD);printf("RESULT status=CERTIFIED pass=1 mechanism=PSC\n");return 0;
 }

 /* Gate 2: Round-80 Joint Elliptic Collision Certificate. */
 mpfr_t jsigx,jTup,jnroot,jlogN,jq,jtwoPhi,jratio,jerr,jrhs,jmargin;
 ini(jsigx);ini(jTup);ini(jnroot);ini(jlogN);ini(jq);ini(jtwoPhi);ini(jratio);ini(jerr);ini(jrhs);ini(jmargin);
 if(mpfr_cmp_ui(phi,0)<=0) goto jecc_fail;

 /* sigma_x <= t_U D_U/4 and T=-tau_x <= 1/2+t_U C_U/4. */
 mpfr_mul(jsigx,tU,Dbd,MPFR_RNDU);mpfr_div_ui(jsigx,jsigx,4,MPFR_RNDU);
 mpfr_mul(jTup,tU,Cbd,MPFR_RNDU);mpfr_div_ui(jTup,jTup,4,MPFR_RNDU);setd(tmp,"0.5",MPFR_RNDU);mpfr_add(jTup,jTup,tmp,MPFR_RNDU);

 /* Continuous upper cutoff is sufficient: log n <= log sqrt(exp(Lmax)+tU/16). */
 mpfr_exp(jnroot,Lmax,MPFR_RNDU);mpfr_div_ui(tmp,tU,16,MPFR_RNDU);mpfr_add(jnroot,jnroot,tmp,MPFR_RNDU);mpfr_sqrt(jnroot,jnroot,MPFR_RNDU);mpfr_log(jlogN,jnroot,MPFR_RNDU);

 /* Verify q_n=T log n/Phi <=2 uniformly. */
 mpfr_mul(jq,jTup,jlogN,MPFR_RNDU);mpfr_mul_ui(jtwoPhi,phi,2,MPFR_RNDD);if(mpfr_cmp(jq,jtwoPhi)>0) goto jecc_fail;

 /* A0 + (sigma_x/Phi) A1. */
 mpfr_div(jratio,jsigx,phi,MPFR_RNDU);mpfr_mul(jrhs,jratio,A1,MPFR_RNDU);mpfr_add(jrhs,jrhs,A0,MPFR_RNDU);

 /* Collision error radius: 1/2 sqrt(E0^2+(E1/Phi)^2). */
 mpfr_sqr(jerr,E0,MPFR_RNDU);mpfr_div(tmp,E1,phi,MPFR_RNDU);mpfr_sqr(tmp,tmp,MPFR_RNDU);mpfr_add(jerr,jerr,tmp,MPFR_RNDU);mpfr_sqrt(jerr,jerr,MPFR_RNDU);mpfr_div_ui(jerr,jerr,2,MPFR_RNDU);mpfr_add(jrhs,jrhs,jerr,MPFR_RNDU);
 one(jmargin);mpfr_sub(jmargin,jmargin,jrhs,MPFR_RNDD);
 if(mpfr_cmp_ui(jmargin,0)>0){
   mpfr_set(margin,jmargin,MPFR_RNDD);mpfr_set(lhs,jrhs,MPFR_RNDU);
   printf("JOINT-ELLIPSE PSC BOX PREC=%d K=%lu\n",PREC,K);pr("A0_upper",A0,MPFR_RNDU);pr("A1_upper",A1,MPFR_RNDU);pr("phi_lower",phi,MPFR_RNDD);pr("sigmax_upper",jsigx,MPFR_RNDU);pr("T_upper",jTup,MPFR_RNDU);pr("logN_upper",jlogN,MPFR_RNDU);pr("q_numerator_upper",jq,MPFR_RNDU);pr("twoPhi_lower",jtwoPhi,MPFR_RNDD);pr("E0_upper",E0,MPFR_RNDU);pr("E1_upper",E1,MPFR_RNDU);pr("JECC_rhs_upper",jrhs,MPFR_RNDU);pr("margin_lower",jmargin,MPFR_RNDD);printf("RESULT status=CERTIFIED pass=1 mechanism=JECC\n");return 0;
 }

jecc_fail:
 if(!psc_valid){zero(Y);zero(lhs);setd(margin,"-1e100",MPFR_RNDD);} 
 printf("JOINT-ELLIPSE PSC BOX PREC=%d K=%lu\n",PREC,K);pr("A0_upper",A0,MPFR_RNDU);pr("A1_upper",A1,MPFR_RNDU);pr("phi_lower",phi,MPFR_RNDD);pr("E0_upper",E0,MPFR_RNDU);pr("E1_upper",E1,MPFR_RNDU);pr("margin_lower",margin,MPFR_RNDD);printf("RESULT status=JOINT_CORE pass=0 mechanism=NONE\n");return 1;
}
'''

s=s[:start]+new_tail
out_path.write_text(s)
print(out_path)
