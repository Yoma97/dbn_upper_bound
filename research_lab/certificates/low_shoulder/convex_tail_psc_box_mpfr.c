#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

typedef long int mpfr_prec_t; typedef long int mpfr_exp_t; typedef unsigned long int mp_limb_t;
typedef struct { mpfr_prec_t _mpfr_prec; int _mpfr_sign; mpfr_exp_t _mpfr_exp; mp_limb_t *_mpfr_d; } __mpfr_struct;
typedef __mpfr_struct *mpfr_ptr; typedef const __mpfr_struct *mpfr_srcptr; typedef __mpfr_struct mpfr_t[1];
typedef enum { MPFR_RNDN=0, MPFR_RNDZ=1, MPFR_RNDU=2, MPFR_RNDD=3, MPFR_RNDA=4 } mpfr_rnd_t;
extern void mpfr_init2(mpfr_ptr,mpfr_prec_t); extern void mpfr_clear(mpfr_ptr); extern int mpfr_set_str(mpfr_ptr,const char*,int,mpfr_rnd_t); extern int mpfr_set_ui(mpfr_ptr,unsigned long,mpfr_rnd_t); extern int mpfr_set(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_add(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_add_ui(mpfr_ptr,mpfr_srcptr,unsigned long,mpfr_rnd_t); extern int mpfr_sub_ui(mpfr_ptr,mpfr_srcptr,unsigned long,mpfr_rnd_t); extern int mpfr_sub(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_mul(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_mul_ui(mpfr_ptr,mpfr_srcptr,unsigned long,mpfr_rnd_t); extern int mpfr_div(mpfr_ptr,mpfr_srcptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_div_ui(mpfr_ptr,mpfr_srcptr,unsigned long,mpfr_rnd_t); extern int mpfr_sqr(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_sqrt(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_log(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_exp(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_expm1(mpfr_ptr,mpfr_srcptr,mpfr_rnd_t); extern int mpfr_const_pi(mpfr_ptr,mpfr_rnd_t); extern int mpfr_cmp(mpfr_srcptr,mpfr_srcptr); extern int mpfr_cmp_ui(mpfr_srcptr,unsigned long); extern int mpfr_sgn(mpfr_srcptr); extern double mpfr_get_d(mpfr_srcptr,mpfr_rnd_t);
#ifndef PREC
#define PREC 512
#endif
static void ini(mpfr_t x){mpfr_init2(x,PREC);} static void setd(mpfr_t x,const char*s,mpfr_rnd_t r){mpfr_set_str(x,s,10,r);} static void zero(mpfr_t x){mpfr_set_ui(x,0,MPFR_RNDN);} static void one(mpfr_t x){mpfr_set_ui(x,1,MPFR_RNDN);} static void neg(mpfr_t r,mpfr_srcptr a,mpfr_rnd_t rnd){mpfr_t z;ini(z);zero(z);mpfr_sub(r,z,a,rnd);mpfr_clear(z);} static void pr(const char*n,mpfr_srcptr x,mpfr_rnd_t r){printf("%-24s %.17g\n",n,mpfr_get_d(x,r));}

static void F_upper(mpfr_t out, unsigned long n, mpfr_srcptr T, mpfr_srcptr S){
 mpfr_t nn,lL,lU,pos,prod,expo; ini(nn);ini(lL);ini(lU);ini(pos);ini(prod);ini(expo);
 mpfr_set_ui(nn,n,MPFR_RNDN); mpfr_log(lL,nn,MPFR_RNDD); mpfr_log(lU,nn,MPFR_RNDU);
 mpfr_sqr(pos,lU,MPFR_RNDU); mpfr_mul(pos,pos,T,MPFR_RNDU); mpfr_div_ui(pos,pos,4,MPFR_RNDU);
 mpfr_mul(prod,S,lL,MPFR_RNDD); mpfr_sub(expo,pos,prod,MPFR_RNDU); mpfr_exp(out,expo,MPFR_RNDU);
 mpfr_clear(nn);mpfr_clear(lL);mpfr_clear(lU);mpfr_clear(pos);mpfr_clear(prod);mpfr_clear(expo);
}
static void F_upper_real(mpfr_t out, mpfr_srcptr nlower, mpfr_srcptr T, mpfr_srcptr S){
 mpfr_t lL,lU,pos,prod,expo; ini(lL);ini(lU);ini(pos);ini(prod);ini(expo);
 mpfr_log(lL,nlower,MPFR_RNDD); mpfr_log(lU,nlower,MPFR_RNDU);
 mpfr_sqr(pos,lU,MPFR_RNDU); mpfr_mul(pos,pos,T,MPFR_RNDU); mpfr_div_ui(pos,pos,4,MPFR_RNDU);
 mpfr_mul(prod,S,lL,MPFR_RNDD); mpfr_sub(expo,pos,prod,MPFR_RNDU); mpfr_exp(out,expo,MPFR_RNDU);
 mpfr_clear(lL);mpfr_clear(lU);mpfr_clear(pos);mpfr_clear(prod);mpfr_clear(expo);
}
static int sum_bound(mpfr_t out, mpfr_srcptr T, mpfr_srcptr S, mpfr_srcptr V, unsigned long K){
 mpfr_t mu,tmp,rL,rU,Dup,mup,grup,zup,ezup,em1up,F0up,tail,term,onev;
 ini(mu);ini(tmp);ini(rL);ini(rU);ini(Dup);ini(mup);ini(grup);ini(zup);ini(ezup);ini(em1up);ini(F0up);ini(tail);ini(term);ini(onev);
 mpfr_mul(tmp,T,V,MPFR_RNDU); mpfr_div_ui(tmp,tmp,2,MPFR_RNDU); mpfr_sub(mu,S,tmp,MPFR_RNDD); if(mpfr_cmp_ui(mu,0)<=0) goto fail;
 one(out); for(unsigned long n=2;n<=K;n++){F_upper(term,n,T,S);mpfr_add(out,out,term,MPFR_RNDU);} 
 mpfr_set_ui(tmp,K,MPFR_RNDN); mpfr_log(rL,tmp,MPFR_RNDD); mpfr_log(rU,tmp,MPFR_RNDU); if(mpfr_cmp(V,rU)<=0) goto ok;
 mpfr_sub(Dup,V,rL,MPFR_RNDU);
 mpfr_add(tmp,V,rU,MPFR_RNDU); mpfr_mul(tmp,tmp,T,MPFR_RNDU); mpfr_div_ui(tmp,tmp,4,MPFR_RNDU); mpfr_sub_ui(mup,S,1,MPFR_RNDD); mpfr_sub(mup,tmp,mup,MPFR_RNDU);
 mpfr_sqr(tmp,rU,MPFR_RNDU); mpfr_mul(tmp,tmp,T,MPFR_RNDU); mpfr_div_ui(tmp,tmp,4,MPFR_RNDU); mpfr_sub_ui(onev,S,1,MPFR_RNDD); mpfr_mul(onev,onev,rL,MPFR_RNDD); mpfr_sub(grup,tmp,onev,MPFR_RNDU);
 if(mpfr_cmp_ui(mup,0)<0){mpfr_t aa,ezlo;ini(aa);ini(ezlo);neg(aa,mup,MPFR_RNDN);mpfr_mul(zup,aa,Dup,MPFR_RNDU);neg(tmp,zup,MPFR_RNDD);mpfr_exp(ezlo,tmp,MPFR_RNDD);one(em1up);mpfr_sub(em1up,em1up,ezlo,MPFR_RNDU);mpfr_div(F0up,em1up,aa,MPFR_RNDU);mpfr_clear(aa);mpfr_clear(ezlo);} 
 else if(mpfr_cmp_ui(mup,0)==0) mpfr_set(F0up,Dup,MPFR_RNDU); 
 else {mpfr_mul(zup,mup,Dup,MPFR_RNDU);mpfr_expm1(em1up,zup,MPFR_RNDU);mpfr_div(F0up,em1up,mup,MPFR_RNDU);} 
 mpfr_exp(tail,grup,MPFR_RNDU); mpfr_mul(tail,tail,F0up,MPFR_RNDU); mpfr_add(out,out,tail,MPFR_RNDU);
ok: mpfr_clear(mu);mpfr_clear(tmp);mpfr_clear(rL);mpfr_clear(rU);mpfr_clear(Dup);mpfr_clear(mup);mpfr_clear(grup);mpfr_clear(zup);mpfr_clear(ezup);mpfr_clear(em1up);mpfr_clear(F0up);mpfr_clear(tail);mpfr_clear(term);mpfr_clear(onev); return 1;
fail: mpfr_clear(mu);mpfr_clear(tmp);mpfr_clear(rL);mpfr_clear(rU);mpfr_clear(Dup);mpfr_clear(mup);mpfr_clear(grup);mpfr_clear(zup);mpfr_clear(ezup);mpfr_clear(em1up);mpfr_clear(F0up);mpfr_clear(tail);mpfr_clear(term);mpfr_clear(onev); return 0;
}
static int moments_bound(mpfr_t A0, mpfr_t A1, mpfr_srcptr T, mpfr_srcptr S, mpfr_srcptr V, unsigned long K){
 mpfr_t mu,tmp,invlogK,rL,rU,Dup,mup,grup,zU,em1,F0,F1,numer,den,tail0,tail1,term,lU,onev,ezU,zminus;
 ini(mu);ini(tmp);ini(invlogK);ini(rL);ini(rU);ini(Dup);ini(mup);ini(grup);ini(zU);ini(em1);ini(F0);ini(F1);ini(numer);ini(den);ini(tail0);ini(tail1);ini(term);ini(lU);ini(onev);ini(ezU);ini(zminus);
 mpfr_mul(tmp,T,V,MPFR_RNDU); mpfr_div_ui(tmp,tmp,2,MPFR_RNDU); mpfr_sub(mu,S,tmp,MPFR_RNDD);
 mpfr_set_ui(tmp,K,MPFR_RNDN); mpfr_log(rL,tmp,MPFR_RNDD); mpfr_log(rU,tmp,MPFR_RNDU); one(onev); mpfr_div(invlogK,onev,rL,MPFR_RNDU); if(mpfr_cmp(mu,invlogK)<=0) goto fail;
 zero(A0);zero(A1); for(unsigned long n=2;n<=K;n++){F_upper(term,n,T,S);mpfr_add(A0,A0,term,MPFR_RNDU);mpfr_set_ui(tmp,n,MPFR_RNDN);mpfr_log(lU,tmp,MPFR_RNDU);mpfr_mul(tmp,term,lU,MPFR_RNDU);mpfr_add(A1,A1,tmp,MPFR_RNDU);} if(mpfr_cmp(V,rU)<=0) goto ok;
 mpfr_sub(Dup,V,rL,MPFR_RNDU); mpfr_add(tmp,V,rU,MPFR_RNDU);mpfr_mul(tmp,tmp,T,MPFR_RNDU);mpfr_div_ui(tmp,tmp,4,MPFR_RNDU);mpfr_sub_ui(onev,S,1,MPFR_RNDD);mpfr_sub(mup,tmp,onev,MPFR_RNDU);
 mpfr_sqr(tmp,rU,MPFR_RNDU);mpfr_mul(tmp,tmp,T,MPFR_RNDU);mpfr_div_ui(tmp,tmp,4,MPFR_RNDU);mpfr_sub_ui(onev,S,1,MPFR_RNDD);mpfr_mul(onev,onev,rL,MPFR_RNDD);mpfr_sub(grup,tmp,onev,MPFR_RNDU);
 if(mpfr_cmp_ui(mup,0)<0){
   neg(den,mup,MPFR_RNDN); mpfr_mul(zU,den,Dup,MPFR_RNDU); neg(tmp,zU,MPFR_RNDD); mpfr_exp(ezU,tmp,MPFR_RNDD); one(numer); mpfr_sub(numer,numer,ezU,MPFR_RNDU); mpfr_div(F0,numer,den,MPFR_RNDU);
   mpfr_add_ui(tmp,zU,1,MPFR_RNDD); mpfr_mul(tmp,ezU,tmp,MPFR_RNDD); one(numer); mpfr_sub(numer,numer,tmp,MPFR_RNDU); mpfr_sqr(tmp,den,MPFR_RNDD); mpfr_div(F1,numer,tmp,MPFR_RNDU);
 } else if(mpfr_cmp_ui(mup,0)==0){mpfr_set(F0,Dup,MPFR_RNDU);mpfr_sqr(F1,Dup,MPFR_RNDU);mpfr_div_ui(F1,F1,2,MPFR_RNDU);} 
 else {mpfr_mul(zU,mup,Dup,MPFR_RNDU);mpfr_expm1(em1,zU,MPFR_RNDU);mpfr_div(F0,em1,mup,MPFR_RNDU);mpfr_exp(ezU,zU,MPFR_RNDU);mpfr_mul(numer,zU,ezU,MPFR_RNDU);mpfr_expm1(tmp,zU,MPFR_RNDD);mpfr_sub(numer,numer,tmp,MPFR_RNDU);mpfr_sqr(den,mup,MPFR_RNDD);mpfr_div(F1,numer,den,MPFR_RNDU);} 
 mpfr_exp(tail0,grup,MPFR_RNDU);mpfr_mul(tail1,tail0,F1,MPFR_RNDU);mpfr_mul(tail0,tail0,F0,MPFR_RNDU);mpfr_add(A0,A0,tail0,MPFR_RNDU);mpfr_mul(tmp,rU,F0,MPFR_RNDU);mpfr_add(tmp,tmp,F1,MPFR_RNDU);mpfr_exp(tail1,grup,MPFR_RNDU);mpfr_mul(tail1,tail1,tmp,MPFR_RNDU);mpfr_add(A1,A1,tail1,MPFR_RNDU);
ok: mpfr_clear(mu);mpfr_clear(tmp);mpfr_clear(invlogK);mpfr_clear(rL);mpfr_clear(rU);mpfr_clear(Dup);mpfr_clear(mup);mpfr_clear(grup);mpfr_clear(zU);mpfr_clear(em1);mpfr_clear(F0);mpfr_clear(F1);mpfr_clear(numer);mpfr_clear(den);mpfr_clear(tail0);mpfr_clear(tail1);mpfr_clear(term);mpfr_clear(lU);mpfr_clear(onev);mpfr_clear(ezU);mpfr_clear(zminus);return 1;
fail: mpfr_clear(mu);mpfr_clear(tmp);mpfr_clear(invlogK);mpfr_clear(rL);mpfr_clear(rU);mpfr_clear(Dup);mpfr_clear(mup);mpfr_clear(grup);mpfr_clear(zU);mpfr_clear(em1);mpfr_clear(F0);mpfr_clear(F1);mpfr_clear(numer);mpfr_clear(den);mpfr_clear(tail0);mpfr_clear(tail1);mpfr_clear(term);mpfr_clear(lU);mpfr_clear(onev);mpfr_clear(ezU);mpfr_clear(zminus);return 0;
}
int main(int argc,char**argv){
 if(argc<6){fprintf(stderr,"usage: %s tlo thi lamlo lamhi rho [K]\n",argv[0]);return 2;} unsigned long K=argc>6?strtoul(argv[6],0,10):128UL;
 mpfr_t tL,tU,laL,lbU,rhoL,rhoU,piL,piU,Lmin,Lmax,xcmin,xcmax,Xminus,Xplus,hminus,hplus,tmp,tmp2,tmp3,sigmaB,VB,A0,A1,S0,phi,d,dx,Cbd,Dbd;
 mpfr_t sigmaE,kappaB,VE,G,S1,Srho,U,H,eAB,W,nexpr,nlow,Lplus,corr1,corr2,eC,Fjump,nrho,jump,E0,R,E1,halfE,rad,Y,core,lhs,margin;
 mpfr_t *v[]={&tL,&tU,&laL,&lbU,&rhoL,&rhoU,&piL,&piU,&Lmin,&Lmax,&xcmin,&xcmax,&Xminus,&Xplus,&hminus,&hplus,&tmp,&tmp2,&tmp3,&sigmaB,&VB,&A0,&A1,&S0,&phi,&d,&dx,&Cbd,&Dbd,&sigmaE,&kappaB,&VE,&G,&S1,&Srho,&U,&H,&eAB,&W,&nexpr,&nlow,&Lplus,&corr1,&corr2,&eC,&Fjump,&nrho,&jump,&E0,&R,&E1,&halfE,&rad,&Y,&core,&lhs,&margin}; for(size_t i=0;i<sizeof(v)/sizeof(v[0]);i++)ini(*v[i]);
 setd(tL,argv[1],MPFR_RNDD);setd(tU,argv[2],MPFR_RNDU);setd(laL,argv[3],MPFR_RNDD);setd(lbU,argv[4],MPFR_RNDU);setd(rhoL,argv[5],MPFR_RNDD);setd(rhoU,argv[5],MPFR_RNDU);mpfr_const_pi(piL,MPFR_RNDD);mpfr_const_pi(piU,MPFR_RNDU);
 mpfr_div(Lmin,laL,tU,MPFR_RNDD);mpfr_div(Lmax,lbU,tL,MPFR_RNDU);mpfr_exp(xcmin,Lmin,MPFR_RNDD);mpfr_mul(xcmin,xcmin,piL,MPFR_RNDD);mpfr_mul_ui(xcmin,xcmin,4,MPFR_RNDD);mpfr_exp(xcmax,Lmax,MPFR_RNDU);mpfr_mul(xcmax,xcmax,piU,MPFR_RNDU);mpfr_mul_ui(xcmax,xcmax,4,MPFR_RNDU);mpfr_sub(Xminus,xcmin,rhoU,MPFR_RNDD);mpfr_add(Xplus,xcmax,rhoU,MPFR_RNDU);if(mpfr_cmp_ui(Xminus,200)<=0){printf("RESULT status=POLYMATH_REGION\n");return 1;}
 mpfr_div(tmp,rhoU,xcmin,MPFR_RNDU);one(tmp2);mpfr_sub(tmp2,tmp2,tmp,MPFR_RNDD);mpfr_log(tmp2,tmp2,MPFR_RNDD);neg(hminus,tmp2,MPFR_RNDU);one(tmp2);mpfr_add(tmp2,tmp2,tmp,MPFR_RNDU);mpfr_log(hplus,tmp2,MPFR_RNDU);
 mpfr_div_ui(sigmaB,laL,4,MPFR_RNDD);setd(tmp,"0.5",MPFR_RNDD);mpfr_add(sigmaB,sigmaB,tmp,MPFR_RNDD);mpfr_sqr(tmp,xcmin,MPFR_RNDD);mpfr_mul_ui(tmp,tmp,2,MPFR_RNDD);mpfr_div(tmp,tU,tmp,MPFR_RNDU);mpfr_sub(sigmaB,sigmaB,tmp,MPFR_RNDD);
 mpfr_exp(tmp,Lmax,MPFR_RNDU);mpfr_div_ui(tmp2,tU,16,MPFR_RNDU);mpfr_add(tmp,tmp,tmp2,MPFR_RNDU);mpfr_log(VB,tmp,MPFR_RNDU);mpfr_div_ui(VB,VB,2,MPFR_RNDU);if(!moments_bound(A0,A1,tU,sigmaB,VB,K)){printf("RESULT status=WEIGHT_MONOTONICITY_GATE\n");return 1;}one(S0);mpfr_sub(S0,S0,A0,MPFR_RNDD);
 mpfr_div(phi,laL,tU,MPFR_RNDD);mpfr_div_ui(phi,phi,4,MPFR_RNDD);mpfr_sqr(tmp,xcmin,MPFR_RNDD);mpfr_mul_ui(tmp,tmp,2,MPFR_RNDD);one(tmp2);mpfr_div(tmp2,tmp2,tmp,MPFR_RNDU);mpfr_sub(phi,phi,tmp2,MPFR_RNDD);
 one(tmp);mpfr_div(tmp,tmp,xcmin,MPFR_RNDU);one(tmp2);mpfr_mul_ui(tmp2,tmp2,5,MPFR_RNDU);mpfr_mul(tmp3,xcmin,xcmin,MPFR_RNDD);mpfr_mul(tmp3,tmp3,xcmin,MPFR_RNDD);mpfr_div(tmp2,tmp2,tmp3,MPFR_RNDU);mpfr_add(Dbd,tmp,tmp2,MPFR_RNDU);one(Cbd);mpfr_mul_ui(Cbd,Cbd,7,MPFR_RNDU);mpfr_sqr(tmp,xcmin,MPFR_RNDD);mpfr_div(Cbd,Cbd,tmp,MPFR_RNDU);mpfr_mul(tmp,tU,Dbd,MPFR_RNDU);mpfr_div_ui(tmp,tmp,4,MPFR_RNDU);mpfr_sqr(tmp,tmp,MPFR_RNDU);mpfr_mul(tmp2,tU,Cbd,MPFR_RNDU);mpfr_div_ui(tmp2,tmp2,2,MPFR_RNDU);mpfr_add_ui(tmp2,tmp2,1,MPFR_RNDU);mpfr_sqr(tmp2,tmp2,MPFR_RNDU);mpfr_div_ui(tmp2,tmp2,4,MPFR_RNDU);mpfr_add(tmp,tmp,tmp2,MPFR_RNDU);mpfr_sqrt(d,tmp,MPFR_RNDU);
 mpfr_div_ui(sigmaE,laL,4,MPFR_RNDD);setd(tmp,"0.5",MPFR_RNDD);mpfr_add(sigmaE,sigmaE,tmp,MPFR_RNDD);mpfr_mul(tmp,tU,hminus,MPFR_RNDU);mpfr_div_ui(tmp,tmp,4,MPFR_RNDU);mpfr_sub(sigmaE,sigmaE,tmp,MPFR_RNDD);mpfr_sqr(tmp,Xminus,MPFR_RNDD);mpfr_mul_ui(tmp,tmp,2,MPFR_RNDD);mpfr_div(tmp2,tU,tmp,MPFR_RNDU);mpfr_mul(tmp,rhoU,rhoU,MPFR_RNDU);mpfr_add(tmp,rhoU,tmp,MPFR_RNDU);mpfr_mul_ui(tmp,tmp,4,MPFR_RNDU);mpfr_sqr(tmp3,Xminus,MPFR_RNDD);mpfr_div(tmp,tmp,tmp3,MPFR_RNDU);mpfr_add_ui(tmp,tmp,1,MPFR_RNDU);mpfr_mul(tmp,tmp,tmp2,MPFR_RNDU);mpfr_sub(sigmaE,sigmaE,tmp,MPFR_RNDD);
 mpfr_mul_ui(tmp,piL,4,MPFR_RNDD);mpfr_div(tmp,Xplus,tmp,MPFR_RNDU);mpfr_div_ui(tmp2,tU,16,MPFR_RNDU);mpfr_add(tmp,tmp,tmp2,MPFR_RNDU);mpfr_log(VE,tmp,MPFR_RNDU);mpfr_div_ui(VE,VE,2,MPFR_RNDU);mpfr_sub_ui(tmp,Xminus,6,MPFR_RNDD);mpfr_mul_ui(tmp,tmp,2,MPFR_RNDD);mpfr_mul(tmp2,tU,rhoU,MPFR_RNDU);mpfr_div(kappaB,tmp2,tmp,MPFR_RNDU);mpfr_mul(tmp,kappaB,VE,MPFR_RNDU);setd(tmp2,"0.02",MPFR_RNDU);mpfr_mul(tmp2,tmp2,rhoU,MPFR_RNDU);mpfr_add(tmp,tmp,tmp2,MPFR_RNDU);mpfr_exp(G,tmp,MPFR_RNDU);
 if(!sum_bound(S1,tU,sigmaE,VE,K)){printf("RESULT status=ERROR_SUM_GATE\n");return 1;}mpfr_sub(tmp,sigmaE,rhoU,MPFR_RNDD);if(!sum_bound(Srho,tU,tmp,VE,K)){printf("RESULT status=ERROR_SUM_RHO_GATE\n");return 1;}mpfr_mul(tmp,G,Srho,MPFR_RNDU);mpfr_add(tmp,tmp,S1,MPFR_RNDU);
 mpfr_mul(tmp2,tU,hplus,MPFR_RNDU);mpfr_add(U,lbU,tmp2,MPFR_RNDU);mpfr_sqr(tmp2,U,MPFR_RNDU);mpfr_div_ui(tmp2,tmp2,16,MPFR_RNDU);setd(tmp3,"0.627",MPFR_RNDU);mpfr_add(tmp2,tmp2,tmp3,MPFR_RNDU);setd(tmp3,"6.66",MPFR_RNDU);mpfr_sub(tmp3,Xminus,tmp3,MPFR_RNDD);mpfr_div(H,tmp2,tmp3,MPFR_RNDU);mpfr_expm1(tmp2,H,MPFR_RNDU);mpfr_mul(eAB,tmp,tmp2,MPFR_RNDU);
 mpfr_mul(tmp,tU,hminus,MPFR_RNDU);mpfr_sub(W,laL,tmp,MPFR_RNDD);if(mpfr_cmp_ui(W,0)<=0){printf("RESULT status=E_C_W_GATE\n");return 1;}mpfr_mul_ui(tmp,piU,4,MPFR_RNDU);mpfr_div(nexpr,Xminus,tmp,MPFR_RNDD);mpfr_div_ui(tmp,tL,16,MPFR_RNDD);mpfr_add(nexpr,nexpr,tmp,MPFR_RNDD);mpfr_sqrt(nlow,nexpr,MPFR_RNDD);mpfr_sub_ui(nlow,nlow,1,MPFR_RNDD);if(mpfr_cmp_ui(nlow,2)<=0){printf("RESULT status=NLOW_GATE\n");return 1;}
 mpfr_div_ui(tmp,W,4,MPFR_RNDD);mpfr_sqr(tmp2,W,MPFR_RNDD);mpfr_div_ui(tmp2,tmp2,16,MPFR_RNDD);mpfr_add(tmp,tmp,tmp2,MPFR_RNDD);mpfr_div(tmp,tmp,tU,MPFR_RNDD);neg(tmp,tmp,MPFR_RNDU);mpfr_set_ui(tmp2,3,MPFR_RNDN);mpfr_log(tmp2,tmp2,MPFR_RNDU);mpfr_mul(tmp2,tmp2,rhoU,MPFR_RNDU);mpfr_exp(tmp2,tmp2,MPFR_RNDU);mpfr_set_ui(tmp3,3,MPFR_RNDN);mpfr_log(tmp3,tmp3,MPFR_RNDD);mpfr_mul(tmp3,tmp3,rhoL,MPFR_RNDD);neg(tmp3,tmp3,MPFR_RNDU);mpfr_exp(tmp3,tmp3,MPFR_RNDU);mpfr_add(tmp2,tmp2,tmp3,MPFR_RNDU);setd(tmp3,"1.24",MPFR_RNDU);mpfr_mul(tmp2,tmp2,tmp3,MPFR_RNDU);setd(tmp3,"0.125",MPFR_RNDU);mpfr_sub(tmp3,nlow,tmp3,MPFR_RNDD);mpfr_div(corr1,tmp2,tmp3,MPFR_RNDU);mpfr_add(Lplus,Lmax,hplus,MPFR_RNDU);mpfr_sqr(tmp2,Lplus,MPFR_RNDU);mpfr_sqr(tmp3,piU,MPFR_RNDU);mpfr_div_ui(tmp3,tmp3,4,MPFR_RNDU);mpfr_add(tmp2,tmp2,tmp3,MPFR_RNDU);mpfr_sqrt(tmp2,tmp2,MPFR_RNDU);mpfr_mul_ui(tmp2,tmp2,3,MPFR_RNDU);setd(tmp3,"10.44",MPFR_RNDU);mpfr_add(tmp2,tmp2,tmp3,MPFR_RNDU);mpfr_sub_ui(tmp3,Xminus,12,MPFR_RNDD);mpfr_div(corr2,tmp2,tmp3,MPFR_RNDU);mpfr_add(tmp,tmp,corr1,MPFR_RNDU);mpfr_add(tmp,tmp,corr2,MPFR_RNDU);mpfr_exp(eC,tmp,MPFR_RNDU);
 mpfr_log(tmp,nlow,MPFR_RNDU);mpfr_mul(tmp2,tU,tmp,MPFR_RNDU);mpfr_div_ui(tmp2,tmp2,2,MPFR_RNDU);mpfr_sub(tmp3,sigmaE,rhoU,MPFR_RNDD);mpfr_sub(tmp3,tmp3,tmp2,MPFR_RNDD);if(mpfr_cmp_ui(tmp3,0)<=0){printf("RESULT status=JUMP_MONOTONICITY_GATE\n");return 1;}F_upper_real(Fjump,nlow,tU,sigmaE);mpfr_mul(tmp,rhoU,tmp,MPFR_RNDU);mpfr_exp(nrho,tmp,MPFR_RNDU);mpfr_mul(nrho,nrho,G,MPFR_RNDU);mpfr_add_ui(nrho,nrho,1,MPFR_RNDU);mpfr_mul(jump,Fjump,nrho,MPFR_RNDU);mpfr_add(E0,eAB,eC,MPFR_RNDU);mpfr_add(E0,E0,jump,MPFR_RNDU);
 mpfr_add_ui(tmp,Lplus,2,MPFR_RNDU);mpfr_mul(tmp,tmp,rhoU,MPFR_RNDU);mpfr_div_ui(tmp,tmp,2,MPFR_RNDU);mpfr_exp(R,tmp,MPFR_RNDU);mpfr_mul(E1,E0,R,MPFR_RNDU);mpfr_div(E1,E1,rhoL,MPFR_RNDU);
 if(mpfr_cmp_ui(S0,0)<=0){printf("RESULT status=TRIANGLE_SIGN\n");return 1;}mpfr_div_ui(halfE,E0,2,MPFR_RNDU);mpfr_sqr(rad,S0,MPFR_RNDD);mpfr_sqr(tmp,halfE,MPFR_RNDU);mpfr_sub(rad,rad,tmp,MPFR_RNDD);if(mpfr_cmp_ui(rad,0)<=0){printf("RESULT status=TRIANGLE_ERROR\n");return 1;}mpfr_sqrt(Y,rad,MPFR_RNDD);mpfr_mul(core,phi,Y,MPFR_RNDD);mpfr_mul(tmp,d,A1,MPFR_RNDU);mpfr_sub(core,core,tmp,MPFR_RNDD);mpfr_mul_ui(lhs,core,2,MPFR_RNDD);mpfr_sub(margin,lhs,E1,MPFR_RNDD);
 printf("PSC BOX V1 PREC=%d K=%lu\n",PREC,K);pr("Lmin",Lmin,MPFR_RNDD);pr("Lmax",Lmax,MPFR_RNDU);pr("x_min_center",xcmin,MPFR_RNDD);pr("A0_upper",A0,MPFR_RNDU);pr("A1_upper",A1,MPFR_RNDU);pr("S0_lower",S0,MPFR_RNDD);pr("phi_lower",phi,MPFR_RNDD);pr("d_upper",d,MPFR_RNDU);pr("eAB_upper",eAB,MPFR_RNDU);pr("eC_upper",eC,MPFR_RNDU);pr("jump_upper",jump,MPFR_RNDU);pr("E0_upper",E0,MPFR_RNDU);pr("ratio_upper",R,MPFR_RNDU);pr("E1_upper",E1,MPFR_RNDU);pr("Y_lower",Y,MPFR_RNDD);pr("lhs_lower",lhs,MPFR_RNDD);pr("margin_lower",margin,MPFR_RNDD);int pass=mpfr_cmp_ui(margin,0)>0;printf("RESULT status=%s pass=%d\n",pass?"CERTIFIED":"PSC_CORE",pass);return pass?0:1;
}
