input = "ↂↁMMDDDCCLXXVIII"  # this (roman)-input will call decimalToRoman()
# input = 18778 # this (int- input would call romanToDecimal()
dicTupel = [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000), ("ↁ", 5000), ("ↂ", 10000)]


# converts decimal input to roman
def decimalToRoman(input):
    dicTupel.reverse()  # to begin operation with the biggest number
    res = ""
    for k, v in dicTupel:  # loop dicTupel-items
        if (input / v) >= 1:  # if input contains v(alue),
            count = int(input / v)  # how often input contains element
            while count > 0:
                res += k  # add k(ey) to res(ult)
                input -= v  # subtract v(alue) from input
                count -= 1  # decrease counter
    print(res)


# converts roman input to decimal
def romanToDecimal(input):
    operators = ""
    res = 0
    for c in input:  # for each c(har) in input
        for k, v in dicTupel:  # loop dicTupel-items
            if c == k:  # if k(ey) found,
                operators += "+" + str(v)  # concat each operation
                res += v  # add v(alue) to res(ult)
    print(operators)
    print("=" + str(res))


if __name__ == '__main__':

    # check direction of conversion
    if type(input) is int:
        print("Direction: DECIMAL --> ROMAN with: " + str(input))
        decimalToRoman(input)
    elif (type(input) is str):
        print("Direction: ROMAN --> DECIMAL with: " + input)
        romanToDecimal(input)
