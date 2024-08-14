# Pascal-VOC-cropping-image-based-on-bounding-box
ini repository pertama yang ku buat yang benar2 ku bagikan online kodenya. maaf jika repo ini jika tidak berguna untuk proyek mu karena baru pertama kalinya aku juga baru menggunakan github dan aku juga tak semahir itu juga dalam kode pemograman😊


Kode ini di buat menggunakan ChatGPT namun telah ku optimalkan agar tidak error seperti kode yang langsung copy paste dari ChatGPT



---
## Bagaimana cara menggunakannya?
1. Ubah nama file gambar menjadi hanya berisi satu angka seperti ini:
![image](https://github.com/FikriAnwari/Pascal-VOC-cropping-image-based-on-bounding-box/blob/main/documentations-img/img%201.png)
Nama file gambar seperti di bawah ini **dilarang** karena mengandung lebih dari satu angka secara terpisah:
![image2](https://github.com/FikriAnwari/Pascal-VOC-cropping-image-based-on-bounding-box/blob/main/documentations-img/img%204.png)

2. Ubah nama file anotasi(Pascal VOC) menjadi sama dengan nama file gambar nya
![imagexml](https://github.com/FikriAnwari/Pascal-VOC-cropping-image-based-on-bounding-box/blob/main/documentations-img/img%202.png)

3. Ekstrak kode dari file .zip jika kamu mengunduh repo ini sehingga terlihat seperti ini:
![image3](https://github.com/FikriAnwari/Pascal-VOC-cropping-image-based-on-bounding-box/blob/main/documentations-img/img%203.png)


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
