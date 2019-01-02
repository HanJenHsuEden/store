import os

products = []
#檢查檔案是否有存在
if os.path.isfile('products.csv'):
	print('確定有檔案存在')
	with open('products.csv','r') as f:
		for item in f:
			if '商品名稱,價格' in item:
				continue
			name, price = item.strip().split(',')
			products.append([name, price])
			print(products)
else:
	print('檔案不存在...')

#可輸入商品價格建立清單
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name, price])
print(products)

for p in products:
	print(p[0],'的價格是',p[1])

#建立檔案
with open('product.csv','w', encoding = 'utf-8') as f:
	f.write('商品名稱,價錢' + '\n')
	for d in products:
		f.write(d[0] + ',' + d[1] + '\n')