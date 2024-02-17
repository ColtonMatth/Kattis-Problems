//Name: Colton Matthews
//File: unionFind.c
//Date: 10/1/2022

#include <stdio.h>
#include <stdlib.h>

int* parent;
int* size;

int find(int p){
    int root = p;
    while(root != parent[root]){
        root = parent[root];
    }
    while (p != root){
        int _p = parent[p];
        parent[p] = root;
        p = _p;
    }
    return root;
}

int connected(int p, int q){
    return find(p) == find(q);
}

void Union(int p, int q){
    int root_p = find(p), root_q = find(q);
    if (root_p != root_q){

        if (size[root_p] < size[root_q]) {
            parent[root_p] = root_q;
            size[root_q] += size[root_p];
        }

        else {
            parent[root_q] = root_p;
            size[root_p] += size[root_q];
        }
    }
}

int main(){
    int length, query;
    scanf("%d %d", &length, &query);
    if (query){
        size = (int*)malloc((size_t)(length << 3));
        parent = size + length;

        for (int i = 0; i < length; i++){
            size[i] = 1;
            parent[i] = i;
        }

        char operator;
        int p, q;
        while(query > 0){
            scanf(" %c %d %d", &operator, &p, &q);
            if (operator == '='){
                Union(p, q);
            }
            else{
                printf(connected(p, q) ? "yes\n" : "no\n");
            }
            query--;
        }
    }
    free(size);
    return 0;
}
