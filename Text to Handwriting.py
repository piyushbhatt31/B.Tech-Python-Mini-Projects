import pywhatkit
print("<<<----------- Text to Handwriting ---------->>>")
a=input("Enter Text : ")
pywhatkit.text_to_handwriting(a, rgb=(0, 0, 255))
print("Saved!")