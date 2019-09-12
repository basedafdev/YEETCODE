def reverse(x: int) -> int:
    returnVal = 0
    if(x > 0):
        returnVal = int(str(x)[::-1])
    else:
        value = str(x)
        returnVal =int(value[0] + value[::-1][0:len(value)-1])
    if (abs(returnVal) >= 2147483648):
        return 0
    return returnVal

