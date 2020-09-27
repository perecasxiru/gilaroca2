import os
import shutil

os.remove('index.html')
src_files = os.listdir("comics")
try:
    shutil.copy("C:\\Users\\perec\\AppData\\Roaming\\gsak\\html\\stats1.html", "index.html")

except:
    print(e)
    a = input("Error, ha fallat <ENTER> per acabar")
