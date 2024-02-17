//Name: Colton Matthews
//File: tildes.c
//Date: 10/2/2022

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int root(int* p, int a){
    while(p[a] >= 0){
        a = p[a];
    }
    return a;
}

void connect(int* p, int a, int b){
    int root_a = root(p, a), root_b = root(p, b);
    if (root_a == root_b){
        return;
    }
    if (p[root_a] > p[root_b]){
        root_a ^= root_b ^= root_a ^= root_b;
    }
    p[root_a] += p[root_b];
    p[root_b] = root_a;
}

int size(int* p, int a){
    return -p[root(p, a)];
}

int main(){
    int n, q, a, b;
    char c;
    scanf("%d %d", &n, &q);
    int arr[n];
    memset(arr, 0xFF, n*sizeof(int));
    while(q--){
        scanf(" %c %d", &c, &a);
        if (c == 't'){
            scanf("%d", &b);
            connect(arr, a-1, b-1);
        }
        else{
            printf("%d\n", size(arr, a-1));
        }
    }
    return 0;
}