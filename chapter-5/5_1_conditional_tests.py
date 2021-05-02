'''
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least ten tests. Have at least five tests evaluate to True and
another five tests evaluate to False.
'''

colors = ["red", "yellow", "green"];
print("Is blue in colors? I predict False.");
print("blue" in colors);
print("Is green in colors? I predict True.");
print("Green".lower() in colors);

x = 10
y = 3
print(x > 10);
print(x > 10 and y == 3);
print(x > 10 or y == 3);
print(x != 11);

x = "Good";
print(x == "good");
print(x.lower() == "good");
print(x == "good".title());

print(x not in colors);
print(colors);

print(x);
print(y);