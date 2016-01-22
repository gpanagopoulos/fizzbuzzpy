fizz = "Fizz"
buzz = "Buzz"

def checkfizz(num):
    if num % 3 == 0:
        return fizz
    else:
        return ""

def checkbuzz(num):
    if num % 5 == 0:
        return buzz
    else:
        return ""

def runfizzbuzz():
    for i in range(1, 100):
        word = ""
        word += checkfizz(i)
        word += checkbuzz(i)
        if word:
            print(word)
        else:
            print(i)
