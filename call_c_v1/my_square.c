#include <stdio.h>
double my_square(double x)
{
  printf("This is from C\n");
  printf("input = %f\n", x);
  printf("output = %f\n", x*x);
  return x*x;
}
