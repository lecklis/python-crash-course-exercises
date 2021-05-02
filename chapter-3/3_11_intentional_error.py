'''
3-11. Intentional Error: If you haven’t received an index error in one of your
programs yet, try to make one happen. Change an index in one of your programs
to produce an index error. Make sure you correct the error before closing
the program.
'''

list_errors = ["Python", "JavaScript", "C#"];
print(list_errors[-4]);

'''
Traceback (most recent call last):
    print(list_errors[-4]);
IndexError: list index out of range
[Finished in 0.4s with exit code 1]
'''
