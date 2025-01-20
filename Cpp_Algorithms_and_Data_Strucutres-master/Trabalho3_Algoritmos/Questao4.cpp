#include <iostream>
using namespace std;

void printArray(int arr[], int l) //procedimento de impressao do vetor
{
    int i = 0;

    do
    {
        cout<<arr[i]<<" ";

        i++;
    }
    while(i!=l);
}

int partition( int arr[],int begginer,  int last) //rotina de parti��o do vetor
{
    int i = begginer;
    int j;

    for(j = begginer; j < last; j++)
    {
        if (arr[j] >= arr[last])
        {
            swap(arr[i],arr[j]);

            i++;
        }
    }
    swap(arr[i], arr[last]);

    return i;
}

void quicksort(int arr[], const int begginer, const int last) //procedimento de ordena��o pelo m�todo quickSort
{
    if (begginer >= last)
    {
        return;
    }
    int pivot = partition(arr,begginer, last);

    quicksort(arr,begginer, pivot - 1); //execu��o deste m�todo para o vetor � esquerda
    quicksort(arr,pivot + 1, last); //execu��o deste m�todo para o vetor � direita
}

int main()
{
    int arr[]={11,33,22,99,55};

	int Size = sizeof(arr)/sizeof(arr[0]);

	cout<<"array before quickSort:"<<endl;
	printArray(arr, Size); //m�todo de impressao do vetor

	quicksort(arr,0,Size-1); //m�todo de ordena��o quickSort

    cout<<endl;

    cout<<"array after quickSort:"<<endl;
    printArray(arr, Size);

    return 0;
}
