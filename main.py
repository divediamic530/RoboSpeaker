from gtts import gTTS
import os
import playsound
x = input("Enter what you want to speak: ")
sound = gTTS(x, lang="en")
sound.save("welcome.mp3")
os.system("welcome.mp3")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
