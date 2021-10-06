
import speech_recognition as sr
import random
import playsound
import os
from gtts import gTTS
import webbrowser
import time
from time import ctime
import wikipedia
import re  #regular expression istediğimiz kelimeleri daha iyi çekmek için kullanılacak.
import subprocess #program çalıştırabilmek için gerekli modül

wikipedia.set_lang("tr")

r=sr.Recognizer()

nasilsinlar=["nasılsın","naber","ne haber","nasıl gidiyor"]

adinne={
    "adın ne":
    ["benim adım bot","bana bot diyebilirsin","bana bot derler","basitçe bot"
     
     ]        
    }


def record_audio(ask=""):
    with sr.Microphone() as source:
        
        audio=r.record(source,duration=3) # audio=r.record(source,duration=3) audio=r.listen(source) olarakta yapılabilirdi 
        if(ask):
            speak(ask)
        voice_data =""
        try:
            voice_data=r.recognize_google(audio,language="tr-tr")
            print(voice_data)
        except sr.UnknownValueError:
            print("ne dedigini anlayamadim")
        except sr.RequestError:
            print("sistemsel bir hata var")
        return voice_data

def speak(audio_string):
    tts=gTTS(text=audio_string,lang="tr")
    r=random.randint(1,10000)
    audio_file= "audio" +str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)



def respond(voice_data):
    if "Merhaba" in voice_data:
        speak("merhaba efendim")       
        
    if voice_data in nasilsinlar:
        speak("iyiyim teşekkürler sizlere ömür")

    if "ismin nedir" in voice_data:
        metin = random.choice(adinne["adın ne"])    #variable a karşılık gelen variable kullandık ismin ne aracılığı ile 
        speak(metin)
    if "bahset" in voice_data:               
        a21= re.sub('bahset',' ',voice_data) # bahset kelimesini gördüğünde altta yazanları basitçe okuyor doğal dil işleme ile geliştirilebilir
        print(a21)
        speak ("benim adım bot .") 

    if "kimdir" in voice_data.split():
        voice_data=voice_data.split()
        kisiismi=""
        for i in voice_data[:-1]:
            kisiismi=kisiismi+" "+i
        url="https://www.google.com/search?q="+kisiismi+" kimdir"
        webbrowser.get().open(url)
        wiki=wikipedia.summary(kisiismi,sentences=2)
        speak(wiki)
    

def ara(voice_data):
    if "arama" in voice_data.split():
        voice_data=voice_data.split()
        aranan=""
        for i in voice_data[:-1]:
            aranan=aranan+" "+i
        url="https://www.google.com/search?q="+aranan
        webbrowser.get().open(url) 
def neresi(voice_data):        
    if "nerede" in voice_data.split():
        voice_data=voice_data.split()
        lokasyon=""
        for i in voice_data[:-1]:
            lokasyon=lokasyon+" "+i
        url="https://www.google.com/maps/place/"+lokasyon
        webbrowser.get().open(url)
    if "saat kaç" in voice_data:
        speak(ctime())
    
print("Bu program kaynaklanabilecek ses cızırtıları sebebi ile 5 saniyeliğine dinleme konumundadır . Yani her 5 saniye içerisinde söylediklerinizi duyup anlamlandırdıktan sonra işlemini gerçekleştirecek .")       
print("\n\n\n bu program için mantıklı olan kelimeler \n\n\n")
print("merhaba \n")
print("nasılsın \n")
print("ismin nedir \n")
print("kendinden bahset \n")
print("... kimdir (ünlü birisinin adını söyleyin ve kimdir deyin . Örnek : Atatürk kimdir) \n")
print("... arama (herhangi bir şey söyledikten sonra arama deyin . Örnek : Kitap arama) \n")
print("... nerede (bir yer adı söyleyin sonra nerede deyin.Örnek : Ankara nerede) \n")
print("saat kaç deyin size saatin kaç olduğunu söyleyecek \n")
time.sleep(1)
print("dinleniyor...")
while 1:
    voice_data=record_audio()
    respond(voice_data)
    ara(voice_data)
    neresi(voice_data)



