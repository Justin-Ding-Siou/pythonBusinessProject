news = '''
長榮貨運輪「長賜號」（Ever Given）堵在蘇伊士運河（Suez Canal）上進入第6天，救援任務當地時間周一（29日）清晨4時到5時（台灣時間29日上午10時到11時）進到「關鍵階段」，根據最新畫面顯示，長賜號似乎已接近擺正、離脫困不遠。

根據船隻追蹤網站「VesselFinder」的最新畫面指出，在搶救下長賜號目前已接近「擺正」，與先前「橫擋」在運河中間的情形相比，船頭部分似乎已脫離岸邊，救援任務似乎取得重大進展。

荷蘭Boskalis救援團隊於28日開始輪流進行清淤和拖船拖曳作業，並表示已挖除2.7萬多立方公尺的泥沙，船艏卡住土堤的情況也開始鬆動，將有助於救援行動。貝仕船舶管理公司（BSM）也稱，一旦長賜號脫困、能夠移動，將會評估並決定船隻狀態是否適合航行運河。

長賜號自23日起堵住蘇伊士運河，目前在運河兩端等待的船隻至少有327艘。

長榮海運貨櫃輪「長賜輪」（Ever Given）23日擱淺在蘇伊士運河，中斷雙向運輸進入第6天，除了造成全球貿易影響外，美軍也指出蘇伊士運河的長時間中斷將影響美軍艦部署。

據《國會山莊報》（Hill）報導，五角大樓官員證實，蘇伊士運河交通中斷將影響美國軍艦的通行，但強調美軍有其他支援該地區行動的手段，負責美軍中東和中亞地區行動的美國中央司令部公共事務官員瑞巴里希（Rebecca Rebarich）表示：「我們不談具體的部署影響，蘇伊士運河是不可或缺的海上咽喉點，通行中斷越久，對民用和軍事的影響越大。」

瑞巴里希強調：「我們還有其他手段來減輕在運河斷航期間對美國中央司令部負責地區的行動影響和支援。」'''

# 測試學習
s = news[0:]

chars_to_remove = ' .,：，。、／〔〕（）《》「」\n'
for char in chars_to_remove:
    s = s.replace(char, '')
# s = news[0: ] 與 char = chars_to_remove 進行比對，如果有chars_to_remove的內容，將之移除

char_set = set(s)
# 將字串轉為字元

# 印出處理，由 index 由小到大
sorted_chars = sorted(char_set, key=news.index)

# 建構字典
char_dict = {}

# 找到高頻單字
for w in sorted_chars:
    n = s.count(w)
    char_dict[w] = n


# 依出現次數排序，由大到小，前五個
c_sorted = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
print("\n最常用的5個字元:", c_sorted[0:5])

print("\n不重覆中英文字元有 %d 個" % len(char_set))
en_set = {c for c in char_set if c.isascii() == True }
zh_set = sorted(char_set - en_set, key=news.index)
print("\n不重覆英文字元有 %d 個: %s" % (len(en_set), list(en_set)))
print("\n不重覆中文字元有 %d 個: %s" % (len(zh_set), zh_set))


print("他們出現的位置:")
for k, v in c_sorted[0:5]:
  positions = [i for (i, c) in enumerate(news) if c == k]
  print('{}: {}'.format(k, positions))
  