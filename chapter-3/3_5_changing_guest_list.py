'''
3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end
of your program stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list.
'''

#print out the original guest list
guest_list = ['Jason', 'Callan', 'Xuanbin'];
print(f'The original guest list includes {guest_list[0]}, {guest_list[1]}, and {guest_list[2]}.');

#remove the guest using the pop() method.
removed_guest = guest_list.pop(0)
print(f"Unfortunately, {removed_guest} can't make the dinner.");

#replaced the removed guest with the new guest using insert().
guest_list.insert(0, "Chris");

#send invitations
print(f'Hi {guest_list[0]}, are you willing to join my dinner?');
print(f'Hi {guest_list[1]}, are you willing to join my dinner?');
print(f'Hi {guest_list[-1]}, are you willing to join my dinner?');

