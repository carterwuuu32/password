
pwd = 'a123456' #如果以後要改密碼，直接改這一行就好了
i = 3 #剩餘機會

while True:
	password = input('請輸入密碼:')
	if password == pwd:
		print('登入成功!')
		break
	else:
		i = i - 1
		print ('密碼錯誤! 還有', i, '次機會')
		if i == 0:
			break





