import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
number_of_names = len(names)
choose = random.randint(0,number_of_names-1)
name = names[choose]
print(f"{name} is going to buy the meal today!")