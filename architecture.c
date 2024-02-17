//Name: Colton Matthews
//File: architecture.c
//Date: 9/8/2022
#include<stdio.h>
#include<math.h>

int R, C; //variable of amount of rows and columns for the grid. 

int a[100], b[100]; //Declare array in size R and C integers.

int max(int num1, int num2){
    return (num1 > num2) ? num1 : num2;
}

int main() {// driver function
    scanf("%d %d", &R, &C);
    int max_row = 0;
    int max_column = 0;
    for (int i=1; i <= R; i++){
        scanf("%d", &a[i]), max_row = max(max_row, a[i]);
    }
    for(int j = 1; j <= C; j++){
        scanf("%d", &b[j]), max_column = max(max_column, b[j]);
    }

    if(max_row == max_column){
        printf("possible\n");
    }
    else{
        printf("impossible\n");
    }
    return 0;
}
