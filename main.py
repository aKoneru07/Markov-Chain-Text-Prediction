import numpy as np
import random
import string

files = {'Stephen_King_BagOfBones.txt', 'Stephen_King_BlackHouse.txt', 'Stephen_King_Carrie.txt',
         'Stephen_King_It.txt', 'Stephen_King_Misery.txt', 'Stephen_King_SalemsLot.txt',
         'Stephen_King_SongOfSusannah.txt', 'Stephen_King_TheDarkTower.txt',
         'Stephen_King_TheDeadZone.txt', 'Stephen_King_TheDrawingOfTheThree.txt',
         'Stephen_King_TheGirlWhoLovedTomGordon.txt', 'Stephen_King_TheGunslinger.txt',
         'Stephen_King_TheLittleSistersOfEluria.txt', 'Stephen_King_TheShining.txt',
         'Stephen_King_TheWasteLands.txt', 'Stephen_King_WizardAndGlass.txt'}

chain_dict = dict()

WINDOW = 3                                                  # Sliding Window of length 3

for fileName in files:                                      # Iterates through all the Books and creates
    raw_data = open(fileName).read()

    words = raw_data.split()

    for i in range(len(words)-WINDOW):
        key = words[i]
        for w in range (1, WINDOW):
            key += ' ' + words[i+w]

        if(key in chain_dict.keys()):
            chain_dict[key].append(words[i+WINDOW])         # Adds on to a word's existing Markov Chain
        else:
            chain_dict[key] = [words[i+WINDOW]]             # Creates Markov Chain for a word

first_word = random.choice(list(chain_dict.keys()))                                 # Picks Random starting Phrase

while first_word[0].islower() or first_word[WINDOW-1][-1] in string.punctuation:    # Ensures start is a Capitalized
    first_word = random.choice(list(chain_dict.keys()))

chain = first_word.split()

n_words = 50                                                # Defines length of generated text

for i in range(n_words):
    key = chain[-1]
    for w in range(1, WINDOW):
        key = chain[-1-w] + ' ' + key
    chain.append(np.random.choice(chain_dict[key]))         # Randomly selects the next word based on Markov Chain
                                                            #   distribution of the last window of words
s = ""
for w in chain:                                             # Attaches words together
    s += w + " "

print(s)                                                    # Outputs the generated text
