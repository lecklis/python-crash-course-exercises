'''
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
'''

jason_rivera = {
	'first_name' : 'Jason',
	'last_name' : 'Rivera',
	'age' : 21,
};

print(jason_rivera);
print(jason_rivera.get("age", "Age not exists."));

jason_rivera['city'] = 'Chicago';
print(f'Jason Rivera is from {jason_rivera.get("city", "somewhere in the Midwest")}.');

print(jason_rivera);
