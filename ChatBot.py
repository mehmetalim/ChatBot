
from nltk.chat.util import Chat, reflections
print("Merhaba ben Chat bot, size nasıl yardımcı olabilirim?")

ciftler = [

    ["Benim adım (.*)", ["Merhaba %1, nasılsın?"]],
    ['(merhaba|selam|hey)', ['Merhaba']],
    ["Selamunaleyküm", ["Aleykümselam"]],
    ["(nasılsın|Merhaba nasılsın chatbot| nasılsın chatbot)", ["İyiyim sen nasılsın"]],
    ["İyiyim", ["Senin adına çok sevindim, sana nasıl yardımcı olabilirim"]],
    ["(Yaşın kaç?|Kaç yaşındasın)", ["Yaşım yok, 2022 yılında ütretildim"]],
    ["(Adın ne|Senin adın ne|İsmin ne|İsminiz nedir)",["Benim adım ChatBot"]],

    ["(Sen ne iş yaparsın|Senin görevin ne|Ne yaparsın)",["Seninle sohbet ve sanas hizmet vermek için burdayım"]],
    ["En sevdiğin ünlü kim",["Benim en sevdiğim ünlü Barış Manço,(RIP)"]],
    ["Bana dizi önerir misin|En sevdiğin dizi hangisi",["Keslinlikle GİBİ yi tavsiye ederim,mükemmel :)"]],
    ["Bana müzik önerebilir misin", ["Tabi ki, ne tür müzikler dinlersin"]],
    ["Rap", ["O zaman kesinlikle Eminem ve ya Ceza dinlemelisin"]],
    ['Şuan biraz üzgünüm bana şarkı önerirmisin', ["Bence üzgünsen Müslüm Gürses dinlemelisin"]],
    ["(.*) olabilir", [" %1 türü hakkında pek bilgim yok fakat seni müzik uygulamasına yönlendirebilirim :)"]],


    ["(Hangi takımlısın|Hangi takımı destekliyorsun|Hangi takımı tutuyorsun)",["Sahibim Fenerbahçeli, bense içten içe Galatasaraylıyım"]],
    ["Bana kitap önerebilir misin", ["Tabi ki, eğer roman okumayı seviyorsan Ahmet Hamdi Tanpınarın Saatleri Ayarlama Enstitüsüne bayılacaksın	"]],
    ["Bana film önerebilir misin",["Eğer Nuri Bilge Ceylanın Kış Uykusunu izlemediysen hemen hdfilmcehennemini aç ve izle :))"]],
    ['(.*) hava çok (.*)',['%1 hava %2, bence keyfini çıkarmaya bak']],
    ["Sence en güzel şehir neresidir", ["Bence Bursa en güzel şehir :) Sence neresi?"]],
    ['Bence en güzel şehir (.*)',['Sana katılıyorum, %1 nin yemekleri de güzeldir.', '%1 nın doğası da güzeldir', '%1 in insanları da şahanedir' ]],

    ["(.*)",["Sanırım ne demek istediğinizi tam olarak anlamadım, lütfen tekrarlayabilir misiniz?"]]
   # ['(memleketin neresi|nerelisin|)', ['İstanbul, Türkiye']],

]
yansimalar={
    'merhaba': 'merhaba, nasılsın',
    'gittim':'gittin',
    'Selamünaleyküm':'Aleykümselam'
}

chat = Chat(ciftler, yansimalar)
chat.converse(quit='bitti')
