#include <stdio.h>

void reversed_list(int num_list[], int start, int end) {
    while (start < end) {
        int temp = num_list[start];
        num_list[start] = num_list[end];
        num_list[end] = temp;

        start++;
        end--;
    }
}

int main() {
    int N, K;
    scanf("%d %d", &N, &K);

    int A1, A2, B1, B2;
    scanf("%d %d", &A1, &A2);
    scanf("%d %d", &B1, &B2);

    int num_list[N];
    for (int i = 0; i < N; i++) {
        num_list[i] = i + 1;
    }

    for (int i = 0; i < K; i++) {
        reversed_list(num_list, A1 - 1, A2 - 1);
        reversed_list(num_list, B1 - 1, B2 - 1);
    }

    for (int i = 0; i < N; i++) {
        printf("%d\n", num_list[i]);
    }

    return 0;
}