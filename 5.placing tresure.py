row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
position = int(position)
n1 = position%10
n2 = (position - n1)/10
if n1 == 1:
    if n2 == 1:
        row1[0] = "X" 
    elif n2 == 2:
        row1[1] = "X" 
    else:
        row1[2] = "X"
if n1 == 2:
    if n2 == 1:
        row2[0] = "X" 
    elif n2 == 2:
        row2[1] = "X" 
    else:
        row2[2] = "X"
if n1 == 3:
    if n2 == 1:
        row3[0] = "X" 
    elif n2 == 2:
        row3[1] = "X" 
    else:
        row3[2] = "X"
print(f"{row1}\n{row2}\n{row3}")