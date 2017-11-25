password = 'a123456'
i = 3#可嘗試的次數
while i > 0:
    i = i - 1 
    p = input('請輸入密碼: ')
    if p == password:
        print('登入成功!')
        break
    print('密碼錯誤!')
    if i > 0:
        print('還有', i, '次機會')