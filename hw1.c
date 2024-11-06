#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void insertion_sort(double arr[], int n);
void quick_sort(double arr[], int n);
void print_arr(double arr[], int n);
void print_min_max(double arr[], int n);

int main() {
    int arr_idx = 0, buffer_idx = 0, space = 1, n = 2000, bn = 20;
    double arr[n];
    char input;
    char buffer[bn];

    for (int i = 0; i < bn; ++i) buffer[i] = '\0';

    FILE* f = fopen("test1.txt", "r");

    while ((input = fgetc(f)) != EOF) {
        if (input == ' ' && space != 1 && arr_idx < n) {
            arr[arr_idx++] = atof(buffer);
            space = 1;
            buffer_idx = 0;
            for (int i = 0; i < bn; ++i) buffer[i] = '\0';
        }
        else if (buffer_idx < bn - 1) {
            buffer[buffer_idx++] = input;
            space = 0;
        }
    }

    fclose(f);

    if (arr_idx < n)
        arr[arr_idx++] = atof(buffer);
    space = 1;
    buffer_idx = 0;

    for (int i = 0; i < bn; ++i) buffer[i] = '\0';

    printf("Please enter a number to tell me what to do: \n");
    printf("(1) Quick sort\n");
    printf("(2) Insertion sort\n");
    printf("(3) Exit\n");

    while (1) {
        input = getchar();
        if (input == '1') {
            quick_sort(arr, arr_idx);
            print_arr(arr, arr_idx);
            print_min_max(arr, arr_idx);
            break;
        }
        else if (input == '2') {
            insertion_sort(arr, arr_idx);
            print_arr(arr, arr_idx);
            print_min_max(arr, arr_idx);
            break;
        }
        else if (input == '3') break;
        else if (input == ' ' || input == '\r' || input == '\n' || input == '\t') continue;
        else printf("Please enter 1 or 2 or 3\n");
    }
}

void insertion_sort(double arr[], int n) {
    for (int i = 1; i < n; ++i) {
        double current = arr[i];
        int j = i - 1;
        while (j >= 0 && current < arr[j]) {
            arr[j + 1] = arr[j];
            --j;
        }
        arr[j + 1] = current;
    }
}

void quick_sort(double arr[], int n) {
    if (n <= 1) return;
    else {
        int s_idx = 0, p_idx = 0;

        for (int i = 1; i < n; ++i) {
            if (arr[i] < arr[p_idx]) {
                if (s_idx == p_idx) p_idx = i;

                double tmp = arr[s_idx];
                arr[s_idx++] = arr[i];
                arr[i] = tmp;
            }
        }

        double tmp = arr[p_idx];
        arr[p_idx] = arr[s_idx];
        arr[s_idx] = tmp;
        
        quick_sort(arr, s_idx);
        quick_sort(arr + s_idx + 1, n - s_idx - 1);
    }
}

void print_arr(double arr[], int n) {
    for (int i = 0; i < n; ++i) {
        if (i == 0) printf("%.2lf", arr[i]);
        else printf(" %.2lf", arr[i]);
    }
    printf("\n");
}

void print_min_max(double arr[], int n) {
    if (n <= 0) return;
    else {
        printf("Numbers: %d\n", n);
        printf("Smallest number: %.2lf\n", arr[0]);
        printf("Biggest number: %.2lf\n", arr[n - 1]);
    }
}