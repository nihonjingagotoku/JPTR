# JPTR
JPTR [Python](https://www.python.org/) programlama dilinde yazılmış basit bir Japonca-Türkçe sözlük web uygulamasıdır. JPTR [Flask](https://flask.palletsprojects.com/en/2.2.x/) ve [SQlite](https://www.sqlite.org/index.html) kütüphanelerini kullanır. JPTR'nin amacı Türkiyedeki ve Türkçe dilindeki yazılmış/üretilmiş Japonca kaynak eksikliğini mümkün olduğunca gidermek, aklımdaki fikirleri olduğu kadar uygulamaya koymak ve diğer insanları bu konuda çalışmaya teşvik etmektir. JPTR' nin kullanmış olduğu sözlük datasına "dictionary_data.txt" adlı dosyadan ulaşabilirsiniz. 

## JPTR ekran görüntüleri
### Bilgisayardaki görünümü
<img src="https://github.com/nihonjingagotoku/JPTR/blob/main/screenshots/dict_in_desktop_browser_0.png?raw=true" />
<img src="https://github.com/nihonjingagotoku/JPTR/blob/main/screenshots/dict_in_desktop_browser_1.png?raw=true" />


### Telefondaki görünümü
<img src="https://github.com/nihonjingagotoku/JPTR/blob/main/screenshots/dict_in_phone_browser_0.jpg?raw=true" width=300 height=600 align=left/> <img src="https://github.com/nihonjingagotoku/JPTR/blob/main/screenshots/dict_in_phone_browser_1.jpg?raw=true" width=300 height=600 align=left/>


## JPTR' yi çalıştırmak
JPTR' yi çalıştırmak için güncel bir Python sürümü yeterlidir. JPTR **Python 3.10.6** sürümü ile geliştirildiğinden dolayı **Python 3.10.6** sürümünü kullanmanızı öneririz. Hem JPTR'nin sağlıklı çalışması hem de varolan geliştirme ortamınızın etkilenmemesi için [Virtualenv](https://virtualenv.pypa.io/en/latest/) ile kullanmanızı tavsiye ederiz.

### Linux ve Termux için
Repoyu klonlayarak işe başlayalım.
```
git clone https://github.com/nihonjingagotoku/JPTR
cd JPTR
```

Repoyu klonladıktan sonra isteğe bağlı olarak **Virtualenv** kurulumu yapabilirsiniz ya da bu adımı atlayabilirsiniz.
```
virtualenv --python "<Kullanılmak istenen Python sürümünün konumu>" ".env"
source .env/bin/active
```

Şimdi pip ile gerekli paketleri kuralım.
```
pip install -r requirements.txt
```

Kurulum bittikten sonra aşağıdaki komut ile uygulamayı çalıştırabilirsiniz.
```
./run.sh
```

**Tebrikler!** , Şimdi tarayıcınızı açıp http://127.0.0.1:5000 adresine gidip uygulamayı kullanmaya başlayabilirsiniz. Eğer uygulamanın çalışma biçimini değiştirmek istiyorsanız çalıştırma scriptlerinizdeki Ortam değişkenlerini değiştirebilirsiniz. Ortam Değişkenleri hakkında daha fazla bilgi almak için [Ortam Değişkenleri](#ortam-değişkenleri) başlığını okuyabilirsiniz.

### Windows için
Kısaca [Linux](#linux-ve-termux-için) daki adımların aynısı ama bu sefer run.sh yerine run.bat i çalıştıracaksınız.

### macOS
Desteklenmiyor. Büyük ihtimal [Linux](#linux-ve-termux-için) adımlarını birebir uygulayarak çalıştırabilirsiniz.


## Ortam değişkenleri
### DICTIONARY_APP_DATA
Uygulamanın kullanacağı datanın konumunu belirtir. Eğer bu değişken tanımlanmışsa uygulama ilk başlatmada datayı okur, işler ve DICTIONARY_APP_DATABASE değişkeninin tanımlı olduğu dizinde ya bir database oluşturur ya da varolan databasein üzerine yazar.

### DICTIONARY_APP_DATABASE
Uygulamanın kullanacağı ya da oluşturacağı databasein konumunu belirtir. Eğer DICTIONARY_APP_DATA değişkeni tanımlanmamış ise uygulama varolan database i olduğu gibi alır ve kullanır.

## İnternette yayınlamak
JPTR internette yayınlanması için yazılmadığı için bu eylemi yapmanızı önermem, bu eylemle ilgili sorumluluk almam ve size olası bir destek vermem. Eğer bu eylemi yapacaksanız unutmayın ki kaynak kodda düzenlemeniz gereken birçok yer ve fixlemeniz gereken birçok potansiyel **güvenlik açığı** vardır. Yine de bir yerden başlamak istiyorsanız aşağıdaki linke bakabilirsiniz.

https://flask.palletsprojects.com/en/2.2.x/deploying/

## JPTR kelimeleri nasıl arar?
JPTR'in database indeki kayıt yapısı şu şekildedir. Kayıttaki her elemanın doldurulması **zorunludur**. 

| Eleman | İşlev |
| -------| ------|
| `WID` | Database deki her kayıt için verilen bir id dir. Her yeni kayıt eklendiğinde SQlite tarafından kayda otomatik olarak atanır ve otomatik olarak id değeri arttırılır. Bu değer **elle oynanmamalıdır**. |
| `WTYPE` | Sözcüğün türünü belirtir. Sözcüğün isim, fiil, zamir, sıfat ya da başka birşey olduğunu bu eleman belirtir. |
| `JPWORD` | Japonca sözcüğün hiragana ile yazılışını tutar. |
| `KANJI` | Her Japonca sözcük için kanji yazılışını tutar. |
| `ROMAJI` | Her Japonca sözcüğün romaji ya da latince okunuşunu tutar. |
| `TRMEANING` | Her Japonca sözcüğün Türkçe    karşılığını tutar. |

JPTR gelişmiş araştırma yöntemlerini desteklemez. Aramalar baştan sona doğru yapılır. Kullanıcı bir kelime aradığında kullandığı arama seçeneğine göre SQlite query si oluşturulur ve dönen sonuç Jinja tarafından işlenir ve son kullanıcıya sunulur. Örnek bir SQL query si şu şekide olabilir.
```
SELECT * FROM DICTIONARY where JPWORD like '<Aranan Kelime>%'
```

## JPTR' nin sunduğu rotalar
```
/ - /sozluk rotasına yönlendirir.

/sozluk - Sözlükteki sözük arama ve görme işlevinin gerçekleştiği rotadır. search ve all olmak üzere iki tane opsiyonel argüman alır.
 * search - yanına search_opt denen zorunlu parametreyi alır ve aranan şeyle alakalı kayıtları döndürür. all parametresiyle birlikte kullanılamaz.
 * all - Sözlükteki tüm kelimeleri döndürür. search parametresiyle birlikte kullanılamaz.

/sozluk/addword - Sözlüğe kelime eklenilmek istendiğinde gidilmesi gereken rotadır.

/sozluk/statistics - Sözlükteki toplam sözük sayısını döndürür. all diye opsiyonel parametre alabilir.
 * all - Kullanıldığı takdirde sözlükteki tüm kayıtları liste şeklinde sıralar.
```