
words = open('spell.words').readlines()
words = map(lambda x: x.strip(), words)
#print words
print len(words)
print words[0]
print words[len(words)-1]

#took value for word, 
print('zygotic' in words)
print('mistasdas' in words)

#Read in the document
def load_words(file_name):
    words = open(file_name).readlines()
    words = map(lambda x: x.strip(), words)
    return words

#Check to see if a word is there
def check_word(words, word):
    return word.strip('.').lower() in self.words

#Checks a sentence -	
def check_words(words, sentence):
    words_to_check = sentence.split(' ')
    for word in words_to_check:
        if not check_word(words, word):
            print('Word is misspelt : ' + word)
            return False
    return True

print load_words("spell.words")[0]

print check_words(words, 'zygotic')
print check_words(words, 'mistasdas')
print check_words(words, 'zygotic mistasdas elementary')