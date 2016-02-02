fizz = "Fizz"
buzz = "Buzz"


def check_fizz(num):
    if num % 3 == 0:
        return fizz
    else:
        return ""


def check_buzz(num):
    if num % 5 == 0:
        return buzz
    else:
        return ""


def check_fizzbuzz(num):
    word = ""
    word += check_fizz(num)
    word += check_buzz(num)
    if not word:
        word = str(num)
    return word


def run_fizzbuzz():
    for i in range(1, 101):
        word = check_fizzbuzz(i)
        print(word)
