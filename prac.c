#include <stdio.h>
#include <math.h>
int main(){
    const double PI = 3.1415;
    double radius;
    double circumference;
    printf("the radius of the circle is: ");
    scanf("%lf", &radius);
    circumference = 2 * radius * PI;
    printf("the circumference of the circle is %lf\n", circumference);
}