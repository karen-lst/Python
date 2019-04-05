# print(sum(range(1,101)))

def log(func):
	def wrapper(*args,**kw):
		print('call %s():' %func.__name__)
		return func(*args, **kw)
	return wrapper


@log
def now():
	print('2019-4-02')


f = now
f()
