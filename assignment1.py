# question 4 (unit 2) number of odd seven digit integers with non-repeating
# characters, using list comprehension from this week's class.


def question1():

    # lst = {x for x in range (0,9999999) for char in str(x) if (x % 2 == 1)
    #   and str(x).count(char)==1}

    # this list comprehension adds an item to the list if it is odd
    # and if no character in the string occurs greater than once.
    lst = [x for x in range(0, 10000000) if (x % 2 == 1)
           and all([0 for char in list(str(x)) if str(x).count(char) > 1])]
    return len(lst)

# PyCharm CE can convert the list comprehension to for loop for cross-check


def question1_var():

    lst2 = [x for x in range(0, 10000000)]
    count = 0
    for num in lst2:
        if num % 2 == 1 and len(str(num)) == len(set(list(str(num)))):
            count += 1
    return count


import time
start_time = time.time()

print("initial list comprehension approach", question1())
print("--- %s seconds ---" % (time.time() - start_time))
print("second set and list length approach", question1_var())
print("--- %s seconds ---" % (time.time() - start_time))
print("here's my paper solution", 10*9*8*7*6*5*2)
print("--- %s seconds ---" % (time.time() - start_time))