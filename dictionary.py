import json
from difflib import get_close_matches

data = json.load(open('data.json'))
data = dict((k.lower(),v) for k, v in data.items())

def wordDef(w):
		if w in list(data.keys()):
			if len(w) < 5:
				print('ARE YOU KIDDING!\n')
			elif len(w) < 8:
				print('EASY\n')
			else:
				print('OK THAT ONE WAS KINDA HARD\n')
			print(w.title()+':'+'\n')
			return data[w]
		try:
			options = get_close_matches(w, data.keys(), 3)
			if len(options) == 0:
				w = ''
			else:
				for i in range(len(options)):
					print(i+1, options[i])
				print(str(len(options)+1)+' None of these')
				w = options[int(input('Did you mean one of these? (type the number next to the correct option)'))-1]
		except:
			w = ""
		if w in list(data.keys()):
			if len(w) < 5:
				print('ARE YOU KIDDING!\n')
			elif len(w) < 8:
				print('EASY\n')
			else:
				print('OK THAT ONE WAS KINDA HARD\n')
			print(w.title()+':'+'\n')
			return data[w]
		return ["No match found"]


loop = True
while loop:
	loopInput = input('Do you want to use the Dictionary? (Y) or (N)')
	if loopInput.upper() == 'N':
		loop = False
		break
	word = input('Enter a word: ').lower()
	answer = wordDef(word)
	for item in answer:
		print(item)
	print('\n')
