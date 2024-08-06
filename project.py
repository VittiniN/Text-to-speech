# import tkinter as tk #allows you to create GUI graphical user interface 
# from tkinter import filedialog #allows me to create filediloag boxzes allowing me to select files from dierctories ect. 
# from PIL import Image #in this case allows me to open the images 
# import pytesseract
# from gtts import gTTS  #just imported google text to speech recognition
# import os  #allows different set of function to interact with the operating system 

# #step 1 is for me to create a function that allows me to open up a image with text 
# def open_image():
#     file_path = filedialog.askopenfilename() #opening file 
#     if file_path:
#         image = Image.open(file_path)
#         extracted_text = pytesseract.image_to_string(image) #extracting the text from the image
#         text_box.delete(1.0, "end")  # starts at line 1 the end 
#         text_box.insert("end", extracted_text)  # create a box to inset the end of the of start  because we can not use start that means we are inserting new txt 

# # step 2  definning google text to speech 
# def speak_text():
#     text = text_box.get("1.0", "end")
#     tts = gTTS(text, lang="en")
#     tts.save("text.mp3")  #save the audio to your computer 
#     os.system("mpg321 text.mp3")  #mpg321 to  play the audo file , i had to do brew install mpg321 in the terminal
#     os.remove("text.mp3")

# app = tk.Tk()
# app.title("Read the Plaque Project")

# open_button = tk.Button(app, text="Open Image", command=open_image)
# open_button.pack()

# speak_button = tk.Button(app, text="Speak", command=speak_text)
# speak_button.pack()

# text_box = tk.Text(app)
# text_box.pack()

# app.mainloop() # 
