import random 
 
chances = 5 
answer = random.choice(range(1,50)) 
won = False 
print("Guess a number between 1 & 50")
while chances>0 and not won: 
	print('Chances remaining =',chances) 
	guess = int(input('Enter your guess: ')) 
 
	if guess==answer: 
		print("Congrats! You've won.") 
		won = True 
	elif guess>answer and chances>1: 
		print('Your guess is high. Guess lower\n') 
	elif guess<answer and chances>1: 
		print('Your guess is low. Guess higher\n') 
	 
	chances -= 1 
 
if not won and chances==0: 
	print('You failed. Answer:',answer) 