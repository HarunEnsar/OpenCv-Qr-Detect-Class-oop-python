import cv2
from pyzbar.pyzbar import decode
global datas
class QrDetect:
    def __init__(self, img):
        self.img=img

    def qr(self):
        decoded_objects = decode(self.img)
        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            datas=data
        print(datas)
        return datas


#resim=cv2.imread("Yes.png")
#qrFind=QrDetect(resim)
#qrFind.qr()

