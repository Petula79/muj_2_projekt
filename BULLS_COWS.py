import random

# First, you need to install the package.
#
# pip install bullsandcows
#
# Now in your project, import the package and create a new instance.


from bullsandcows import bullsandcows
game = bullsandcows()


def get_digits(num):
    return [int(i) for i in str(num)]


def no_duplicates(num):
    number = get_digits(num)
    if len(number) == len(set(number)):
        return True
    else:
        return False


def num_generator():
    while True:
        num = random.randint(1000, 9999)
        if no_duplicates(num):
            return num


def num_bull_cows(num, guess):
    bull_cow = [0, 0]
    number = get_digits(num)
    guess_p = get_digits(guess)
    for i, j in zip(number, guess_p):
        if j in number:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow


separator, separator_1 = "=" * 55, "-" * 55
separator_2, separator_3 = "*" * 4, "*" * 3

print(separator_1, "Hi there", separator_1, sep="\n")
print(f"I've generated a random 4 digit number for you.", separator,
      sep="\n")
print(f"LET'S PLAY A BULLS AND COWS GAME."
      .center(len(separator)), separator, sep="\n")

game_num = num_generator()
score_counter = 0
while score_counter >= 0:
    print(separator_1)
    guess = input("Enter your guess: ")
    score_counter += 1
    if not guess.isdigit():
        print("The input you entered is not a number! Try again.")
        continue
    elif not no_duplicates(int(guess)):
        print("Number should not have repeated digits! Try again.")
        continue
    elif len(guess) != 4:
        print("Enter 4 digits only! Try again.")
        continue
    elif str(guess).startswith("0"):
        print("The input cannot begin with '0'! Try again.")
        continue
    bull_cow = num_bull_cows(game_num, guess)
    if bull_cow[0] == 0 and bull_cow[1] == 0:
        print(separator_3, bull_cow[0], "BULLS", bull_cow[1], "COWS",
              separator_3)
        continue
    elif bull_cow[0] == 0 and bull_cow[1] == 1:
        print(separator_3, bull_cow[0], "BULLS", bull_cow[1], "COW",
              separator_2)
        continue
    elif bull_cow[0] == 0 and bull_cow[1] >= 2:
        print(separator_3, bull_cow[0], "BULLS", bull_cow[1], "COWS",
              separator_3)
        continue
    elif bull_cow[0] == 1 and bull_cow[1] == 0:
        print(separator_2, bull_cow[0], "BULL", bull_cow[1], "COWS",
              separator_3)
        continue
    elif bull_cow[0] == 1 and bull_cow[1] == 1:
        print(separator_2, bull_cow[0], "BULL", bull_cow[1], "COW",
              separator_2)
        continue
    elif bull_cow[0] == 1 and bull_cow[1] >= 2:
        print(separator_2, bull_cow[0], "BULL", bull_cow[1], "COWS",
              separator_3)
        continue
    elif bull_cow[0] == 2 and bull_cow[1] == 0:
        print(separator_3, bull_cow[0], "BULLS", bull_cow[1], "COWS",
              separator_3)
        continue
    elif bull_cow[0] == 2 and bull_cow[1] == 1:
        print(separator_3, bull_cow[0], "BULLS", bull_cow[1], "COW",
              separator_2)
        continue
    elif bull_cow[0] == 2 and bull_cow[1] == 2:
        print(separator_3, bull_cow[0], "BULLS", bull_cow[1], "COWS",
              separator_3)
        continue
    elif bull_cow[0] == 3 and bull_cow[1] == 0:
        print(separator_3, bull_cow[0], "BULLS", bull_cow[1], "COWS",
              separator_3)
        continue
    elif bull_cow[0] == 3 and bull_cow[1] == 1:
        print(separator_3, bull_cow[0], "BULLS", bull_cow[1], "COW",
              separator_2)
        continue
    else:
        print(separator, "YOU WON!".center(len(separator)),
              separator, sep="\n")
        print(f"Correct, you've guessed the right number "
              f"in {score_counter} guesses!", separator, sep="\n")
        break

mins, secs = game.get_time()
print(f"Total time spent: {mins} min & {secs} sec")
