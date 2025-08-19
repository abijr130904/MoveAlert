
```
# Motion Alarm Sensor via HP Camera

## Deskripsi
Proyek ini menggunakan kamera HP sebagai webcam untuk mendeteksi gerakan orang atau objek. Sistem akan memutar alarm suara saat gerakan terdeteksi dan otomatis berhenti jika tidak ada gerakan. Cocok untuk monitoring rumah atau ruangan tanpa hardware tambahan.

## Fitur
- Deteksi gerakan menggunakan kamera HP.
- Alarm suara otomatis saat ada gerakan.
- Alarm otomatis berhenti jika tidak ada gerakan.
- Sensitif terhadap objek jauh maupun dekat.
- Tampilan bounding box pada objek yang bergerak.

## Persyaratan
- Python 3.x
- Paket Python:
  - opencv-python
  - numpy
  - pygame
- HP Android dengan aplikasi [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam)

## Instalasi dan setup scrip 

- Sesuaikan IP webcam diHP.Buka file main.py ganti di bagian code 
  [CAMERA_URL = "http://192.168.1.4:8080/video"]
- instal dependency yang dibutuhkan cuku ketikkan perintah : pip install -r requirements.txt
- Jalankan scrip denga perintah bash : python main.py



