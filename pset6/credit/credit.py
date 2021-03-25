# asks user for input
card_number = input("Number: ")

every_second_digit = []
every_second_digit = card_number[-2::-2]

digits = []
for i in every_second_digit:
    digits.append(int(i) * 2)

str_digits = ''.join(str(e) for e in digits)

result = 0
# calculates sum of every second digits from backwards
for i in str_digits:
    result += int(i)

remaining_digits = card_number[-1::-2]
str_remaining_digits = ''.join(str(a) for a in remaining_digits)

# adds remaining digits to the result
for i in str_remaining_digits:
    result += int(i)

# prints type of card
if result % 10 == 0:
    if len(card_number) == 15 and card_number[0] == '3' and (card_number[1] == '4' or card_number[1] == '7'):
        print("AMEX", end="\n")
    elif len(card_number) == 16 and card_number[0] == '5' and (card_number[1] == '1' or card_number[1] == '2' or card_number[1] == '3' or card_number[1] == '4' or card_number[1] == '5'):
        print("MASTERCARD", end="\n")
    elif (len(card_number) == 13 or len(card_number) == 16) and card_number[0] == '4':
        print("VISA", end="\n")
    else:
        print("INVALID 1", end="\n")
else:
    print("INVALID", end="\n")

