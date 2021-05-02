'''
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
'''

guest_list = ['Jason', 'Callan', 'Xuanbin'];

message_to_jason = f"Hi {guest_list[0]}, would you like to join my dinner party?";
print(message_to_jason);

message_to_callan = f"Hi {guest_list[1]}, would you like to join my dinner party?";
print(message_to_callan);

message_to_xuanbin = f"Hi {guest_list[-1]}, would you like to join my dinner party?";
print(message_to_xuanbin);
