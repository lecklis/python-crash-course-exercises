'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to ten. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
'''

value1 = "Yes";
value2 = "No";

print(value1 != value2);
print(value1 == value2);
print(value1.upper() == "YES" and value2.lower() == "no");
print(value1.upper() == "YES" or value2.upper() == "NOPE");

value3 = "Unknown";

booleen_list = ["Yes", "No", "unknown"];
print(value1 in booleen_list and value2 in booleen_list);
print(value1 in booleen_list and value3 not in booleen_list);
print(value1 in booleen_list and value3.lower() in booleen_list);

num1 = -10;
num2 = 10;
num3 = 20;

print(-10 + 20 > 0);
print(-10 <= -10 or 20 > 20);