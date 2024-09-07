
#import installer
from pystyle import Colors as cr
from pystyle import Colorate
import art
import os
import mdl

ch = lambda cr, text: Colorate.Horizontal(cr, text)
t2a = lambda txt: art.text2art(txt)

def banner():
	print(ch(cr.purple_to_blue, t2a("SNOS")))
	print("\n")
	ins = input(ch(cr.blue_to_purple, "Напишите username или ID: "))
	inl = input(ch(cr.blue_to_purple, "Ссылка на нарушение (None - если нету): "))
	return [ins, inl]

while True:
	os.system("clear")
	inn = banner()
	print("\n\n")
	print(ch(cr.green_to_blue, "Запуск...\n\n\n"))
	mdl.tread(mdl.snos_g, inn)