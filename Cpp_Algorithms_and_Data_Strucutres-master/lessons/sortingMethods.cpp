#include < iostream >
using namespace std;

void selectionSort(int arr[]) {
  for (int i = 0; i < 4; i++) {
    int min = i;

    for (int j = i + 1; j < 5; j++) {
      if (arr[j] < arr[min]) {
        min = j;
      }
    }
    if (min != i) {
      int temp = arr[min];
      arr[min] = arr[i];
      arr[i] = temp;
    }
  }
}

void insertionSort(int arr[]) {
  int key;
  int j = 0;
  for (int i = 1; i < 5; i++) {
    key = arr[i];
    j = i - 1;
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j = j - 1;
    }
    arr[j + 1] = key;
  }

}

void bubbleSort(int a[]) {
  for (int i = 0; i < 5; i++) {
    for (int j = 0; j < (5 - i - 1); j++) {
      if (a[j] > a[j + 1]) {
        int temp = a[j];
        a[j] = a[j + 1];
        a[j + 1] = temp;
      }
    }
  }
}

void merge(int arr[], int l, int m, int r) {
  int i = l;
  int j = m + 1;
  int k = l;

  /* create temp array */
  int temp[5];

  while (i <= m && j <= r) {
    if (arr[i] <= arr[j]) {
      temp[k] = arr[i];
      i++;
      k++;
    } else {
      temp[k] = arr[j];
      j++;
      k++;
    }

  }

  /* Copy the remaining elements of first half, if there are any */
  while (i <= m) {
    temp[k] = arr[i];
    i++;
    k++;

  }

  /* Copy the remaining elements of second half, if there are any */
  while (j <= r) {
    temp[k] = arr[j];
    j++;
    k++;
  }

  /* Copy the temp array to original array */
  for (int p = l; p <= r; p++) {
    arr[p] = temp[p];
  }
}

/* l is for left index and r is right index of the 
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) {
  if (l < r) {
    // find midpoint
    int m = (l + r) / 2;

    // recurcive mergesort first and second halves 
    mergeSort(arr, l, m);
    mergeSort(arr, m + 1, r);

    // merge
    merge(arr, l, m, r);
  }
}

// quick sort sorting algorithm
int Partition(int arr[], int s, int e)
{
 int pivot = arr[e];
 int pIndex = s;
 
 for(int i = s;i<e;i++)
 {
 if(arr[i]<pivot)
 {
 int temp = arr[i];
 arr[i] = arr[pIndex];
 arr[pIndex] = temp;
 pIndex++;
 }
 }
 
 int temp = arr[e];
 arr[e] = arr[pIndex];
 arr[pIndex] = temp;
 
 return pIndex;
}
 
void QuickSort(int arr[], int s, int e)
{
 if(s<e)
 {
 int p = Partition(arr,s, e);
 QuickSort(arr, s, (p-1));  // recursive QS call for left partition
 QuickSort(arr, (p+1), e);  // recursive QS call for right partition
 }
}

//end of the algorithm of sorting methods

int main() {

  int myarr[5];
  cout << "Enter 5 integers in random order: " << endl;
  for (int i = 0; i < 5; i++) {
    cin >> myarr[i];
  }

  cout << "UNSORTED ARRAY: " << endl;
  for (int i = 0; i < 5; i++) {
    cout << myarr[i] << "  ";
  }
  cout << endl;

  selectionSort(myarr); // sorting actually happening

  cout << "SORTED ARRAY: " << endl;
  for (int i = 0; i < 5; i++) {
    cout << myarr[i] << "  ";
  }

  //-----------------------------------------------------

  int myarray[5];
  cout << "Enter 5 integers in any order" << endl;
  for (int i = 0; i < 5; i++) {
    cin >> myarray[i];
  }

  cout << "Before Sorting: " << endl;
  for (int i = 0; i < 5; i++) {
    cout << myarray[i] << " ";
  }

  insertionSort(myarray);

  cout << endl << "After Sorting: " << endl;
  for (int i = 0; i < 5; i++) {
    cout << myarray[i] << " ";
  }

  //---------------------------------------------------------

  int myarray[5];
  int size;
  cout << "Enter 5 integers in any order: " << endl;
  for (int i = 0; i < 5; i++) {
    cin >> myarray[i];
  }
  cout << "Before Sorting" << endl;
  for (int i = 0; i < 5; i++) {
    cout << myarray[i] << " ";
  }

  bubbleSort(myarray); // sorting

  cout << endl << "After Sorting" << endl;
  for (int i = 0; i < 5; i++) {
    cout << myarray[i] << " ";
  }

//--------------------------------------------------------

int myarray[5];
  //int arr_size = sizeof(myarray)/sizeof(myarray[0]);
  int arr_size = 5;

  cout << "Enter 5 integers in any order: " << endl;
  for (int i = 0; i < 5; i++) {
    cin >> myarray[i];
  }
  cout << "Before Sorting" << endl;
  for (int i = 0; i < 5; i++) {
    cout << myarray[i] << " ";
  }
  cout << endl;
  mergeSort(myarray, 0, (arr_size - 1)); // mergesort(arr,left,right) called

  cout << "After Sorting" << endl;
  for (int i = 0; i < 5; i++) {
    cout << myarray[i] << " ";
  }

  //--------------------------------------------------------------------------

int size=0;
 cout<<"Enter Size of array: "<<endl;
 cin>>size;

 int myarray[size];
 
 cout<<"Enter "<<size<<" integers in any order: "<<endl;
 for(int i=0;i<size;i++)
 {
 cin>>myarray[i];
 }
 cout<<"Before Sorting"<<endl;
 for(int i=0;i<size;i++)
 {
 cout<<myarray[i]<<" ";
 }
 cout<<endl;
 
 QuickSort(myarray,0,(size-1));  // quick sort called
 
 cout<<"After Sorting"<<endl;
 for(int i=0;i<size;i++)
 {
 cout<<myarray[i]<<" ";
 }

  return 0;
}