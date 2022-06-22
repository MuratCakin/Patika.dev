# Binary Search
İkili arama algoritması, elimizde bulunan veri dizisini sıralı olduğunu varsayıyor, bu durumu değiştirerek sonuca varmak istiyor.

İkili arama algoritması, diziyi her seferinde ikiye bölerek ikili arama yapar. Sıralı bir listem var ise benim Big-o logn olarak karşımıza çıkıyor.

Aradığım sayı 15 ve benim değer kümem [10,15,20,16,22,36,23] diyelim. Binary Search bu diziyi manipüle ederek şu ifadeye dönüştürüyor. [10,15,16,20,22,23,36]. 36 sayısını en yüksek sayı, 10 sayısını en düşük sayı ilan ediyor. Benim aradığım sayı ile ortada kalan sayıyı kıyaslıyor eğer benim sayım büyükse kendinden küçük bütün sayıları siliyor. Ve kendine yeni bir ortanca belirliyor. Böylelikle gereksiz arama yapmaktan kurtarıyor.

![Binary-Search](https://raw.githubusercontent.com/Kodluyoruz/taskforce/main/veri-yapilari-algoritmalar/binary-search/figures/binary-search.png)

## ÖRNEK
[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.
(root x'dir. root'un sağından y bulunur. Solunda z bulunur vb.)

>CEVAP:  
>İlk eleman root olarak seçilir.  
Sonra gelen elemanlar root dan aşağı doğru bakılarak büyükse sağa küçükse sola dallanır.
	
|             |  |  |     |  |  |  |  |  |  |  |  |
|--           |--|--|-    |- |- |- |- |- |- |- |- |
|             |  |  |     |  |  |  | 7|  |  |  |  |  
|             |  |  |     |  |  | /|  |\ |  |  |  | 
|             |  |  |     |  | 5|  |  |  |8 |  |  | 
|             |  |  |     | /|  |\ |  |  |  |\ |  | 
|             |  |  | 1   |  |  |  |6 |  |  |  | 9|
|             |  | /|     |\ |  |  |  |  |  |  |  |
|             | 0|  |     |  | 3|  |  |  |  |  |  |
|             |  |  |     | /|  |\ |  |  |  |  |  |
|             |  |  |  2  |  |  |  |4 |  |  |  |  |	
