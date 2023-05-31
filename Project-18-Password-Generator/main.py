import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

no_of_letters = int(input("How many letters do you want in your password? "))
no_of_nums = int(input("How many nums do you want in your password? "))
no_of_symbols = int(input("How many symbols do you want in your password? "))

seq = 0
seq1 = 0
seq2 = 0
password = ""

while seq < no_of_letters:
    seq += 1
    password += random.choice(letters)
    if seq == no_of_letters:
        break

while seq1 < no_of_nums:
    seq1 += 1
    password += random.choice(nums)
    if seq1 == no_of_nums:
        break

while seq2 < no_of_symbols:
    seq2 += 1
    password += random.choice(symbols)
    if seq2 == no_of_symbols:
        break

print(f"\nYour password is: {password}")

#alternate using FOR LOOP instead of WHILE

# for letter in range(1, no_of_letters +1):
#   password += random.choice(letters)
