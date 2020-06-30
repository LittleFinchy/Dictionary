import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def wordDef(w):
	try:
		w = get_close_matches(w, data.keys(), 1)[0]
	except:
		w = ""
	if w in list(data.keys()):
		print(w.title()+':'+'\n')
		return data[w]
	return "No match found"


word = input('Enter a word: ').lower()

print(wordDef(word))

# message to the user bragging bout how dumb/easy their word was