#include<stdio.h>
int main()
{
    printf("hello user:\n");
    printf("hello sir ");
    printf(" enter your marks all subjects\n");
    float percentage, marks;
    scanf("%f", &marks);
    percentage = ((marks / 500.0) * 100);
printf("your percentage is %f", percentage);
    return 0;
    
}