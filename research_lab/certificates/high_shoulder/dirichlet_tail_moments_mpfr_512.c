#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef long int mpfr_prec_t; typedef long int mpfr_exp_t; typedef unsigned long int mp_limb_t;
typedef struct { mpfr_prec_t _mpfr_prec; int _mpfr_sign; mpfr_exp_t _mpfr_exp; mp_limb_t *_mpfr_d; } __mpfr_struct;
typedef __mpfr_struct *mpfr_ptr; typedef const __mpfr_struct *mpfr_srcptr; typedef __mpfr_struct mpfr_t[1];
typedef enum { MPFR_RNDN=0, MPFR_RNDZ=1, MPFR_RNDU=2, MPFR_RNDD=3, MPFR_RNDA=4 } mpfr_rnd_t;
extern void mpfr_init2(mpfr_ptr,mpfr_prec_t); extern void mpfr_clear(mpfr_ptr); extern int mpfr_set_str(mpfr_ptr,const char*,int,mpfr_rnd_t); extern int mpfr_set_ui(mpfr_ptr,unsigned long,mpfr_rnd_t); extern int mpfr_set(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_add(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_sub(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_mul(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_div(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_sqr(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_log(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_exp(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern double mpfr_get_d(mpfr_srcptr,mpfr_rnd_t);
#ifndef PREC
#define PREC 512
#endif
static void term_upper(mpfr_ptr val, mpfr_ptr logn_upper, unsigned long n, mpfr_srcptr pL){
 mpfr_t nn,lL,lU,prod,z,expo; mpfr_init2(nn,PREC);mpfr_init2(lL,PREC);mpfr_init2(lU,PREC);mpfr_init2(prod,PREC);mpfr_init2(z,PREC);mpfr_init2(expo,PREC);
 mpfr_set_ui(nn,n,MPFR_RNDN); mpfr_log(lL,nn,MPFR_RNDD); mpfr_log(lU,nn,MPFR_RNDU);
 /* prod <= p*log n because both factors are positive lower bounds */
 mpfr_mul(prod,pL,lL,MPFR_RNDD); mpfr_set_ui(z,0,MPFR_RNDN); mpfr_sub(expo,z,prod,MPFR_RNDU); mpfr_exp(val,expo,MPFR_RNDU); mpfr_set(logn_upper,lU,MPFR_RNDU);
 mpfr_clear(nn);mpfr_clear(lL);mpfr_clear(lU);mpfr_clear(prod);mpfr_clear(z);mpfr_clear(expo);
}
static void tails_upper(mpfr_ptr I0,mpfr_ptr I1,unsigned long M,mpfr_srcptr pL){
 mpfr_t mm,lL,lU,one,aU,expoU,powU,denL,tmp,tmp2; mpfr_init2(mm,PREC);mpfr_init2(lL,PREC);mpfr_init2(lU,PREC);mpfr_init2(one,PREC);mpfr_init2(aU,PREC);mpfr_init2(expoU,PREC);mpfr_init2(powU,PREC);mpfr_init2(denL,PREC);mpfr_init2(tmp,PREC);mpfr_init2(tmp2,PREC);
 mpfr_set_ui(mm,M,MPFR_RNDN); mpfr_set_ui(one,1,MPFR_RNDN); mpfr_log(lL,mm,MPFR_RNDD); mpfr_log(lU,mm,MPFR_RNDU);
 /* aU = 1-p with p replaced by lower bound: upper (less negative) coefficient */
 mpfr_sub(aU,one,pL,MPFR_RNDU); /* aU<0 */
 /* negative coefficient times lower log gives an upper exponent */
 mpfr_mul(expoU,aU,lL,MPFR_RNDU); mpfr_exp(powU,expoU,MPFR_RNDU);
 mpfr_sub(denL,pL,one,MPFR_RNDD);
 mpfr_div(I0,powU,denL,MPFR_RNDU);
 mpfr_div(tmp,lU,denL,MPFR_RNDU); mpfr_sqr(tmp2,denL,MPFR_RNDD); mpfr_div(tmp2,one,tmp2,MPFR_RNDU); mpfr_add(tmp,tmp,tmp2,MPFR_RNDU); mpfr_mul(I1,powU,tmp,MPFR_RNDU);
 mpfr_clear(mm);mpfr_clear(lL);mpfr_clear(lU);mpfr_clear(one);mpfr_clear(aU);mpfr_clear(expoU);mpfr_clear(powU);mpfr_clear(denL);mpfr_clear(tmp);mpfr_clear(tmp2);
}
int main(int argc,char**argv){
 if(argc<2){fprintf(stderr,"usage: %s p [M]\n",argv[0]);return 2;} unsigned long M=argc>2?strtoul(argv[2],0,10):1000000UL;
 mpfr_t pL,A0,A1,v,lU,I0,I1,tmp; mpfr_init2(pL,PREC);mpfr_init2(A0,PREC);mpfr_init2(A1,PREC);mpfr_init2(v,PREC);mpfr_init2(lU,PREC);mpfr_init2(I0,PREC);mpfr_init2(I1,PREC);mpfr_init2(tmp,PREC);
 mpfr_set_str(pL,argv[1],10,MPFR_RNDD); mpfr_set_ui(A0,0,MPFR_RNDU); mpfr_set_ui(A1,0,MPFR_RNDU);
 for(unsigned long n=2;n<=M;n++){term_upper(v,lU,n,pL);mpfr_add(A0,A0,v,MPFR_RNDU);mpfr_mul(tmp,v,lU,MPFR_RNDU);mpfr_add(A1,A1,tmp,MPFR_RNDU);} tails_upper(I0,I1,M,pL); mpfr_add(A0,A0,I0,MPFR_RNDU); mpfr_add(A1,A1,I1,MPFR_RNDU);
 printf("DIRICHLET MOMENT AUDIT V2 (PREC=%d)\n",PREC); printf("p=%s M=%lu A0_upper=%.17g A1_upper=%.17g\n",argv[1],M,mpfr_get_d(A0,MPFR_RNDU),mpfr_get_d(A1,MPFR_RNDU)); return 0;
}
