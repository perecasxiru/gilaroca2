import os
import shutil

os.remove('index.html')
try:
    shutil.copy("C:\\Users\\perec\\AppData\\Roaming\\gsak\\html\\stats1.html", "index.html")

except:
    print(e)
    a = input("Error, ha fallat <ENTER> per acabar")
