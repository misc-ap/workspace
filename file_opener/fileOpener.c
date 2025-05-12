#include <stdio.h>
int main(int argc, char *argv[])
{
  if (argc < 2)
  {
    printf("\x1b[31mNo argument provided!(use -h for help)\x1b[0m\n");
    return 1;
  }
  int j = 1;
  while (argc > j && argv[j][0] == '-')
  {
    if (argv[1][1] == 'h' && argv[1][2] == '\0')
    {
      printf("\x1b[33m+ Usage: fdisp <file1> <file2> ...\n+ fdisp -h for help\x1b[0m\n");
      printf("This program reads the contents of the specified files and prints them to the standard output.\n");
      return 0;
    }
    else
    {
      printf("\x1b[31mInvalid option: %s\x1b[0m\n", argv[1]);
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
      printf("\x1b[33m(make sure the name is correct with extension or you are in correct directory)\x1b[0m\n");
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
