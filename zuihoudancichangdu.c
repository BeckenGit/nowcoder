#include<stdio.h>
#define MAXSIZE 5000
int main(){
  char str[MAXSIZE];
  gets(str);
  //printf("%s\n", str);

  int lens = 0;
  while(str[lens] != '\0'){
    lens++;
  }
  int lastlens = 0;
  lens--;
  while(str[lens] != ' ' && lens >= 0){
    lens--;
    lastlens++;
  }
  printf("%d\n", lastlens);

  return 0;
}
