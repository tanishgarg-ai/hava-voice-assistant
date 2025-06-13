import os
import urllib.request
import zipfile

url = "https://alphacephei.com/vosk/models/vosk-model-en-in-0.5.zip"
output_path = "vosk-model-en-in-0.5.zip"

print("Downloading model... (1 GB)")
urllib.request.urlretrieve(url, output_path)
print("Download complete. Extracting...")

with zipfile.ZipFile(output_path, 'r') as zip_ref:
    zip_ref.extractall(".")

print("Model ready.")