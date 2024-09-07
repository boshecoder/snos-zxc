ukrainian_male_names = [
    "Oleksandr", "Andriy", "Vadim", "Vasyl", "Viktor", "Volodymyr", "Dmytro", "Ivan", "Mykhailo", "Serhiy", "Yuriy"
]

ukrainian_female_names = [
    "Anna", "Halyna", "Irina", "Kateryna", "Nataliia", "Olha", "Tetiana"
]

russian_male_names = [
    "Aleksandr", "Aleksey", "Andrey", "Anton", "Artem", "Vadim", "Vasiliy", "Viktor", "Vladimir", "Vyacheslav", 
    "Daniil", "Dmitriy", "Evgeniy", "Egor", "Ivan", "Ilya", "Kirill", "Konstantin", "Maksim", "Mikhail", 
    "Nikolai", "Oleg", "Pavel", "Roman", "Sergey", "Stanislav", "Stepan", "Timofey", "Yuriy", "Yaroslav"
]

russian_female_names = [
    "Anna", "Valentina", "Vera", "Viktoriya", "Ekaterina", "Elena", "Irina", "Kseniya", "Lyubov", "Mariya", 
    "Marina", "Nadezhda", "Olga", "Svetlana", "Tatyana"
]

belarusian_male_names = [
    "Alyaksandr", "Aleg", "Andrey", "Vadzim", "Vasil", "Viktor", "Dzmitry", "Ivan", "Mikhaіl", "Syargey", "Yauhen"
]

belarusian_female_names = [
    "Alena", "Volha", "Iryna", "Natalla", "Svyatlana", "Tatsiana"
]

ukraine_last_names = [
    "Ivanov", "Petrov", "Sidorov", "Kuznetsov", "Smirnov", "Popov", "Sokolov", "Vasiliev", "Pavlov", "Kozlov",
    "Shevchenko", "Kravchenko", "Kovalenko", "Dmytrenko", "Bondarenko", "Kostenko", "Melnyk", "Grishchenko", "Mishchenko", "Zaychenko", 
    "Yakovlev", "Andreev", "Bogdanov", "Kirillov", "Fedorov", "Nikitin", "Semenov", "Kolesnikov", "Golubev", "Stepanov",
    "Tkachenko", "Chernenko", "Yaremchuk", "Vasylyuk", "Kononenko", "Marchenko", "Ovcharuk", "Hrytsenko", "Lytvyn", "Korniyenko"
]

russia_last_names = [
    "Ivanov", "Smirnov", "Kuznetsov", "Popov", "Sokolov", "Vasiliev", "Petrov", "Pavlov", "Kozlov", "Volkov",
    "Sidorov", "Novikov", "Fedorov", "Nikitin", "Borisov", "Stepanov", "Kiselev", "Mikhailov", "Yakovlev", "Andreev",
    "Demidov", "Grigoriev", "Zaitsev", "Yegorov", "Konovalov", "Sergeev", "Kirillov", "Semenov", "Nikolaev", "Kolesnikov", 
    "Belov", "Golovin", "Voronov", "Maksimov", "Martynov", "Dmitriev", "Alexandrov", "Leonov", "Soloviev", "Yuryev"
]

belarus_last_names = [
    "Ivanov", "Sidorov", "Kuznetsov", "Smirnov", "Petrov", "Popov", "Sokolov", "Vasiliev", "Pavlov", "Kozlov",
    "Kravchenko", "Shevchenko", "Kovalenko", "Dmytrenko", "Bondarenko", "Kostenko", "Melnyk", "Grishchenko", "Mishchenko", "Zaychenko", 
    "Yakovlev", "Andreev", "Bogdanov", "Kirillov", "Fedorov", "Nikitin", "Semenov", "Kolesnikov", "Golubev", "Stepanov",
    "Tkachenko", "Chernenko", "Yaremchuk", "Vasylyuk", "Kononenko", "Marchenko", "Ovcharuk", "Hrytsenko", "Lytvyn", "Korniyenko"
]

email_domains = [
    "gmail.com",
    "yahoo.com",
    "hotmail.com",
    "outlook.com",
    "icloud.com",
    "protonmail.com",
    "yandex.ru",
    "mail.ru",
    "aol.com",
    "live.com",
    "gmx.de",
    "zoho.com",
    "fastmail.com",
    "tutanota.com",
    "inbox.com",
    "mail.com",
    "hushmail.com",
    "posteo.de",
    "yandex.com",
    "rambler.ru",
    "bk.ru",
]

nums = []
nums_n = ["ru_n1", "ru_n2", "ru_n3", "ru_n4", "ru_n5", "br_n1"]
for i in nums_n:
	with open(f"{i}.txt", "r") as f:
		nms = eval(f.read())
		for l in nms:
			nums.append(l)

all_last_names = russia_last_names + ukraine_last_names + belarus_last_names
all_male_names = ukrainian_male_names + belarusian_male_names + russian_male_names
all_female_names = ukrainian_female_names + belarusian_female_names + russian_female_names