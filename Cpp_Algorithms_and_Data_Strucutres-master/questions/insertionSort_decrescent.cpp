#include<iostream>
using namespace std;


void insertionSort(int data[], int n) //exemplo da ordenação de cartas do baralho 
{ //time complexity: O(n²)
    int i, j;
    for(i = 1; i<n; i++)
    {
        int tmp = data[i];

        for(j = i; j>0 && tmp>data[j-1]; j--)
        {
            data[j] = data[j-1];
        }
        data[j] = tmp;
    } 
}

int main(){
    int n;
    int arr[5];
    cout<<"Enter 5 integers in any order: "<<endl;

    for(int n = 0; n<5; n++){
        cin>>arr[n];
    }

    cout<<"Before sorting:"<<endl;
    for(int n = 0; n<5; n++){
        cout<<arr[n]<<" ";
    }

    insertionSort(arr, 5);

    cout<<endl<<endl<<"After sorting:"<<endl;
    for(int n = 0; n<5; n++){
        cout<<arr[n]<<" ";
    }

    return 0;
}