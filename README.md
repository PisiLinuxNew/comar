# comar
ÇOMAR (Açılımı: COnfiguration MAnageR), dizgenin düzgün çalışması için gerekli olan donanım, açılış, ağ, kullanıcı, zaman, görüntü gibi ayarların mümkün olduğu kadar kendiliğinden yapılmasını sağlayan, kullanıcılara bir yetki denetiminde bu ayarları bayağı ve anlaşılır bir biçimde değiştirme olanağı sağlayan bir yazılımdır.

Giriş

Bu belge, Ulusal Dağıtım'ın yapılandırma yönetim sistemi olan ÇOMAR'ın, ne amaçla geliştirildiğini, hangi sorunlara çözüm getirdiğini, yapısını ve bileşenlerini anlatır. Hedef kitlesi, ÇOMAR'ı yakından tanımak isteyen kullanıcılar ve sistem yöneticileridir. Bilişim okuryazarı seviyesine göre yazılmış olmakla birlikte, bazı tartışmaları takip edebilmek için, bir işletim sisteminin bileşenleri, ve uygulamaların nasıl ayarlandığı gibi sistem yönetimi konularında bilgi sahibi olmak gerekebilir.

Sorun
Çeşitli uygulamalar bir sistem içinde bir araya getirildiklerinde, birbirleriyle uyumlu çalışabilmeleri için ayarlanmaları gerekmektedir. Kurulan bir uygulamanın masaüstü menüsüne eklenmesi, açabildiği dosya tiplerini sisteme bildirmesi, yeni kurulan bir spam (istenmeyen eposta) filtreleyicinin mevcut eposta sunucusuna bağlanması gibi çok sayıda entegrasyon işlemi bulunmaktadır. Kullanıcı, bu ayarları yapabilmek için, kendi yapmak istediği işin dışındaki teknik konularda bilgi kazanmak zorunda kalmakta ve zaman kaybetmektedir.

Belgeler

Özgür yazılım camiası, bu işleri kolaylaştırmak için nasıl (ing. howto) belgeleri adıyla çeşitli belgeler hazırlamıştır. Bunlar bir işi yapabilmek için neler yapılması gerektiğini adım adım anlatan kısa belgelerdir. Kullanıcıların belge okumak istememeleri ve belgelerin kısıtlı sayıda senaryoyu kapsaması yüzünden faydalı olamamaktadırlar. Burda aklımıza, madem bir işi adım adım belgeleyebiliyoruz, bunu bir program haline getirip otomatik olarak yapılmasını sağlayamaz mıyız? sorusu gelmektedir. Bu yapılabilirse, kullanıcının zaman tasarrufu yanında, bu belgelerin çeşitli dillere tercüme edilmesi gibi işler de gereksiz hale gelecektir.

Diğer Linux Dağıtımları

Linux dağıtımları gelişme süreçleri içerisinde bu tür entegrasyon problemleri ile karşılaştıkça bunlara ayrı ayrı çözümler üretip kendi sistemlerine (özellikle paket yönetici yazılımlarının içine) dahil etmişlerdir. Bu çözümler, kurulu uygulamalar (menü), fontlar, açılış işlemleri (initscripts) gibi tek tek alt sistemler bazındadır. Genellikle, uygulama paketleri, dosya sistemi üzerinde sabit bir dizine, söz konusu alt sisteme neler sağladıklarını kaydetmekte; bu alt sistemi kullanacak uygulamalar ise, buraya önceden belirlenmiş biçimde kaydedilen dosyaları tarayarak, sağlanan hizmetleri bulmaktadır. Uygulamaların entegrasyonu için, ya uygulamalar buradaki standartları bilecek biçimde değiştirilmekte, ya da gerekli çevrimi yapacak üçüncü bir yönetici uygulama araya sokulmaktadır. Kayıt ve çevrim işlemleri için özel veri biçimleri, kabuk, Perl ya da Python betikleri, bazen de bunların bir karışımı kullanılmaktadır.
Bir de uygulama kurulur, kaldırılır ve güncellenirken çalışan özel betikler bulunmaktadır. Bunlarla güncelleme sırasında eski ayarların taşınması gibi işler yapılmaktadır. Bazı sistemler (örneğin Debian'ın debconf'u) kurulum anında bu betiklerin kullanıcıya soru sorabilmeleri ve uygulamayı cevaplara göre ayarlamalarını sağlamaktadır.
