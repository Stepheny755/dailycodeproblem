#include <time.h>
#include <ctime>
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
  clock_t start_time = clock();
  if(sleep(1)==1){
    f();
  }
  clock_t done_time = clock();
  cout << (double)(done_time-start_time)/(CLOCKS_PER_SEC);
  cout << (double)(done_time-start_time);
  return 0;
}
