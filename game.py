import random
from func import letter_found

print('Игра виселица.')

words_list = ('skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage')

secret_word = random.choice(words_list)
print(secret_word)
print('Загадано слово, состоящее из {} букв.'.format(len(secret_word)))
gamer_word = ['_ '] * len(secret_word)
print(''.join(gamer_word))


errors_counter = 0
while True:
	letter = input('введите ОДНУ латинскую букву: ').lower()
	if len(letter) != 1 or not letter.isalpha():
		continue

	if letter in secret_word:
		print(''.join(letter_found(letter, secret_word, gamer_word)))
		if '_ ' not in gamer_word:
			print('вы выиграли!!!')
			print('было загадано слово', secret_word.upper())
			break
	else:
		errors_counter += 1
		print('ошибок допущено', errors_counter)
		if errors_counter > 3:
			print('вы проиграли :(')
			break

print('играйте еще!')
