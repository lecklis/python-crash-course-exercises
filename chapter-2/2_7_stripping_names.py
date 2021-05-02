'''
2-7. Stripping Names: Use a variable to represent a person’s name, and include
some whitespace characters at the beginning and end of the name. Make sure
you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
'''

name = " Zhaozhi Li ";
print(name); #original
print(name.strip()); #remove whitespaces from both left and right
print(name.rstrip()); #remove whitespaces on the right
print(name.lstrip()); #remove whitespaces on the left

team_members = "Team members include: \n\tZhaozhi Li,\n\tJason Rivera,\n\t...";
print(team_members);
