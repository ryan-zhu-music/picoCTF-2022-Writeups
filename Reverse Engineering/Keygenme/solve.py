from hashlib import md5

flag = "picoCTF{br1ng_y0ur_0wn_k3y_"
hash = md5(flag.encode()).hexdigest()

a = hash[12]
b = hash[12 + 0x6c - 0x66]
c = hash[12 + 0x6c - 0x66 + 0x66 - 0x5f]
d = hash[12 + 0x6c - 0x66 + 0x66 - 0x5f + 0x5f - 0x5e]

print("Flag:", flag + b + d + c + "4" + d + b + a + d + "}")