import operator
#Defining the function to calculate the number of characters in the string, and then it is stored in the dictionary D.
def most_frequent(val):
    D = dict()
    for i in val:
        if i not in D:
            D[i] = 1
        else:
            D[i] += 1

#Sort the dictionary in the decreasing order using the sorted built-in function.
    Dsort = dict(sorted(  D.items(),
                       key=operator.itemgetter(1),
                       reverse=True))

#Printing the elements of dictionary in different lines.
    for key, value in Dsort.items():
        print(key, ' : ', value)
    exit(0) #End of defining the function.

#Main function to take input and to perform the function call.
if __name__ == '__main__':
    str = input('Please enter a string\n').casefold()
    print(most_frequent(str)) #Function call
