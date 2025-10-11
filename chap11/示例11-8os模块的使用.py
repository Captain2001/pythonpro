import os
print('当前的工作路径：', os.getcwd())
lst = os.listdir()
print('当前路径下的所有目录及文件：', lst)
print('指定路径下所有目录及文件：', os.listdir('E:/PythonFile/pythonpro'))
# 创建目录
# os.mkdir('好好学习')
# os.makedirs('./aa/bb/cc')
# 删除目录
# os.rmdir('./好好学习')
# os.removedirs('./aa/bb/cc')

os.chdir('E:/PythonFile/pythonpro')
print('当前的工作路径：', os.getcwd())

for dirs, dirlst, filelst in os.walk('E:/PythonFile/pythonpro'):
    print(dirs)
    print(dirlst)
    print(filelst)
    print('---------------------')
