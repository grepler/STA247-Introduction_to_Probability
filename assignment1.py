# question 4 (unit 2) number of odd seven digit integers with non-repeating
# characters, using list comprehension from this week's class.

lst = [x for x in range (0,9999999) for char in str(x) if (x % 2 == 1)
       and str(x).count(char)==1]
print(len(lst))