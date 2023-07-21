from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 准备数据集
positive_strings = ['good', 'great', 'excellent']
negative_strings = ['bad', 'terrible', 'awful']
X = positive_strings + negative_strings
y = [1] * len(positive_strings) + [0] * len(negative_strings)

# 特征提取
vectorizer = CountVectorizer()
X_transformed = vectorizer.fit_transform(X)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2)

# 构建模型
model = MultinomialNB()
model.fit(X_train, y_train)

# 模型评估
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
