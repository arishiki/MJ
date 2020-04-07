import math
import csv

#added comment

def nCm(n, m):
    dividee = 1
    for x in range(n, n-m, -1):
        dividee *= x
    return dividee//math.factorial(m)

csvfile = open('result.csv', 'w', newline = '')
csvwriter = csv.writer(csvfile, delimiter=',')

for i in range(16, 0, -1):
    row = list(map(lambda j: 1-nCm(i*3+13, j)/nCm(i*4+13,j), range(1,13)))
    csvwriter.writerow(row)

# 対戦相手の手牌を除外した残り枚数の場合
#1-nCm(i*3+13, j)/nCm(i*4+13,j)

# 対戦相手の手牌も引き得ない山牌と思う場合
#1-nCm(i*3+39+13, j)/nCm(i*4+39+13,j)

csvfile.close()
