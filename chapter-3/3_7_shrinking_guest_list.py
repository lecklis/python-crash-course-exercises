'''
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
• Print a message to each of the two people still on your list, letting them
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
'''

guest_list = ['Nenad', 'Chris', 'Steve', 'Callan', 'Xuanbin', 'George'];

''' Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
'''
print(f'''Hello {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}, and {guest_list[5]},
	\nUnfortunately, there is enough space for only two guests.
	\nZhaozhi''');

''' Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
'''
dropped_guest = guest_list.pop();
print(f'Sorry {dropped_guest}, I am unable to invite you to dinner.');

dropped_guest = guest_list.pop();
print(f'Sorry {dropped_guest}, I am unable to invite you to dinner.');

dropped_guest = guest_list.pop();
print(f'Sorry {dropped_guest}, I am unable to invite you to dinner.');

dropped_guest = guest_list.pop();
print(f'Sorry {dropped_guest}, I am unable to invite you to dinner.');

print(guest_list);

'''
Print a message to each of the two people still on your list, letting them
know they’re still invited.
'''

print(f"Hi {guest_list[0]}, you're still invited to my dinner.");
print(f"Hi {guest_list[1]}, you're still invited to my dinner.");

'''
Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
'''
del guest_list[0];
del guest_list[0];
print(guest_list);
