#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, string argv[])
{
    // Checks if user added 2 values
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        int i = 0;
        int len = strlen(argv[1]);
        for (; i < len; i++)
        {
            // Checks if all characters in second argument are digits,
            // if not, returns status code 1 and prints correct usage
            if (!isdigit(argv[1][i]))
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
    }

    // Prompts user to enter text, which will be enciphered
    char *text = get_string("Text: ");
    int input = atoi(argv[1]);
    int len = strlen(text);
    int i = 0;
    int alphabetical_index;
    int cipher_text;
    char converted_cipher;

    printf("ciphertext: ");

    // Cycle runs for every character in the text user entered
    for (; i < len; i++)
    {
        // For lowercase letters
        if (text[i] >= 'a' & text[i] <= 'z')
        {
            // Converts characters to alphabetical index
            alphabetical_index = text[i] - 'a' + 1;
            // Formula which enciphers alphabetically indexed text
            cipher_text = (alphabetical_index + input) % 26;
            // Converts text represented as integers to characters
            converted_cipher = cipher_text + 'a' - 1;
            printf("%c", converted_cipher);

        }

        //For uppercase letters
        else if (text[i] >= 'A' & text[i] <= 'Z')
        {
            // Converts characters to alphabetical index
            alphabetical_index = text[i] - 'A' + 1;
            // Formula which enciphers alphabetically indexed text
            cipher_text = (alphabetical_index + input) % 26;
            // Converts text represented as integers to characters
            converted_cipher = cipher_text + 'A' - 1;
            printf("%c", converted_cipher);
        }
        // For other characters
        else
        {
            // Keep text as it is
            cipher_text = text[i];
            converted_cipher = cipher_text;
            printf("%c", converted_cipher);
        }
    }
    printf("\n");
}
