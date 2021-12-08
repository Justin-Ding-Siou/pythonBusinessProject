news = '''
去年（2020）WWDC 全球開發者大會時，Apple 就明指將在兩年內從原本的 Intel（英特爾）處理器過渡到自家研發的 Apple Silicon 處理器，這與意味著未來 Mac 電腦將全面捨棄 x86 架構而轉向 ARM 架構。

由於 Apple 陸續推出搭載 M1 處理器的 MacBook Air、MacBook Pro、iMac 和 Mac mini 等產品，據市調公司的研究，這使 Apple 直接躍升成為 ARM 電腦市場的唯一龍頭，尤其在 ARM 筆記型電腦市場更佔去 80% 的份額。


透過市調公司《Strategy Analytics》的報告，發現 ARM 電腦市場正以非常快的速度持續增長，研究發現 Apple 幾乎是帶領整個 ARM 電腦產品最大的參與者，並預計將在 2021 年達到 79% 的 ARM 筆記型電腦市場佔有率。

《Strategy Analytics》指出，由於 Apple 即將在 10 月 18 日正式公開全新 MacBook Pro 系列，並採用強化過後的 M1X 處理器，在性能方面將比 M1 獲得翻倍以上的成果，而這也將帶動 ARM 筆電市場，2021 年總產值將成長三倍達到 9.49 億美元（約新台幣 265 億元）。

除了 Apple 外，聯發科（MediaTek）近年在 ARM 電腦市場也獲得不錯的成長，目前市佔為 18%，而高通（Qualcomm）則為 3%，排行第三。'''

# 將字串轉為字元
s = news[0:]

chars_to_remove = ' .,：，。、／〔〕（）《》「」\n'
for char in chars_to_remove:
    s = s.replace(char, '')
# s = news[0: ] 與 char = chars_to_remove 進行比對，如果有chars_to_remove的內容，將之移除

char_set = set(s)
# 將字串轉為字元

# 印出處理，由 index 由小到大
sorted_chars = sorted(char_set, key=news.index)

# 判斷位元
en_set = {c for c in char_set if c.isascii() == True}
zh_set = sorted(char_set - en_set, key=news.index)

# 建構字典

zh_char_dict = {}
en_char_dict = {}

# 找到英數高頻單字
for w in zh_set:
    n = s.count(w)
    zh_char_dict[w] = n

# 找到中文高頻單字
for w in en_set:
    n = s.count(w)
    en_char_dict[w] = n

# 依中文出現次數排序，由大到小，前五個
c_sorted = sorted(zh_char_dict.items(), key=lambda x: x[1], reverse=True)
print("\n中文最常用的5個字元:", c_sorted[0:5])

# print("test:", zh_set)
print("他們出現在原文的位置:")
for k, v in c_sorted[0:5]:
    positions = [i for (i, c) in enumerate(news) if c == k]
    print('{}: {}'.format(k, positions))




print()
# 依英文出現次數排序，由大到小，前五個
c_sorted = sorted(en_char_dict.items(), key=lambda x: x[1], reverse=True)
print("\n英文最常用的5個字元:", c_sorted[0:5])

# print("test:", en_set)
print("他們出現在原文的位置:")
for k, v in c_sorted[0:5]:
    positions = [i for (i, c) in enumerate(news) if c == k]
    print('{}: {}'.format(k, positions))
