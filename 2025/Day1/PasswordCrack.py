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


print(crack_password(combos))