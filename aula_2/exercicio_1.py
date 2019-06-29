
def exemplo_args(*args):
	print(args)
	print(type(args))

exemplo_args(1, 'dois', 3.0, True)

def exemplo_args_2(a, b, *args):
	return a + b + sum(args)

print(exemplo_args_2(2, 2))
print(exemplo_args_2(0, 0, 2, 2))

def exemplo_kwargs(**kwargs):
	