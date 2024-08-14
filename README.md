# Pascal-VOC-cropping-image-based-on-bounding-box
ini repository pertama yang ku buat yang benar2 ku bagikan online kodenya. maaf jika repo ini jika tidak berguna untuk proyek mu karena baru pertama kalinya aku juga baru menggunakan github dan aku juga tak semahir itu juga dalam kode pemograman😊


Kode ini di buat menggunakan ChatGPT namun telah ku optimalkan agar tidak error seperti kode yang langsung copy paste dari ChatGPT



---
## Bagaimana cara menggunakannya?
1. Ubah nama file gambar menjadi hanya berisi satu angka seperti ini:
![image](https://drive.google.com/file/d/1tjJ_EA-bSQoS8D3px1UzEJOJAVD5Irvu/view?usp=drive_link)
Nama file gambar seperti di bawah ini di larang karena mengandung lebih dari satu angka secara terpisah:
![image2](https://drive.google.com/file/d/1FRSdldcn8ygtJ4IfuIaGhu4IRX1Kifw6/view?usp=drive_link)

2. Ubah nama file anotasi(Pascal VOC) menjadi sama dengan nama file gambar nya
![imagexml](https://drive.google.com/file/d/1CZ3tBHIbLjnDn1DQHvHSx9W3mSsQhJL6/view?usp=drive_link)

3. Ekstrak kode dari file .zip jika kamu mengunduh repo ini sehingga terlihat seperti ini:
![image3](https://drive.google.com/file/d/1pmOLfJA5gRxdouJ5GF9ouDi5_On48w7Y/view?usp=sharing)


4. Ubah kode pada app.py pada bagian:
```
annotations_dir = '../STERIL-yang-n-nya-PascalVOC-export/Annotations'
images_dir = '../STERIL-yang-n-nya-PascalVOC-export/JPEGImages'
```
menjadi lokasi file gambar yang kamu simpan ke `images_dir` dan lokasi file annotasi dalam bentuk .xml ke `annotations_dir`

5. Karena terkadang file gambar tidak memiliki ekstensi yang sama kau bisa ubah kode pada bagian:
```
files_gambar = sorted([f for f in os.listdir(images_dir) if f.endswith('.png') or f.endswith('.jpeg')],
               key=extract_number)
```
di bagian `if.endswith('.png')` kau bisa ubah menjadi menjadi ekstensi yang sesuai dengan file gambarmu `if.endswith('EKSTENSI_FILE_GAMBAR_KAMU')` jika kau memiliki 2 ekstensi gambar yang berbeda misalnya .jpg, .png kamu bisa mengubahnya seperti ini `if.endswith('.jpg') or f.endswith('.png')` jika punya 3 kau bisa ubah menjadi `if.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg')`

6. Jalankan skrip di terminalmu dengan cara `python app.py`

7. Jika sudah buka folder `saved` yang satu direktori dengan `app.py`

8. Proses selesai semoga kode ini membantu mu😊
