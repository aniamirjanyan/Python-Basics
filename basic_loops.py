
nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found it')
        break
    print(num)
# if we dont want to break we can use continue
for num in nums:
    if num == 3:
        print('Found it')
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(1, 11):      # starts at 1 ends with 10
    print(i)

while x < 10:               # iterates but stops
    if x == 5:
        break
    print(x)
    x += 1

while True:                 # infinite loop
    print(x)
    x += 1
