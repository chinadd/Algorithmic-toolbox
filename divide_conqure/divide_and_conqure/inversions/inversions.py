# Uses python3
"""#include <bits/stdc++.h>
 
int  _mergeSort(int arr[], int temp[], int left, int right);
int merge(int arr[], int temp[], int left, int mid, int right);
 
/* This function sorts the input array and returns the
   number of inversions in the array */
int mergeSort(int arr[], int array_size)
{
    int *temp = (int *)malloc(sizeof(int)*array_size);
    return _mergeSort(arr, temp, 0, array_size - 1);
}
 
/* An auxiliary recursive function that sorts the input array and
  returns the number of inversions in the array. */
int _mergeSort(int arr[], int temp[], int left, int right)
{
  int mid, inv_count = 0;
  if (right > left)
  {
    /* Divide the array into two parts and call _mergeSortAndCountInv()
       for each of the parts */
    mid = (right + left)/2;
 
    /* Inversion count will be sum of inversions in left-part, right-part
      and number of inversions in merging */
    inv_count  = _mergeSort(arr, temp, left, mid);
    inv_count += _mergeSort(arr, temp, mid+1, right);
 
    /*Merge the two parts*/
    inv_count += merge(arr, temp, left, mid+1, right);
  }
  return inv_count;
}
 
/* This funt merges two sorted arrays and returns inversion count in
   the arrays.*/
int merge(int arr[], int temp[], int left, int mid, int right)
{
  int i, j, k;
  int inv_count = 0;
 
  i = left; /* i is index for left subarray*/
  j = mid;  /* i is index for right subarray*/
  k = left; /* i is index for resultant merged subarray*/
  while ((i <= mid - 1) && (j <= right))
  {
    if (arr[i] <= arr[j])
    {
      temp[k++] = arr[i++];
    }
    else
    {
      temp[k++] = arr[j++];
 
     /*this is tricky -- see above explanation/diagram for merge()*/
      inv_count = inv_count + (mid - i);
    }
  }
 
  /* Copy the remaining elements of left subarray
   (if there are any) to temp*/
  while (i <= mid - 1)
    temp[k++] = arr[i++];
 
  /* Copy the remaining elements of right subarray
   (if there are any) to temp*/
  while (j <= right)
    temp[k++] = arr[j++];
 
  /*Copy back the merged elements to original array*/
  for (i=left; i <= right; i++)
    arr[i] = temp[i];
 
  return inv_count;
}
 
/* Driver progra to test above functions */
int main(int argv, char** args)
{
  int arr[] = {1, 20, 6, 4, 5};
  printf(" Number of inversions are %d \n", mergeSort(arr, 5));
  getchar();
  return 0;
}
"""
import sys
def merge_sort(a,b,left,right):
    count=0
    mid=0
    if right>left:
        mid=(left + right+1) // 2
        count += merge_sort(a,b,left,mid-1)
        count += merge_sort(a,b,mid,right)
        count += merge(a,b,left,mid,right)
    return count

def merge(a,b,left,mid,right):
    count=0
    i=left
    j=mid
    k=left
    
    while ((i<=mid-1) and (j<=right)):
        if a[i]<=a[j]:
            b[k]=a[i]
            k +=1
            i +=1
        else:
            b[k]=a[j]
            k +=1
            j +=1
            count += mid-i
    while i<=mid-1:
        b[k]=a[i]
        k +=1
        i +=1
    while j<=right:
        b[k]=a[j]
        k +=1
        j +=1
    for i in range(left,right+1):
        #print (i)
        #print (k)
        a[i]=b[i]
        
    return count
    
def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        if a[right]< a[left]:
            number_of_inversions +=1
        return number_of_inversions
    ave = (left + right+1) // 2
    
    """
    print ("left")
    print (left)
    print ("right")
    print (right)
    print ("ave")
    print (ave)"""
    
    for i in range(left,ave):
        for j in range(ave,right+1):
            if a[j] < a[i]:
                number_of_inversions +=1
                #print ("number of inversions")
                #print(number_of_inversions)
    number_of_inversions += get_number_of_inversions(a, b, left, ave-1)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    #print(get_number_of_inversions(a, b, 0, len(a)-1))
    print(merge_sort(a, b, 0, len(a)-1))
