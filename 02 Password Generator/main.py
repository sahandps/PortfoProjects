import random
import string
import nltk
from nltk.corpus import words


class Password_generator:

    def __init__(self):
        pass

    def generate(self):

        while True:
            lenght = int(input("Give me the lenght of password you want"))
            choice = int(input("pick the password type: 1 for PinCodeGenerator, 2 for Random_password, 3 for  easy_to_remember "))

            if choice == 1:
                self.PinCodeGenerator(lenght)
            elif choice == 2:
                self.Random_password(lenght)
            elif choice == 3:
                self.easy_to_remember(lenght)
            elif choice == 4:
                break
            else:
                print("Your input was not correct")
                continue           

    def PinCodeGenerator(self, lenght):
        range_start = 10**(lenght-1)
        range_end = (10**lenght) -1
        print(random.randint(range_start, range_end))


    def Random_password(self, length):
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        print(random_string)

    def easy_to_remember(self, length):
        word_list = words.words()
        selected_words = random.sample(word_list, length)
        final_password = "-".join(selected_words)
        print(final_password)
    

def main():
    password = Password_generator()
    password.generate()


if __name__ == "__main__":
    main()

