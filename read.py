data= [] #建立空清單叫data
count = 0 #計時器
with open('reviews.txt', 'r') as f:
	for line in f: #每次讀取一行,並命名為line
		data.append(line) #將line加入data清單中
		count += 1 #count = count +1
		if count % 1000 == 0: #%是用來求餘數 
			print(len(data)) #讀取檔案的過程中，印出len(data)才知道讀取進度
print(len(data)) #len可求清單或字串的長度 #共1000000筆留言

print(data[0]) 
print('----------')
print(data[1])		