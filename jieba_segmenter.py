import jieba
sent = input("Please write your chinese sentence to segment and press enter: ")
print(" ".join(jieba.cut(sent)))