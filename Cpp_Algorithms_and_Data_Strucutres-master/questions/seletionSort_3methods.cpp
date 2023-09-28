#include<iostream>
using namespace std;


void insertionSort(int data[], int n) //exemplo da ordenação de cartas do baralho 
{ //time complexity: O(n²)
    int i, j;
    for(i = 1; i<n; i++)
    {
        int tmp = data[i];

        for(j = i; j>0 && tmp<data[j-1]; j--)
        {
            data[j] = data[j-1];
        }
        data[j] = tmp;

        cout<<endl<<endl;
        for(int k = 0; k<5; k++)
        {
            cout<<data[k]<<" ";
        }
        system("pause");
    } 
}

void selectionSort(int data[], int n) //seleção do menor, e seu destino à esquerda
{//time complexity: O(n²)
    for(int i  = 0; i<n-1; i++)
    {
        for(int j = n-1; j>i; --j)
        {
            if(data[j]<data[j-1])
            {
                swap(data[j], data[j-1]);
            }
        }
    cout<<endl<<endl;
    for(int k = 0; k<5; k++)
    {
        cout<<data[k]<<" ";
    }
    system("pause");
    }
}
void bubbleSort(int data[], int n) //permutação aos pares
{//time complexity: O(n²)
    for(int i = 0; i< n-1; i++)
    {
        for(int j = n-1; j>i; --j)
        {
            if(data[j]<data[j-1])
            {
                swap(data[j], data[j-1]);
            }
        }
    cout<<endl;
    for(int k = 0; k<5; k++)
    {
        cout<<data[k]<<" ";
    }
    system("pause");
    }
}


int main(){
    int n;
    int arr[5];
    cout<<"Enter 5 integers in any order(6, 2, 4, 3, 9): "<<endl;

    for(int n = 0; n<5; n++)
    {
        cin>>arr[n];
    }

    cout<<"Before sorting:"<<endl;
    for(int n = 0; n<5; n++)
    {
        cout<<arr[n]<<" ";
    }

    cout<<"Insertion Sort Method"<<endl<<endl;
    system("pause");

    insertionSort(arr, 5);

    cout<<"Selection Sort Method"<<endl<<endl;
    system("pause");

    selectionSort(arr, 5);

    cout<<"Bubble Sort Method"<<endl<<endl;
    system("pause");

    bubbleSort(arr, 5);

    return 0;
}