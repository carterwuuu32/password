
while True:
	password = input('請輸入密碼，最多輸入3次密碼:')
	if password == 'a123456':
		print('登入成功!')
		break
	else:
		password2 = input('密碼錯誤! 還有2次機會:')
		if password2 == 'a123456':
			print('登入成功!')
			break
		else:
			password3 = input('密碼錯誤! 還有1次機會:')
			if password3 == 'a123456':
				print('登入成功!')
				break
			else:
				print('密碼錯誤3次，無法登入!')
				break






