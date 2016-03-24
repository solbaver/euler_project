#this decision is the first problem of the project Euler
def sum(n, max):
	sum = 0
	count = 0
	while (max-count)>n:
		count = count + n
		sum = sum + count
	return sum
print sum (3, 1000) + sum (5, 1000) - sum (15, 1000)
