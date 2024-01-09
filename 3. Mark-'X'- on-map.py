# Mark 'X' on a map
row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]
map = [row1, row2, row3]
user = input("please enter like this a1,a2,a3,b1,b2,b3,c1,c2,c3 to mark 'X' on map: ")
letter = user[0].lower()
number_index = int(user[1]) - 1
abc = ['a', 'b', 'c']
letter_index = abc.index(letter)
map[number_index][letter_index] = "X"
print(f"{row1} \n{row2} \n{row3}")


#         ( OR )
# simple code using if-elif-else statements
row1 = ["","",""]
row2 = ["","",""]
row3 = ["","",""]
map = [row1, row2, row3]
user = input("please enter like this a1,a2,a3,b1,b2,b3,c1,c2,c3 to mark 'X' on map: ")
if user == "A1" or user == "a1":
  map[0][0] = "X"
elif user == "A2" or user == "a2":
  map[0][1] = "X"
elif user == "A3" or user == "a3":
  map[0][2] = "X"

if user == "B1" or user == "b1":
  map[1][0] = "X"
elif user == "B2" or user == "b2":
  map[1][1] = "X"
elif user == "B3" or user == "b3":
  map[1][2] = "X"

if user == "C1" or user == "c1":
  map[2][0] = "X"
elif user == "C2" or user == "c2":
  map[2][1] = "X"
elif user == "C3" or user == "c3":
  map[2][2] = "X"
print(f"{row1}\n{row2}\n{row3}")


# Output:
Sample - 1
please enter like this a1,a2,a3,b1,b2,b3,c1,c2,c3 to mark 'X' on map: a1
['X', '', ''] 
['', '', ''] 
['', '', '']

Sample - 2
please enter like this a1,a2,a3,b1,b2,b3,c1,c2,c3 to mark 'X' on map: a3
['', '', ''] 
['', '', ''] 
['X', '', '']

Sample - 3
please enter like this a1,a2,a3,b1,b2,b3,c1,c2,c3 to mark 'X' on map: c3
['', '', '']
['', '', '']
['', '', 'X']

Sample - 4
please enter like this a1,a2,a3,b1,b2,b3,c1,c2,c3 to mark 'X' on map: b2
['', '', ''] 
['', 'X', ''] 
['', '', '']
