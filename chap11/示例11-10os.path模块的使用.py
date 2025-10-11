import os
print('获取目录或文件的绝对路径：', os.path.abspath('./b.txt'))
print('判断目录或文件在磁盘上是否存在：', os.path.exists('./b.txt'))
print('判断目录或文件在磁盘是否存在：', os.path.exists('./newb.txt'))
print('判断目录或文件在磁盘是否存在：', os.path.exists('./好好学习'))
print('拼接路径：', os.path.join('E:/PythonFile/pythonpro', 'b.txt'))
# print('判断目录或文件在磁盘是否存在：', os.path.exists(os.path.join('E:/PythonFile/pythonpro', 'b.txt')))
print('分割文件的名和文件后缀名：', os.path.splitext('b.txt'))
# print('提取文件名：', os.path.basename(r'E:/PythonFile/pythonpro/chap11/b.txt'))
print('提取文件名：', os.path.basename(r'E:\PythonFile\pythonpro\chap11\b.txt'))
print('提取路径：', os.path.dirname(r'E:\PythonFile\pythonpro\chap11\b.txt'))

print('判断一个路径是否是有效路径：', os.path.isdir(r'E:\PythonFile\pythonpro\chap11'))
print('判断一个路径是否是有效路径：', os.path.isdir(r'E:\PythonFile\pythonpro\chap110'))

print('判断一个路径是否是有效文件：', os.path.isfile(r'E:\PythonFile\pythonpro\chap11\b.txt'))
print('判断一个路径是否是有效文件：', os.path.isfile(r'E:\PythonFile\pythonpro\chap11\bbb.txt'))

