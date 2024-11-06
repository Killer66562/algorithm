#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

#define N 100
#define R_MIN -9999
#define R_MAX 9999

void print_arr(int arr[], int n);
void bucket_sort(int arr[], int n, int b_size);

typedef struct {
    size_t size;
    int* head;
} array;

int resize_array(array arr, size_t n) {
    int* new_head = (int*)malloc(n);
    if (new_head != NULL) {
        arr.head = new_head;
        arr.size = n;
        return 0;
    }
    else return -1;
}

void array_get(array arr, int i) {
    return *(arr.head + i);
}

int main() {
    srand((unsigned int)time(NULL));

    int arr[N];
    for (int i = 0; i < N; ++i) arr[i] = rand() % (R_MAX - R_MIN + 1) + R_MIN;
    print_arr(arr, N);

    return 0;
}

void print_arr(int arr[], int n) {
    for (int i = 0; i < n; ++i) {
        if (i > 0) printf(" %d", arr[i]);
        else if (i < 0) return;
        else printf("%d", arr[i]);
    }
}

void bucket_sort(int arr[], int n, int b_size) {
    int* buckets[b_size];
    int size_per_bucket[b_size];
    int contents_per_bucket[b_size];
    int largest = INT_MIN;

    for (int i = 0; i < n; ++i) if (arr[i] > largest) largest = arr[i];
    int sep = largest / b_size;
    for (int i = 0; i < n; ++i) {
        int div = arr[i] / sep;
        if (div < b_size) node_insert(buckets[div], arr[i]);
        else node_insert(buckets[b_size - 1], arr[i]);
    }
    for (int i = 0; i < b_size; ++i) node_insertion_sort(buckets[i], b_size);
}

