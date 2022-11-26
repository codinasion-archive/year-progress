ZERO_BAR = "▁"
ONE_BAR = "▂"
TWO_BAR = "▃"
THREE_BAR = "▄"
FOUR_BAR = "▅"
FIVE_BAR = "▆"


def ProgressBar(PERCENT=0):

    FIVES = PERCENT // 5
    FOURS = (PERCENT % 5) // 4
    THREES = (PERCENT % 5) % 4 // 3
    TWOS = ((PERCENT % 5) % 4) % 3 // 2
    ONES = (((PERCENT % 5) % 4) % 3) % 2 // 1
    ZEROS = 20 - (FIVES + FOURS + THREES + TWOS + ONES)

    BAR = f"{FIVES * FIVE_BAR}{FOURS * FOUR_BAR}{THREES * THREE_BAR}{TWOS * TWO_BAR}{ONES * ONE_BAR}{ZEROS * ZERO_BAR} {PERCENT}%"

    return BAR
