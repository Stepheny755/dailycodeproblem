#include <time.h>
#include <iostream>

#define NSTOMSCONV 10000000

using namespace std;

int sleep(int dur){
  struct timespec t1;
  t1.tv_nsec=NSTOMSCONV*dur;
  if(nanosleep(&t1,NULL)<0){
    return 0;
  }
  return 1;
}

void f(){
  cout << "f";
}

int main(){
  if(sleep(1)==1){
    f();
  }

  return 0;
}
