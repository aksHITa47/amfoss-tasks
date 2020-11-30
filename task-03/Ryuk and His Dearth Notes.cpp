#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int getMin(int arr[], int n)
{
    int res = arr[0];
    for (int i = 1; i < n; i++)
        res = min(res, arr[i]);
    return res;
}

int main()
{
    int N , array1[1000000], array2[1000000], array3[1000000],i;
    cin>>N;
    for(i=0;i<N;i++){
        cin>>array1[i];
    }
    
    for(i=0;i<N;i++){
        cin>>array2[i];
    }

    
    for(i=0;i<N;i++){
        array3[i] = array2[i] / array1[i];
    }
    
    
    //cout<<"\n";
    
    cout <<getMin(array3, N);
   
  return 0;
}

       

       
