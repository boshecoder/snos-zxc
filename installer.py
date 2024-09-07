import os

print("Установка")
for i in ["fake_useragent", "requests", "pystyle", "art"]:
	os.system(f"pip install {i}")
print("Установлено")