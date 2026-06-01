import random
words =["python","computer","programing","code"]
word=random.choice(words)
guessed= []
attempts= 6
while attempts > 0:
    display= ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_"
    print("\nword:",display)
    if "_" not in display:
        print("Congratulations! you guessed the word:", word)
        break
    guess= input("Enter a letter:").lower()
    if guess in word: guessed.append(guess)
    else:
        attempts-= 1
        print("wrong guess! Attemps left:", attempts)
if attempts==0:
    print("game over! the word was:",word)



