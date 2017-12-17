# -*- coding: UTF-8 -*-
from sklearn.cluster import KMeans
from sklearn.datasets.base import Bunch
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

try:
    import cPickle as pickle
except:
    import pickle
from numpy import *


def _readfile(path):
    with open(path, "rb") as fp:
        content = fp.read()
    return content


# 停用词表
stopword = r'D:/work-space/eTensor/哈工大停用词表.txt'
stplist = _readfile(stopword).splitlines()

tfidfspase = Bunch(target_name=[], label=[], filenames=[], contents=[], tdm=[], vocabulary={})
seg_path = 'C:/Users/MC/Desktop/fc/'
#
catelist = os.listdir(seg_path)
print(catelist)
# 循环读取分词后的文本
tfidfspase.target_name.extend(catelist)
print(tfidfspase.target_name)

for mydir in catelist:
    class_path = seg_path + mydir
    # file_list = os.listdir(class_path)
    print(class_path)
    # 分类标签
    tfidfspase.label.append(mydir.split('.')[0])
    # 保存当前文件的文件路径
    tfidfspase.filenames.append(class_path)
    # 读取文本
    tfidfspase.contents.append(_readfile(class_path).strip())

# for t in tfidfspase.contents:
#     print(t.decode('utf-8'))

# 计算TF-IDF权值
vectorizer = TfidfVectorizer(stop_words=stplist, sublinear_tf=True)
# 该类会统计每个词语的IF-IDF权值
transformer = TfidfTransformer()
# 文本转为词频矩阵，单独保存字典文件
tfidfspase.tdm = vectorizer.fit_transform(tfidfspase.contents)
tfidfspase.vocabulary = vectorizer.vocabulary
num_sample, num_features = tfidfspase.tdm.shape
# sample(文本):4,features（属性）: 844
print("sample:%d,features: %d" % (num_sample, num_features))

# 构建K-MEAN模型
# 只分为四类
k = 4
km = KMeans(n_clusters=k, init="random", n_init=1, verbose=1)
km.fit(tfidfspase.tdm)
