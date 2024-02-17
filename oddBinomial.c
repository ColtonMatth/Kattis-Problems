//Name: Colton Matthews
//File: oddBinomial.c
//Date: 11/26/2022

#include <stdio.h>

typedef unsigned long long ll;

int bit(ll n){
    n -= (n >> 1) & 0x5555555555555555;
    n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333);
    n = (n + (n >> 4)) & 0x0f0f0f0f0f0f0f0f;
    return (int)((n * 0x0101010101010101) >> 56);
}

ll odds(ll n){
    return n < 2 ? n : 3 * odds(n >> 1) + (n%2 ? 1L << (bit(n - 1)) : 0L);
}

int main(){
    ll n;
    scanf("%llu", &n);
    printf("%llu\n", odds(n));
    return 0;
}