from binary_converter import binaryToInt

f = open("input/day 3 input", "r")

inpu = []
for line in f:
    inpu.append(line.strip())

mostCommonBits = ""
for i in range(len(inpu[0])):
    oneCount = 0 # Amount of 1's in that postition
    zeroCount = 0 # Amount of 0's in that position
    for s in inpu:
        c = s[i]
        if c == "1":
            oneCount += 1
        elif c == "0":
            zeroCount += 1

    if oneCount > zeroCount:
        mostCommonBits += "1"
    else:
        mostCommonBits += "0"

gamma = binaryToInt(mostCommonBits)
epsilon = binaryToInt(mostCommonBits, oneChar="0", zeroChar="1")

print(gamma)
print(epsilon)
print(gamma * epsilon)