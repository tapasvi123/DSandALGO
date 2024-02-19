#include <stdio.h>
void sort(int a[],  int l){
    // Edge case: if only one element:
        if (l==1){
            return; 
        }

    //Main Recursive block: Moving the largest element to the end
        for(int i=0;i<l-1;i++){
            if (a[i]>a[i+1]){
                // Swap
                int temp=a[i+1];
                a[i+1]=a[i];
                a[i]=temp;
            }
        }

    //recursive calling
        sort(a, l-1);
}
int main(){
    int arr[]={5,4,3,2,1,6};
    int size= sizeof(arr)/sizeof(arr[0]);
    sort(arr, size);
    for(int i=0; i<size; i++){
        printf("%d ", arr[i]);
    }
    return 0;
}


// 5 4 3 2 1 
// 4 5



