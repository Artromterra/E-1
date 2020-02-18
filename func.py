LETTER = ""
SECRET_WORD = ""
GAMER_WORD = ""

def letter_found(letter, secret_word, gamer_word):
	for idx, symbol in enumerate(secret_word):
		# print(idx, symbol)
		if symbol == letter:
			gamer_word[idx] = symbol.upper()
	return gamer_word

