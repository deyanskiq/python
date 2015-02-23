#include <iostream>
#include <math.h>
using namespace std;
double fill_tetrahedron(int  num)
  { 
   
      return (sqrt(2) * pow(num, 3))/12000;
      }
    int main ()
{   int num;
cout << "Enter the length of the edge: " ; 
  cin>>num;     
          cout << fill_tetrahedron(num)<<endl;              
                          
    system ("pause");
    return 0;
}

