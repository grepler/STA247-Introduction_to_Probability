# question 4 (unit 2) number of odd seven digit integers with non-repeating
# characters, using list comprehension from this week's class.

def question1():

    lst = [x for x in range (0,9999999) for char in str(x) if (x % 2 == 1)
       and str(x).count(char)==1]
    return(len(lst))

# PyCharm CE can convert the list comprehension to for loop for cross-check

def question1_var():
    lst = []
    for x in range(0, 9999999):
        for char in str(x):
            if (x % 2 == 1) and str(x).count(char) == 1:
                lst.append(x)
    return(len(lst))

