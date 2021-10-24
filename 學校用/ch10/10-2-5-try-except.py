s='昔人已乘黃鶴去，此地空余黃鶴樓。\
黃鶴一去不復返，白雲千載空悠悠'#崔顥 黃鶴樓
try:
    with open('poem.txt','wt',encoding='utf-8') as fout:
        fout.write(s)
except:
    print('無法寫入檔案')