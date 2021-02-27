text = input("Please enter some text: ")


def count_letters(text):
    """Function calculates number of letters in given text"""
    letter_count = 0
    for i in text:
        if i.isalnum():
            letter_count += 1
    return letter_count


def count_words(text):
    """Function calculates number of words in given text"""
    empty_spaces = 0
    word_count = 0
    for i in range(0, len(text)):
        if text[i] == ' ':
            empty_spaces += 1
            word_count = empty_spaces + 1
    return word_count


def count_sentences(text):
    """Function calculates number of sentences in given text"""
    sentence_count = 0
    for i in range(0, len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == '!':
            sentence_count += 1
    return sentence_count


def coleman_liau_index(letter_count, word_count, sentence_count):
    """Formula for Coleman-Liau index, which calculates
       readability of given text"""
    # Average number of letters per 100 words
    l = 100.00 * letter_count / word_count
    # Average number of sentences per 100 words
    s = 100.00 * sentence_count / word_count
    index = round(0.0588 * l - 0.296 * s - 15.8)
    return index


def print_index(index):
    if index > 16:
        print("Grade 16+", end="\n")
    elif index < 1:
        print("Before Grade 1", end="\n")
    else:
        print("Grade: ", index, end="\n")


def main():
    letter_count = count_letters(text)
    word_count = count_words(text)
    sentence_count = count_sentences(text)
    coleman_liau_index(letter_count, word_count, sentence_count)
    index = coleman_liau_index(letter_count, word_count, sentence_count)
    print_index(index)


main()

