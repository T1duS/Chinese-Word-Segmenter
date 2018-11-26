sent = input("Please write your chinese sentence to segment and press enter: ")

words = set([])

with open('chinese-word-list.txt') as f:
	for word in f:
		words.add(word[:-1])

valid = [] # checks sent[i:j] is valid
n = len(sent)

for i in range(n):
	valid.append([])
	for j in range(n+1):
		if j > i and sent[i:j] in words: 
			valid[i].append(1)
		else:
			valid[i].append(0) 

cur = 0
while cur < n:
	for i in range(n,cur,-1):
		if(valid[cur][i]):
			print(sent[cur:i],end=' ')
			cur = i
			break
	else:
		print(sent[cur],end=' ')
		cur += 1


