def min(a, b):
    ''' 使用min可以找出a與b較小的值
    Args:
        a: 輸入的第一個參數
        b: 輸入的第二個參數

    Returns:
       回傳a與b中較小的值
    '''
    if a > b:
        return b
    else:
        return a
help(min)
print(min.__doc__)