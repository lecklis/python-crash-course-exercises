'''
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.
'''

alien_color = " ";
score = 0;
if alien_color == "green":
	print("You just earned 5 points!");
	score = score + 5;
elif alien_color =="yellow":
	print("You just earned 10 points!");
	score = score + 10;
elif alien_color == "red":
	print("You just earned 15 points!");
	score = score + 15;
print(f'Your score is {score}.');