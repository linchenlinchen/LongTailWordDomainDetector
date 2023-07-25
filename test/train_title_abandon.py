from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pickle
import random
# 准备数据集
with open("/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/crawler/match_title.csv",'r') as ps:
    positive_strings = [x.replace(" ","").replace("...","").replace("\n","") for x in ps.readlines()]
with open("/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/crawler/midmatch_title.csv",'r') as ms:
    middle_strings = [x.replace(" ","").replace("...","").replace("\n","") for x in ms.readlines()]
with open("/Users/leenchardmen/PycharmProjects/LongTailWordDomainDetector/crawler/dismatch_title.csv",'r') as ns:
    negative_strings = [x.replace(" ","").replace("...","").replace("\n","") for x in ns.readlines()]

positive_strings += middle_strings
# 二分类
random.shuffle(positive_strings)
random.shuffle(negative_strings)
X = positive_strings + negative_strings
y = [1] * len(positive_strings) + [0] * len(negative_strings)

# 特征提取
vectorizer = CountVectorizer()
X_transformed = vectorizer.fit_transform(X).toarray()
print(len(X_transformed))
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.1)

# 构建模型
model = MultinomialNB()
model.fit(X_train, y_train)

# 模型评估
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

# 保存模型
with open("model.pickle", "wb") as f:
    pickle.dump(model, f)

# 加载保存的模型
with open("model.pickle", "rb") as f:
    loaded_model = pickle.load(f)

# 使用加载的模型进行分类
new_corpus = [
    "致远阁-交易服务城",
    "Are you okay?",
    "中国传媒发展有限公司"
]
X_new = vectorizer.transform(new_corpus)
predictions = loaded_model.predict(X_new)
print(predictions)

##三分类
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC
# corpus = positive_strings + middle_strings + negative_strings
# labels = ["positive" for x in range(len(positive_strings))] + ["middle" for x in range(len(middle_strings))] + ["negative" for x in range(len(negative_strings))]
# print(corpus)
# # 特征提取
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(corpus)

# # 划分训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# # 训练模型
# model = SVC()
# model.fit(X_train, y_train)

# # 保存模型
# with open("model_3_split.pickle", "wb") as f:
#     pickle.dump(model, f)

# # 加载模型并进行分类
# with open("model_3_split.pickle", "rb") as f:
#     loaded_model = pickle.load(f)
    
# new_corpus = [
#     "项远购-",
#     "Are you okay?",
#     "高血压会出现哪些并发"
# ]
# X_new = vectorizer.transform(new_corpus)
# predictions = loaded_model.predict(X_new)
# print(predictions)
