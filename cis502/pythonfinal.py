def testGen(s):
	for i in range(s):
		print(s)
		yield i

st = testGen(3)
print(next(st))

print(next(st))
print(next(st))