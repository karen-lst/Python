import os.path as op
import os
import logging
logging.basicConfig(level=logging.INFO)

# # op.abspath('test.py')
# print(op.abspath('test.py'))
# print(op.normpath('D://Documents//GitHub//python-learning-notes//mianshi//test.py'))
# # print(op.relpath('python3笔记.py'))
# print(op.dirname('D://Documents//GitHub//python-learning-notes//mianshi//test.py'))
# print(op.basename('D://Documents//GitHub//python-learning-notes//mianshi//test.py'))
# print(op.exists('D://Documents//GitHub//python-learning-notes//mianshi//test.py'))

# os.system("C:\\Windows\\System32\\calc.exe")

# os.getlogin()
# print(os.getlogin())
# print(os.cpu_count())

# dic = {'name':'karen','age':23}
dic = dict(name='kren',age=23)
aa = {'city':'beijing'}
del dic['name']

# logging.info('aa:{}'.format(aa))
# print(dic)
dic.update(aa)
# print(dic)

