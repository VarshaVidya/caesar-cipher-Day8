alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

cipher_word = ""
shift_value = 0
for i in range(0, len(text)):
  for j in range(0, 26):
    if direction == "encode":
      if text[i] == alphabet[j]:
        shift_value = j + shift
        if shift_value <= 25:
          cipher_word += alphabet[shift_value]
        else:
            shift_value = shift_value - 26
            cipher_word += alphabet[shift_value]
    elif direction == "decode":
      if text[i] == alphabet[j]:
        shift_value = j - shift
        if shift_value >= 0:
          cipher_word += alphabet[shift_value]
        else:
            shift_value = shift_value + 26
            cipher_word += alphabet[shift_value]

print(f"The coded text is: {cipher_word}")




