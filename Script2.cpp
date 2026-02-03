#include <stdio.h>
#include <math.h>

#include "counting_functions.hpp"

long double CountG(long double a, long double T)
{
    long double pi = 3.1416;
    long double g = ((4*pi*pi)/(T*T))*(a + 1/(12*a));
    //printf("g = %.6Lf, ", g);
    return g;
}

long double CountSigmaG(long double a, long double T)
{
    long double pi = 3.1416;
    long double sigmaT = 0.003;
    long double sigmaA = 0.0005;
    long double sigmaL = 0.0005;
    long double sigmaG = sqrtl(powl(8*pi*pi*powl(T, -3)*(a + 1/(12*a))*sigmaT, 2) +
                               powl(4*pi*pi*powl(T, -2)*(1 - 1/(12*a*a))*sigmaA, 2) +
                               powl(2*pi*pi*powl(T, -2)*(1/(3*a))*sigmaL, 2));
    //printf("sigmaG = %.6Lf, ", sigmaG);
    return sigmaG;
}

long double CountEpsG(long double g, long double sigmaG)
{
    long double epsG = sigmaG / g;
    //printf("epsG = %.6Lf\n", epsG * 100);
    return epsG;
}

long double CountT2a(long double T, long double a)
{
    long double T2a = T * T * a;
    //printf("T2a = %.6Lf, ", T2a * 4 / 25);
    return T2a;
}

long double CountSigmaT2a(long double T, long double a)
{
    long double sigmaT = 0.003;
    long double sigmaA = 0.5;
    long double sigmaT2a = sqrtl(powl(2*T*a*sigmaT, 2) + powl(T*T*sigmaA, 2));
    //printf("sigmaT2a = %.6Lf, ", sigmaT2a * 4 / 25);
    return sigmaT2a;
}

long double CountA2(long double T, long double a)
{
    long double a2 = a * a;
    //printf("a2 = %.0Lf, ", a2 * 3 / 2000);
    return a2;
}

long double CountSigmaA2(long double a)
{
    long double sigmaA = 0.5;
    long double sigmaA2 = 2 * a * sigmaA;
    //printf("sigmaA2 = %.4Lf, ", sigmaA2 * 3 / 2000);
    return sigmaA2;
}
