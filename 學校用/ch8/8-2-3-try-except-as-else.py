try:
    num = int(input('請輸入整數'))
except EOFError:
    print('輸入EOF')
except ValueError as ve:
    print('發生ValueError錯誤',ve)
except Exception as e:
    print('發生其他錯誤',e)
else:
    print('輸入整數為', num)