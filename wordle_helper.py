
valid_answers = open("answers.txt").read().splitlines() #["SAUTE","HELLO","BAlPE","TALLL","PTNLL","\0"]
valid_answers.append("\0")
correct_letters = {0:"_",1:"_",2:"_",3:"_",4:"_"}



def updateCorrect(letter, place):

	correct_letters[place] = letter

	i = 0
	while valid_answers[i] != "\0":
		if valid_answers[i][place] != letter:
			del(valid_answers[i])
			i -= 1
		i += 1


def updateMaybe(letter, place):
	
	i = 0
	while valid_answers[i] != "\0":
		if valid_answers[i][place] == letter or letter not in valid_answers[i]:
			del(valid_answers[i])
			i -= 1
		i += 1


def updateWrong(letter):

	i = 0
	while valid_answers[i] != "\0":
		if letter in valid_answers[i]:
			del(valid_answers[i])
			i -= 1
		i += 1



#C-R-A+N-E+ S-H-T*I-K- E-L-A+T+E+

print(" | +-+-+-+-+-+-+-+-+-+-+-+ |\n",
	  "| + after a green letter  |\n",
      "| * after a yellow letter |\n",
      "| - after grey            |\n",
	  "| Ex: c+r+n-a*e-          |\n",
	  "| +-+-+-+-+-+-+-+-+-+-+-+ |")

flag = 1
while flag == 1:
	

	if len(valid_answers) <= 5:
		
		print(f"\nSorry cant really help any further.Choose from these words: \n{valid_answers} ")
		break

	word = input("\nEnter word: ").lower()
	for i in range(0,len(word)):

		if word[i-1] in correct_letters.values():
			print(word[i])
			continue

		else:
			if word[i] == "+":
				updateCorrect(word[i-1],i//2)

			if word[i] == "*":
				updateMaybe(word[i-1],i//2)

			if word[i] == "-":
				updateWrong(word[i-1])

	#if len(valid_answers) <= 30:
		print(valid_answers)	
	
	print("\nDiscovered letters: ", end = " ")
	for vals in list(correct_letters.values()):
		print(vals,end = " ")
	

