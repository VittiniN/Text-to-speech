import requests
import random
from gtts import gTTS
import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup
import re

response = requests.get("https://readtheplaque.com/static/plaques.geojson")

if response.status_code == 200:
    data = response.json()['features']
    valid_plaques = [plaque['properties']['description'] for plaque in data if 'description' in plaque['properties'] and plaque['properties']['description'].strip()]

    if not valid_plaques:
        print("No valid descriptions found.")
    else:
        random_plaque = random.choice(valid_plaques)
        soup = BeautifulSoup(random_plaque, 'html.parser')
        cleaned_text = ' '.join(soup.stripped_strings)

        cleaned_text = re.sub(r'<.*?>', '', cleaned_text)

        print(cleaned_text)
else:
    print('Error:', response.status_code)


def speak_text(description):
    tts = gTTS(description, lang="en")
    tts.save("description.mp3")
    messagebox.showinfo("Description Spoken", "Description has been spoken and saved as description.mp3")

app = tk.Tk()
app.title("Read the Plaque Project")

speak_button = tk.Button(app, text="Speak", command=lambda: speak_text(cleaned_text))
speak_button.pack()

text_box = tk.Text(app)
text_box.insert("1.0", cleaned_text)  # Display the description in the text box
text_box.pack()

app.mainloop()

# response = requests.get("abc") # this is me making the call to get the apo
# if response.status_code == 200:
#data = response.json()['features']

