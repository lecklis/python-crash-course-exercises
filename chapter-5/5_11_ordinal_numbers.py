'''

5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending
for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.

'''

numbers = [value for value in range(1, 10)];
print(numbers);

for i in numbers:
	if i == 1:
		print(f'{i}st');
	elif i == 2:
		print(f'{i}nd');
	elif i == 3:
		print(f'{i}rd');
	else:
		print(f'{i}th');