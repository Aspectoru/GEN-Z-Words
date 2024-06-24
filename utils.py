import random

char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""

pass_length = int(input('masukkan panjang password :'))

for i in range(pass_length):    
    password += random.choice(char)

print("password anda :", password)