import cv2
import qrDetect

class Cam:

    def __init__(self,camPort):
        self.camPort=camPort

    def openCam(self):
        cap = cv2.VideoCapture(self.camPort)
        if cap.isOpened():
            print("Kamera açıldı")
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Görüntü alınamadı")
                    break
                else:
                    print("Görüntü Alınıyor")
                    try:
                        qrFind=qrDetect.QrDetect(frame)
                        qrFind.qr()

                    except:
                        print("Qr Verisi Alınamıyor")

                    cv2.imshow("Cam", frame)

                if cv2.waitKey(1) == ord('q'):
                    qrdata = qrFind.qr()
                    print("Alınan Qr verisi",qrdata)
                    break
        else:
            print("Kamera açılmadı!!!")

        cap.release()
        return qrdata

camera=Cam(0)
camera.openCam()
qrVerisi=camera.openCam()
print("Alınan Qr verisi son", qrVerisi)
cv2.destroyAllWindows()