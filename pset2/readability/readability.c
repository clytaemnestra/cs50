#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int calculate_letters(char *);
int calculate_words(char *);
int calculate_sentences(char *);
int nr_of_letters;
int nr_of_words;
int nr_of_sentences;


int main(void)
{
    char *text = get_string("Type some text: ");

    nr_of_letters = calculate_letters(text);
    nr_of_words = calculate_words(text);
    nr_of_sentences = calculate_sentences(text);

    // Average number of letters per 100 words
    float L = 100.00 * nr_of_letters /  nr_of_words;
    // Average number of sentences per 100 words
    float S = 100.00 * nr_of_sentences / nr_of_words;

    // Formula for Coleman-Liau index, which calculates
    // readability of given text
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int round_index = round(index);

    if (round_index > 16)
    {
        printf("Grade 16+\n");
    }
    else if (round_index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", round_index);
    }
}

// Function calculates number of letters in given text
int calculate_letters(char *text)
{
    nr_of_letters = 0;
    int str_length = strlen(text);
    for (int i = 0; i < str_length; i++)
    {
        if (isalpha(text[i]))
        {
            nr_of_letters++;
        }
    }
    return nr_of_letters;
}

// Function calculates number of words in given text
int calculate_words(char *text)
{
    int empty_spaces = 0;
    int str_length = strlen(text);
    for (int i = 0; i < str_length; i++)
    {
        if (text[i] == ' ')
        {
            empty_spaces += 1;
            nr_of_words = empty_spaces + 1;
        }
    }
    return nr_of_words;
}

// Function calculates number of sentences in given text
int calculate_sentences(char *text)
{
    int str_length = strlen(text);
    int full_stops = 0;
    nr_of_sentences = 0;
    for (int i = 0; i < str_length; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            nr_of_sentences++;
        }
    }
    return nr_of_sentences;
}


