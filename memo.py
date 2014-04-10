dic = {}



def fib(n,dic):
	if n < 2:
		return 1
	else: 
		if dic.has_key(n-1) and dic.has_key(n-2):
			return dic[n-1] + dic[n-2]
		else:
			dic[n] = fib(n-1,dic) + fib(n-2,dic)
			return fib(n-1,dic) + fib(n-2,dic)
			
			
print fib(4,dic)
dic = {}
print fib(10,dic)