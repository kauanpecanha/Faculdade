#include<iostream>
using namespace std;

void merge(int array[], int const left, int const mid, int const right) 
{
    auto const subArrayOne = mid - left + 1;
    auto const subArrayTwo = right - mid;
 
    // Create temp arrays
    auto *leftArray = new int[subArrayOne],
         *rightArray = new int[subArrayTwo];
 
    // Copy data to temp arrays leftArray[] and rightArray[]
    for (auto i = 0; i < subArrayOne; i++)
        leftArray[i] = array[left + i];
    for (auto j = 0; j < subArrayTwo; j++)
        rightArray[j] = array[mid + 1 + j];
 
    auto indexOfSubArrayOne
        = 0, // Initial index of first sub-array
        indexOfSubArrayTwo
        = 0; // Initial index of second sub-array
    int indexOfMergedArray
        = left; // Initial index of merged array
 
    // Merge the temp arrays back into array[left..right]
    while (indexOfSubArrayOne < subArrayOne
           && indexOfSubArrayTwo < subArrayTwo) {
        if (leftArray[indexOfSubArrayOne]
            <= rightArray[indexOfSubArrayTwo]) {
            array[indexOfMergedArray]
                = leftArray[indexOfSubArrayOne];
            indexOfSubArrayOne++;
        }
        else {
            array[indexOfMergedArray]
                = rightArray[indexOfSubArrayTwo];
            indexOfSubArrayTwo++;
        }
        indexOfMergedArray++;
    }
    // Copy the remaining elements of
    // left[], if there are any
    while (indexOfSubArrayOne < subArrayOne) {
        array[indexOfMergedArray]
            = leftArray[indexOfSubArrayOne];
        indexOfSubArrayOne++;
        indexOfMergedArray++;
    }
    // Copy the remaining elements of
    // right[], if there are any
    while (indexOfSubArrayTwo < subArrayTwo) {
        array[indexOfMergedArray]
            = rightArray[indexOfSubArrayTwo];
        indexOfSubArrayTwo++;
        indexOfMergedArray++;
    }
    delete[] leftArray;
    delete[] rightArray;
}
int partition(int arr[], int low, int high)
{
    int pivot = arr[high]; // pivot
    int i
        = (low
           - 1); // Index of smaller element and indicates
                 // the right position of pivot found so far
 
    for (int j = low; j <= high - 1; j++) {
        // If current element is smaller than the pivot
        if (arr[j] < pivot) {
            i++; // increment index of smaller element
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}



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
    } 
} 
void selectionSort(int arr[], int n) //seleção do menor, e seu destino à esquerda
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
    }
}
void bubbleSort(int arr[], int n) //permutação aos pares
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
    }
}
void mergeSort(int array[], int const begin, int const end)//divisão e conquista
{ //time complexity: O(n log2 n)
    if (begin >= end)
        return; // Returns recursively
 
    auto mid = begin + (end - begin) / 2;
    mergeSort(array, begin, mid);
    mergeSort(array, mid + 1, end);
    merge(array, begin, mid, end);
}
void quickSort(int arr[], int low, int high) //pivot - menores à esquerda, maiores, à direita
{ //time complexity: O(n log2 n)
    if (low < high) {
        /* pi is partitioning index, arr[p] is now
        at right place */
        int pi = partition(arr, low, high);
 
        // Separately sort elements before
        // partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
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



// arquivo que estava no testing.cpp

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