#include<stdio.h>
#define MAXSIZE 2000
int main(){
  //difine variable
  //2<=n<=2000,1<=p<=300,1<=q<=100.
  int n;
  int i, j, k, p, q;
  int processArray[MAXSIZE][2];


  while(scanf("%d", &n) != EOF){
    //input 有n行，每行两个整数，代表上述的二元组(p,q).
    for(i = 0; i < n; i++){
      scanf("%d%d", &p, &q);

      //find position
      j = 0;
      while(j < i && (p == processArray[j][0] && q > processArray[j][1] || p > processArray[j][0])){
        j++;
      }

      //insert
      for(k = i; k > j; k--){
        processArray[k][0] = processArray[k-1][0];
        processArray[k][1] = processArray[k-1][1];
      }
      processArray[j][0] = p;
      processArray[j][1] = q;

      //output processArray
      /*
      for(j = 0; j < i+1; j++){
        printf("(%d,%d) ", processArray[j][0], processArray[j][1]);
      }
      printf("\n");
      */
    }

    int waittime = 0;
    double totalwaittime = 0;
    int endtime = processArray[0][0]+processArray[0][1];
    for(i = 1; i < n; i++){
      printf("%d->", endtime);
      waittime = (processArray[i][0] < endtime)? endtime-processArray[i][0] : 0;
      printf("%d ",waittime);
      totalwaittime+=waittime;
      endtime += processArray[i][1];
    }
    printf("\n%d\n", totalwaittime);
    double result = totalwaittime/n;
    printf("%.4f\n",result);
  }
  return 0;
}
