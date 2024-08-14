import os
import cv2
import re
import xml.etree.ElementTree as ET

# Path folder dataset
annotations_dir = '../STERIL-yang-n-nya-PascalVOC-export/Annotations'
images_dir = '../STERIL-yang-n-nya-PascalVOC-export/JPEGImages'
output_dir = 'saved'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Ambil dan urutkan semua file .jpg dan .jpeg
def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else 0

# Ambil dan urutkan semua file .jpg dan .jpeg secara numeris
files_gambar = sorted([f for f in os.listdir(images_dir) if f.endswith('.png') or f.endswith('.jpeg')],
               key=extract_number)

# Ambil dan urutkan file anotasinya
files_anotasi = sorted([f for f in os.listdir(annotations_dir) if f.endswith('.xml') ],
               key=extract_number)

print(files_gambar)
print(files_anotasi)

# # Parsing file XML
# tree = ET.parse("../p xml/STERIL-PascalVOC-export/Annotations/image(1).xml")
# root = tree.getroot()

# List untuk menyimpan objek
objects = []

# Loop melalui semua file
for i in range(len(files_anotasi)):
    # Mengambil gambar
    filename_gambar = files_gambar[i]
    img_path = os.path.join(images_dir, filename_gambar)
    img = cv2.imread(img_path)
    
    # Cek apakah gambar berhasil dibaca
    if img is None:
        print(f"Error: Gambar {filename_gambar} tidak dapat dibaca.")
        continue
    
    # Mengambil file XML yang sesuai
    filename_anotasi = files_anotasi[i]
    xml_path = os.path.join(annotations_dir, filename_anotasi)
    
    # Parsing file XML
    tree = ET.parse(xml_path)
    root = tree.getroot()

    objects = []  # List untuk menyimpan objek

  # Ambil semua objek dari file XML
    for idx, member in enumerate(root.findall('object')):
        name = member.find('name').text
        bndbox = member.find('bndbox')
        xmin = int(float(bndbox.find('xmin').text))
        ymin = int(float(bndbox.find('ymin').text))
        xmax = int(float(bndbox.find('xmax').text))
        ymax = int(float(bndbox.find('ymax').text))

        # Crop dan simpan objek sebagai gambar baru
        crop_img = img[ymin:ymax, xmin:xmax]
        output_filename = f"{name}_{filename_gambar.split('.')[0]}_{idx+1}.jpg"
        output_path = os.path.join(output_dir, output_filename)
        cv2.imwrite(output_path, crop_img)
        
        # Simpan informasi objek dalam dictionary
        obj_info = {
            'name': name,
            'xmin': xmin,
            'ymin': ymin,
            'xmax': xmax,
            'ymax': ymax
        }
        
        # Tambahkan ke list objek
        objects.append(obj_info)

    # Cetak semua objek yang ditemukan
    for j, obj in enumerate(objects):
        print(f"Objek {j+1}:")
        print(f"  Nama: {obj['name']}")
        print(f"  Bounding Box: ({obj['xmin']}, {obj['ymin']}), ({obj['xmax']}, {obj['ymax']})")




