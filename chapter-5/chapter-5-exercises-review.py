# Chapter 5 exercise review

'''
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least ten tests. Have at least five tests evaluate to True and
another five tests evaluate to False.
'''

# need to review this question!!!
print(1 < -1);
print(1 < -1 and 1 > 0);
print(1 < -1 or 1 > 0);
print('a' == 'b');
print('a' > 'b');
print('a' < 'b');
print('z' > 'a');
print(ord('a'));
print(ord('a') > 10);
print('good' > 'bad');

'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to ten. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
'''

print("good" == "bad");
print("good" != "bad");

print("good" == "Good".lower());
print("G" == "g".upper());

print(1 == 2);
print(1 != 2);
print(1 > 2);
print(1 < 2);
print(1 >= 1);
print(1 <= 2);

print("Good".upper() == "GOOD" and "Bad".lower() == "bad");
print("Good".lower() == "GOOD" or "BAD".title() == "Bad");

fruits = ["apple", "banana", "grape"];
print("apple" in fruits);
print("banana" not in fruits);
print("pple" in fruits);
print("apple" and "grape" in fruits);

print("apple" or "orange" not in fruits);
# putput: apple...why not True????
# solved: use parentheses () to output booleen values.



'''
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)
'''

alien_color = 'green';
if alien_color == 'green':
	print("You just earned 5pts!");

if alien_color == 'yellow':
	print("You just earned 5pts!");

'''
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned
10 points.
• Write one version of this program that runs the if block and another that
runs the else block.
'''

alien_color = "green";
if alien_color == "green":
	print("You just earned 5pts!");
else:
	print("You didn't earn 5pts!");


if alien_color == "yellow":
	print('You just earned 5pts!');
else:
	print("Oops, you missed 5pts!");


'''
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.
'''

alien_color = "green";
if alien_color == "green":
	print("You just earned 5pts!");
elif alien_color == "yellow":
	print("You just earned 10pts!");
else:
	print("You just earned 15pts!");


alien_color = "yellow";
if alien_color == "green":
	print("You just earned 5pts!");
elif alien_color == "yellow":
	print("You just earned 10pts!");
else:
	print("You just earned 15pts!");


alien_color = "red";
if alien_color == "green":
	print("You just earned 5pts!");
elif alien_color == "yellow":
	print("You just earned 10pts!");
else:
	print("You just earned 15pts!");


'''
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is
a baby.
• If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
• If the person is age 65 or older, print a message that the person is an
elder.
'''

age = 65;
if age < 2:
	print("baby");
elif 2 <= age < 4:
	print("toddler");
elif 4 <= age < 13:
	print("kid");
elif 13 <= age < 20:
	print("teengaer");
elif 20 <= age < 65:
	print("adult");
else:
	print("elder");

'''
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
'''

favorite_fruits = ["apple", "grape", "banana", "orange"];
if "apple" in favorite_fruits:
	print(f"I really like {favorite_fruits[0]}s!");

if "pears" not in favorite_fruits:
	print("I don't like pears.");

'''
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.
'''
usernames = ["admin", "jason", "callan", "josh"];
for username in usernames:
	if username == "admin":
		print(f'Hello {username}, would you like to see a status report?');
	else:
		print(f'Hello {username.title()}, thank you for logging in again!');



'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.
'''

# review this question!!

'''
usernames = []; #"admin", "jason", "callan", "josh"];
if usernames:
	print("We need to find some users!");
else:
	for username in usernames:
		if username == "admin":
			print(f'Hello {username}, would you like to see a status report?');
		else:
			print(f'Hello {username.title()}, thank you for logging in again!');
'''
usernames = ['admin', 'zhaozhi', 'jason', 'callan', 'christine'];
usernames = [];
if usernames:
	for username in usernames:
		if username == "admin":
			print(f'Hello {username}, would you like to see a status report?');
		else:
			print(f'Hello {username}, welcome back!');
else:
	print("We need to find some users!");

'''
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
current_users containing the lowercase versions of all existing users.)
'''

#review this exercise
current_users = ['george', 'zhaozhi', 'jason', 'callan', 'christine'];

new_users = ['otto', 'zhaozhi', 'Jason'];

for user in new_users:
	if (user and user.lower()) in current_users:
		print("This username is not available");
	else:
		print("Avaiable for use.");

###

print('Jason'.lower() in current_users);
print('Jason' in current_users);
print('Jason'.lower() or 'Jason' in current_users); #jason 
print(('Jason'.lower() or 'Jason') in current_users); #True

###

user = "Jason";
print(user in current_users); # False
print(user.lower() in current_users); #True
print(user or user.lower() in current_users); #Jason
print((user and user.lower()) in current_users); #True


'''
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending
for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.
'''

# review this question
ordinal_numbers = [value for value in range(1, 10)];
print(ordinal_numbers);
for number in ordinal_numbers:
	if number == 1:
		print(f'{number}st');
	elif number == 2:
		print(f'{number}nd');
	elif number == 3:
		print(f'{number}rd');
	else:
		print(f'{number}th');


'''
5-12. Styling if statements: Review the programs you wrote in this chapter, and
make sure you styled your conditional tests appropriately.
'''



'''
5-13. Your Ideas: At this point, you’re a more capable programmer than you
were when you started this book. Now that you have a better sense of how
real-world situations are modeled in programs, you might be thinking of some
problems you could solve with your own programs. Record any new ideas you
have about problems you might want to solve as your programming skills continue
to improve. Consider games you might want to write, data sets you might
want to explore, and web applications you’d like to create.
'''