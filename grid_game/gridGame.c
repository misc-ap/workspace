#include <stdio.h>
#include <stdlib.h>


void swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}

int main()
{
  printf("\033]2;GRID GAME\007");
  int r = 24, c = 50, q = 0;
  char b;
  int xy[25][90], x = 0, y = 0;
  for (int i = 0; i < r; i++)
  {
    for (int j = 0; j < c; j++)
    {
      xy[i][j] = 0;
    }
  }
  xy[x][y] = 1;
  while (1)
  {
    system("clear");
    printf("\033[8;26;101t"); // in case terminal is resized
    for (int i = 0; i < r; i++)
    {
      printf(" ");
      for (int j = 0; j < c; j++)
      {
        if (xy[i][j] == 1)
        {
          printf("\033[38;2;255;255;255m\033[1m0\033[0m ");
        }
        else
        {
          printf("\033[38;2;100;100;100m.\033[0m ");
        }
      }
      printf("\n");
    }
    printf("\033[0m");
    printf("Use /W/A/S/D to move, any other key to quit: ");
    scanf(" %c", &b);
    printf("\n");
    switch (b)
    {
    case 'w':
      if (x > 0)
      {
        swap(&xy[x][y], &xy[x - 1][y]);
        x--;
      }
      break;
    case 's':
      if (x < r - 1)
      {
        swap(&xy[x][y], &xy[x + 1][y]);
        x++;
      }
      break;
    case 'a':
      if (y > 0)
      {
        swap(&xy[x][y], &xy[x][y - 1]);
        y--;
      }
      break;
    case 'd':
      if (y < c - 1)
      {
        swap(&xy[x][y], &xy[x][y + 1]);
        y++;
      }
      break;
    default:
      q = 1;
    }
    if (q)
    {
      break;
    }
  }
  system("clear");
  return 0;
}
