import random
def guessNumber():
    randomNumber = random.randint(1,20)
    attempt = 0
    while True:
        

        try:
            enteredNumber = int(input("Guess the number"))
            attempt +=1
            if(enteredNumber>20 or enteredNumber < 1):
                print("enter only between 1 and 2")
                continue
            
            if enteredNumber > randomNumber :
                print("Entered number is too high")
            elif enteredNumber < randomNumber:
                print("number too low")
            else:
                print("correct guess in attempts ", attempt)
                break
        except:
            print("please enter only integers from 1 to 20")
guessNumber()
            


