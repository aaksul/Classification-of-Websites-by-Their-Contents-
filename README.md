<span style="color:#006699">Website Categorization and Filtering</span>  <span style="color:#006699">\(Computer Project 2019\)</span>  <span style="color:#006699">Alperen Aksu</span>  <span style="color:#006699">Aydın Yardımcı</span>  <span style="color:#006699">Counselor: Prof\. Dr\. Banu Diri</span>

<span style="color:#FFFFFF">Scope of Our Project</span>

* <span style="color:#0066CC">Project:</span>
  * <span style="color:#0066CC">Existing websites \, according to their content</span>
  * <span style="color:#0066CC">Filtering of classified websites</span>


<span style="color:#FFFFFF">Motivation of Our Project</span>

<span style="color:#0066CC">The development of the Internet has created many undesirable situations. One of them is that people of all ages can access all kinds of content on the internet.\.</span>

<span style="color:#0066CC">The problem of our project is that adult and violent content can be accessed by minors.\.</span>

<span style="color:#FFFFFF">Purpose of Our Project</span>

<span style="color:#0066CC">Our project has been developed to prevent minors from accessing this type of content.\.</span>

<span style="color:#FFFFFF">The Method of Our Project</span>

<span style="color:#0066CC">In our project, it is necessary to infer from the content of the site in order to determine the category of the sites visited \. This inference has been carried out by machine learning methods.\.</span>

<span style="color:#0066CC">A browser plug-in has been developed to block the website to be accessed on the Internet.\.</span>

<span style="color:#FFFFFF">Machine learning</span>

* <span style="color:#0066CC">In order to generate a classification model in machine learning, a dataset to train the model is required.\.</span>
* <span style="color:#0066CC">This dataset has been generated by us since it is not available on the internet.\.</span>

<span style="color:#FFFFFF">Generating Dataset</span>

* <span style="color:#0066CC">Dataset must be generated from content of sites which have specified categories</span>
* <span style="color:#0066CC">Two ways have been followed for this\.</span>
  * <span style="color:#0066CC">“</span>  <span style="color:#0066CC"> _alexa\.com/topsites/”_ </span>  <span style="color:#0066CC">was obtained by pulling the domain names of the sites listed under certain categories on the website.;</span>
  * <span style="color:#0066CC"> _Google API and Yandex API_ </span>  <span style="color:#0066CC">kullanılarak belirli sorgulara karşılık cevap gelen alan adları çekilmiştir\.</span>
  * <span style="color:#0066CC">Bu alan adları kullanılarak içerikler çekilmiş\, karşılık gelen kategoriler ile birlikte veri seti oluşturulmuştur\.</span>


<span style="color:#FFFFFF">Retrieving Domain Names</span>

<span style="color:#0066CC">There is no specific list of Turkish sites by categories, Domain names were obtained by making related queries over Google API and Yandex API.\.</span>

<img src="img\Araprojeslayt0.png" width=395px />

<img src="img\Araprojeslayt1.png" width=500px />

<span style="color:#FFFFFF">Retrieving Content Of Sites</span>

* <span style="color:#0066CC">Websites contain some meaningful words in specific HTML elements that related to their contents. These HTML elements are:\.</span>
  * <span style="color:#0066CC">Title</span>
  * <span style="color:#0066CC">Description\(Meta Data\)</span>
  * <span style="color:#0066CC">Keywords\(Meta Data\)</span>

<img src="img\Araprojeslayt2.png" width=500px />

<span style="color:#FFFFFF">Retrieving Content Of Sites</span>

<span style="color:#0066CC"> The "beautifulsoup" library developed in Python language was used to pull the content in the tags.\.</span>

<img src="img\Araprojeslayt3.png" width=484px />

<span style="color:#FFFFFF">Steeming Contents</span>

<span style="color:#0066CC">Punctuation marks have been deleted\.</span>

<img src="img\Araprojeslayt4.png" width=326px />

<span style="color:#0066CC">Turkish letters have been translated into English letter equivalents.\.</span>

<img src="img\Araprojeslayt5.png" width=500px />

<span style="color:#0066CC">Stopwords \ (conjunction \, preposition \, pronoun \. \. \. \) Has been deleted\.</span>

<img src="img\Araprojeslayt6.png" width=232px />

<span style="color:#0066CC">Characters other than English letters have been deleted\.</span>

<img src="img\Araprojeslayt7.png" width=303px />

<span style="color:#FFFFFF">Generating Training Model</span>

* <span style="color:#0066CC">While creating our model, the "keras" library developed in the Python language was used.\. Our Model consists of three layers\. These layers:</span>
  * <span style="color:#0066CC">Embedding</span>
  * <span style="color:#0066CC">GRU</span>
  * <span style="color:#0066CC">Dense</span>

<img src="img\Araprojeslayt8.png" width=443px />

<span style="color:#2A6099">In the embedding layer, each word has been translated into 100 dimensional vectors</span> \.

<span style="color:#FFFFFF">Modelin Oluşturulması</span>

<img src="img\Araprojeslayt9.png" width=500px />

<span style="color:#FFFFFF">Add-onn</span>

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

