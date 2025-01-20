#include <iostream>
using namespace std;

int findMinor(int v[], int index, int new_size)
{
    if (index == new_size)
    {
    	return index;
	}

    int m = findMinor(v, index + 1, new_size);


 	if(v[index]<v[m])
 	{
 	    return index;
    }
    else
    {
        return m;
    }
}

void selectionSort(int v[], int Size, int index = 0)
{

    if (index == Size)
    {
    	 return;
	}


    int m = findMinor(v, index, Size-1);


    if (m != index)
    {
        swap(v[m], v[index]);
	}

    selectionSort(v, Size, index + 1);
}

void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}


int main()
{
    int vet[] = {88, 66, 55, 22, 11, 99};

    int Size = sizeof(vet)/sizeof(vet[0]);

    cout<<"original array:"<<endl;

    printArray(vet, Size);

    selectionSort(vet, Size);

    cout<<"sorted array:"<<endl;

    printArray(vet, Size);

    return 0;
}
