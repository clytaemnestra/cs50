#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float dollars;
    int cents;

    //Get amount of dollars from user
    do
    {
        dollars = get_float("Please enter amount of dollars.");
        cents = round(dollars * 100);
    }
    while (dollars < 0);

    int count = 0;
    int change = 0;

    //Use quarters, while possible
    while ((change + 25) <= cents)
    {
        change = change + 25;
        count ++;
    }

    //Use dimes, while possible
    while ((change + 10) <= cents)
    {
        change = change + 10;
        count ++;
    }

    //Use nickels, while possible
    while ((change + 5) <= cents)
    {
        change = change + 5;
        count ++;
    }

    //Use pennies, while possible
    while ((change + 1) <= cents)
    {
        change = change + 1;
        count ++;
    }

    //Print minimum amount of coins
    printf("%i\n", count);
}
