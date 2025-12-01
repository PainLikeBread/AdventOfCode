fileOutput = open("input.txt", "r")
combos = fileOutput.read().splitlines()

def crack_password(input):
    dial = 50
    zeroCount = 0
    for turn in input:
        direction = turn[0]
        amount = int(turn[1:])
        if direction == "L":
            dial = (dial - amount) % 100
        else:
            dial = (dial + amount) % 100
        if (dial == 0):
            zeroCount += 1
    return zeroCount

#print(crack_password(combos))

def method0x434C49434B(input):
    dial = 50
    zeroCount = 0
    for turn in input:
        direction = turn[0]
        amount = int(turn[1:])
        if direction == "L":
            dial -= amount
            
            print("direction: " + str(direction) + ", amount " + str(amount) + ", crossed zero? " + str(dial < 0) + ", Number of 0 crosses? " + ", turn count: " + str(dial))
        else:
            dial += amount
            print("direction: " + str(direction) + ", amount " + str(amount) + ", crossed zero? " + str(dial > 100) + ", Number of 0 crosses? " + ", turn count: " + str(dial))
        dial = dial % 100
        print("true dial: " + str(dial))
    return zeroCount

print("PASSWORD: " + str(method0x434C49434B(combos)))