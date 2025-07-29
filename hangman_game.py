import random

stages=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = [
    'hello', 'dark','alchemy', 'anagram', 'asterisk', 'backpack', 'bizarre',
    'cactus', 'cascade', 'citadel', 'clique', 'cobblestone',
    'conundrum', 'cryptic', 'cyclone', 'dazzle', 'dolphin',
    'dungeon', 'enigmatic', 'espresso', 'exorcism', 'flicker',
    'gargoyle', 'gizmo', 'goblet', 'guffaw', 'hiccup',
    'horizon', 'illusion', 'javelin', 'jukebox', 'kangaroo',
    'labyrinth', 'lasagna', 'leopard', 'lightbulb', 'lynx',
    'marshmallow', 'mystical', 'nightmare', 'obelisk', 'octopus',
    'ostrich', 'panther', 'phantom', 'phoenix', 'ravenous',
    'revolver', 'sorcery', 'sphinx', 'tornado', 'vampire',
    'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward',
    'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou',
    'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm',
    'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom',
    'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness',
    'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl',
    'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip',
    'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable',
    'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove',
    'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy',
    'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph',
    'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard',
    'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy',
    'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy',
    'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking',
    'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo',
    'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit',
    'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph',
    'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify',
    'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx',
    'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel',
    'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy',
    'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz',
    'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw',
    'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk',
    'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied',
    'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz',
    'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth',
    'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize',
    'vixen', 'vodka', 'voodoo', 'vortex', 'voyeurism', 'walkway',
    'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey',
    'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy',
    'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked',
    'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch',
    'zipper', 'zodiac', 'zombie'
]

lives = 6
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game_over = False
correct_letters = []

while not game_over:
    print(f"\n******************* {lives}/6 LIVES LEFT **********************")
    display = ""
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        print("You win!")
        game_over = True
        break

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed '{guess}'. Try another letter.")
        continue

    if guess in chosen_word:
        correct_letters.append(guess)
    else:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose! The word was:", chosen_word)

    print(stages[6 - lives])
