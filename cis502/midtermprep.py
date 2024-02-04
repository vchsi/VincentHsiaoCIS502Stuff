def decorator(funct):
	def wrapper():
		for i in range(4):
			funct()
	return wrapper

@decorator
def rooster():
	print("Jerky")

rooster()