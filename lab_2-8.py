# author: JHR 09/21/22

# x = input for a team's score

x = 1

if x > 15:
    print ("You have won a Gold Medal!")
else: 
    if 14 >= x >= 12:
        print ("You have won a Silver Medal!")
    else:
        if 11 >= x >= 9:
            print ("You have won a Bronze Medal!")
        else:
            print ("You failed!")
