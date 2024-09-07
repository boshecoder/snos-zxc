import requests
import random
from gen_names import belarus_last_names, russia_last_names, ukraine_last_names, ukrainian_male_names, belarusian_male_names, russian_male_names, russian_female_names, belarusian_female_names, ukrainian_female_names, email_domains, nums
from texts import get

key = "59f882c22c9d456183694a05832d0afa"

def gen_en(user, link):
	gender = random.randint(1, 2)
	country = random.randint(1, 3)
	if gender == 1:
		if country == 1:
			name = random.choice(belarusian_male_names)
			last_name = random.choice(belarus_last_names)
		elif country == 2:
			name = random.choice(russian_male_names)
			last_name = random.choice(russia_last_names)
		elif country == 3:
			name = random.choice(ukrainian_male_names)
			last_name = random.choice(ukraine_last_names)
	elif gender == 2:
		if country == 1:
			name = random.choice(belarusian_female_names)
			last_name = random.choice(belarus_last_names)
		elif country == 2:
			name = random.choice(russian_female_names)
			last_name = random.choice(russia_last_names)
		elif country == 3:
			name = random.choice(ukrainian_female_names)
			last_name = random.choice(ukraine_last_names)
		last_name += "a"
	order = random.randint(1, 2)
	if order == 1:
		full_name = name + last_name
	elif order == 2:
		full_name = last_name + name
	if random.randint(1, 2) == 2:
		full_name = full_name.lower()
	while True:
		domain = random.choice(email_domains)
		if "ru" in domain and country == 3:
			pass
		elif "de" in domain and country == 2 or country == 1:
			pass
		else:
			break
	email = f"{full_name}@{domain}"
	
	isak = []
	if country == 1:
		pass
	if country == 2:
		pass
	if country == 3:
		pass
	number = random.choice(nums)
	text = get(user, link)
	return {"email": email, "number": number, "text": text}


#import os
#import threading
#osel = []
#i = 0
#url = "https://api.api-ninjas.com/v1/validatephone?number="
#headers = {'X-Api-Key': "FUC+stCkzSkjYk61fiosnQ==3p1macMX6uOpFZ2c"
#}
#def dohua():
#	global i, osel
#	while i <= 250:
#		try:
#			country = 1 #random.randint(1, 3)
#			if country == 1:
#				number = "375" + str(random.randint(100000000, 999999999))
#			elif country == 2:
#				number = "7" + str(random.randint(1000000000, 9999999999))
#			elif country == 3:
#				number = "380" + str(random.randint(100000000, 999999999))
#			print(number)
#			data = str(requests.get(url + number, headers=headers).text).replace("true", "True").replace("false", "False")
#			data = eval(data)
#			if data['is_valid'] == True:
#				print("True")
#				osel.append(number)
#				i += 1
#		except:
#			pass
#treads = []
#for _ in range(10):
#	treads.append(threading.Thread(target=dohua))
#for tread in treads:
#	tread.start()
#for tread in treads:
#	tread.join()

#os.system("clear")
#with open(f"isak_br_{random.randint(10000, 99999)}.txt", "w+") as f:
#	f.write(str(osel))
#print(osel)