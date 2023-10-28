# Wikipedia'dan Günlük Tweetler Oluşturma

Bu proje, Wikipedia'nın güncellemelerini alır ve Twitter üzerinde paylaşmak için kullanır. Aşağıda kodun nasıl çalıştığını ve nasıl yapılandırılacağını bulabilirsiniz.

## Adımlar

1. **Gerekli Kütüphaneleri İndirme:**

   İlk adım olarak, aşağıdaki Python kütüphanelerini projenize dahil edin. Bu kütüphaneler, veri çekme, Twitter'a tweet gönderme ve veri işleme işlemleri için gereklidir.

   - `os`: Dosya işlemleri ve çevre değişkenlerine erişim için kullanılır.
   - `time`: Zaman gecikmeleri için kullanılır.
   - `datetime`: Tarih ve saat işlemleri için kullanılır.
   - `requests`: HTTP istekleri yapmak için kullanılır.
   - `html`: HTML etiketlerini temizlemek için kullanılır.
   - `bs4` (Beautiful Soup): HTML belgelerini analiz etmek ve içeriklerini çıkarmak için kullanılır.
   - `requests_oauthlib`: OAuth kimlik doğrulama ile Twitter API ile iletişim kurmak için kullanılır.

2. **Sabitlerin Tanımlanması:**

   Proje için kullanılan sabit değerleri belirleyin. Bu sabitler şunlardır:

   - `WIKIPEDIA_URL`: Wikipedia'dan veri çekmek için kullanılan URL.
   - `TWITTER_API_URL`: Twitter API'sine gönderilecek isteklerin yapıldığı URL.
   - `WAIT_INTERVAL`: Her tweet arasındaki bekleme süresi (saniye cinsinden).
   - `TD_ELEMENT_ID`: Wikipedia sayfasındaki güncellemeleri içeren `td` elementinin ID'si.

3. **Twitter API Kimlik Doğrulaması:**

   Twitter API ile iletişim kurabilmek için kimlik doğrulaması yapmanız gerekir. Aşağıdaki bilgileri sağlayarak kimlik doğrulaması yapın:

   - `consumer_key`: Twitter API tüketici anahtarı.
   - `consumer_secret`: Twitter API tüketici sırrı.
   - `access_token`: Twitter API erişim anahtarı.
   - `access_token_secret`: Twitter API erişim sırrı.

4. **Bugünkü Tarihi Alın ve Hashtag Oluşturun:**

   Kod, bugünkü tarihi alır ve Türkçe tarih formatında bir hashtag oluşturur.

5. **HTML Etiketlerini Temizleme İşlevi Oluşturun:**

   `strip_tags` adlı bir işlev tanımlanır. Bu işlev, HTML etiketlerini temizler ve içeriği düz metin haline getirir.

6. **Wikipedia Verilerini Çekme:**

   `get_wikipedia_data` işlevi, Wikipedia'dan verileri çeker. Bu işlev, Wikipedia sayfasındaki güncellemeleri alır ve temizler.

7. **Tweet Gönderme İşlevi Oluşturun:**

   `post_tweet` adlı işlev, belirtilen tweet metnini Twitter'a gönderir. Tweet gönderme işlevi, Twitter API ile iletişim kurar ve gönderilen tweetin durumunu kontrol eder.

8. **Ana İşlevi Oluşturun:**

   Ana işlev olan `main` işlevi, Wikipedia verilerini alır, tweetler oluşturur ve Twitter'a gönderir. Belirtilen bekleme süresi ile her tweet arasında bir gecikme sağlar.

9. **Kodu Çalıştırın:**

   Kodu çalıştırmak için, `if __name__ == '__main__':` bloğunu kullanarak `main` işlevini çağırın. Bu, kodun otomatik olarak çalıştırılmasını sağlar.

## Kullanım

Bu proje, günlük güncellemeleri otomatik olarak almak ve Twitter üzerinde paylaşmak için kullanılabilir. Kullanmadan önce, Twitter API kimlik bilgilerinizi ve diğer gereksinimlerinizi yapılandırmanız gerekecektir. Projeyi çalıştırmak için aşağıdaki adımları takip edin:

1. Gerekli kütüphaneleri yükleyin:

   ```bash
   pip install requests beautifulsoup4 requests_oauthlib
   ```

2. Twitter API kimlik bilgilerinizi belirleyin:

   - `CONSUMER_KEY`
   - `CONSUMER_SECRET`
   - `ACCESS_TOKEN`
   - `ACCESS_TOKEN_SECRET`

3. Kodu çalıştırın:

   ```bash
   python main.py
   ```

Kod, Wikipedia'dan güncellemeleri alacak ve belirtilen bekleme süresi ile Twitter üzerinde paylaşacaktır.

## Lisans

Bu proje, MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına başvurun.
