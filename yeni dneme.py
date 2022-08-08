import cv2
path=r'C:\Users\melik\Desktop\sincap.png'
image=cv2.imread(path)
window_name='image'
cv2.imshow(window_name,image)
cv2.waitKey(0)
