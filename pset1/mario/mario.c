#include <stdio.h>
#include <cs50.h>

int main(void)
{

    //Obtain height from user
    int height;
    do
    {
        height = get_int("Please enter height.");
    }
    while (height < 1 || height > 8);


    //Number of iterations
    for (int i = 0; i < height; i++)
    {
        //Prints empty spaces
        for (int j = height - i - 1; j > 0; j--)
        {
            printf(" ");
        }
        //Prints hashes
        for (int h = 0; h <= i; h++)
        {
            printf("#");
        }
        printf("\n");
    }
}