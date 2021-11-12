from flask import Flask, request, jsonify
from flask_cors import CORS
from time import perf_counter
from PIL import Image
from numpy import array
from svd import *
import io
import base64
import re

app = Flask(__name__)
CORS(app)
# venv\Scripts\activate
# python api.py
@app.route('/compress', methods=['POST', 'GET'])
def compressImage():
    imageURL = request.get_json()
    imageBase64 = imageURL["data"]
    compressionRates = imageURL["rates"]
    if(compressionRates=='low'):
        tingkatKompresi=3
    elif(compressionRates=='med'):
        tingkatKompresi=2
    else:
        tingkatKompresi=1

    mulai=perf_counter()
    metadata=imageBase64.split(",",maxsplit=1)[0]
    content=imageBase64.split(",",maxsplit=1)[1]
    tipe=re.split("[/;]",metadata)[1]
    sebelum_img=Image.open(io.BytesIO(base64.b64decode(content)))
    sebelum_array=array(sebelum_img)
    m=sebelum_array.shape[0]
    n=sebelum_array.shape[1]
    banyakEigen = min(m,n)
    k = 10
    if(sebelum_img.mode=='RGB'):
        setelah_array=kompresiGambarNLayer(sebelum_array,3,k)
        print(1)
        im = finalisasi(setelah_array,tipe)
    elif(sebelum_img.mode=='L'):
        setelah_array=kompresiGambarNLayer(sebelum_array,1,k)
        print(2)
        im = finalisasi(setelah_array,tipe)
    elif(sebelum_img.mode=='RGBA'):
        a=sebelum_array[:,:,3]
        setelah_array=kompresiGambarNLayer(sebelum_array,3,k)
        setelah_array[:,:,3]=a
        setelah_array=pertahankanTransparansi(setelah_array)
        print(3)
        im = finalisasi(setelah_array,tipe)
    elif(sebelum_img.mode=='LA'):
        a=sebelum_array[:,:,1]
        setelah_array=kompresiGambarNLayer(sebelum_array,1,k)
        setelah_array[:,:,1]=a
        setelah_array=pertahankanTransparansi(setelah_array)
        print(4)
        im = finalisasi(setelah_array,tipe)
    else:
        try:
            setelah_array=kompresiGambarNLayer(sebelum_array,sebelum_array.shape[2],k)
            print(5)
            im = finalisasi(setelah_array,tipe)
        except:
            print('Proses gagal !')
            im=''

    selesai=perf_counter()
    lama=selesai-mulai
    lamaWaktu = "{:.2f}".format(lama)
    rasio=100*(k*(m+n)+k)/(m*n)
    rasioGambar="{:.2f}".format(rasio)
    print(f'Waktu pengerjaan : {lamaWaktu} detik')
    print(f'Rasio kompresi : {rasioGambar}%') 
    im = str(im)
    berhasil = "yess"
    if im == '' :
        berhasil = "noo"
    sizeCompres = (len(im) * 3) / 4 - im.count('=', -2)
    im = str(metadata)+','+str(im)    
    return jsonify(
        gambarKompres=str(im),
        waktuKompres=str(lamaWaktu),
        rasioKompres=str(rasioGambar), 
        sizeKompres=str(sizeCompres),
        berhasilKompres=str(berhasil)
    )

if __name__ == '__main__':
    app.run(debug=True)
