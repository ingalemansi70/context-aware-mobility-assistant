import easyocr
import pyttsx3

# Reader ko ek hi baar load karenge
reader = easyocr.Reader(['en'])
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def read_and_speak(cropped_img):
    results = reader.readtext(cropped_img)
    full_text = ""
    for bbox, text, prob in results:
        if prob > 0.5:
            full_text += text + " "
    
    if full_text:
        print(f"Detected Text: {full_text}")
        engine.say(full_text)
        engine.runAndWait()
        return full_text
    else:
        return "No text found"