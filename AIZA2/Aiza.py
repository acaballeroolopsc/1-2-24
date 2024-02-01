def uppercase_decorator(func):
	def wrapper(args, **kwargs):
		result = funcz(*args, **kwargs)
		return result.upper()
    return wrapper
    
square= lambda x: x**2

#Example usage
result=square(5)
print(result)

