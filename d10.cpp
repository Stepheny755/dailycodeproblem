#include <time.h>
#include <ctime>
#include <iostream>

#define NSTOMSCONV 1000000

using namespace std;

int sleep(int dur){
  struct timespec t1;
  t1.tv_sec=0;
  t1.tv_nsec=NSTOMSCONV*dur;
  cout << t1.tv_nsec;
  if(nanosleep(&t1,NULL)<0){
    return 0;
  }
  return 1;
}

void f(){
  int a = 1;
  for(int i = 0;i < 1000;i++){
    a *= 2;
    cout << a;
  }
  cout << "f" << endl;
}

int main(){
  clock_t start_time = clock();
  
  sleep(1);
  f();
  clock_t done_time = clock();
  printf("%g",(double)(done_time-start_time));
  printf("%g",(double)(done_time-start_time)/CLOCKS_PER_SEC);
  return 0;
}
