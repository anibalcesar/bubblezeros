#!/usr/bin/python


#
# CONSTANTS AND DEFINITIONS
#
BUBBLE = 0


#
# CODE
#
def bubbleIntegers(inputArray):
    """
    Moves the defined integers to the beginning of a given array

    @type  inputArray: list
    @param inputArray: array of integers

    @rtype: list
    @returns: same array but with zeros at the beginning
    """

    # extract the defined integers
    cleaned = [] 
    removed = []
    cleaned, removed = extractIntegers(inputArray, removed)

    # join arrays
    removed.extend(cleaned)
    return removed

# bubbleIntegers()

def extractIntegers(inputArray, removed):
    """
    Moves the defined integers to the beginning of a given array

    @type  inputArray: list
    @param inputAarray: array of integers

    @type  removed: list
    @param removed: array of removed integers

    @rtype: tuple
    @returns: cleaned array and array of removed integers
    """

    # integer not found: do nothing to input
    if not BUBBLE in inputArray:
        return inputArray, removed

    # defined integer found: remove it
    inputArray.remove(BUBBLE)
    removed.append(BUBBLE)
    return extractIntegers(inputArray, removed)

# extractIntegers()

# main code
if __name__ == "__main__":

    # read input
    inputArray = input("Enter the array: ")

    # print new array
    newArray = bubbleIntegers(inputArray)
    print newArray
