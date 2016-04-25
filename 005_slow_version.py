#it is a solution for euler problen number 5

numbers = []
lent = len(numbers)
n = 15

i = n

while i > 0:
	check = True
	for num in numbers:
		if num % i == 0:
			check = False
	if check ==True:
		numbers.append(i)
	i = i - 1
print numbers

max_number = 1

for num in numbers:
	max_number = max_number * num

print max_number

answer = max_number

while max_number > n:
	check = True
	for num in numbers:
		if max_number % num != 0:
			check = False
		
	if check == True:
		answer = max_number
		
	max_number = max_number - n
	
print numbers
print answer
	
