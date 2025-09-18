# import json

# with open("date.json", 'r') as file:
# 	date = json.load(file)


# for item in date[person]:
# 	print(item)


# d1 = str(datetime.now())
# print(d1[0:-7])

# d2 = 'efwfefw'

# print(d2[1:4])
# from decimal import *

# x = Decimal("0.128456789")
# x = x.quantize(Decimal('1.00'), ROUND_HALF_EVEN)

# print(x)
# class bild:
# 	def __init__(self, name, year):
# 		self.name = name
# 		self.year = year

	
# 	def drop(self):
# 		print(f'{self.name} {self.year}')

# class school(bild):
# 	def m(self):
# 		super().drop()

# 	def drop(self):
# 		print("eee")

# s = school("moscow", "15")


# s.m()
# s.drop()

# res = (lambda a, b: a if a > b else b)
# print(res(12,13))

# def ff(func):
# 	def wrapper():
# 		print(123)
# 		func()
# 	return wrapper

# @ff
# def n():
# 	print(123)

# n()
from random import *

import random

def main():
	letters = "QWERTYUIOPASDFGHJKLZXCVBNM "  # Алфавит (включая пробел)
	letters_key = []

	# Создание ключа путем случайного перемешивания букв алфавита
	letters_key = list(letters)
	random.shuffle(letters_key)  # Перемешиваем для создания ключа

	print(f"Ключ для шифрования: {''.join(letters_key)}")

	# Зашифровка текста
	word = "hello world"
	word_key_list = []
	for i in range(len(word)):
		letter = word[i].upper()
		if letter in letters:
			list_index = letters.index(letter)
			word_key_list.append(letters_key[list_index])
		else:
			word_key_list.append(letter)

	word_key = ''.join(word_key_list)
	print(f"Зашифрованное слово: {word_key.lower()}")

	# Расшифровка текста
	decoded_word = []
	for i in range(len(word_key)):
		letter = word_key[i].upper()
		if letter in letters_key:
			list_index = letters_key.index(letter)
			decoded_word.append(letters[list_index])
		else:
			decoded_word.append(letter)

	word_stok = ''.join(decoded_word)
	print(f"Расшифрованное слово: {word_stok.lower()}")

main()











































