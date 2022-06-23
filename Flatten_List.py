# Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
# output: [1,'a','cat',2,3,'dog',4,5]


# Yeni bir fonksiyon tanımlarken henüz yazma aşamasında yapının içinde tekrar tanımladığım fonksiyonu kullanabilirim.
# Bu işleme Recursive Function denir. Örneğimizin dışında faktoriyel örneğinden mantığı daha rahat anlayabilirisiniz. 

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flattenList = []

def flatten(l):
    for i in l:
        if isinstance(i, list):
            flatten(i)
        else:
            flattenList.append(i)
    return flattenList
    
flatten(l)
print(flattenList)

def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n-1)


