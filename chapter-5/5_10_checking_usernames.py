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

current_users = ["zhaozhi_li", "jason_rivera", "callan_davey", "christine_david", "terence_ow"];
new_users = ["zhaozhi_li", "jason_rivera", "edward_micthell", "ted_anderson", "bryan_baland"];
for new_users in new_users:
	if new_users in current_users:
		print("Sorry, please select a different username.");
	else:
		print("The username is available");
print("Click here to sign up.");

#review this exercise