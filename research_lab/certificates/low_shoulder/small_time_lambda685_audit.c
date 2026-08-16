#include <stdio.h>
#include <stdint.h>
typedef long int mpfr_prec_t; typedef long int mpfr_exp_t; typedef unsigned long int mp_limb_t;
typedef struct { mpfr_prec_t _mpfr_prec; int _mpfr_sign; mpfr_exp_t _mpfr_exp; mp_limb_t *_mpfr_d; } __mpfr_struct;
typedef __mpfr_struct *mpfr_ptr; typedef const __mpfr_struct *mpfr_srcptr; typedef __mpfr_struct mpfr_t[1];
typedef enum { MPFR_RNDN=0,MPFR_RNDZ=1,MPFR_RNDU=2,MPFR_RNDD=3,MPFR_RNDA=4 } mpfr_rnd_t;
extern void mpfr_init2(mpfr_ptr,mpfr_prec_t); extern void mpfr_clear(mpfr_ptr); extern int mpfr_set_str(mpfr_ptr,const char*,int,mpfr_rnd_t); extern int mpfr_set_ui(mpfr_ptr,unsigned long,mpfr_rnd_t); extern int mpfr_add(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_sub(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_mul(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_div(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_exp(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_log(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_sqrt(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_sqr(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern double mpfr_get_d(mpfr_srcptr,mpfr_rnd_t); extern int mpfr_cmp_ui(mpfr_srcptr,unsigned long);
#ifndef PREC
#define PREC 512
#endif
static void I(mpfr_t x){mpfr_init2(x,PREC);} static void S(mpfr_t x,const char*s,mpfr_rnd_t r){mpfr_set_str(x,s,10,r);} static void U(mpfr_t x,unsigned long n){mpfr_set_ui(x,n,MPFR_RNDN);} static void P(const char*n,mpfr_t x,mpfr_rnd_t r){printf("%-24s %.17g\n",n,mpfr_get_d(x,r));}
static void NEG(mpfr_t y,mpfr_t x,mpfr_rnd_t r){mpfr_t z;I(z);U(z,0);mpfr_sub(y,z,x,r);mpfr_clear(z);}
int main(void){
 mpfr_t T,s,q,ln2,two_neg_s,sm1,A0h,A1h,tmp,tmp2,tmp3,E100,A0t,A1t,A0,A1,S0,eab,ec,jump,E0,R,E1,phi,d,half,rad,Y,core,lhs,margin;
 mpfr_t *v[]={&T,&s,&q,&ln2,&two_neg_s,&sm1,&A0h,&A1h,&tmp,&tmp2,&tmp3,&E100,&A0t,&A1t,&A0,&A1,&S0,&eab,&ec,&jump,&E0,&R,&E1,&phi,&d,&half,&rad,&Y,&core,&lhs,&margin};for(size_t i=0;i<sizeof(v)/sizeof(v[0]);i++)I(*v[i]);
 /* For 0<t<=0.01 and lambda>=6.85:
    u=t log n<=1 gives exponent > 1.9624; use s=1.962.
    Above u=1 through the moving cutoff the exponent >1.3560; use q=1.355. */
 S(T,"0.01",MPFR_RNDU);S(s,"1.962",MPFR_RNDD);S(q,"1.355",MPFR_RNDD);U(tmp,2);mpfr_log(ln2,tmp,MPFR_RNDU);
 mpfr_mul(tmp,s,ln2,MPFR_RNDD);NEG(tmp,tmp,MPFR_RNDU);mpfr_exp(two_neg_s,tmp,MPFR_RNDU);
 U(tmp,1);mpfr_sub(sm1,s,tmp,MPFR_RNDD);
 U(tmp,2);mpfr_mul(tmp,two_neg_s,tmp,MPFR_RNDU);mpfr_div(tmp,tmp,sm1,MPFR_RNDU);mpfr_add(A0h,two_neg_s,tmp,MPFR_RNDU);
 mpfr_mul(A1h,ln2,two_neg_s,MPFR_RNDU);mpfr_div(tmp,ln2,sm1,MPFR_RNDU);mpfr_sqr(tmp2,sm1,MPFR_RNDD);U(tmp3,1);mpfr_div(tmp3,tmp3,tmp2,MPFR_RNDU);mpfr_add(tmp,tmp,tmp3,MPFR_RNDU);U(tmp2,2);mpfr_mul(tmp2,two_neg_s,tmp2,MPFR_RNDU);mpfr_mul(tmp,tmp,tmp2,MPFR_RNDU);mpfr_add(A1h,A1h,tmp,MPFR_RNDU);
 U(tmp,1);mpfr_sub(sm1,q,tmp,MPFR_RNDD);
 U(tmp,1);mpfr_sub(tmp,tmp,q,MPFR_RNDU);U(tmp2,100);mpfr_mul(tmp,tmp,tmp2,MPFR_RNDU);mpfr_exp(E100,tmp,MPFR_RNDU);
 U(tmp,100);mpfr_mul(tmp,q,tmp,MPFR_RNDD);NEG(tmp,tmp,MPFR_RNDU);mpfr_exp(A0t,tmp,MPFR_RNDU);mpfr_div(tmp,E100,sm1,MPFR_RNDU);mpfr_add(A0t,A0t,tmp,MPFR_RNDU);
 U(tmp,100);mpfr_mul(tmp2,q,tmp,MPFR_RNDD);NEG(tmp2,tmp2,MPFR_RNDU);mpfr_exp(A1t,tmp2,MPFR_RNDU);mpfr_mul(A1t,A1t,tmp,MPFR_RNDU);
 mpfr_div(tmp2,tmp,sm1,MPFR_RNDU);mpfr_sqr(tmp3,sm1,MPFR_RNDD);U(tmp,1);mpfr_div(tmp,tmp,tmp3,MPFR_RNDU);mpfr_add(tmp2,tmp2,tmp,MPFR_RNDU);mpfr_mul(tmp2,tmp2,E100,MPFR_RNDU);mpfr_add(A1t,A1t,tmp2,MPFR_RNDU);
 mpfr_add(A0,A0h,A0t,MPFR_RNDU);mpfr_add(A1,A1h,A1t,MPFR_RNDU);U(tmp,1);mpfr_sub(S0,tmp,A0,MPFR_RNDD);
 /* Deliberately overpadded unconditional Polymath remainder envelopes. */
 S(tmp,"6.85",MPFR_RNDD);mpfr_div(tmp,tmp,T,MPFR_RNDD);NEG(tmp,tmp,MPFR_RNDU);mpfr_exp(eab,tmp,MPFR_RNDU);U(tmp,512);mpfr_mul(eab,eab,tmp,MPFR_RNDU);
 /* The radius-0.1 disk has scaled logarithmic variable >6.7.  Since
    W/4+W^2/16 at W=6.7 equals 4.480625, use 4.48. */
 S(tmp,"4.48",MPFR_RNDD);mpfr_div(tmp,tmp,T,MPFR_RNDD);NEG(tmp,tmp,MPFR_RNDU);U(tmp2,1);mpfr_add(tmp,tmp,tmp2,MPFR_RNDU);mpfr_exp(ec,tmp,MPFR_RNDU);
 /* After the worst n^y loss the error-series power stays >1.305 and
    log N is >6.7/(2t), so the true jump exponent exceeds 4.37/t;
    use 4.35 with a padded prefactor 8. */
 S(tmp,"4.35",MPFR_RNDD);mpfr_div(tmp,tmp,T,MPFR_RNDD);NEG(tmp,tmp,MPFR_RNDU);mpfr_exp(jump,tmp,MPFR_RNDU);U(tmp,8);mpfr_mul(jump,jump,tmp,MPFR_RNDU);mpfr_add(E0,eab,ec,MPFR_RNDU);mpfr_add(E0,E0,jump,MPFR_RNDU);
 /* Same symmetric-normalization envelope valid up to lambda=10.52. */
 S(tmp,"0.526",MPFR_RNDU);mpfr_div(tmp,tmp,T,MPFR_RNDU);S(tmp2,"0.2",MPFR_RNDU);mpfr_add(tmp,tmp,tmp2,MPFR_RNDU);mpfr_exp(R,tmp,MPFR_RNDU);mpfr_mul(E1,R,E0,MPFR_RNDU);U(tmp,10);mpfr_mul(E1,E1,tmp,MPFR_RNDU);
 /* L>=685, so Phi=L/4+o(1)>171.24; d is 1/2+astronomically small. */
 S(phi,"171.24",MPFR_RNDD);S(d,"0.501",MPFR_RNDU);U(tmp,2);mpfr_div(half,E0,tmp,MPFR_RNDU);mpfr_sqr(rad,S0,MPFR_RNDD);mpfr_sqr(tmp,half,MPFR_RNDU);mpfr_sub(rad,rad,tmp,MPFR_RNDD);mpfr_sqrt(Y,rad,MPFR_RNDD);mpfr_mul(core,phi,Y,MPFR_RNDD);mpfr_mul(tmp,d,A1,MPFR_RNDU);mpfr_sub(core,core,tmp,MPFR_RNDD);U(tmp,2);mpfr_mul(lhs,core,tmp,MPFR_RNDD);mpfr_sub(margin,lhs,E1,MPFR_RNDD);
 printf("STRICT SMALL-TIME lambda>=6.85 audit PREC=%d\n",PREC);P("A0_head_upper",A0h,MPFR_RNDU);P("A1_head_upper",A1h,MPFR_RNDU);P("A0_tail_upper",A0t,MPFR_RNDU);P("A1_tail_upper",A1t,MPFR_RNDU);P("A0_upper",A0,MPFR_RNDU);P("A1_upper",A1,MPFR_RNDU);P("S0_lower",S0,MPFR_RNDD);P("E0_upper",E0,MPFR_RNDU);P("R_upper_at_T",R,MPFR_RNDU);P("E1_upper",E1,MPFR_RNDU);P("Y_lower",Y,MPFR_RNDD);P("lhs_lower",lhs,MPFR_RNDD);P("margin_lower",margin,MPFR_RNDD);int ok=mpfr_cmp_ui(margin,0)>0;printf("AUDIT_RESULT pass=%d\n",ok);for(size_t i=0;i<sizeof(v)/sizeof(v[0]);i++)mpfr_clear(*v[i]);return ok?0:1;
}
