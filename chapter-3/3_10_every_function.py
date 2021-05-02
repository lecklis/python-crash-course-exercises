'''
3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.
'''

#create a list containing five different colors.
colors = ["blue", "red", "yellow", "green", "pink"];
print(colors);

#reverse order
colors.reverse();
print(colors);

#alphebatical order
colors.sort();
print(colors);

#reversed alphebatical order
colors.sort(reverse=True);
print(colors);

#change yellow to purple !!!
colors.sort();
colors[2] = "purple";
print(colors);

