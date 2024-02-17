#include <stdio.h>
#include <stdlib.h>

int fill(int n, int* arr){
    if (!arr[n]){
        arr[n] = (fill(n-1, arr) << 2) - fill(n-2, arr);
    }
    return arr[n];
}

int main(){
    int* arr = (int*)calloc(16, sizeof(int));
    arr[0] = 1;
    arr[1] = 1;
    int n;
    while (1){
        scanf("%d", &n);
        if (n < 0){
            break;
        }
        else if (n & 1){
            printf("0\n");
        }
        else{
            printf("%d\n", fill((n >> 1) + 1, arr));
        }
    }
    free(arr);
    return 0;
}