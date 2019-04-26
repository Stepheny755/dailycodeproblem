#include <time.h>

#DEFINE NSTOMSCONV = 100000

using namespace std;

int sleep(int dur){
  struct timspec t1;
  t1.tv_nsec=NSTOMSCONV*dur;
  if(nanosleep(&t1,NULL)<0){
    return 0
  }
  return 1
}

void f(){
  print("f");
}

int main(){

  if(sleep(1)==1){
    f()
  }

  return 0;
}
