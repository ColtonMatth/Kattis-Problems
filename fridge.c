//Name: Colton Matthews
//File: fridge.c
//Date: 10/14/2022

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct integers{
    char value;
    int amount;
};

int comparator(const void *a, const void *b){
    return ((struct integers*)a) -> amount - ((struct integers*)b) -> amount;
}

void print_character(char c, int n){
    char buffer[n + 1];
    for (int i = 0; i < n; i++){
        buffer[i] = c;
    }
    buffer[n] = '\0';
    printf("%s\n", buffer);
}

char least_width(struct integers* integer, int value){
    char least_value = '9';
    int index = 0;
    while (integer[index].amount == value && index < 10){
        if ((integer[index].value < least_value) && (integer[index].value != '0')){
            least_value = integer[index].value;
        }
        index++;
    }
    return least_value;
}

void lowest(struct integers* integer){
    if (integer[0].value == '0'){
        if (integer[0].amount == integer[1].amount){
            print_character(least_width(integer, integer[0].amount), integer[0].amount + 1);
        }
        else{
            printf("1");
            print_character('0', integer[0].amount + 1);
        }
    }
    else if(integer[0].amount == 0){
        printf("%c\n", least_width(integer, 0));

    }
    else{
        print_character(least_width(integer, integer[0].amount), integer[0].amount + 1);
    }
}

int main(){
    struct integers integer[10];
    for (int i = 0; i < 10; i++){
        integer[i].value = (char)('0' + i);
        integer[i].amount = 0;
    }
    char buffer[1001];
    scanf("%s", buffer);
    size_t len = strlen(buffer);
    for (int i = 0; i < len; i++){
        integer[buffer[i] - '0'].amount++;
    }
    qsort(integer, 10, sizeof(struct integers), comparator);
    lowest(integer);
    return 0;
}