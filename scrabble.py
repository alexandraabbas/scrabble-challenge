import sys

# open file, create list of words
sowpods = []
with open('sowpods.txt', 'r+') as f:
	for row in f:
		sowpods.append(row.rstrip())

# define main function
def main():
	# find valid words from sowpods
	valid_words = []
	for word in sowpods:
		counter = 0
		list_letters = list(args[1].upper())
		for character in word:
			for letter in list_letters:
				if character == letter:
					counter += 1
					list_letters.pop(list_letters.index(letter))
					if counter == len(word) and len(word) <= len(args[1]):
						valid_words.append(word)
						break

	# determine the scores
	scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
	         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
	         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
	         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
	         "x": 8, "z": 10}

	score_list = []
	for word in valid_words:
		score = 0
		counter = 0
		for character in word:
			for k, v in scores.items():
				if k.upper() == character:
					score = score + v
					counter += 1
				if counter == len(word):
					score_list.append(score)
					break

	# print results
	result = zip(score_list, valid_words)

	def getKey(item):
		return item[0]
	result = sorted(result, key = getKey, reverse = True)

	for item in result:
		print '%i, %s' % item

# take a command line argument
args = sys.argv
if len(sys.argv) < 2:
	print 'Usage: scrabble.py [RACK]'
else:
	main()






