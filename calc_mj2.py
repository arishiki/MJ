import math
import csv
import ff

#mj2では対戦相手の手牌も引き得ない山牌と思う場合を計算

csvfile = open('result2.csv', 'w', newline = '')
csvwriter = csv.writer(csvfile, delimiter=',')

for i in range(16, 0, -1):
    row = list(map(lambda j: 1-ff.nCm(i*3+39+13, j)/ff.nCm(i*4+39+13,j), range(1,13)))
    csvwriter.writerow(row)

# 対戦相手の手牌を除外した残り枚数の場合
#1-nCm(i*3+13, j)/nCm(i*4+13,j)

# 対戦相手の手牌も引き得ない山牌と思う場合
#1-nCm(i*3+39+13, j)/nCm(i*4+39+13,j)

csvfile.close()
