//Name: Colton Matthews
//File: divideby100.c
//Date: 9/23/2022

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void equal_length(char* num, int num_len, int div_len) {
    while (num[num_len - 1] == '0') num_len--;
    if (num_len == 1) {
        printf("%c\n", num[0]);
    }
    else {
        printf("%c.",num[0]);
        printf("%.*s\n", num_len - 1, num + 1);
    }
}

void less_length(char* num, int num_len, int div_len) {
    printf("0.");
    if (div_len - num_len > 1) printf("%0*d", div_len - num_len - 1, 0);
    while (num[num_len - 1] == '0') num_len--;
    printf("%.*s\n", num_len, num);
}

void greater_length(char* num, int num_len, int div_len) {
    int padded = 0;
    while (num[num_len - 1] == '0' && padded < div_len - 1) {
        num_len--;
        padded++;
    }
    if (padded == div_len - 1) {
        printf("%.*s\n", num_len, num);
    } 
    else {
        int int_part_len = num_len + padded - div_len + 1;
        printf("%.*s.", int_part_len, num);
        printf("%.*s\n",  div_len - 1 - padded, num + int_part_len);
    }
}

void read(char **n, int *lN, int *lM) {
    size_t x = 0;
    *lN = (int)getline(n, &x, stdin) - 1;
    x = 0;
    char* tmp;
    *lM = (int)getline(&tmp, &x, stdin) - 1;
    free(tmp);
}

int main(void) {
    char *n;
    int lineN, lineM;
    read(&n, &lineN, &lineM);
    if (lineN == lineM) equal_length(n, lineN, lineM);
    else if (lineN < lineM) less_length(n, lineN, lineM);
    else greater_length(n, lineN, lineM);
    free(n);
    return 0;
}