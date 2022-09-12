
answer = 15
factor = 99 - answer

def calculation():
    result = (friend_number + factor)
    hundreds = (result % 1000) // 100
    result = (result - 100)
    result = (result + hundreds)
    result = (friend_number - result)
    return (result)

friend_number = int(input("Enter a number between 50 and 99: "))
while friend_number < 50 or friend_number > 99:
    print("That number is invalid")
    friend_number = int(input("Enter a number between 50 and 99: "))
else:
    print(calculation())


