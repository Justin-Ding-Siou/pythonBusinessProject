s='昔人已乘黃鶴去，此地空余黃鶴樓。\
黃鶴一去不復返，白雲千載空悠悠。'#崔顥 黃鶴樓
with open('poem.txt','wt',encoding='utf-8') as fout:
    print(s,file=fout)
    fout.write(s)