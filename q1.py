numbers = []
for i in range(10):
    numbers.append(int(input()))


x = 0
count = 0
while(x < 9):
    
    if numbers[x]%2 == 0 and numbers[x+1]%2 == 0:
        x = x+1
        count = count + 1
        while (numbers[x]%2 == 0):
            if x == 9:
                break
            x = x+1

    else:
        x = x+1

print(count)
# ******************************
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
