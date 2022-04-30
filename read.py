data= [] #建立空清單叫data
count = 0 #計數器
with open('reviews.txt', 'r') as f:
	for line in f: #每次讀取一行,並命名為line
		data.append(line) #將line加入data清單中
		count += 1 #count = count +1
		if count % 1000 == 0: #%是用來求餘數 
			print(len(data)) #讀取檔案的過程中，印出len(data)才知道讀取進度
print('檔案讀取完了，總共有', len(data), '筆資料') #len可求清單或字串的長度 #共1000000筆留言

print(data[0]) 
print('----------')
print(data[1])		

#求留言平均長度
sum_len = 0
for d in data: #d為每一筆留言，data為裝著1000000筆留言的清單
	sum_len += len(d) #sum_len = sum_len + len(d)
print('每筆留言平均長度是', sum_len/len(data))	

#篩選概念
new = [] #新的清單
for d in data:
    if len(d) < 100: #若留言長度小於100
    	new.append(d) #把留言裝進new清單中
print('一共有', len(new), '筆留言長度小於100') #放在for loop外，避免一直列印
print(new[0])