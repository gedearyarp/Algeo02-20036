from re import A
from PIL import Image
from numpy import array,transpose,matmul,zeros,sqrt,add,dot,diag,uint8,ones,abs,outer,divide,zeros_like
from numpy.linalg import norm
import base64
import io

def bagiTiapElemen(a,b):
    #Menerima dua buah vektor berukuran sama dan melakukan pembagian element-wise
    #Bila penyebut 0, akan mengembalikan 0
    return divide(a,b,out=zeros_like(a, dtype=float),where=b!=0)

def eigenDominan(A, toleransi):
    #Mengembalikan nilai eigen dan vektor eigen yang bersesuaian dengan nilai eigen paling besar dari sebuah matriks A
    #Pencarian menggunakan metode power iteration sampai perubahan nilai eigen dibawah batas toleransi atau mencapai 10000 langkah
    m, n = A.shape
    k=min(m,n)
    v = ones(k) / sqrt(k)
    if m > n:
        A = matmul(transpose(A),A)
    elif m < n:
        A = matmul(A,transpose(A))
    
    nilaiEigen = bagiTiapElemen(matmul(A,v),v)[0]
    jumlahIterasi=0
    while( True):
        Av = matmul(A,v)
        vBaru = Av / norm(Av)
        nilaiEigenBaru = (bagiTiapElemen(matmul(A,vBaru),vBaru))[0]
        jumlahIterasi+=1
        if ((abs(nilaiEigen - nilaiEigenBaru) < toleransi) or (jumlahIterasi>=10000)):
            print("dilakukan ",jumlahIterasi," kali iterasi")
            break

        v = vBaru
        nilaiEigen = nilaiEigenBaru

    return nilaiEigenBaru, vBaru

def svd(A, k=None, toleransi=1):
    #Mengembalikan hasil dekomposisi svd berupa matriks u,s,v dari sebuah matriks
    #Elemen u, s, dan v hanya dicari sampai elemen ke k saja untuk menghemat waktu
    #Pencarian u, s, v diawali dengan pencarian vektor dan nilai eigen menggunakan metode power iteration
    A = array(A, dtype=float)
    m, n = A.shape
        
    SVDKeN = []
    if k is None:
        k = min(m, n)

    for i in range(k):
        print("Proses pencarian singular value ke-",i+1)
        salinanA = A.copy()

        for u, nilaiSingular, v in SVDKeN[:i]:
            salinanA -= nilaiSingular * outer(u, v)

        if m > n:
            _, v = eigenDominan(salinanA, toleransi=toleransi)
            uAwal = matmul(A,v)
            sigma = norm(uAwal)  
            u = uAwal / sigma
        else:
            _, u = eigenDominan(salinanA, toleransi=toleransi)
            vAwal = matmul(transpose(A),u)
            sigma = norm(vAwal)  
            v = vAwal / sigma

        SVDKeN.append((u, sigma, v))

    us, S, vs = [array(x) for x in zip(*SVDKeN)]
    return transpose(us), S, vs

def kompresiSVD(arr,k):
  #Menerima sebuah array dan banyaknya singular values yang akan digunakan
  #Mengembalikan hasil kompresi / hasil perkalian u, s, dan v sampai urutan ke-k
  u,s,v=svd(arr,k)
  hasilKompresi=dot(u[:,:k],dot(diag(s[:k]),v[:k,:]))
  return hasilKompresi

def kompresiGambarNLayer(arr,n,k):
  #Menerima sebuah gambar berbentuk array 'arr' yang memiliki n buah channel
  #Mengembalikan gambar berbentuk array n channel yang sudah dikompresi dengan k singular values
  hasil=zeros(arr.shape)
  if(n==1):
    hasil=kompresiSVD(arr,k)
  else:
    for i in range(n):
      print("Mengolah layer ke-",i+1)
      hasil[:,:,i]=kompresiSVD(arr[:,:,i],k)
  return hasil

def pertahankanTransparansi(arr):
  #Menerima sebuah gambar berbentuk array yang mengandung channel transparansi
  #Mengembalikan gamabr berberntuk array setelah di set seluruh channel menjadi 0 bila channel transparansi bernilai 0
  channel=arr.shape[2]
  layerTrpPixel = [0 for x in range(channel)]
  for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
      if arr[i,j,-1]==0:
        arr[i,j,:] = layerTrpPixel
  return arr

def finalisasi(arr,tipe):
  #Menerima sebuah gambar berupa array dan ekstensi yang bersesuaian
  #Memastikan nilai pada array berupa bilangan bulat pada skala yang benar
  #Mengembalikan gambar yang sama namun dalam representasi base64 (string)
  arr=(arr-arr.min())/(arr.max()-arr.min())*255
  im = Image.fromarray(arr.astype(uint8))
  buffered = io.BytesIO()
  im.save(buffered, format=tipe)
  img_str = base64.b64encode(buffered.getvalue())
  return img_str.decode('UTF-8')