# Chapter 2 exercises

''' question 2-1: Simple Message: Assign a message to a variable, and then print that
message. '''

simple_message = "assign a message and prin it out.";
print(simple_message);

'''2-2. Simple Messages: Assign a message to a variable, and print that message.
Then change the value of the variable to a new message, and print the new
message.'''

simple_messages = "original message";
print(simple_messages);

simple_messages = "updated message";
print(simple_messages);

''' 2-3. Personal Message: Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?” '''

name = "Jason Rivera";
message = "Hi, "+name+"! How is your Python course?";
print(message);

'''
2-4. Name Cases: Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.
'''

name = "Zhaozhi Li";
print(name.upper());
print(name.lower());
print(name.title());

''' 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks: 
Albert Einstein once said, “A person who never made a
mistake never tried anything new.”
'''

famous_quote = 'Andrew Ng, one of the most reputable AI researchers in the world, once said: "AI is the new electricity."';
print(famous_quote);

'''
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the
famous person’s name using a variable called famous_person. Then compose
your message and represent it with a new variable called message. Print your
message.
'''

famous_person = "Andrew Ng";
quote = "AI is the new electricity.";
message = f'{famous_person}, one of the most profound AI researchers, once said: "{quote}"';
print(message);

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

'''
2-8. Number Eight: Write addition, subtraction, multiplication, and division
operations that each result in the number 8. Be sure to enclose your operations
in print() calls to see the results. You should create four lines that look like this:
print(5+3)
Your output should simply be four lines with the number 8 appearing once
on each line.
'''

#addition, 
print(4+4);

#subtraction,
print(10-2);

#multiplication,
print(2*4);

'''
2-9. Favorite Number: Use a variable to represent your favorite number. Then,
using that variable, create a message that reveals your favorite number. Print
that message.
'''

favorite_number = 1_00;
message = "My favorite number is "+str(favorite_number)+".";
print(message);

'''
2-10. Adding Comments: Choose two of the programs you’ve written, and
add at least one comment to each. If you don’t have anything specific to write
because your programs are too simple at this point, just add your name and
the current date at the top of each program file. Then write one sentence
describing what the program does.
'''

#this is a single-line comment
print('"#" sign creates a single-line comment.');

'''
This is a multiple-line
comment.
'''
print(" ''' " +"sign creates mutiple lines of \ncomments.");

'''
2-11. Zen of Python: Enter import this into a Python terminal session and skim
through the additional principles.
'''

import this

