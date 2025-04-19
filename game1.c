#include<stdio.h>
void clear(){
   printf("\033[H\033[J");
}

void swap(int *a,int *b){
  int temp=*a;
  *a=*b;
  *b=temp;
}

int main()
{
  int n,q=0;
  char b;
  printf("Enter size : ");
  scanf("%d",&n);
  int xy[n][n],x=n/2,y=n/2;
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      xy[i][j]=0;
    }
  }
  xy[x][y]=1;
  while(1){
    clear();
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
        printf("%d ",xy[i][j]);
      }
      printf("\n");
    }
    scanf(" %c",&b);
    switch(b){
     case 'w':
        if (x > 0) {
          swap(&xy[x][y], &xy[x - 1][y]);
          x--;
        }
        break;
      case 's':
        if (x < n - 1) {
          swap(&xy[x][y], &xy[x + 1][y]);
          x++;
        }
        break;
      case 'a':
        if (y > 0) {
          swap(&xy[x][y], &xy[x][y - 1]);
          y--;
        }
        break;
      case 'd':
        if (y < n - 1) {
          swap(&xy[x][y], &xy[x][y + 1]);
          y++;
        }
        break;
     default:
        q=1;
    }
    if(q){break;}
    printf("completed switch");
  }
  
  return 0;
}
