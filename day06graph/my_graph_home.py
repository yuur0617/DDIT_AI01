import matplotlib.pyplot as plt
from day06graph.daostock_home import DaoStock


sd = DaoStock()
#DAO사용해서 DB에서 데이터 가져오기
samsung = sd.select("삼성전자")
sk = sd.select("SK") 
lg = sd.select("LG")
hanwha = sd.select("한화")
posco = sd.select("포스코스틸리온")

print(samsung)

# 가격을 담을 리스트 생성
samPriceList = []
lgPriceList = []
skPriceList = []
hanwhaPriceList = []
poscoPriceList = []

# 각 x좌표를 담을 리스트 생성
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
# 각 y좌표를 담을 리스트 생성
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
# samsung 데이터 꺼내오기
for idx, i in enumerate(samsung):
    firstPrice = samsung[0].get('price')
    price = i.get('price')
    gap = price - firstPrice
    percent = gap/firstPrice*100
    samPriceList.append(percent)
    x1.append(0)
    y1.append(idx)
    

for idx, i in enumerate(lg):
    firstPrice = lg[0].get('price')
    price = i.get('price')
    gap = price - firstPrice
    percent = gap/firstPrice*100
    lgPriceList.append(percent)
    x2.append(1)
    y2.append(idx)
    
for idx, i in enumerate(sk):
    firstPrice = sk[0].get('price')
    price = i.get('price')
    gap = price - firstPrice
    percent = gap/firstPrice*100
    skPriceList.append(percent)
    x3.append(2)
    y3.append(idx)
    
for idx, i in enumerate(hanwha):
    firstPrice = hanwha[0].get('price')
    price = i.get('price')
    gap = price - firstPrice
    percent = gap/firstPrice*100
    hanwhaPriceList.append(percent)
    x4.append(3)
    y4.append(idx)
    
for idx, i in enumerate(posco):
    firstPrice = posco[0].get('price')
    price = i.get('price')
    gap = price - firstPrice
    percent = gap/firstPrice*100
    poscoPriceList.append(percent)
    x5.append(4)
    y5.append(idx)

fig = plt.figure()

ax = fig.add_subplot(1,1,1,projection='3d')       

ax.plot(x1, y1, samPriceList,'r')
ax.plot(x2, y2, lgPriceList,'g')
ax.plot(x3, y3, skPriceList,'b')
ax.plot(x4, y4, hanwhaPriceList,'k')
ax.plot(x5, y5, poscoPriceList,'y')

plt.show()