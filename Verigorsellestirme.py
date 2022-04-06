#------------------------------------------
#-- Veri Gorsellestirme
#------------------------------------------

#-- Matplotlib

# Matplotlib bir cok gorsellestirmenin ilk kutuphanesi oldugu icin daha dusuk seviyede gorsellestirmeler
## icin kullanilir.

#Kategorik bir degisken varsa bunu sutun grafikle gorsellestirebiliriz.
## Bu islemide Seaborn icinden Countplot veya matplotlib icinden bar ile gerceklestirebiliriz

#Sayisal degisken : Sayisal degiskenleride histogram ve boxplot uzerinden gosterebiliriz.
##Boxplot aykiri degerleride gosterir.

#Veri gorsellestirme icin python en uygun arac diyemeyiz.
## Bunun icin veri tabanina bagli bir program kullanmak daha mantikli olur.
### Biz burada ufak capli gorsellestirme islemlerimizi gerceklestirecegiz.

#-- Kategorik Degisken Gorsellestirme

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500) #Sag tarafa dogru daha fazla degisken gormemizi saglar.
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts()#Bu komut ile kategorik degisken hakkinda bilgi aliriz.
df["sex"].value_counts().plot(kind="bar")#plot kisminda bize hangi cesitte cizecegimizi sorar
## bu islemi kind = ile betimleriz. Burada gordugunuz uzere bar seklinde istenilmistir.
plt.show() # islemi yazdiktan sonra bu komutla gorsellestirmenin cagirilmasi gerekmektedir.

#-- Sayisal Degisken Gorsellestirme

#-Histgoram Gosterimi
plt.hist(df["age"])
plt.show() #Elimizdeki sayisal degiskenin belirli araliklara gore dagilimini bize gosterir.

#-Boxplot gosterimi
plt.boxplot(df["fare"])
plt.show()



#------------------------------------------
#-- Matplotlib Ozellikleri
#------------------------------------------

#- Plot

x = np.array([1, 8]) # elimizde bu sekilde iki array oldugunu dusunursek
y = np.array([0, 150])

plt.plot(x, y)
plt.show()
#bu sekilde kesisimlerini cizgi seklinde gorebiliriz.
# cizgi degilde sadece nokta olarak gormek istersek
plt.plot(x, y,"o")
plt.show()
# bu sekilde y den sonra bir o stringi koyarak bu islemi gerceklestirebiliriz
## Farkli matematiksel degerler koyarakta matematiksel isaretler koyulmasini saglayabiliriz.
plt.plot(x, y,"2")
plt.show() #

#- Marker

plt.plot(x, y,"2")
plt.show() # oldugu gibi kesisim noktalarinin isaretlerini degistirebiliriz

markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']
#Kullanilabilecek ifadelerin bir kismi

#- Line

#bu komutta cizginin rengini ve seklini degisirebiliriz.
## kesikli cizgiler noktalardan olusan cizgiler yapabilmek gibi
y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashdot", color="r")
plt.show()

#- Multiple Lines

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

#ayni grafikte birden fazla cizgi gosterimi yapabiliriz.

#- Label

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
# Başlık
plt.title("Bu ana başlık") # Grafigin ana baslik kismini buradan

#  Eksen isimlendirme
plt.xlabel("X ekseni isimlendirmesi")

plt.ylabel("Y ekseni isimlendirmesi")

plt.grid() # Grafige ızgara yani kareleme yapmak icin kullanabiliriz.

plt.show()

#- Subplot

# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)# Grafik ekranini 1 sati 2 sutunlu bir alan olarak olustur
## Ve bu alanin 1. kismina bu grafigi yerlestir anlamina gelir --1,2,1--
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 2, 2)
plt.title("2")
plt.plot(x, y)
plt.show()

# 3 grafiği bir satır 3 sütun olarak konumlamak.
# plot 1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 1) #1 satir 3 sutunlunun 1. grafigi olarak
plt.title("1")
plt.plot(x, y)

# plot 2
x = np.array([8, 8, 9, 9, 10, 15, 11, 15, 12, 15])
y = np.array([24, 20, 26, 27, 280, 29, 30, 30, 30, 30])
plt.subplot(1, 3, 2) #1 satir 3 sutunlunun 2. grafigi olarak
plt.title("2")
plt.plot(x, y)

# plot 3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3) #1 satir 3 sutunlunun 3. grafigi olarak
plt.title("3")
plt.plot(x, y)

plt.show()

#------------------------------------------
#-- Seaborn İle Veri Gorsellestirme
#------------------------------------------

from matplotlib import pyplot as plt
df = sns.load_dataset("tips")
df.head()
#Text ya da string formatinda olan degiskenlere kategorik degiskenler diyoruz.
## Bu degiskenlerin gorsellestirilmesinde countplot
df["sex"].value_counts()
sns.countplot(x=df["sex"],data=df)# Countplotda x ve data kisimlarini nereden alacagini
##kutuphaneye tanitmamiz gerekmektedir.
### goruldugu uzere x icin sex degiskenini dataframe olarak tanimlarken
#### bu degerleri nereden aldiginida data = olarak tanimliyoruz.

plt.show()

#-- Seaborn ile Sayisal DEgisken gosterme
sns.boxplot(x= df["total_bill"])
plt.show()

#Histgoram ile gosterecek olursak
df["total_bill"].hist() #histogram gostrimi icin sonuna hist yazmamiz yeterlidir.
plt.show()