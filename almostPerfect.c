//Name: Colton Matthews
//File: almostPerfect.c
//Date: 11/8/2022

#include <stdio.h>
#include <math.h>

void perfect(int n){
    int square = (int)sqrt(n) + 1;
    int sum = 1;
    for (int i = 2; i < square; i++){
        if (n % i == 0){
            int proper = n / i;
            if (i != proper){
                sum += proper;
            }
            sum += i;
        }
    }
    printf(sum == n ? "%d perfect\n" : (abs(sum - n) < 3) ? "%d almost perfect\n" : "%d not perfect\n", n);
}

int main(){
    int n;
    while (scanf("%d", &n) == 1){
        perfect(n);
    }
    return 0;
}