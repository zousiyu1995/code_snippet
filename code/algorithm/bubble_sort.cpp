#include <iostream>
#include <algorithm>
using namespace std;

template <typename T>
void bubble_sort(T arr[], int size)
{
    int i, j;
    for (i = 0; i < size - 1; i++)
        for (j = 0; j < size - 1 - i; j++)
            if (arr[j] > arr[j + 1])
                swap(arr[j], arr[j + 1]);
}

int main()
{
    int arr[] = {61, 17, 29, 22, 34, 60, 72, 21, 50, 1, 62};
    int size = (int)sizeof(arr) / sizeof(*arr);
    bubble_sort(arr, size);
    for (int i = 0; i < size; i++)
        cout << arr[i] << ' ';
    cout << endl;

    float arrf[] = {17.5, 19.1, 0.6, 1.9, 10.5, 12.4, 3.8, 19.7, 1.5, 25.4, 28.6, 4.4, 23.8, 5.4};
    size = (int)sizeof(arrf) / sizeof(*arrf);
    bubble_sort(arrf, size);
    for (int i = 0; i < size; i++)
        cout << arrf[i] << ' ';
    return 0;
}