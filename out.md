<span style="color:#006699">Website Kategorizasyonu ve Filtrelenmesi</span>  <span style="color:#006699">\(Bilgisayar Projesi 2019\-Güz\)</span>  <span style="color:#006699">Alperen Aksu</span>  <span style="color:#006699">Aydın Yardımcı</span>  <span style="color:#006699">Danışman: Prof\. Dr\. Banu Diri</span>

<span style="color:#FFFFFF">Projemizin Kapsamı</span>

* <span style="color:#0066CC">Projemiz:</span>
  * <span style="color:#0066CC">Mevcut websitelerinin\, içeriklerine göre sınıflandırılmasını</span>
  * <span style="color:#0066CC">Sınıflandırılan websitelerin Filtrelenmesini</span>
  * <span style="color:#0066CC">kapsamaktadır\.</span>

<span style="color:#FFFFFF">Projemizin Motivasyonu</span>

<span style="color:#0066CC">İnternetin gelişimi\, birçok istenmeyen durum doğurmuştur\. Bunlardan biri de internette var olan her türlü içeriğe her yaştan kişinin  erişebiliyor olmasıdır\.</span>

<span style="color:#0066CC">Yetişkinler için olan ve şiddet içeren içeriklere\, reşit olmayan kişiler tarafından erişilebiliyor olması projemizin ele aldığı sorundur\.</span>

<span style="color:#FFFFFF">Projemizin Amacı</span>

<span style="color:#0066CC">Projemiz\, reşit olmayan kişilerin bu tip içeriklere erişimini engellemek amacı ile geliştirilmiştir\.</span>

<span style="color:#FFFFFF">Projemizin Metodu</span>

<span style="color:#0066CC">Projemizde\, gezilen sitelerin kategorisinin belirlenmesi için site içeriğinden çıkarım yapılması gerekmektedir\. Bu çıkarım\, makine öğrenmesi yöntemleri ile gerçekleştirilmiştir\.</span>

<span style="color:#0066CC">İnternette erişilmek istenen sitenin engellenmesi için tarayıcı eklentisi geliştirilmiştir\.</span>

<span style="color:#FFFFFF">Makine Öğrenmesi</span>

* <span style="color:#0066CC">Makine öğrenmesinde sınıflandırma modeli oluşturulabilmesi için modeli eğitecek veri seti gerekmektedir\.</span>
* <span style="color:#0066CC">Bu veri seti\, internette halihazır da bulunmadığından dolayı tarafımızdan oluşturulmuştur\.</span>
* <span style="color:#0066CC">Gezilen sitelerin içerikleri\, oluşturulan modelde test edilerek sitelerin kategorileri belirlenmiştir\.</span>
* <span style="color:#0066CC">Bu kategoriler:</span>
  * <span style="color:#0066CC">Yetişkin\, Haber\, Oyun\, Bilim</span>

<span style="color:#FFFFFF">Veri Setinin Oluşturulması</span>

* <span style="color:#0066CC">Modelin eğitiminde kullanılacak veri setinin\, kategorisi belli olan site içeriklerinden oluşması gerekmektedir\.</span>
* <span style="color:#0066CC">Bunun için iki yol izlenmiştir\.</span>
  * <span style="color:#0066CC">“</span>  <span style="color:#0066CC"> _alexa\.com/topsites/”_ </span>  <span style="color:#0066CC">sitesi üzerinden belirli kategoriler altında listenen sitelerin alan adları çekilerek elde edilmiştir;</span>
  * <span style="color:#0066CC"> _Google API ve Yandex API_ </span>  <span style="color:#0066CC">kullanılarak belirli sorgulara karşılık cevap gelen alan adları çekilmiştir\.</span>
  * <span style="color:#0066CC">Bu alan adları kullanılarak içerikler çekilmiş\, karşılık gelen kategoriler ile birlikte veri seti oluşturulmuştur\.</span>

<span style="color:#FFFFFF">Site Alan Adlarının Çekilmesi</span>

<span style="color:#FFFFFF">Site Alan Adlarının Çekilmesi</span>

<span style="color:#0066CC">Alexa\.com sitesi üzerinden site alan adları çekilmiştir\.</span>

alexa\.com’daki her bir class formatı

alexa\.com’daki class üzerinden site alan adlarının elde edilmesi

<span style="color:#FFFFFF">Site Alan Adlarının Çekilmesi</span>

<span style="color:#0066CC">Türkçe siteleri içeren belirli bir liste olmadığı için Google API ve Yandex API üzerinden anlamlı sorgular yapılarak alan adları elde edilmiştir\.</span>

<img src="img\Araprojeslayt0.png" width=395px />

<img src="img\Araprojeslayt1.png" width=500px />

<span style="color:#FFFFFF">Site İçeriklerinin Çekilmesi</span>

* <span style="color:#0066CC">Websiteleri\, içerikleri hakkında en nitelikli bilgiyi kaynak kodlarında bulunan ortak bazı HTML etiketlerinde barındırmaktadır\. Bu etiketler;</span>
  * <span style="color:#0066CC">Title</span>
  * <span style="color:#0066CC">Description\(Meta Data\)</span>
  * <span style="color:#0066CC">Keywords\(Meta Data\)</span>

<img src="img\Araprojeslayt2.png" width=500px />

<span style="color:#FFFFFF">Site İçeriklerinin Çekilmesi</span>

<span style="color:#0066CC">Etiketlerde bulunan içeriklerin çekilmesi için Python dilinde geliştirilmiş “beautifulsoup” kütüphanesi kullanılmıştır\.</span>

<img src="img\Araprojeslayt3.png" width=484px />

<span style="color:#FFFFFF">İçerik Üzerinde Ön İşlem</span>

<span style="color:#0066CC">Noktalama işaretleri silinmiştir\.</span>

<img src="img\Araprojeslayt4.png" width=326px />

<span style="color:#0066CC">Türkçe karakterler ingilizce karakter karşılıklarına çevrilmiştir\.</span>

<img src="img\Araprojeslayt5.png" width=500px />

<span style="color:#0066CC">Stopwords \(bağlaç\,edat\,zamir\. \. \. \) silinmiştir\.</span>

<img src="img\Araprojeslayt6.png" width=232px />

<span style="color:#0066CC">Ingilizce karakterler dışındaki karakterler silinmiştir\.</span>

<img src="img\Araprojeslayt7.png" width=303px />

<span style="color:#FFFFFF">Veri Setinin Yapısı</span>

<span style="color:#0066CC">Site İçerikleri ve kategorileri csv dosyasına yazılmıştır\.</span>

Csv dosyasından bir kısım

<span style="color:#FFFFFF">Modelin Oluşturulması</span>

* <span style="color:#0066CC">Modelimiz oluşturulurken Python dilinde geliştirilmiş “keras” kütüphanesi kullanılmıştır\. Modelimiz üç katmanlıdır\. Bu katmanlar:</span>
  * <span style="color:#0066CC">Embedding</span>
  * <span style="color:#0066CC">GRU</span>
  * <span style="color:#0066CC">Dense</span>

<img src="img\Araprojeslayt8.png" width=443px />

<span style="color:#2A6099">Embedding katmanında her bir kelime 100 boyutlu vektörlere çevrilmiştir</span> \.

<span style="color:#FFFFFF">Modelin Oluşturulması</span>

<img src="img\Araprojeslayt9.png" width=500px />

<span style="color:#FFFFFF">Eklenti Ve Model Veri İletişimi</span>

<span style="color:#0066CC">İnternet üzerinde gezilen sayfaların alan adlarının modele iletilmesi ve modelin ürettiği sonuca göre sayfaların engellenmesi ile ilgili bilgilerin modelden eklentiye aktarılması için JSON yapısı kullanılmıştır\.</span>

<span style="color:#0066CC">Daha önceden ziyaret edilen web siteler erişim durumuna göre liste olarak JSON yapısında saklanmaktadır\.</span>

<img src="img\Araprojeslayt10.png" width=229px />

<img src="img\Araprojeslayt11.png" width=457px />

<img src="img\Araprojeslayt12.png" width=500px />

<span style="color:#FFFFFF">Eklenti Oluşturulması</span>

<span style="color:#0066CC">Web sitesi bağlantı isteğinin engellenmesi ve aynı zamanda kullanıcının girdiği sitelerin adresinin elde edilmesi gerekmektedir\. Bu nedenle tarayıcı üzerinde çalıcak eklenti oluşturuldu\. Eklentinin tarayıcı üzerinde doğru çalısması açısından Google tarafından belirlenen standarta uyarak eklenti pakedi gerçekleştirildi\.</span>

<img src="img\Araprojeslayt13.png" width=500px />

<span style="color:#FFFFFF">Sitenin Alan Adının Elde Edilmesi</span>

<span style="color:#0066CC">Tarayıcı üzerinde alan adlarına erişmek için arka planda tüm sekmelerin izlenmesi gerekmektedir\. Bunun için arka plan \(background\.js\) kod bloğu oluşturup eklenti yapısına eklenerek gerekli bilgiler elde edilmiştir\.</span>

<img src="img\Araprojeslayt14.png" width=500px />

<span style="color:#FFFFFF">Sitenin Engellenmesi</span>

<span style="color:#0066CC">JSON ile modelden alınan bilgiye göre internet sayfasının erişimine izin verilmesi veya engellenmesi gerekmektedir\. Bunun için arka plan \(background\.js\) kod bloğuna gerekli sayfa yönlendirme kodları yazılmıştır\.</span>

<span style="color:#0066CC">Modelden alınan sonuca göre web site; \(blocked\) izin verilen siteler listesine veya \(trusted\) engellenen sitelerin listesine eklenmektedir\.</span>

<img src="img\Araprojeslayt15.png" width=500px />

<span style="color:#FFFFFF">Web Site Oluşturma</span>

<span style="color:#0066CC">Eklenti ayarlarının yapılabilmesi\, kullanıcının eklenti denetimini sağlaması\, eklentiyi durdurabilmesi\, ziyaret edilen web siteleri görüntüleyebilmesi ve gerektiği durumda engellenen ve güvenilen listeler arası web site adreslerini taşıyarak erişim durumlarını değiştirebilmesi amacıyla web sitesi tasarlanarak gerekli kodlaması gerçekleştirilmiştir\.</span>

<img src="img\Araprojeslayt16.png" width=500px />

<span style="color:#FFFFFF">Engellenenler Sayfası</span>

<img src="img\Araprojeslayt17.png" width=500px />

<span style="color:#FFFFFF">Güvenilenler Sayfası</span>

<img src="img\Araprojeslayt18.png" width=500px />

<span style="color:#FFFFFF">Güvenilenler Sayfası</span>

<img src="img\Araprojeslayt19.png" width=500px />

<img src="img\Araprojeslayt20.png" width=500px />

<img src="img\Araprojeslayt21.png" width=500px />

<span style="color:#0066CC">Yapılabilmesi planlanan işlemlerin bir bölümünü kullanıcının daha rahat ulaşması amacıyla tarayıcı üzerinde eklentiye açılır menü \(pop\-up\) tasarlanarak gerekli kodlaması gerçekleştirilmiştir\.</span>

<img src="img\Araprojeslayt22.png" width=298px />

<img src="img\Araprojeslayt23.png" width=321px />

<img src="img\Araprojeslayt24.png" width=500px />

<span style="color:#FFFFFF">Modelin Sayısal Başarısı</span>

<span style="color:#0066CC">Modelimiz toplam 4700 adet içerikten oluşan veri seti ile eğitilmiştir\.</span>

<span style="color:#0066CC">4700 adet içerikten 3800 içerik eğitim amaçlı\, 900 adet içerik ise test için ayrılmıştır\.</span>

<span style="color:#0066CC">Bu eğitim sonucunda eğitim verisi üzerinde %100 isabetlilik oranı elde edilirken test verisinde %92 isabetlilik oranı elde edilmiştir\.</span>

<span style="color:#FFFFFF">Modelin Sayısal Başarısı</span>

<img src="img\Araprojeslayt25.png" width=500px />

* <span style="color:#0066CC">Dinlediğiniz İçin Teşekkürler…</span>
                  * <span style="color:#0066CC">Alperen Aksu</span>
                  * <span style="color:#0066CC">Aydın Yardımcı</span>

