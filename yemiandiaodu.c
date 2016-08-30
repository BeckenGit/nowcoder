//http://www.nowcoder.com/questionTerminal/3166de5ab30e4907babd170835e22d11
#define MAXSIZE 200
#include<stdio.h>
int isInArray(int val, int cache[MAXSIZE], int cacheSize){
  int i = 0;
  for(i = 0; i < cacheSize; i++){
    if(val == cache[i])
      return 1;
  }
  return 0;
}

int main(){
  int m, n;//Cache的大小n和m个页面请求
  int cache[MAXSIZE], cacheSize;
  int pageId, result;
  int i, j;

  while(scanf("%d%d", &n, &m) != EOF){
    cacheSize = 0;
    result = 0;
    //printf("%d%d\n", n, m);
    //2<=n<=20,1<=m<=100，1<=页编号<=200.
    for(i = 0; i < m; i++){
      scanf("%d", &pageId);

      //updatae chche
      if(!isInArray(pageId, cache, cacheSize)){
        result++;
        if(cacheSize < n){
          cache[cacheSize] = pageId;
          cacheSize++;
        }
        else{
          for(j = 0; j < cacheSize-1; j++){
            cache[j] = cache[j+1];
          }
          cache[cacheSize-1] = pageId;
        }
      }

      //cache state
      for(j = 0; j < cacheSize; j++){
        printf("%d ", cache[j]);
      }
      printf("\n");

    }
    printf("%d\n", result);
  }
  return 0;
}
