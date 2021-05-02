'''
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.
'''

menu = ("beef", "pork", "salad", "chicken", "salmon");
for food in menu:
	print(food);

'''
menu[1] = "vegetable";
print(menu);

'''
revised_menu = ("beef", "port", "salad", "shrimp", "vegetable");
print(revised_menu)