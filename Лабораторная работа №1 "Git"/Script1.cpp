#include <stdio.h>
#include <math.h>

#include "counting_functions.hpp"

int main()
{
    long double a[] =
    {
        0.200,
        0.230,
        0.250,
        0.270,
        0.300,
        0.320,
        0.350,
        0.380,
        0.410
    };
    
    long double T[] =
    {
        1.576,
        1.541,
        1.530,
        1.527,
        1.522,
        1.522,
        1.531,
        1.547,
        1.572
    };
    
//    long double g = 0;
//    long double sigmaG = 0;
//    long double epsG = 0;
//    long double T2a = 0;
//    long double a2 = 0;
//    long double sigmaT2a = 0;
//    long double sigmaA2 = 0;
    
    long double avT2a3 = 0;
    long double avA2 = 0;
    long double avT2a = 0;
    long double avA4 = 0;
    long double avT4a2 = 0;
    
    for (int i = 0; i < 9; i++) {
//        a2 = CountA2(T[i], a[i]);
//        sigmaA2 = CountSigmaA2(a[i]);
//        T2a = CountT2a(T[i], a[i]);
//        sigmaT2a = CountSigmaT2a(T[i], a[i]);
//        g = CountG(a[i] * 0.001, T[i]);
//        sigmaG = CountSigmaG(a[i] * 0.001, T[i]);
//        epsG = CountEpsG(g, sigmaG);
        
        avT2a3 += T[i]*T[i]*a[i]*a[i]*a[i];
        avA2 += a[i]*a[i];
        avT2a += T[i]*T[i]*a[i];
        avA4 += a[i]*a[i]*a[i]*a[i];
        avT4a2 += T[i]*T[i]*T[i]*T[i]*a[i]*a[i];
    }
    
    avT2a3 /= 9;
    avA2 /= 9;
    avT2a /= 9;
    avA4 /= 9;
    avT4a2 /= 9;
    
    long double b = (avT2a3 - avA2 * avT2a)/(avA4 - avA2 * avA2);
    long double k = avT2a - b * avA2;
    long double sigmaB = (1/3)*sqrtl((avT4a2 - avT2a * avT2a)/(avA4 - avA2*avA2) - b*b);
    long double sigmaK = sigmaB*sqrtl(avA4 - avA2 * avA2);
    
    printf("b = (%.6Lf+-%.10Lf), k = (%.6Lf+-%.6Lf)\n", b, sigmaB, k, sigmaK);
    printf("avT2a3 = %.6Lf\n", avT2a3);
    printf("avA2 = %.6Lf\n", avA2);
    printf("avT2a = %.6Lf\n", avT2a);
    printf("avA4 = %.6Lf\n", avA4);
    printf("avT4a2 = %.6Lf\n", avT4a2);
    
    return 0;
}
