#include <stdio.h>

// reference https://www.tutorialspoint.com/cprogramming/c_file_io.htm
main() {

   FILE *fp;
   char buff[255];

   // open file containing flag
   fp = fopen("key", "r");

   // read in flag from file
   fscanf(fp, "%s", buff);

   // print flag
   printf("flag : %s\n", buff );

   // close file
   fclose(fp);
}
