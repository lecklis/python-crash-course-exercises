# Chapter 2 exercise review

''' question 2-1: Simple Message: Assign a message to a variable, and then print that
message. '''

message = "Hello world!";
print(message);

'''2-2. Simple Messages: Assign a message to a variable, and print that message.
Then change the value of the variable to a new message, and print the new
message.'''

original_msg = "This is original.";
print(original_msg);

updated_msg = "This is updated.";
print(updated_msg);

''' 2-3. Personal Message: Use a variable to represent a person’s name, and print
a message to that person. Your message should be simple, such as, “Hello Eric,
would you like to learn some Python today?” '''

name = "Jason Rivera";
print(f"Hello {name}, would you like to meet up today?");

'''
2-4. Name Cases: Use a variable to represent a person’s name, and then print
that person’s name in lowercase, uppercase, and title case.
'''

name = "jason rivera";
print(name.lower());
print(name.upper());
print(name.title());

''' 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
quote and the name of its author. Your output should look something like the
following, including the quotation marks: 
Albert Einstein once said, “A person who never made a
mistake never tried anything new.”
'''

print('Andrew Ng once said, "AI is the new electricity."');

'''
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the
famous person’s name using a variable called famous_person. Then compose
your message and represent it with a new variable called message. Print your
message.
'''

famous_person = "Andrew Ng";
quote = "AI is the new electricity.";
print(f'{famous_person} once said, "{quote}"');

'''
2-7. Stripping Names: Use a variable to represent a person’s name, and include
some whitespace characters at the beginning and end of the name. Make sure
you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(),
rstrip(), and strip().
'''

# 这题需要多练习
name = " Jason Rivera ";
print(name);
print("\t"+name);
print("\n"+name);
print(name.strip());
print(name.rstrip());
print(name.lstrip());


'''
2-8. Number Eight: Write addition, subtraction, multiplication, and division
operations that each result in the number 8. Be sure to enclose your operations
in print() calls to see the results. You should create four lines that look like this:
print(5+3)
Your output should simply be four lines with the number 8 appearing once
on each line.
'''

print(4+4);
print(10-2);
print(2*4);
print(24/3);

'''
2-9. Favorite Number: Use a variable to represent your favorite number. Then,
using that variable, create a message that reveals your favorite number. Print
that message.
'''

#加分：2
number = 8;
print(f'My favorite number is {number + 2}.');

'''
2-10. Adding Comments: Choose two of the programs you’ve written, and
add at least one comment to each. If you don’t have anything specific to write
because your programs are too simple at this point, just add your name and
the current date at the top of each program file. Then write one sentence
describing what the program does.
'''

#Good job!
number = 8;
print(f'My favorite number is {number + 2}.');

'''
2-11. Zen of Python: Enter import this into a Python terminal session and skim
through the additional principles.
'''

import this;