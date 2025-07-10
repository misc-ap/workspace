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
  int xy[24][50], x = 0, y = 0;
  for (int i = 0; i < r; i++)
  {
    for (int j = 0; j < c; j++)
    {
      xy[i][j] = 0;
    }
  }
  xy[23][49] = 2;
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
        if (x == 23 && y == 49)
        {
          system("clear");
          printf("\033[1;32mCongratulations! You reached the goal!★\033[0m\n");
          printf("Press 'enter' to exit...");
          getchar();
          getchar();
          return 0;
        }
        if (xy[i][j] == 1)
        {
          printf("\033[48;2;60;179;113m\033[38;2;128;0;0m\033[1m● \033[0m");
        }
        else if (xy[i][j] == 2)
        {
          printf("\033[5m\033[48;2;60;179;113m\033[38;2;0;0;128m\033[1m◉ \033[0m");
        }
        else
        {
          printf("\033[48;2;60;179;113m\033[38;2;100;100;100m. \033[0m");
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
