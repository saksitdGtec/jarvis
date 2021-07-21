import speech_recognition as sr
from gtts import gTTS, lang
from playsound import playsound
from datetime import datetime

r = sr.Recognizer()   

with sr.Microphone() as source:
    playsound("signal.mp3")
    audio= r.record(source, duration=6)
    playsound("signal.mp3")
    
    try:
        text= r.recognize_google(audio, language="th")
        if "ผม" in text:
            text=text.replace("ผม", "ฉัน")
        if "ครับ" in text:
            text=text.replace("ครับ", "ค่ะ")    
            
        if text == "กี่โมงแล้ว":
            now = datetime.now()
            text = now.strftime("ขณะนี้เวลา%Hนาฬิกา%Mนาที%Sวินาที")  
            
        if text == "วันนี้เป็นยังไงบ้าง":
            text="วันนี้ สบายดีค่ะ"
            # if "ห้า" in text:
            #     text="2 * 5 = 25  " + str(2*5)            
        
    except:
        text = "ขอโทษค่ะ"
        
    
        
    tts = gTTS(text,lang="th")        
    tts.save("answer.mp3")
    playsound("answer.mp3")
    
   

