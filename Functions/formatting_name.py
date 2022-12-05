def formatting_name(name):
    name = name.title()
    return name


name = input("enter the name to format : ")
formatted_name = formatting_name(name)
print(f"Your formatted name is : {formatted_name}")
