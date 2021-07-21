# jarvis
* สร้าง ai ตอบโต้ตอบจากเสียงพูด
pip install SpeechRecognition
pip install gTTS
pip install playsound

***
ต้องติดตั้ง pyAudio ด้วยคำสั่งนี้ ดาวนโหลด
python library ที่
Unofficial Windows Binaries for Python Extension Packages
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

For win 32 bit:
pip install PyAudio‑0.2.11‑cp37‑cp37m‑win32.whl

For win 64 bit:
pip install PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl

*cp38 คือ python compile 3.8 เลือก pyAudio ให้ตรงกับ python ที่ใช้งานอยู่
PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl
PyAudio‑0.2.11‑cp39‑cp39‑win32.whl

-ใช้งาน ต้องรอสัญญานเสียงแรกหยุดก่อน แล้วพูดใส่ mic จะได้ยินสัญญานเสียงอีกครั้ง jarvis ควรจะพูดออกมา

-whl คือ การzip ไฟล์ของ python คล้าย zip ของวินโดว์
ref: https://python3.wannaphong.com/2015/01/install-egg-whl-python.html

เช่นติตตั้งโมดูล
pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl

