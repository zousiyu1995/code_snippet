#include <iostream>
#include <algorithm>
using namespace std;

template <typename T>
int partition(T arr[], int low, int high)
{
    int pivot = arr[high]; // 挑最后一个元素做 pivot
    int storeIndex = low - 1;

    // 遍历数组
    for (int j = low; j < high; j++)
    {
        if (arr[j] <= pivot)
        {
            storeIndex++; // 移动储存点
            swap(arr[storeIndex], arr[j]);
        }
    }
    // 将 pivot 放到两个子数组中间
    swap(arr[storeIndex + 1], arr[high]);

    return (storeIndex + 1); // 返回索引
}

template <typename T>
void quick_sort(T arr[], int low, int high)
{
    // 数组尺寸大于1
    if (low < high)
    {
        int p = partition(arr, low, high);
        quick_sort(arr, low, p - 1);
        quick_sort(arr, p + 1, high);
    }
}

int main()
{
    int arr[] = {61, 17, 29, 22, 34, 60, 72, 21, 50, 1, 62, 99, 90};
    int size = (int)sizeof(arr) / sizeof(*arr);
    quick_sort(arr, 0, size - 1);
    for (int i = 0; i < size; i++)
        cout << arr[i] << ' ';
    cout << endl;

    float arrf[] = {17.5, 19.1, 0.6, 1.9, 10.5, 12.4, 3.8, 19.7, 1.5, 25.4, 28.6, 4.4, 23.8, 5.4};
    size = (int)sizeof(arrf) / sizeof(*arrf);
    quick_sort(arrf, 0, size - 1);
    for (int i = 0; i < size; i++)
        cout << arrf[i] << ' ';
    return 0;
}
