#include <cs50.h>
#include <stdio.h>

int main(void)
{

    //Get Start Size From User
    int start_size;
    do
    {
        start_size = get_int("Please enter start size. ");
    }
    while (start_size < 9);

    //Get End Size From User
    int end_size;
    do
    {
        end_size = get_int("Please enter end size. ");
    }
    while (end_size < start_size);

    //Calculate Number of Years Neccessary For the Popultation to Grow
    //From Start Size to End Size
    int years = 0;
    while (start_size < end_size)
    {
        start_size = start_size + (start_size / 3) - (start_size / 4);
        years ++;
    }

    printf("Years: %i\n", years);
}