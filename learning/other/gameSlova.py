from random import randint

file = open('words.txt','r')
words = file.readlines()
length = len(words)

def getRandomWord():
	random_no = randint(0,length)
	word = words[random_no].strip()
	return word	


def gamePlay(random_word):
	chances = 7
	is_found = False
	gussed_letters = []
	guess = ''
	print('	'+'_ '*len(random_word)+'\n')
	while chances>0:
		guess = input('Guess the letter or the Entire word: ')
		if guess==random_word:
			is_found = True
		else:
			if guess in gussed_letters :
				print(f"You have already gussed the letter {guess}..try something else\n")
				continue
			print('	',end='')
			is_current_guess = False
			for letter in random_word:
				if letter == guess :
					is_current_guess = True
					gussed_letters.append(letter)
					print(letter,end=' ')
					if len(random_word) == len(gussed_letters):
						is_found = True
				elif letter in gussed_letters:
					print(letter,end=' ')
				else:
					print('_',end=' ')	
			print()		
		if is_found:
			print(f"Congrats your guess was correct, the word was '{random_word}'\n")		
			break
		if not is_current_guess:
			print(f'{guess} is not in word')
			chances-=1
			print(f'You have {chances} chances remaining\n')

	if not is_found:
		print(f"\n Sorry your guesses were wrong, the word was '{random_word}'\n")		


def main():
	print(" Word Guessing Game ".center(60,'-'))
	while True:
		random_word = getRandomWord()
		gamePlay(random_word)
		choice = input("Do You Wanna Play(yes/no) :")
		if choice in ['no','No','NO','n','N']:
			break


if __name__ == '__main__':
	main()