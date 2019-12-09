cube = lambda x : x**3

"""
	new list created over here using map returns [None, None, None] and fibonnaci series is created in fib variable  
"""
def fibonacci(n): 
	fib = [0, 1] 
	print(list(map(lambda x : fib.append(sum(fib[-2:])),range(2,n)))) 
	return fib 

if __name__ == '__main__':
	print(list(map(cube,fibonacci(5)))) 

