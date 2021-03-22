

Website Kategorizasyonu ve

Filtrelenmesi

(Bilgisayar Projesi 2019-Güz)

Alperen Aksu

Aydın Yardımcı

Danışman: Prof. Dr. Banu Diri





l

Projemiz:

\- Mevcut websitelerinin, içeriklerine göre

sınıflandırılmasını

\- Sınıflandırılan websitelerin Filtrelenmesini

\- kapsamaktadır.





l

İnternetin gelişimi, birçok istenmeyen durum

doğurmuştur. Bunlardan biri de internette var

olan her türlü içeriğe her yaştan kişinin

erişebiliyor olmasıdır.

l

Yetişkinler için olan ve şiddet içeren içeriklere,

reşit olmayan kişiler tarafından erişilebiliyor

olması projemizin ele aldığı sorundur.





l

Projemiz, reşit olmayan kişilerin bu tip içeriklere

erişimini engellemek amacı ile geliştirilmiştir.





l

Projemizde, gezilen sitelerin kategorisinin

belirlenmesi için site içeriğinden çıkarım

yapılması gerekmektedir. Bu çıkarım, makine

öğrenmesi yöntemleri ile gerçekleştirilmiştir.

l

İnternette erişilmek istenen sitenin engellenmesi

için tarayıcı eklentisi geliştirilmiştir.





l

Makine öğrenmesinde sınıflandırma modeli

oluşturulabilmesi için modeli eğitecek veri seti

gerekmektedir.

l

l

l

Bu veri seti, internette halihazır da bulunmadığından

dolayı tarafımızdan oluşturulmuştur.

Gezilen sitelerin içerikleri, oluşturulan modelde test

edilerek sitelerin kategorileri belirlenmiştir.

Bu kategoriler:

\- Yetişkin, Haber, Oyun, Bilim





l

l

Modelin eğitiminde kullanılacak veri setinin,

kategorisi belli olan site içeriklerinden oluşması

gerekmektedir.

Bunun için iki yol izlenmiştir.

\- “alexa.com/topsites/” sitesi üzerinden belirli kategoriler

altında listenen sitelerin alan adları çekilerek elde edilmiştir;

\- Google API ve Yandex APIkullanılarak belirli sorgulara

karşılık cevap gelen alan adları çekilmiştir.

\- Bu alan adları kullanılarak içerikler çekilmiş, karşılık

gelen kategoriler ile birlikte veri seti oluşturulmuştur.









l

Alexa.com sitesi üzerinden site alan adları

çekilmiştir.

alexa.com’daki her bir class formatı

alexa.com’daki class üzerinden site alan adlarının elde edilmesi





l

Türkçe siteleri içeren belirli bir liste olmadığı için

Google API ve Yandex API üzerinden anlamlı

sorgular yapılarak alan adları elde edilmiştir.





l

Websiteleri, içerikleri hakkında en nitelikli bilgiyi

kaynak kodlarında bulunan ortak bazı HTML

etiketlerinde barındırmaktadır. Bu etiketler;

\- Title

\- Description(Meta Data)

\- Keywords(Meta Data)





l

Etiketlerde bulunan içeriklerin çekilmesi için

Python dilinde geliştirilmiş “beautifulsoup”

kütüphanesi kullanılmıştır.





l

Noktalama işaretleri silinmiştir.

l

l

Türkçe karakterler ingilizce karakter karşılıklarına çevrilmiştir.

Stopwords (bağlaç,edat,zamir. . . ) silinmiştir.

l

Ingilizce karakterler dışındaki karakterler silinmiştir.





l

Site İçerikleri ve kategorileri csv dosyasına

yazılmıştır.

Csv dosyasından bir kısım





l

Modelimiz oluşturulurken Python dilinde

geliştirilmiş “keras” kütüphanesi kullanılmıştır.

Modelimiz üç katmanlıdır. Bu katmanlar:

\- Embedding

\- GRU

\- Dense

Embedding katmanında

her bir kelime 100 boyutlu

vektörlere çevrilmiştir.





Yetişki

n

Haber

Oyun

Bilim

Dens

Embeddin

g

e

GRU





l

İnternet üzerinde gezilen sayfaların alan adlarının modele

iletilmesi ve modelin ürettiği sonuca göre sayfaların

engellenmesi ile ilgili bilgilerin modelden eklentiye aktarılması

için JSON yapısı kullanılmıştır.

l

Daha önceden ziyaret edilen web siteler erişim durumuna göre

liste olarak JSON yapısında saklanmaktadır.





l

Web sitesi bağlantı isteğinin engellenmesi ve aynı zamanda

kullanıcının girdiği sitelerin adresinin elde edilmesi gerekmektedir. Bu

nedenle tarayıcı üzerinde çalıcak eklenti oluşturuldu. Eklentinin

tarayıcı üzerinde doğru çalısması açısından Google tarafından

belirlenen standarta uyarak eklenti pakedi gerçekleştirildi.





l

Tarayıcı üzerinde alan adlarına erişmek için arka planda tüm

sekmelerin izlenmesi gerekmektedir. Bunun için arka plan

(background.js) kod bloğu oluşturup eklenti yapısına eklenerek

gerekli bilgiler elde edilmiştir.





l

JSON ile modelden alınan bilgiye göre internet sayfasının erişimine

izin verilmesi veya engellenmesi gerekmektedir. Bunun için arka plan

(background.js) kod bloğuna gerekli sayfa yönlendirme kodları

yazılmıştır.

l

Modelden alınan sonuca göre web site; (blocked) izin verilen siteler

listesine veya (trusted) engellenen sitelerin listesine eklenmektedir.





l

Eklenti ayarlarının yapılabilmesi, kullanıcının eklenti denetimini

sağlaması, eklentiyi durdurabilmesi, ziyaret edilen web siteleri

görüntüleyebilmesi ve gerektiği durumda engellenen ve

güvenilen listeler arası web site adreslerini taşıyarak erişim

durumlarını değiştirebilmesi amacıyla web sitesi tasarlanarak

gerekli kodlaması gerçekleştirilmiştir.





















l

Yapılabilmesi planlanan işlemlerin bir bölümünü kullanıcının

daha rahat ulaşması amacıyla tarayıcı üzerinde eklentiye açılır

menü (pop-up) tasarlanarak gerekli kodlaması

gerçekleştirilmiştir.









l

l

l

Modelimiz toplam 4700 adet içerikten oluşan

veri seti ile eğitilmiştir.

4700 adet içerikten 3800 içerik eğitim amaçlı,

900 adet içerik ise test için ayrılmıştır.

Bu eğitim sonucunda eğitim verisi üzerinde

%100 isabetlilik oranı elde edilirken test

verisinde %92 isabetlilik oranı elde edilmiştir.









