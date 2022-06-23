# Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
# input: [[1, 2], [3, 4], [5, 6, 7]]
# output: [[[7, 6, 5], [4, 3], [2, 1]]

l = [[1, 2], [3, 4], [5, 6, 7]]
newList = []

def Reverse(l):
    for x in l:
        if isinstance(x, list):
            x.reverse()
            newList.append(x)
        else:
          newList.append(x)
    newList.reverse()
    return newList


