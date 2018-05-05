#include <iostream>
#include <algorithm>
using namespace std;

template <typename T>
void insert_sort(T arr[], int size)
{
    // 从第二个元素开始循环遍历未排序数组
    for (int i = 1; i < size; i++)
    {
        int temp = arr[i];
        int j = i - 1; //已排序数组最大索引
        // 从后向前扫描已排序数组
        while (j >= 0)
        {
            if (arr[j] > temp)
                arr[j + 1] = arr[j];
            else
                break;
            j--;
        }
        arr[j + 1] = temp;
    }
}

int main()
{
    int arr[] = {61, 17, 29, 22, 34, 60, 72, 21, 50, 1, 62};
    int size = (int)sizeof(arr) / sizeof(*arr);
    insert_sort(arr, size);
    for (int i = 0; i < size; i++)
        cout << arr[i] << ' ';
    cout << endl;

    float arrf[] = {17.5, 19.1, 0.6, 1.9, 10.5, 12.4, 3.8, 19.7, 1.5, 25.4, 28.6, 4.4, 23.8, 5.4};
    size = (int)sizeof(arrf) / sizeof(*arrf);
    insert_sort(arrf, size);
    for (int i = 0; i < size; i++)
        cout << arrf[i] << ' ';
    return 0;
}
