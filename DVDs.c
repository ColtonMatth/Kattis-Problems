//Name: Colton Matthews
//File: DVDs.c
//Date: 10/14/2022

#include <stdio.h>

int minimal_run(int n){
    int instances = 1;
    int next;

    for (int i = 0; i < n; i++){
        scanf("%d", &next);
        if (instances == next){
            instances++;
        }
    }
    return n - instances + 1;
}

int main(){
    int n;
    scanf("%d", &n);
    while(n--){
        int len;
        scanf("%d", &len);
        printf("%d\n", minimal_run(len));
    }
    return 0;
}