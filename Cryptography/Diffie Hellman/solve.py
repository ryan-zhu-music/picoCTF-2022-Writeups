import string
message = "H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_8F7GK99J"

p = 13 #modulus
g = 5 #base

a = 7 #Alice's number
b = 3 #Bob's number

A = pow(g, a, p)

secret = pow(A, b, p)

alphabet = string.ascii_uppercase + string.digits

FLAG = ""
for i in message:
    if i == "_":
        FLAG += "_"
    else:
        index = (alphabet.index(i) + len(alphabet) - secret) % len(alphabet)
        FLAG += alphabet[index]

print(f"Flag: picoCTF{{{FLAG}}}")