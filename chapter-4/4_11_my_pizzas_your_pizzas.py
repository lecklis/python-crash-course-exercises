'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite
pizzas are:, and then use a for loop to print the first list. Print the message
My friend’s favorite pizzas are:, and then use a for loop to print the second
list. Make sure each new pizza is stored in the appropriate list.

'''

my_hobbies = ["sketching", "blogging", "programming"];
friend_hobbies = my_hobbies;

my_hobbies.append("reading");
friend_hobbies.append("swimming");

print(f'My hobbies include: {my_hobbies}.');
print(f"My friend’s hobbies are: {friend_hobbies}.");

print("\nMy friend's hobbies include the following:");
for hobby in friend_hobbies:
	print(hobby);