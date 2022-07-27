'''

I - ARITHMETIC OPERATORS

    These functions are basic, but help to make the code more readable in other sections.

A - Coding Philosophy
    A wise programmer once said:
    "Your code should explain your comments to the computer..."

    and so you shall see in the code below.

'''

from PROG_GenFunctions import validateInputs

# Part 1 - Elementary Functions

def difference(finalNum, initialNum):

    ''' 
    While this function may seem silly at first glance, I've created it for several reasons:

        1 - To reduce my operators shown down to only '+'s,
        2 - To ensure that order of operations are always fully followed
        3 - To help with reference calculations in engineering, and
        4 - To make code more readable from left to right and not worrying about match parentheses
    '''

    # 1 - Validation of Inputs
    userInputArr = [finalNum, initialNum]

    # 2 - Calculate Result
    return if validateInputs(userInputArr, "difference") else return (finalNum - initialNum)


def ratio(numOfRatio, denOfRatio):

    ''' 
        While this function may also seem silly at first glance, I've created it for several reasons:

        1 - To reduce my operators down to only '+'s,
        2 - To ensure that order of operations are always fully followed
        3 - To make code more readable from left to right and not worrying about match parentheses

    '''

    # 1 - Validation of Inputs
    userInputArr = [numOfRatio, denOfRatio]

    # Checks for Nonnumeric inputs
    if !validateInputs(userInputArr, "Ratio"):

        return # Kill Statement

    # Divide by Zero Issues
    if denOfRatio == 0:

        print("Denominator cannot be {} for ratio!".format(denOfRatio))
        return # Kill Statement

    return (numOfRatio / denOfRatio)


def integerRatio(numOfRatio, denOfRatio):

    return ratio(numOfRatio, denOfRatio)


def iFactorial(numOfRatio, isNegative = True):

    # 1 Validation of Inputs

    # First checks to make sure it is an integer
    if not isinstance(numOfRatio, int):

        # Checks to make sure the number is at least a float, and if not, aborts the function.
        if not isinstance(numOfRatio, float): 
            
            print("{} is not a number!".format(numOfRatio))
            return # Kill Statement 

        # Attempts to Redeem Float By Converting It Into an Integer Required for Factorial Calculations
        numOfRatio = int(numOfRatio)

    # Next, check to make sure the number is positive, and if not, convert it unless overridden in function inputs
    if numOfRatio < 0 and isNegative:

        print("{} converted to a positive number!".format(numOfRatio))
        numOfRatio = -numOfRatio

    # Usually only happens if the user explicitly says do not convert.
    else

        print("{} cannot be a negative number in iFactorial!".format(numOfRatio))
        return # Kill Statement

    # Baseline Starting Point because 1 * n = n
    iResult = 1

    # A Factorial Calculation is given as n * (n - 1) * (n - 2) ... (n - (n - 2) * (n - (n - 1)))
    # Function stops at 1 instead of 0 because multiplying by 1 is meaningless.
    while numOfRatio != 1:

        iResult *= numOfRatio
        numOfRatio -= 1

    # Once numOfRatio reaches 1, the result is ready for return
    return iResult


def reciprical(numOfRatio):

    # Validation of Inputs
    if not isinstance(numOfRatio, (int, float)):

        print("{} is not a valid input for reciprical".format(numOfRatio))
        return

    # Shows 
    if numOfRatio == 0:

        print("{} has an indeterminant reciprocal!".format(numOfRatio))
        return

    # Calculates from ratio as 1 / numOfRatio
    return ratio(1, numOfRatio)


def polynomialTerm(polynomialCoeff, polynomialBase, polynomialPower = 1):

    # Setup for Validation of Inputs
    userInputArr = [polynomialCoeff, polynomialBase, polynomialPower]

    return polynomialCoeff * (polynomialBase ** polynomialPower) if validateInputs(userInputArr, "polynomialTerm") else return


def scientificNotation(polynomialCoeff, polynomialPower):

    # Validation taken care of in next step
    return polynomialTerm(polynomialCoeff, 10, polynomialPower)


def convertFloatToPercent(decimalNum):

    if not isinstance(decimalNum, (int, float)):
    
        print("{} is not a valid input for convertFloatToPercent!".format(decimalNum))
        return
        
    return 100 * decimalNum


def sumOfNumsOverProduct(inputNumbersArr):

    # Some Good Ol' Fashioned Validation: Make sure it's an array and the array has numbers only.
    if len(inputNumbersArr) == 1:

        print("Your input {} is not valid array for sumOfNumsOverProduct.".format(inputNumbersArr))
        return

    for inputNumber in range(len(inputNumbersArr)):

        if not isinstance(inputNumbersArr[inputNumber], (int, float)):

            print("{} is not a valid number within {}!".format(inputNumbersArr[inputNumber], inputNumbersArr))
            return

        elif inputNumbersArr[inputNumber] == 0:

            print("Warning! Digit {} within array {} has a zero which will be disregarded in the Sum over Product!")

        else

            pass
    
    
    sumOfNums  = sum(inputNumbersArr)
    prodOfNums = 1
    
    for inputNumber in range(len(inputNumbersArr)):

        prodOfNums *= inputNumbersArr[inputNumber] if inputNumbersArr[inputNumber] != 0 else prodOfNums = prodOfNums

    return ratio(sumOfNums, prodOfNums)


def sAddFractions(numOfFraction_1, denOfFraction_1, numOfFraction_2, denOfFraction_2, bDebug = False):

    # 1 - Validation to ensure inputs are numeric
    userInputArr = [numOfFraction_1, denOfFraction_1, numOfFraction_2, denOfFraction_2]

    if validateInputs(userInputArr, "sAddFractions") != True:

        return
    
    # 2 - Transformative Process From Float to Integers, which is the definition of a rational num
    componentsOfFraction_1 = [numOfFraction_1, denOfFraction_1]
    componentsOfFraction_2 = [numOfFraction_2, denOfFraction_2]
    fractionsArr = [componentsOfFraction_1, componentsOfFraction_2]

    for fraction in range(len(fractionsArr)):

        # Put Validation Function here, if possible
        for numOfFraction in range(len(fraction)):

            if not isinstance(numOfFraction, int):

                # Do something here to transform them into decimaless integers

    print("Validation Complete:\nFractions: {} / {} + {} / {}".format(numOfFraction_1, denOfFraction_1, numOfFraction_2, denOfFraction_2))

    fractionMult_1 = factorsOfNumArr(denOfFraction_1)
    fractionMult_2 = factorsOfNumArr(denOfFraction_2)

    # Creates Factors and Find Correct Multiplier:
    

    # Multiply Numerator


def maximumPerimeterOfRectangle(areaOfRectangle):

    if not isinstance(areaOfRectangle, (int, float)):
        
        print({} "is not a valid input for maximumPerimeterOfRectangle()".format(areaOfRectangle))
        return

    return 2 * (areaOfRectangle + 1)


def minimumPerimeterOfRectangle(areaOfRectangle):

    if not isinstance(areaOfRectangle, (int, float)):
        
        print({} "is not a valid input for minimumPerimeterOfRectangle()".format(areaOfRectangle))
        return

    return 4 * math.sqrt(areaOfRectangle)


def decimalToBinary(numOfRatio):

    if not isinstance(numOfRatio, (int, float)):

        print("{} is not a valid number for binary!".format(numOfRatio))
        return

    exponent = 0

    comparativeNum = polynomialTerm(1, 2, exponent)
    binaryDigitsArr = []

    while comparativeNum < numOfRatio:

        exponent += 1
        comparativeNum = polynomialTerm(1, 2, exponent)


    if type(numOfRatio) == int or numOfRatio == int(numOfRatio):

        while comparativeNum > 0:

            if comparativeNum > numOfRatio:

                binaryDigitsArr.append(0)

            else: 
                
                binaryDigitsArr.append(1)
                numOfRatio -= comparativeNum

            exponent -= 1
            comparativeNum = polynomialTerm(1, 2, exponent)

        return binaryDigitsArr

    if type(numOfRatio) == float:

        # Set up code to have two bounds to look for
        comparativeNumMax = comparativeNum
        comparativeNumMid = 0
        # comparativeNumMin = -infinity
            
    
# Print Return Statements

def sCompoundFraction(decimalNum):

    if not isinstance(decimalNum, (int, float)):

        print("{} is not a valid input for sCompoundFraction!")
        return

    if type(decimalNum) == int:

        print("Input is already an integer:\n{} / 1".format(decimalNum))
        return 


    # Post Validation
    # Is the code below legit?
    iWholeNum = 0

    while decimalNum > 1:

        iWholeNum += 1
        decimalNum -= 1

    sFraction = sTransformDecToFraction(decimalNum)
    print("{} + {}".format(int(iWholeNum), sFraction))


def iAddForwardSubtractBackward(numOfRatioAdd, numOfRatioSub, numOfRatio_Start, numOfRatio_Stop, bPrint = False):

    userInputArr = [numOfRatioAdd, numOfRatioSub, numOfRatio_Start, numOfRatio_Stop]

    validateInputs(userInputArr, "iAddForwardSubtractBackward")

    # More Validation Steps are Needed For This Function To Ensure No Inf Loops

    bInfLoop = True

    if numOfRatioAdd > numOfRatioSub:

        if numOfRatioStop > numOfRatioStart:

            bInfLoop = False

    if numOfRatioAdd < numOfRatioSub:

        if numOfRatioStop < numOfRatioStart:

            bInfLoop = False

    # Start of Function
    numOfRatio = numOfRatio_Start
    iCounter = 0

    while numOfRatio < numOfRatio_Stop and !bInfLoop:

        numOfRatio += numOfRatioAdd
        numOfRatio -= numOfRatioSub
        iCounter += 1

    bPrint and print("It took {} iterations to get from {} to {} by adding {} and subtracting {}".format(iCounter, numOfRatio_Start, numOfRatio_Stop, numOfRatioAdd, numOfRatioSub))

# CONTINUE HERE

def bCheckForType(sFunctionName, vArrInputs, dataType):

    # Validation for data type

    for vDataPoint in vArrInput:

        vDataInQuestion = vArrInputs[vDataPoint]

        if type(vDataInQuestion) != dataType:

            print("{} accepts the type {} only.  Please check inputs and try again.".format(sFunctionName, dataType))
            return False

    return True


def sAddByCounting(numOfRatio_1, numOfRatio_2, bDebug = False):

    userInputArr = [numOfRatio_1, numOfRatio_2]

    if !bCheckForType("sAddByCounting", userInputArr, int): return

    iAddCount = 0

    # Double Check Operations Here
    while iAddCount <= numOfRatio_2:

        iAddCount += 1
        iIntermediateSum = numOfRatio_1 + 1

        print("{} was added to {} to create {}".format(iAddCount, numOfRatio_1, iIntermediateSum))


def sSubtractByCounting(numOfRatio_1, numOfRatio_2, bDebug = False):

    if type(numOfRatio_1) != int or type(numOfRatio_2) != int:   #DRY!

        print("sSubtractByCounting accepts integer only.  Please check inputs and try again.\nnumOfRatio_1 = {}\n numOfRatio_2 = {}".format(numOfRatio_1, numOfRatio_2))
        return

    # Swaps Numbers If Entered Out of Sequence
    numOfRatio_1, numOfRatio_2 = numOfRatio_2, numOfRatio_1 if numOfRatio_2 > numOfRatio_1

    iSubtractCount = 0

    # Double Check Operations Here
    while iSubtractCount <= numOfRatio_2:

        iSubtractCount += 1
        iIntermediateDiff = numOfRatio_1 - 1

        print("{} was taken away from {} to create {}}".format(iSubtractCount, numOfRatio_1, iIntermediateDiff))


def sMultiplyByAdding(numOfRatio_1, numOfRatio_2, bDebug = False):

print("sSubtractByCounting accepts integer only.  Please check inputs and try again.\nnumOfRatio_1 = {}\n numOfRatio_2 = {}".format(numOfRatio_1, numOfRatio_2))

    iMultCount = 0

    while iMultCount <= numOfRatio_2:

        iMultCount += 1
        iIntermediateProduct = numOfRatio_1 + iMultCount * numOfRatio_2

        print("{} was added to {} to create {}}".format(iMultCount, numOfRatio_1, iIntermediateProduct))