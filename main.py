import random as rand
import time

def roll_dice(num_dice):
    """
    Roll a set of dice randomly.
    :param: num_dice: the number of dice we are rolling
    :return: a list of the dice that were rolled
    """
    list_dice = []
    for die in range(num_dice):
        list_dice.append(rand.randint(1, 6))

    return list_dice


def count_score(dice_list):
    """
    Get the score from the set of dice. If the set contains 3's, remove all and a score of 0 is awarded. Else the lowest value is scored.
    :param: dice_list: A list of dice values that were rolled.
    :return: An integer of the score that is awarded.
    """
    if 3 in dice_list:
        # Remove 3's from the board
        while 3 in dice_list:
            dice_list.remove(3)

        return 0
    else:
        lowest_die = min(dice_list)
        # Remove the lowest dice from the set
        dice_list.remove(lowest_die)

        return lowest_die


def play_game(num_dice):
    """
    Play a full game of this dice game. 5 Dice are always used at the start.
    :param: num_dice: the number of dice we are rolling
    :return: the total score of a full game.
    """
    total_score = 0
    while num_dice > 0:
        # Roll dice
        dice_set = roll_dice(num_dice)
        # Score the dice for each round
        total_score += count_score(dice_set)
        num_dice = len(dice_set)

    return total_score


# Create a dictionary to hold each score and the number of times the score occurs
dict = {}
iterations = 10000
num_dice = 5
start_time = time.time()

# Simulate the Dice Game for the number of iterations given above
for i in range(iterations):
    score = play_game(num_dice)

    # Check to see if the score is in the dictionary, otherwise add a new key to it.
    if score in dict:
        dict[score] += 1
    else:
        dict[score] = 1

end_time = time.time()

# Print the Results
print("Number of simulations was", iterations, "using", num_dice, "dice.")
for i in range(31): #31 is used here because the max score possible is 30 (6*5)
    if i in dict:
        print("Total", i, "occurs", dict[i]/iterations, "occurred", dict[i], "times.")
    else:
        print("Total", i, "occurs 0.0 occurred 0 times.")
print("Total simulation took", end_time-start_time, "seconds.")
