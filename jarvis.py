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
        
    except:
        text = "ขอโทษค่ะ"
        
    
        
    tts = gTTS(text,lang="th")        
    tts.save("answer.mp3")
    playsound("answer.mp3")
    
   

