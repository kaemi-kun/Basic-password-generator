
import string
import random
length = int(input("What should be the length of password?\n"))
def generate_password(length):
    ques1 = input("uppercase? (Y/N) \n") == "Y"
    ques2 = input(" lowercase? (Y/N) \n") == "Y"
    ques3 = input(" Numbers? (Y/N) \n") == "Y"
    ques4 = input(" special characters? (Y/N) \n") == "Y"
    pool = []
    if ques1:
        pool.extend(string.ascii_uppercase)
    if ques2:
        pool.extend(string.ascii_lowercase)
    if ques3:
        pool.extend(string.digits)
    if ques4:
        pool.extend(string.punctuation)

    password = ''.join(random.choice(pool) for _ in range(length))

    print(password)
generate_password(length)
