################
# PANDAS
################
import seaborn as sns
import pandas as pd
pd.set_option("display.max_rows",None) #Tum satirlar
pd.set_option("display.max_columns",None)#Tum sutunlari gosterir
pd.set_option("display.width",1000)
######1. Gorev Titanic Kutuphanesi
df =sns.load_dataset("titanic")
df.head()

##### 2. Gorev Kadın erkek sayisi
df["sex"].value_counts()

#### 3. Gorev her bir sutuna ait degerlerin unique degerlerini bulunuz

df.nunique()

### 4. pclass degiskenin unique degerlerinin sayisin

df["pclass"].nunique()

### 5.pclass ve parch degiskenlerinin sinif sayisi

df[["pclass","parch"]].nunique()

## 6 embarked degiskeninin tipini kontrol ediniz
df["embarked"].dtypes
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtypes

# 7 embarked degeri c olanların tum bilgilerini gosteriniz
df[df["embarked"]=="C"]

# 8 embarked degeri s olmayanlari gosteriniz

df[df["embarked"] != "S"]["embarked"].unique()

#9 Yası 30 dan kucuk ve kadın olan tüm bilgilerini gosteriniz

df[(df["sex"]== "female") & (df["age"]<30)]

#10 Fare'i 500 den buyuk veya yasi 70 den buyuk

df[(df["fare"]>500) |(df["age"]>70)]

#11 Bos degelerin toplami
df.isnull().sum()

#12 Who degiskenini veriden cıkarın

df.drop("who",axis=1,inplace=True)
df.head()

#13 deck degiskenindeki bos degerleri en cok tekrar eden deger ile doldurunuz

deck_mode = df["deck"].mode()[0]
df["deck"].fillna(deck_mode,inplace=True)
df["deck"].isnull().sum()

# 14 age degiskeninde bos degerleri age medyani ile

df["age"].fillna(df["age"].median(),inplace=True)
df["age"].isnull().sum()

# 15 Survived degiskeninin pclass ve cinsiyet icin kırılımında sum,count ve mean degelrini
df.groupby(["pclass","sex"]).agg({"survived": ["sum", "count", "mean"]})

df.pivot_table(values="survived",index=["pclass","sex"],aggfunc=["mean","sum","count"])

#16 30 yasın altında olanlar 1, 30 esıt ve ustunde olanlara 0 verecek bir fonk
#yazılan bu fonksiyonu age_flag olustururacagız
def age_30(age):
    if age <30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x : age_30(x))
df.head()
#2.Yol
df["age_flag"] = df["age"].apply(lambda x : 1 if x<30 else 0)

#