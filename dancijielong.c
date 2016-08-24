#include<stdio.h>
#include<malloc.h>
#define MAXNUM 200
#define MAXCHAR 11
int jobend(int* state, int size){
  int j;
  for(j = 0; j < size; j++){
    if(state[j] == 0)
      return 0;
  }
  return 1;
}

void judge(char strs[MAXNUM][MAXCHAR], int size, int* state, char startchar, int* resultAddr){
  int i, j;

  for(i = 0; i < size; i++){

    if(state[i] == 0 && (startchar == '#' || startchar == strs[i][0])){

      //printf("%s ", strs[i]);

      state[i] = 1;

      //get end char
      j = 0;
      while(strs[i][j] != '\0'){
        j++;
      }

      if(jobend(state, size) == 1){
        *resultAddr = 1;
        return;
      }
      else{
        judge(strs, size, state, strs[i][j-1], resultAddr);
        //restore state
        state[i] = 0;
      }
    }
  }
}

int main(){

  //input
  int num;
  char strs[MAXNUM][MAXCHAR];
  int i;

  while(scanf("%d", &num) != EOF){
    //scanf("%d", &num);
    for(i = 0; i < num; i++){
      scanf("%s", strs[i]);
    }

    //回溯法
    int state[MAXNUM] = {};
    int result = 0;
    judge(strs, num, state, '#', &result);
    if(result == 1)
      printf("Yes\n");
    else
      printf("No\n");
  }

  return 0;
}
