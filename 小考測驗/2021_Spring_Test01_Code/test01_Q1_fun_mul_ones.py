def fun_mul_ones(n):
  extra_md = '1'
  prev_md = '' 
  for i in range(n):
    md = prev_md + extra_md  # 組合當下被乘數字串
    result = int(md) ** 2
    print(f'{md} * {md} = {result}')
    prev_md = md             # 當下被乘數字串變成前一個被乘數
   
   
fun_mul_ones(11)
print()