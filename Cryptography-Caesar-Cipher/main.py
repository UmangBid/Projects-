alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def refactor_position(p_position, p_cipher_type):
    if p_cipher_type == 'E':
        while p_position > 25:
            p_position = p_position - 26
        return p_position
    else:
        while p_position < 0:
            p_position = p_position + 26
        return p_position

def caesar_cipher(p_initial_text, p_shift_amount, p_cipher_type):
  final_text = ""
  if p_cipher_type == "D":
    p_shift_amount *= -1
  for char in p_initial_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + p_shift_amount
      new_position = refactor_position(new_position, p_cipher_type)
      final_text += alphabet[new_position]
    else:
      final_text += char
  print(f"Here's the {'decode' if p_cipher_type=='D' else 'encode'}d result: {final_text}")



from logo import logo
print(logo)

end_program = False
while not end_program:
  enc_dec = input("Type 'E' to encrypt, type 'D' to decrypt:\n")
  text = input("Enter your message:\n").upper()
  shift = int(input("Enter the shift number:\n"))
  caesar_cipher(p_initial_text=text, p_shift_amount=shift, p_cipher_type=enc_dec)
  restart = input("Type 'Y' if you want to go again. Otherwise type 'N'.\n")
  if restart == "N":
    end_program = True
    print("See you next time!")



# Before cleaning

# def encrypt(p_message, p_shift_amount):
#   cipher_message = ""
#   for char in p_message:
#     if char in alphabet:
#         position = alphabet.index(char)
#         new_position = position + p_shift_amount
#         while new_position > 25:
#             new_position = new_position - 26
#         new_letter = alphabet[new_position]
#         cipher_message += new_letter
#     else:
#         cipher_message += char
#   return f"The encoded text is {cipher_message}"


# def decrypt(p_message, p_shift_amount):
#   message = ""
#   for char in p_message:
#     if char in alphabet:
#         position = alphabet.index(char)
#         old_position = position - p_shift_amount
#         while old_position < 0:
#             old_position = old_position + 26
#         new_letter = alphabet[old_position]
#         message += new_letter
#     else:
#         message += char
#   return f"The decoded text is {message}"
