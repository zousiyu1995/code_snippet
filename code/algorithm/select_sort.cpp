#include <iostream>
#include <algorithm>
using namespace std;

template <typename T>
void select_sort(T arr[], int size)
{
    for (int i = 0; i < size - 1; i++)
    {
        // 假设最小元素为未排序部分的第一个
        int min = i;
        // 遍历未排序部分
        for (int j = i + 1; j < size; j++)
        {
            // 找到当前循环内的最小值
            if (arr[j] < arr[min])
            {
                min = j;
            }
        }
        swap(arr[i], arr[min]);
    }
}

int main()
{
    int arr[] = {61, 17, 29, 22, 34, 60, 72, 21, 50, 1, 62};
    int size = (int)sizeof(arr) / sizeof(*arr);
    select_sort(arr, size);
    for (int i = 0; i < size; i++)
        cout << arr[i] << ' ';
    cout << endl;

    float arrf[] = {17.5, 19.1, 0.6, 1.9, 10.5, 12.4, 3.8, 19.7, 1.5, 25.4, 28.6, 4.4, 23.8, 5.4};
    size = (int)sizeof(arrf) / sizeof(*arrf);
    select_sort(arrf, size);
    for (int i = 0; i < size; i++)
        cout << arrf[i] << ' ';
    return 0;
}