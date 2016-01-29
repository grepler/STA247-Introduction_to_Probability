# question 4 (unit 2) number of odd seven digit integers with non-repeating
# characters, using list comprehension from this week's class.


def question4a():

    # lst = {x for x in range (0,9999999) for char in str(x) if (x % 2 == 1)
    #   and str(x).count(char)==1}

    # this list comprehension adds an item to the list if it is odd
    # and if no character in the string occurs greater than once.
    lst = [x for x in range(1000000, 10000000) if (x % 2 == 1)
           and all([0 for char in list(str(x)) if str(x).count(char) > 1])]
    return len(lst)

# PyCharm CE can convert the list comprehension to for loop for cross-check


def question4a_var():

    lst2 = [x for x in range(1000000, 10000000)]
    count = 0
    for num in lst2:
        if num % 2 == 1 and len(str(num)) == len(set(list(str(num)))):
            count += 1
    return count

def question4b():

    # lst = {x for x in range (0,9999999) for char in str(x) if (x % 2 == 1)
    #   and str(x).count(char)==1}

    # this list comprehension adds an item to the list if it is odd
    # and if no character in the string occurs greater than once.
    lst = [x for x in range(1000000, 10000000) if (x % 2 == 0)
           and all([0 for char in list(str(x)) if str(x).count(char) > 1])]
    return len(lst)

# PyCharm CE can convert the list comprehension to for loop for cross-check


def question4b_var():

    lst2 = [x for x in range(1, 10000000)]
    count = 0
    for num in lst2:
        if num % 2 == 0 and len(str(num))==7 and len(str(num)) == len(set(list(str(num)))):
            count += 1
    return count

import time
start_time = time.time()

print("--- Question 4a ---")
# print("initial list comprehension approach", question4a())
# print("--- %s seconds ---" % (time.time() - start_time))
# print("second set and list length approach", question4a_var())
# print("--- %s seconds ---" % (time.time() - start_time))
# print("here's my paper solution", 5*8*8*7*6*5*4)
# print("--- %s seconds ---" % (time.time() - start_time))


print("--- Question 4b ---")
print("initial list comprehension approach", question4b())
print("--- %s seconds ---" % (time.time() - start_time))
print("second set and list length approach", question4b_var())
print("--- %s seconds ---" % (time.time() - start_time))
print("here's my paper solution", 5*8*8*7*6*5*4)
print("--- %s seconds ---" % (time.time() - start_time))

# Program Output
# initial list comprehension approach 268800
# --- 29.135972023010254 seconds ---
# second set and list length approach 268800
# --- 39.74933314323425 seconds ---
# here's my paper solution 302400
# --- 39.74935793876648 seconds ---
# Process finished with exit code 0

