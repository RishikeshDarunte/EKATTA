import random

while True:
    l = int(input("Enter the desired password length (minimum 5): "))
    if l >= 5:
        break  
    print("Password length must be at least 5. Please try again.")

num_alpha = l // 2  # 50% alphabets
num_numeric = l * 3 // 10  # 30% numbers
num_special = l - (num_alpha + num_numeric)  #20% special

alphabets = random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', num_alpha)
numbers = random.sample('0123456789', num_numeric)
specials = random.sample('@#$%&*', num_special)

password = alphabets + numbers + specials
random.shuffle(password)

print("Generated Password:", ''.join(password))
