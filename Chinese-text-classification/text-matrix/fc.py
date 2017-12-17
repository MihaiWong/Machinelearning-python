import os

import jieba


# 获取所有文件夹
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        # print(dirs)  # 当前路径下所有子目录
        # print(files)  # 当前路径下所有非目录子文件
    return files


# 停用词
def stop():
    array = []
    file_name = 'D:/work-space/eTensor/哈工大停用词表.txt'
    file = open(file_name)
    while 1:
        line = file.readline()
        array.append(line.replace('\n', ''))
        if not line:
            break
        pass  # do something
    # print(array)
    return array


# 文件存储
def writefile(file_name, content):
    try:
        with open(file_name(), 'wb') as f:
            f.write(content)
    except:
        pass


# 文件读取 同时写入分词
# todo 1.读取分离     2. 增加标签
def readfile():
    filedirs = file_name('C:/Users/MC/Desktop/train/')
    for dirs in filedirs:
        # print(dirs)
        new_contents = ''
        with open('C:/Users/MC/Desktop/train/' + dirs, 'rb') as f:
            content = f.read().decode('utf-8')
            content = content.replace("\r\n", "")  # 删除换行
            content = content.replace(" ", "")  # 删除空行、多余的空格
            content_seg = jieba.cut(content)  # 为文件内容分词
            for seg in content_seg:
                if seg not in stop() and seg != None:
                    new_contents = new_contents + seg + " "
        print(new_contents)
        # for txt in file_name('C:/Users/MC/Desktop/fc/'):
        #     if dirs in txt:
        #         print('C:/Users/MC/Desktop/fc/' + txt)
        #         writefile('C:/Users/MC/Desktop/fc/' + txt, str(new_contents))
        print('****************************')


readfile()
# print(file_name('C:/Users/MC/Desktop/fc/'))
