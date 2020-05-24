from collections import Counter
import sys
import string

from nltk.corpus import stopwords
import pandas as pd 

file_name = input("Enter the file name you would like to sum up : \n")
text = ''
number_words = 0

try:
    with open(file_name,'r') as file:
        for line in file.readlines():
            text += line
except FileNotFoundError:
    sys.exit("That file does not exist.")

text = ''.join(word for word in text if ord(word) < 128)


while True:
    number_words = str(input("\nEnter how many words the sum will be : "))
    if number_words.isdigit():
        number_words = int(number_words)
        break

    print("Sorry, I could'nt understand that.")
    
remove_punctuation = [character for character in text
                      if character not in string.punctuation]

remove_punctuation = ''.join(remove_punctuation)
remove_punctuation = remove_punctuation.split()

remove_stopwords = [word for word in remove_punctuation
                    if word not in stopwords.words('english')]

counter = Counter(remove_stopwords)

non_stop_words = [tup[0] for tup in counter.most_common(number_words)]

for word in non_stop_words:
    if word.isdecimal():
        non_stop_words.pop(non_stop_words.index(word))

final_result = ', '.join([word for word in non_stop_words if not word.isdigit()])
    
print(final_result.replace('92',"'"))
