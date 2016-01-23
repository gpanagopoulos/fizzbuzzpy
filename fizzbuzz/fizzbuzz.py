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

def checkfizzbuzz(num):
    word = ""
    word += checkfizz(num)
    word += checkbuzz(num)
    if not word:
        word = str(num)
    return word

def runfizzbuzz():
    for i in range(1, 100):
        word = checkfizzbuzz(i)
        print(word)
