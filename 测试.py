# print(sum(range(1,101)))

def now():
	print('2019-4-02')


def log(func):
	def wrapper(*args,**kw):




f = now
f()
print(now.__name__)
print(f.__name__)