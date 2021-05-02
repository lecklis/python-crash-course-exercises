'''
3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
call to the end of your program informing people that you found a bigger
dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
'''

guest_list = ['Chris', 'Callan', 'Xuanbin'];

#inform existing guests that more people will join.
print(f'''Hey {guest_list[0]}, {guest_list[1]}, and {guest_list[2]}! 
	\nWe got a larger-than-expected table. We will have more people to join us! 
	\nCheers,
	\nLi Zhaozhi''');

#Use insert() to add one new guest to the beginning of your list.
guest_list.insert(0, "Nenad");
print(guest_list);

#Use insert() to add one new guest to the middle of your list.
guest_list.insert(2, "Steve");
print(guest_list);

#Use append() to add one new guest to the end of your list.
guest_list.append("George");
print(guest_list);

#Print a new set of invitation messages, one for each person in your list.
print(f'Hi {guest_list[0]}, are you able to join my dinner?');
print(f'Hi {guest_list[1]}, are you able to join my dinner?');
print(f'Hi {guest_list[2]}, are you able to join my dinner?');
print(f'Hi {guest_list[3]}, are you able to join my dinner?');
print(f'Hi {guest_list[4]}, are you able to join my dinner?');
print(f'Hi {guest_list[5]}, are you able to join my dinner?');


