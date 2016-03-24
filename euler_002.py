#this decision is the second problem of the project Euler
import math

sqrt_five = math.sqrt(5)
pi = (sqrt_five + 1) / 2

def fib(n):
	return int(pi ** n / sqrt_five + 0.5)

count = 0
sum = 0
new_fib = 0
step = 3 
#because every third Fibonacci number - even

while True:
	count = count + step
	new_fib = fib(count)
	if new_fib <4000000:
		sum = sum + new_fib
	else:	
		break
	
print sum
