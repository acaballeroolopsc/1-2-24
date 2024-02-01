def uppercase_decorator(func):
	def wrapper(args, **kwargs):
		result = funcz(*args, **kwargs)
		return result.upper()

 list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter(lambda x: x % 2 == 0, list1)

list(filter(lambda x: x % 2 == 0, list1))
>> [2, 4, 6, 8, 10]


square= lambda x: x**2

#Example usage
result=square(5)
print(result)

