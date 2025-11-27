import random
def roll_die():
    emoji = { 
        1: '⚀',
        2: '⚁',
        3: '⚂',
        4: '⚃',
        5: '⚄',
        6: '⚅'
    }
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    return emoji[die1],emoji[die2]