import pywhatkit
import cv2
print("<<<----------- Text to Handwriting ---------->>>")
a=input("Enter Text : ")
pywhatkit.text_to_handwriting(a, rgb=(0, 0, 255), save_to="abc.png")
img=cv2.imread("abc.png")
cv2.imshow("Converted",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
