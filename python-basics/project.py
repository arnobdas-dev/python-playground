"""
word and character count
------------------------
"""

# def count_word_characters(text):
#     clean_text = text.strip()
#     words = clean_text.split()
#     num_words = len(words)
#     num_characters_no_space = len(clean_text.replace(" ", ""))
#     num_characters_with_space = len(clean_text)
#     return num_words, num_characters_no_space, num_characters_with_space

# print("Welcome to Word & Character Counter!!!")
# text = input("Enter your text: ")

# num_words, num_characters_no_space, num_characters_with_space = count_word_characters(text)

# print("\nResults:")
# print(f"Number of words: {num_words}")
# print(f"Number of characters (without spaces): {num_characters_no_space}")
# print(f"Number of characters (with spaces): {num_characters_with_space}")

"""
Gussing game
------------
"""

# import random
# key = random.randint(1,10)
# enter = 0
# print("Guess the number 1-10")
# while True:
#     try:
#        guess = int(input("Enter you guess gain: "))
#        enter +=1
#        if guess == key:
#            print("congratulation!!! You win the game")
#            break
#        elif guess > key:
#            print("Number is lower")
#        elif guess < key:
#            print("Number is bigger")
#        else:
#            print("Retry with correct number.")
#            break
#     except:
#         print("Retry with correct number.")
#         break

""" 
Calculator
"""
# def calculate(a,b,oparation):
#     if oparation == '+':
#         return a+b
#     elif oparation =='-':
#         return a-b
#     elif oparation =='*':
#         return a*b
#     elif oparation =='/':
#         return a/b
#     elif oparation =='**':
#         return a**b
#     elif oparation =='%':
#         return a%b
#     else:
#         return "Error: Invalid operation."
# print("Welcome user")
# print("Available operation: +,-,*,**,/,%")
# print("type 'E' for exit\n")
# while True:
#     num1 = input("Enter your first number: ")
#     if num1.upper()=='E':
#         break
#     num2 = input("Enter your second number: ")                                                     
#     if num2.upper()=='E':
#         break
#     num3 = input("Enter your operator: ")
#     if num3.upper()=='E':
#         break
#     try:
#         num1 = float(num1)
#         num2 = float(num2)
#         result = calculate(num1,num2,num3)
#         print(f"result is: {result}")
#     except:
#         print("Invalid input")
   
    

