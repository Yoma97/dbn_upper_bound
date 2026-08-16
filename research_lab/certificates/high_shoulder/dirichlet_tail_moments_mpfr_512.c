#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef long int mpfr_prec_t; typedef long int mpfr_exp_t; typedef unsigned long int mp_limb_t;
typedef struct { mpfr_prec_t _mpfr_prec; int _mpfr_sign; mpfr_exp_t _mpfr_exp; mp_limb_t *_mpfr_d; } __mpfr_struct;
typedef __mpfr_struct *mpfr_ptr; typedef const __mpfr_struct *mpfr_srcptr; typedef __mpfr_struct mpfr_t[1];
typedef enum { MPFR_RNDN=0, MPFR_RNDZ=1, MPFR_RNDU=2, MPFR_RNDD=3, MPFR_RNDA=4 } mpfr_rnd_t;
extern void mpfr_init2(mpfr_ptr,mpfr_prec_t); extern void mpfr_clear(mpfr_ptr); extern int mpfr_set_str(mpfr_ptr,const char*,int,mpfr_rnd_t); extern int mpfr_set_ui(mpfr_ptr,unsigned long,mpfr_rnd_t); extern int mpfr_set(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_add(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_sub(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_mul(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_div(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_sqr(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_log(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_exp(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern double mpfr_get_d(mpfr_srcptr,mpfr_rnd_t);
#define PREC 512
static void term_upper(mpfr_ptr val, mpfr_ptr logn_out, unsigned long n, mpfr_srcptr pL){
 mpfr_t nn,l,e,z;mpfr_init2(nn,PREC);mpfr_init2(l,PREC);mpfr_init2(e,PREC);mpfr_init2(z,PREC);mpfr_set_ui(nn,n,MPFR_RNDN);mpfr_log(l,nn,MPFR_RNDU);mpfr_mul(e,pL,l,MPFR_RNDD);mpfr_set_ui(z,0,MPFR_RNDN);mpfr_sub(e,z,e,MPFR_RNDU);mpfr_exp(val,e,MPFR_RNDU);mpfr_set(logn_out,l,MPFR_RNDU);mpfr_clear(nn);mpfr_clear(l);mpfr_clear(e);mpfr_clear(z);
}
/* upper integrals from M to infinity at lower p: I0=M^(1-p)/(p-1), I1=M^(1-p)(log M/(p-1)+1/(p-1)^2) */
static void tails_upper(mpfr_ptr I0,mpfr_ptr I1,unsigned long M,mpfr_srcptr pL){
 mpfr_t mm,l,one,a,pow,den,tmp,tmp2;mpfr_init2(mm,PREC);mpfr_init2(l,PREC);mpfr_init2(one,PREC);mpfr_init2(a,PREC);mpfr_init2(pow,PREC);mpfr_init2(den,PREC);mpfr_init2(tmp,PREC);mpfr_init2(tmp2,PREC);mpfr_set_ui(mm,M,MPFR_RNDN);mpfr_set_ui(one,1,MPFR_RNDN);mpfr_log(l,mm,MPFR_RNDU);mpfr_sub(a,one,pL,MPFR_RNDU);mpfr_mul(a,a,l,MPFR_RNDU);mpfr_exp(pow,a,MPFR_RNDU);mpfr_sub(den,pL,one,MPFR_RNDD);mpfr_div(I0,pow,den,MPFR_RNDU);mpfr_div(tmp,l,den,MPFR_RNDU);mpfr_sqr(tmp2,den,MPFR_RNDD);mpfr_div(tmp2,one,tmp2,MPFR_RNDU);mpfr_add(tmp,tmp,tmp2,MPFR_RNDU);mpfr_mul(I1,pow,tmp,MPFR_RNDU);mpfr_clear(mm);mpfr_clear(l);mpfr_clear(one);mpfr_clear(a);mpfr_clear(pow);mpfr_clear(den);mpfr_clear(tmp);mpfr_clear(tmp2);
}
int main(int argc,char**argv){if(argc<2){fprintf(stderr,"usage: %s p [M]\n",argv[0]);return 2;}unsigned long M=argc>2?strtoul(argv[2],0,10):1000000UL;mpfr_t pL,A0,A1,v,l,I0,I1,tmp;mpfr_init2(pL,PREC);mpfr_init2(A0,PREC);mpfr_init2(A1,PREC);mpfr_init2(v,PREC);mpfr_init2(l,PREC);mpfr_init2(I0,PREC);mpfr_init2(I1,PREC);mpfr_init2(tmp,PREC);mpfr_set_str(pL,argv[1],10,MPFR_RNDD);mpfr_set_ui(A0,0,MPFR_RNDU);mpfr_set_ui(A1,0,MPFR_RNDU);for(unsigned long n=2;n<=M;n++){term_upper(v,l,n,pL);mpfr_add(A0,A0,v,MPFR_RNDU);mpfr_mul(tmp,v,l,MPFR_RNDU);mpfr_add(A1,A1,tmp,MPFR_RNDU);}tails_upper(I0,I1,M,pL);/* tail n>M <= integral_M^inf */mpfr_add(A0,A0,I0,MPFR_RNDU);mpfr_add(A1,A1,I1,MPFR_RNDU);printf("p=%s M=%lu A0=sum_n>=2 n^-p <= %.17g A1=sum log(n)n^-p <= %.17g\n",argv[1],M,mpfr_get_d(A0,MPFR_RNDU),mpfr_get_d(A1,MPFR_RNDU));return 0;}
