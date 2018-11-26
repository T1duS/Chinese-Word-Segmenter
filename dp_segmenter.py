from math import log10

sent = input("Please write your chinese sentence to segment and press enter: ")

freq = dict()
total = 0

with open('big.txt') as f:
	for line in f:
		freq[line.split()[0]] = int(line.split()[1])
		total += int(line.split()[1])

idf = [] # idf of sent[i:j]
n = len(sent)

for i in range(n):
	idf.append([])
	for j in range(n+1):
		if j > i and sent[i:j] in freq: 
			idf[i].append(log10(total/(freq[sent[i:j]]+1)))
		else:
			idf[i].append(int(1e18)) 
 
dp = [0]*(n+1)
words = [[]]*(n+1)
for i in range(1,n+1):
	dp[i] = idf[0][i]
	words[i] = [sent[0:i]]
	for j in range(1,i):
		if(dp[j]*idf[j][i] < dp[i]):
			dp[i] = dp[j]*idf[j][i]
			words[i] = words[j]+[sent[j:i]]

print(" ".join(words[n]))			



