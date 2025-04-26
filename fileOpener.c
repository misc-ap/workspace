#include <stdio.h>
int main(int argc, char *argv[])
{
  if (argc < 2)
  {
    printf("No argument provided!\n");
    return 1;
  }
  FILE *fp;
  char ch;
  int i = 1;
  while (i < argc)
  {
    fp = fopen(argv[i], "r");
    if (fp == NULL)
    {
      perror(argv[i]);
      fprintf(stderr, "(make sure the name is correct with extension or you are in correct directory)\n");
      i++;
      continue;
    }
    if (argc > 2)
    {
      printf("\n----- Reading file: %s -----\n", argv[i]);
    }
    while ((ch = fgetc(fp)) != EOF)
    {
      printf("%c", ch);
    }
    fclose(fp);
    i++;
  }
  return 0;
}
