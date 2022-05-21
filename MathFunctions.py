# Even though is a math.function, this is an exercise
# for myself in the event I take this into a different
# language that doesn't have such libraries.

def iFactorial(iNum):

    iResult = 1

    while iNum != 0:

        iResult *= iNum
        iNum -= 1

    return iResult

# Combinations in probability and statestics
def iCombinations(iSelection, iSetTotal):

    return iFactorial(iSetTotal) / (iFactorial(iSelection) * iFactorial(iSetTotal - iSelection))


# Permutations are similar to combinations
def iPermutations(iSelection, iSetTotal):

    return iFactorial(iSetTotal) / iFactorial(iSetTotal - iSelection)

# Numerical solution to a polynomial term according to the power rule
def iIntegratePolyTerm(iCoeff, iVar, iPower):

    iNewPower = iPower + 1

    return (iCoeff * (iVar ** iNewPower)) / iNewPower

# Numerical solution to a polynomial term according to the power rule
def iDifferentiatePolyTerm(iCoeff, iVar, iPower):

    iNewPower = iPower - 1

    return (iCoeff * iPower * (iVar ** iNewPower))

# Tested.  Returns an array of prime numbers that when multiplied together, create the original number.  Optimized for speed
def iArrFactorsOfNum(iNum):

    iArrFactors = []
    iDivisor = 2

    while iDivisor <= iNum:

        #print ("Number = " + str(iNum))
        #print ("Divisor = " + str(iDivisor))

        while iNum % iDivisor == 0:

            iArrFactors.append(iDivisor)
            #print(str(iNum) + " is divisible by " + str(iDivisor))

            iNum /= iDivisor
            #print("New Number: " + str(iNum))

        if iDivisor != 2:

            iDivisor += 2

        else:

            iDivisor += 1

    if len(iArrFactors) == 1:

        return "1 and itself"

    return iArrFactors

def bIsPrimeNumber(iNum):

    iMidPoint = iNum // 2
    iDivisor = 2

    while iNum <= iMidPoint:

        if iNum % iDivisor == 0: return False

        if iDivisor != 2:

            iDivisor += 2

        else:

            iDivisor += 1

    return True


def bHasPrimeFactor(iNum, iFactor):

    iArrOfFactors = iArrFactorsOfNum(iNum)

    for iPrimeNo in range(len(iArrOfFactors)):

        if iArrOfFactors[iPrimeNo] == iFactor:

            return True
        
    return False


def iArrBreakDigits(iNum):

    return int(iDigits) for iDigits in str(iNum)


def bDiffRequiresBorrowing(iLargerNum, iSmallerNum):

    if iLargerNum =< iSmallerNum return False

    # Turn numbers into arrays and analyze them from right to left
    iArrSNum = iArrBreakDigits(iSmallerNum)
    iArrLNum = iArrBreakDigits(iLargerNum)

    # print(iArrSSum + " vs. " + iArrLSum)

    iArrSNLen = len(iArrSNum) - 1
    iArrLNLen = len(iArrLNum) - 1

    # Needs to iterate R to L.

    while iArrSNLen >= 0:

        if iArrSNum[iArrSNLen] > iArrLNum[iArrLNLen]:

            return True

        iArrSNLen -= 1
        iArrLNLen -= 1

    return False


def bAddRequiresCarryingDigits(iLargerNum, iSmallerNum):

    # Switches inputs in the event they were entered out of order
    if iLargerNum < iSmallerNum:

        iLargerNum, iSmallerNum = iSmallerNum, iLargerNum

    iArrSNum = iArrBreakDigits(iSmallerNum)
    iArrLNum = iArrBreakDigits(iLargerNum)

    # Provides indices of right most index
    iArrSNLen = len(iArrSNum) - 1
    iArrLNLen = len(iArrLNum) - 1

    # Needs to iterate R to L, and only on the smallest number.

    while iArrSNLen >= 0:

        if iArrSNum[iArrSNLen] + iArrLNum[iArrLNLen] > 10:

            return True

        iArrSNLen -= 1
        iArrLNLen -= 1

    return False

# Test Functions