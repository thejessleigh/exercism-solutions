import re

def is_isogram(word):
    letters = list(re.sub(r'\W+', '', word).lower())
    seen_letters = []
    for letter in letters:
    	if letter in seen_letters:
    		return False
    	
    	seen_letters.append(letter)

    return True
