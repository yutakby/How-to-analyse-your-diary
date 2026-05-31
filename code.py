import matplotlib.pyplot as plt
import numpy as np #txt = "I think. Therefore, I am."

diary = [
]

def sentence_count(txt):#what about ..., 273.15, !, ?, etc
    occurence = 0
    for i in list(txt):
        if i in [".", "?", "!"]:
            occurence += 1
    return occurence

def word_count(txt):
    return len(txt.split(" "))

capital = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lower_case = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
black_list = [".", ",", " ", "!", "(", ")", "?", '"', ":", "-", "…", "“", "”"]#omitting list
"""
def word_extract(txt): #cleans the words
    word_list = []
    for i in txt.split(" "): #"I", "think.", "Therefore", "I", "am."
        letters = list(i)
        for j in letters:
            if j in black_list or j in numbers:
                letters.remove(j)
            if j in capital:
                letters[letters.index(j)] = lower_case[capital.index(j)]#any methods of changing elements??
        if len(letters)>3:
            if (letters[-1],letters[-2]) == ("s", "'"):#Yuta's
                letters.pop(-1)
                letters.pop(-1)
        for j in letters:
            if j == "'":
                j.remove("'")
        a_word = "".join(letters) #thanks to Mikulas Pater 2026
        word_list.append(a_word)
    return word_list
"""
def matching(letters1, letters2):
    matches = []
    n = min(len(letters1), len(letters2))
    for i in range(n):
        if letters1[i] == letters2[i]:
            matches.append(1)
    return len(matches)/n
    
def word_extract(txt): #cleans the words
    word_list = []
    for i in txt.split(" "): #"I", "think.", "Therefore", "I", "am."goes through every letter
        letters = list(i)
        remove_list = []
        for j in letters:
            if j in black_list or j in numbers:
                remove_list.append(j)
            if j in capital:
                letters[letters.index(j)] = lower_case[capital.index(j)]
        for i in remove_list:
            letters.remove(i)
        if len(letters)>1:
            if (letters[-1],letters[-2]) == ("s", "’"):#Yuta’s
                letters.pop(-1)
                letters.pop(-1)
        for j in letters:
            if j == "’":
                letters. remove(j)
        word_list.append(letters)
    for i in range(len(word_list)):
        for j in word_list[i+1:]:#!!
            w_length_i = int(len(word_list[i])/2)+1
            w_length_j = int(len(j)/2)+1
            if w_length_i > 2 and w_length_j > 2:
                if word_list[:w_length_i] == word_list[:w_length_j] and matching(word_list[i], j)>0.70:#head is the same AND matching rate is above 80%
                    #print(word_list[i], j)##
                    word_list[i] = j##
    true_word = []
    for i in word_list:
        a_word = "".join(i)
        if a_word == "":
            continue
        true_word.append(a_word)
    return true_word

def sentences():                               #creates lists of data points for each days(down)
    y = []
    for i in diary:
        y.append(sentence_count(i))
    return y
def total_words():
    y = []
    for i in diary:
        y.append(word_count(i))
    return y
def unique_words():
    y = []
    for i in diary:
        y.append(len(set(word_extract(i))))
    return y
def unique_density():
    y = []
    for i in range(len(diary)):
        if unique_words()[i] == 0:
            y.append(0)
        else:
            y.append(total_words()[i]/unique_words()[i])
    return y
def sentence_length():
    y = []
    for i in range(len(diary)):
        if sentences()[i] == 0:
            y.append(0)
            continue
        y.append(total_words()[i]/sentences()[i])
    return y                                           #(up)

def dictionary():
    dictionary = set()
    for i in diary:
        for j in set(word_extract(i)):
            dictionary.add(j)
    return list(dictionary)
def new_words():#how do u feed??
    added_num_list = []
    a = set()
    for i in diary:
        added_words = len(set(word_extract(i)) - a)
        added_num_list.append(added_words)
        a = a.union(set(word_extract(i)))
    return added_num_list
def integral():#= total unique words until the day
    ydx = []
    y = new_words()
    a = 0
    for i in y:
        a += i
        ydx.append(a)
    return ydx

x = range(len(diary))
fig, axs = plt.subplots(2,3)

y = new_words()                                                     #outputs
axs[0,0].plot(x, y, label = "new words")
ydx = integral()
axs[0,0].plot(x, ydx)
axs[0,0].set_title("New words, Accumulated words")

y = sentences()
axs[0,1].plot(x, y, label = "sentences")
axs[0,1].set_title("Sentences")

y = total_words()
axs[1,0].plot(x, y)
axs[1,0].set_title("Total words")

y = unique_words()
axs[1,1].plot(x, y)
axs[1,1].set_title("Unique words")

y = unique_density()
axs[1,2].plot(x, y)
axs[1,2].set_title("Total_word / Unique_word")

y = sentence_length()
axs[0,2].plot(x, y)
axs[0,2].set_title("Total_word / Sentence")

plt.show()
