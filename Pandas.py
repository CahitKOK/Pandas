#-------------------------------------------------------
#-- PANDAS
#-------------------------------------------------------

# Pandaslar veri manipulasyonu ve veri analatigi dedigimiz zaman ilk akla gelen kutuphanelerdendir.

#-------------------------------------------------------
#-- Pandas Series
#-------------------------------------------------------

import pandas as pd # Komutuyla ilk olarak kutuphanemizi import ediyoruz
# Veri analitigi ve manipulasyonu gibi islemleri genel olarak dataframeler
## üzerinden yapıyor olacagız. Zamana baglı indexlerdir.


pd.Series([10,77,12,4,5]) #Series metoduyla serimizi içeride verdigimiz liste seklinde olusturabiliyor.
## Ek olarak olusturdugumuz seri bize tip ve index bilgisinide veriyor

#:: 0    10
#   1    77
#   2    12
#   3     4
#   4     5
#  dtype: int64

s=pd.Series([10,77,12,4,5])
type(s) #tip bilgisini kontrol ettigimizde ::: Out[22]: pandas.core.series.Series yazmaktadir.
#tipleri bilmek önemlidir. Cunku kullanacagımız fonksiyon bizden dataframe beklerken
## fonksiyonu bir pandas serisi sokmaya calısırsak hata aliriz.

s.index # serimizin index bilgisine ulasıp, kactan kaca kadar ve kacar kacar arttigini burada
## gorebiliyoruz. ::: Out[23]: RangeIndex(start=0, stop=5, step=1)

s.dtype # icerindeki elemanlari tip bilgisimi verir
s.size # eleman sayisini verir
s.ndim # boyut sayisini verir

# Pandas serileri tek boyutlu olurlar ve index bilgileri mevcuttur.

s.values # bir pandas serisinin eleman degerlerine bakmak istersek bize bunu numpy arrayi gibi gosterir.
#::: Out[27]: array([10, 77, 12,  4,  5], dtype=int64)
type(s.values) # bu kodla bunu teyit edebiliriz ::: Out[28]: numpy.ndarray
s.head(3) # Bastan ilk uc degeri getirir
s.tail(3) # Son indexten uc degeri getirir.

#-------------------------------------------------------
#-- Veri Okuma
#-------------------------------------------------------

import pandas as pd
df = pd.read_csv("../Dataset/winequality-red.csv")# Sol tarafta aynı klasörde calistigimiz dosyalar icin bu sekilde okuma islemi
## yapilirken ayrica dosyanin bilgisayardaki konumu yazilarakta yapilabilir
pd.read_csv("C:\Users\trcah\PycharmProjects\pythonProject4\winequality-red.csv")
# Kisayol olarakta soldaki csv dosyasina sag tikliyarak copy path bolumunden "Path From Content Root" kismina
## tiklanarak islem gerceklestirilebilir.
df.head() # Head komutu ile elimizdeki datayi goruntuluyebilir.
#Parantez içine yazdigimiz eleman kadar görüntülenmeyide saglayabiliriz.

#-------------------------------------------------------
#-- Veriye Hizli Bakis
#-------------------------------------------------------

import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")#Bu komut ile seaborn kutuphanesindeki veri setlerine erisebiliyoruz.
df.head()
df.tail() # sondan degerleri gorebiliriz.
df.shape #komutu ike boyut bilgisine ulasabiliriz.
df.info() # degiskenlerin ve elemanlarin daha detayli bilgilerine ulasabiliriz
#info içinde kaç degisken,degiskenlerin turleri ve iclerinde bulunan dolu elemanlarin sayisini verir.
#ayrica datasetin hafizada tuttugu yeride gosterir.
df.columns #Dataframe içinde bulunan degiskenlerin isimlerini bu sekilde yazdirabiliriz.
df.index # kac eleman oldugunu ve kacar kacar arttigini verir.
df.describe().T # Degiskenlerin istatistik bilgilerine ulasmak icin kullandigimiz komuttur.
# T ifadesi ile transpose almış oluruz yani istatistik bilgleri ters halde onumuze getirir.
df.isnull().values.any() #hergangi bir degiskende eksik deger var mi diye sorar True,False olarak cevaplar.
df.isnull().sum() # Her bir degerde kac tane eksik bilgi var sayi olarak ifade eder.
## Her 1 sayisi bir tane bos degeri ifade eder.
df["sex"].head() # Sadece koseli parantez icinde yazan degiskenin degerlerini getirir.
#Dataframelerden degisken secmek icin bu sekilde yapariz.
df["sex"].value_counts() # Bu degiskenin icindeki degerlerin sayisini verir.

#-------------------------------------------------------
#-- Pandas Secim İslemleri
#-------------------------------------------------------

import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

#Dis ozellikler index inceleme
df.index
df[0:13] #0'dan 13'e kadar olan degerler.
df.drop(0,axis=0).head() # axis = 0 satirlarda,axis = 1 sutunlarda islemler yaptirir.
# Drop islemide dataframeden degeleri siler
delete_indexes = [1,3,5,7]
df.drop(delete_indexes,axis=0).head(5) # bu islemde toplu silme islemi gerceklestirebeliriz.
#Bu silme islemini kalici yapmak icin tekrar atamasini yapabilir ya da
df.drop(delete_indexes,axis=0,inplace=True).head(5) #inplace= True yazabiliriz.

#-- Degiskeni İndexe Cevirme
#Degiskeni secme
df["age"].head()
df.age.head() #goruldugu uzere degisken secimi iki farkli sekildede yapilabilir.
df.index =df["age"] # index atamasini bu komutla yaparken
df.drop("age",axis=1,inplace=True) # yukarida ogrendigimiz komutlada silme islemini gerceklestiriyoruz
df.head()
#-- Indexi Degiskene Cevirme

# Bu islemi iki sekilde gerceklestirebiliyoruz.
df["age"] = df.index #Degiskenin icinde age olmadigi icin direkt atama olarakta bu islem gerceklestirilebilir.
df.head()
#İkinci yol olarak
df.reset_index().head() #Bu sekilde eski indexi degisken olarak ekleyebiliriz.
#Bu silinme haricinde eklenmeyi engellemek icin ise reset_index(drop = True) ifadesi kullanabiliriz.

#-------------------------------------------------------
#-- Degiskenler Uzerinde İslemler
#-------------------------------------------------------

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)# Bu komut ile ciktimizdaki ... ifadelerini kaldirip
## butun degerlerin gosterilmesi saglanir
df = sns.load_dataset("titanic")
df.head()

"age" in df # age degiskeni df dataframe'in icinde var mi sorusunu sorar
df["age"]
df.age # Gosterilen iki sekilde degisken secimi yapabiliriz.
df["age"].head()
type(df["age"].head()) # Type sorgusundanda gorulecegi uzere dataframe icerisinde
## bir degisken secimi yapilirsa artik degiskenin tipi pandas serisine donusur.
#::: Out[57]: pandas.core.series.Series
type(df[["age"]].head())# eger dataframe olarak kalmasini istiyorsak iki koseli parantez kullanmaliyiz.
#:: Out[58]: pandas.core.frame.DataFrame

df[["age","sex"]] #Birden fazla degisken secmek icinde bu sekilde yapabiliriz.

df["age2"] = df["age"]**2 # bu gibi atama islemleriyle yeni degiskenler ekleyebiliriz.

df.drop("age2",axis=1).head() # Degiskeni silmek icin drop ile islem yapabiliriz. Kalici olmaasi icinde
## onceden ogrendigimiz inplace = True yapabiliriz.

#Bir kac degiskeni silmek icinde bir liste oluturup
## O listenin icine silmek istedigimiz degiskenlerin adlarini liste olarak yazip
## "age2" yerine listenin ismini yazmamiz yeterli olacaktir.

col_name = ["age","sex","class"]
df.drop(col_name,axis=1,inplace=True) # ornekte oldugu gibi

df.loc[:,df.columns.str.contains("age")].head() # Contains icinde verdigimiz degiskenin baska degiskende bulunup
# bulunmadigini bulur ve bize getirir.
## loc yazilimi bu secimi yapabilmek icindir "," onceki kısım satirlari sonraki kisim ise sutunlar
### uzerinde islem yapilmasini saglar.
#### "~" isareti ile bu kodun disindakileri sec diyebiliriz.
df.loc[:,~df.columns.str.contains("age")].head() #bu koddaki gibi
df[[col for col in df.columns if "age" in col]]
age_list = df[[col for col in df.columns if "age" in col]]
df[age_list]
#-------------------------------------------------------
#-- Loc & Iloc
#-------------------------------------------------------

df.iloc[0:3]# Bu komut ile 0 dan 3 kadar olan indexlerin degerleri alinir
df.iloc[0,0] # Bu komutla ise 1. indexin ve 1. degiskenin degeri gelir.
#::: Out[66]: 0 gibi

# bu islemleri loc ile yaparsak bize 3. index yada degisken dahil bir sekilde sonuc verir.
df.iloc[0:3,0:2] # index bilgileri istersek
df.loc[0:3,"age"]# degisken bilgiside girilebilir.
df.loc[0:3,col_name] # col_name gibi listleride direkt olarak girebiliriz.
##Bu islem bize coklu gosterim yapmamizi saglar.

#-------------------------------------------------------
#-- Kosullu Secim
#-------------------------------------------------------

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"]>50].head() # Kosullu secimin ilk adiminda hangi degiskene kosulu soracagimizi belirtemimiz gerekir
df[df["age"]>50]["age"].count() # Yasi 50den buyuk kac kisi var sorusunu bu sekilde sorabiliriz.

df.loc[df["age"] > 50,"class"].head() # yasi 50 den buyuk olanlarin sinif bilgilerinin secimi
## bu sekilde yapilabilir. Yeni atama yapilarakta uzerinden islemler gerceklestirilebilir

df.loc[df["age"] > 50,["age","class"]].head() #bu sekildede bir liste girerek istenen butun bilgiler cekilebilir.
# IKI KOSUL GIRME
df.loc[(df["age"] > 50) & (df["sex"] == "male" ),["age","class"]].head()
# Hem yasi 50 den buyuk hemde erkek olanlarin alindigi bir kosullandirma oldu
## ikili kosullandirmalarda kosullandirmalar. Ayri ayri olacak sekilde parantez icine alinmak zorundadir


#-------------------------------------------------------
#-- Toplulastirma ve Gruplama
#-------------------------------------------------------

#- count()
#- first()
#- last()
#- mean() Ortalamasi
#- median()
#- min()
#- max()
#- std()
#- var()
# sum()
#- pivot table


import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")
df.head()

# Direkt olarak yas ortalamasi almak icin mean kullanabiliriz.
## Yukarida bu kisimla ilgili olarak detayli calisma yapmistik
### Tekrar gosterecek olursak

df["age"].mean()
# gruplastirma islemi burada devreye giriyor farzedelim biz cinsiyetlere gore yas ortalamasini
## ogrenmek istiyoruz bunun icin asagidaki islemi yapmamiz lazim
df.groupby("sex")["age"].mean()
#groupby komutunu yazdiktan sonra hangi degiskeni gruplastiracagimizi normal parantez icinde
## istedigimiz degisken degerlerini ise koseli parantez icinde yaziyoruz
#:: Out[4]:
#       sex
#       female    27.915709
#       male      30.726645
#       Name: age, dtype: float64 seklinde ciktimizi aliyoruz
# gruplastirilan bir degiskenin birden farkli degerini gormek istersek
df.groupby("sex").agg({"age":["mean","sum"]}) #bu komutla bunu saglayabiliriz.
#buradaki fark ikinci kisimda agg komutunu ekledikten sonra degiskenleri sozluk olarak yazmaktir.
## birden fazla degiskene bakilacagindan degisleride sozluk icinde liste olarak yazariz.
#::: Out[6]:
#              age
#             mean       sum
#sex
#female  27.915709   7286.00
#male    30.726645  13919.17

df.groupby("sex").agg({"age":"mean",
                       "survived" : "mean"})
#Burada survived degiskenininde ortalamasini bu sekilde gorebiliyoruz.

df.groupby(["sex","embark_town","class"]).agg({"age":"mean",
                       "survived" : "mean"})
#burada gruplastirmayi liste haline getirip farkli degiskenleri istersek
## aldigimiz ciktida farkli degiskenlerin kirilmasini yani degerlerinin detaylanmasini saglayabiliriz.

#-------------------------------------------------------
#-- Pivot Table
#-------------------------------------------------------

import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns",None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived","sex","embarked")#ilk girilen degisken kesisenleri
## ikinci degisken satir ifadesini
### ucuncu degisken ise sutunlari ifade eder.

df.pivot_table("survived","sex","embarked",aggfunc="std") # bu aggfunc ile hesaplanan degeri degistirebiliriz
## aggfunc ifadesi otomatik olarak mean heaplar

df.pivot_table("survived","sex","embarked",aggfunc=["std","mean"])
#bir kac degeri ayni anda gosterebiliriz

df.pivot_table("survived","sex",["embarked","class"])
#Ayrica satir ve ya sutun kisiminda liste olarak degiskenleri girersek bunlarin hepsini gosterir.
## Burada fancy indexde kullanabiliriz.

#Farzedelim yaslara gore de degerlendirmek istiyoruz.
# Yas sayisal bir degiskeni hayatta kalma acisindan nasil degerlendiririz buna bakalim
## Oncelikle bunun icin sayisal degiskeni kategorik degiskene cevirmeliyiz

df["new_age"] = pd.cut(df["age"],[0,10,18,28,40,90])
#degiskeni biliyorsak ve kategorileri kendimiz belirlemek istersek cut methodunu kullanirken
## Degiskeni bilmedigimizi dusunelim bu durumda qcut kodu degiskenin degerlerini kucukten buyuge siralar
### Kategorileri ceyrek dilimler olacak sekilde duzenler

df.pivot_table("survived","sex","new_age")
#:: Out[5]:
#new_age   (0, 10]  (10, 18]  (18, 28]  (28, 40]  (40, 90]
#sex
#female   0.612903  0.729730   0.75000  0.821918  0.770833
#male     0.575758  0.131579   0.15894  0.209302  0.176471

#-------------------------------------------------------
#-- Apply ve Lambda
#-------------------------------------------------------

pd.set_option("display.max_columns",None) #Bu komutla ... gibi kod ciktisindaki ciktilari ortadan kaldiriyoruz.
pd.set_option("display.width",500)

#Apply satir ya da sutunlarda otomatik olarak fonksiyon calistirmayi saglar
#Lambda ise bir fonksiyon tanimlama şeklidir. Farki kullan at fonksiyon olmasidir.

df["age2"] = df["age"]*2

df["age3"] = df["age"]*5
(df["age"]/10).head() # Head komutunun calismasi icin bu islemde degisken ve islemi parantez icine kalmak gerekir
(df["age2"]/10).head()
(df["age3"]/10).head() # Degiskenlerde bolme islemini tek tek bu sekilde yapabiliriz.

#Bu islemi dongu ilede yapabiliriz.

for col in df.columns:
    if "age" in col:
        print(col) #icerisinde age olan degiskenleri yakala ve yazir dongusu

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head()) #burada istedigimiz islemi gerceklestirmis olsakta
        ## atama olmadigi icin kaydini yapmadik

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10 #bu islemde kayit ederek donguyu yazmis olsun
df.head()
#Simdi apply sayesinde tek satirda bu islemi yapacagiz
df[["age","age2","age3"]].apply(lambda x:x/10).head()
#age degiskenlerinin barindiranlarin secim isleminide loc ile yapabiliriz
df.loc[:, df.columns.str.contains("age")].apply(lambda x:x/10).head()
#df.columns.str.contains("age") bu komutumuzla degiskenlerin icinde str olanlardaki age degiskenini sec komutudur.
#Bir standartlastirma fonksiyonu dusunelim

df.loc[:, df.columns.str.contains("age")].apply(lambda x:(x-x.mean())/x.std()).head()
#Standartlastirma islemide bu sekilde yapilmaktadir.
#lambda x üzerinde yapilacak islem aciklamasi kisminda bir fonksiyonda yazilabilir.
## Ornegin

def standart_scaler(col_name):
    return (col_name - col_name.mean())/col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()
#Sonuctan gorulecegi uzere ayni islemlerdir.
#Bu islemin donsuturme islemi icinde
df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()
df["age"].head()
#seklinde yapabiliriz.

#-------------------------------------------------------
#-- Birlestirme (Join) İşlemler
#-------------------------------------------------------

import numpy as np
import pandas as pd
m = np.random.randint(1,30, size=(5,3))
df1= pd.DataFrame(m, columns=["var1","var2","var3"])
df2 = df1 + 99
df2.head()

# Birlestirmede iki yontemi kullanacagiz.
## Birtanesi merge digeri ise concat komutudur.

pd.concat([df1,df2])
#:: Out[27]:
  # var1  var2  var3
#0    17    25     1
#1    12    18    17
#2    23    12    12
#3     1    23     1
#4     8     9    27
#0   116   124   100
#1   111   117   116
#2   122   111   111
#3   100   122   100
#4   107   108   126
#concat komutu ile direkt olarak alt alta birlestirebiliriz.
# burada dikkat etmemiz gereken kisim birlestirme esnasinda iki dataframede index bilgisini tutar
#Bunu düzeltmek için ignore index komutunu kullaniyoruz.
pd.concat([df1,df2],ignore_index=True)

#-- Merge ile Birlestirme

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

#ilk dataframede calisanlar ve bagli olduklari depertmanlar varken
## İkincide ise calisanlar ve calisanlarin ise basladiklari tarihleri vermektedir.
### Maksadimiz ise Bir calisanin butun bilgilerini bir araya getirmek

pd.merge(df1,df2) #Burada kendisi otomatik olarak calisanlar argumanina gore yapmaktadir.
#Kendimiz hangi argumani esas alacagini belirlemek istersek
pd.merge(df1,df2,on="employess") #on = ile argumanin adini girebiliriz.
df3 = pd.merge(df1,df2) # degiskeni kayit ediyoruz.
# Her calisanin mudur bilgisine ulasmak istedigimizi dusunelim

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})
#Gorulecegi uzere burada ortak olan nokta hangi birime baglı olduklari yani "group" argumani
pd.merge(df4,df3)
#Diyebiliriz kendisi ortak argumanı bulur ya da kendimiz on = ile kendimiz girebiliriz.
pd.merge(df4,df3,on = "group")


