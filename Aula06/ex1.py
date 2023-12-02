import my_modules 

events = ["Kill enemy","Find secret", "Learn a skill","Consume a power-up","Find Companion"]
events2 = ["Complete mission", "Get to level 10", "Kill a boss"]


generated_events = my_modules.random_events(events)
inverted_events = my_modules.invert_events(generated_events)

print(f"Generated events: {generated_events}")

print(f"Inverted envents: {inverted_events}")

events2_randomized = my_modules.random_events(events2)

list_with_added_events = my_modules.add_events(inverted_events, events2_randomized )
print(f"List with added events: {list_with_added_events}")

process_all_events = my_modules.process_events(list_with_added_events)


print(process_all_events)