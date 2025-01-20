#include <iostream>
#include <algorithm>
using namespace std;

int partition(int arr[], int beggining, int last)
{
    int i = beggining;
    int j = last;
    int pivot = arr[beggining];
    while(i < j)
    {
        while(pivot >= arr[i])
        {
            i++;
        }
        while(pivot < arr[j])
        {
            j--;
        }
        if(i < j)
        {
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[beggining], arr[j]);
    return j;
}

void quickSort(int arr[], int beggining, int last)
{
    if (beggining<last)
    {
        int pivot = partition(arr, beggining, last);

        quickSort(arr, beggining, pivot - 1); //chamada recursiva para o subvetor à esquerda do pivo
        quickSort(arr, pivot + 1, last); //chamada recursiva para o subvetor à direita do pivo
    }
}

void printArray(int arr[], int size)
{
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
}

int main()
{
    int arr[] = {11, 88, 44, 33, 22, 66, 77, 55, 99};


    int size = sizeof(arr) / sizeof(int);

    cout<<"Before Sorting"<<endl;
    printArray(arr, size);

    cout<<endl<<endl;

    quickSort(arr, 0, size - 1);

    cout<<"After Sorting"<<endl;
    printArray(arr, size);

    return 0;
}
