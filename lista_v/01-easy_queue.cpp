#include <cstdio>

using namespace std;

int main() {
  int num, queue[1000000], inicio = 0, fim = 0, opcao, item;

  scanf("%d",&num);
  
  while (num--) {
    scanf("%d",&opcao);
    
    if (opcao == 1) {
      scanf("%d",&item);
      queue[fim++] = item;
    } else if ( opcao == 2 ) {
      if (inicio < fim) {
        inicio++;
      }
    } else {
      if (inicio < fim) {
          printf("%d\n",queue[inicio]);
      } else {
        printf("Empty!\n");
      }
    } 
  }
  return 0;
}
