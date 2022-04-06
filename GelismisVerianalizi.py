#-------------------------------------------#
#-- Gelismis Fonsiyonel Kesifci Veri Analizi
#-------------------------------------------#


#-------------------------------------------
#-- Genel Resim
#-------------------------------------------

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head() #Bastan veriyi inceler
df.tail() #Sondan veriyi inceler
df.shape #Satir ve stun bilgisini
df.info()
df.columns #degisken isimleri
df.index # kac deger var kacar kacar artiyor
df.describe().T
df.isnull().values.any()#Veri setinde eksik deger var mı ?
df.isnull().sum()#Hangi degiskende toplam kac tane eksik deger var
#Asagida yapacagimiz fonksiyonla girilecek her degerin degerlerinin
## kolay bir bicimde bilgilerinin okunabilir bir bicimde cikti olarak
### gelmesini saglayacagiz
def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### Quantiles #####################")
    print(dataframe.isnull().sum())
check_df(df)

df = sns.load_dataset("tips")
check_df(df)

#-------------------------------------------
#-- Kategorik Degisken Analizi
#-------------------------------------------

df["embarked"].value_counts()
df["sex"].unique() # Unique degerleri icindeki deger siniflaridir.
df["sex"].nunique() # İcerisinde kac tane unique deger
##yani sinif var sorusunun yanitidir.

#Bizim icin kategorik olan veri tipleri 3 tanedir bool,category ve object
#Yanlız burada veriye hakim olmak gerekir. İnt gibi gozukurken
## Aslinda bir kategorik degiskeni temsil eden degiskenler olabilir.
### Ornegimizdeki pclass ve survived gibi
#Kategorik degiskenler
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category","object","bool"]]
#bu kod ile degiskenlerin icine for dongusu ile girdikten sonra eger
## stringe cevrilen tip bilgisi icinde kategorik degisken ifadeleri barindiriyorsa
### onlari bize sec diyoruz.
cat_cols
#Numerik ama kategorik demek
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int", "float"]]
#Burada kategorik degisken olup numerik gibi islem goren degiskenleri seciyoruz
##Yukaridan farkli olarak nunique ile sinif sayisina bakip tahminde bulunuyoruz.
### 10 taneden azsa numerik olamak bu sayilarin kategorik anlamda ifade ettigi bir sey var diyoruz.
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

cat_cols = cat_cols + num_but_cat

#Eger cat_but_car da degiskenler olsaydi bunlari kategorik degiskenlerin icinden cikarmamiz gerekecekti

cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols].nunique() #Degiskenlerin sinif sayilarina bakarak buradan dogrulama yapabiliriz.

[col for col in df.columns if col not in cat_cols]

df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df) #Burada yaptigimiz islemi bir fonksiyon ile halledebiliriz.
##Boylece degerlerin hepsini yamayarak zamandan kar elde ederiz

def cat_summary(dataframe,col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("####################################")

cat_summary(df,"sex")

for col in cat_cols:
    cat_summary(df,col)

#Bu dongu sayesinde cat_cols icindeki butun degerleri col degeri olarak yukarida yazmis oldugumuz fonksiyona sokabiliyoruz.

#Bize degiskenleri verdiginde bilgilerini getirirken ayrica birde sutun grafiginide bize getirsin
##Hatirlanacagi uzere elimizde kategorik degisken varsa bunu sutun grafigi ile gosterebiliriz.
### Bunlardan biri olan seaborn kutuphanesinden countplot grafigini kullanalim

def cat_summary(dataframe,col_name,plot = False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("####################################")

    if plot:
        sns.countplot(x=dataframe[col_name],data=dataframe)
        plt.show(block= True) #Burada block komutu bize cikti vermeden önce tüm degerlerin donmesini beklemek anlamindadir.

cat_summary(df,"sex",plot=True) #Fomksiyonun icinde plot= False dedigimiz icin biz True olarak gondermeden
## Grafigin ciktisini gostermez if plot kismi hic yazilmamis gibi cikti vermeye devam eder

#Countplotta bool degerler kullanilmazlar
## Bu sebepten bizbutun degiskenlerin ciktisini grafik olarak istersek degerlerini verir ama grafigi vermez
### Bunun icin bool degerinde olan degiskenleri grafike sokmamak gerekir
# Oncelikle butun degerleri fonksiyona sokmak icin dongumuzu yazalim

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("Bool Deger Grafige Girmez")
    else:
        cat_summary(df,col ,plot=True)
#Dongumuzde bu sekilde eger komutu yokarsak sorunsuz bir sekilde butun degerlerin ciktisini alabiliriz.
## Bu donguler ve fonksiyonlar bir veriyle ilk tanismamizda bize cogu bilgileri aktaracaktir.

#Bool degerinde olan adult_male degiskenini int ifadeye cevirirsek bu sorunuda ortadan kaldirabiliriz.
df["adult_male"].astype(int) #astype ile secilen verinin tipini degistirebiliriz
#bunu elimizle tek tek yapabiliriz fakat buyuk bir veride cok fazla bu sekilde deger oldugunu dusunursek

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df,col ,plot=True)

#Bu sekilde sadece veri tipini degistirerek butun degerleri countplota sokabiliriz

