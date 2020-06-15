courses = ["History", "Math", "Physics", "CompSci"]

print(courses[0])
print(courses[:2])
print(len(courses))

courses.append("Art")       # adding item to the list
courses.insert(0, "Art")    # inserting at position 0

courses_2 = ["Art", "Education"]
courses.insert(0, courses_2)        # will add the list to the list
courses.extend(courses_2)           # adds items from list_2 to the list

courses.remove("Math")              # will remove the item Math
courses.pop()                       # will remove the LAST item and return ut

courses.reverse()           # prints in reverse
#courses.sort()              # sorted list

nums = [1, 4, 9, 3, 6, 2]
nums.sort()                 # sorts in ascending order
nums.sort(reverse=True)     # sorts in descending order

print(min(nums))            # or max
print(sum(nums))            # prints the sum

courses.index("CompSci")    # index where the item is found
print("Art" in courses)     # boolean

for item in courses:
    print(item)             # will print every item

for index, course in enumerate(courses):    # prints items with indeces
    print(index, course)

course_str = " - ".join(courses_2)          # Art - Education
new_list = course_str.split("-")            # split and create list

empty_list = []
empty_list = list()

# - - - - - - - - - - - TUPLES - - - - - - - - - - - - - - -
# If you want unmutable list use tuple
tuple = ('history', 'math', 'physics', 'compsci')
# it is immuatble
# everything else is same as list

# - - - - - - - - - - - SETS - - - - - - - - - - - - - - - -
# prints in sorted order
# don't care about order
# helps to throw away duplicates
set = {'history', 'math', 'physics', 'compsci', 'art'}
set_2 = {'design', 'art', 'history'}

print(set.intersection(set_2))    # shows common courses
print(set.difference(set_2))      # items that were not in set_2
print(set.union(set_2))           # all of the items in both sets