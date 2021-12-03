def binaryToInt (string: str, oneChar = "1", zeroChar = "0"):
    out = 0
    for i in range(len(string)):
        currentDigit = None
        if string[len(string) - 1 - i] == oneChar:
            currentDigit = 1
        elif string[len(string) - 1 - i] == zeroChar:
            currentDigit = 0
        
        out += (2**i) * currentDigit
    return(out)

if __name__ == "__main__":
    print(binaryToInt("1011"))