'''
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
'''

favorite_fruits = {"apple", "banana", "orange"};
if "apple" in favorite_fruits:
	print("I really like apples!")
if "banana" in favorite_fruits:
	print("I really like bananas!");
if "grapes" not in favorite_fruits:
	print("Grapes are not my favorite fruit.");