#include <stdio.h>
int main(int argc, char *argv[])
{
  if (argc < 2)
  {
    printf("No argument provided!(use -h for help)\n");
    return 1;
  }
  int j = 1;
  while (argc > j && argv[j][0] == '-')
  {
    if (argv[1][1] == 'h')
    {
      printf("+ Usage: fdisp <file1> <file2> ...\n+ fdisp -h for help\n");
      printf("This program reads the contents of the specified files and prints them to the standard output.\n");
      return 0;
    }
    else
    {
      printf("Invalid option: %s\n", argv[1]);
      return 1;
    }
    j++;
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
