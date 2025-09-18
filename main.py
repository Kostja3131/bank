import sys
import pygame
from settings import * 



def run_game():
	pygame.init()#нужно чтобы работало
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) #отображает окно 
	pygame.display.set_caption("Alien Invasion")

	while True:
		for event in pygame.event.get():
			screen.fill(ai_settings.bg_color)
			if event.type == pygame.QUIT:
				sys.exit()

        # Update the screen (redraw)
		pygame.display.flip()


run_game()


























# with open('file.txt', 'r') as file:  # Открываем файл для чтения
#     lines = file.readlines()  # Считываем все строки файла
#     space = ""  # Переменная для хранения итогового результата
#     for line in lines:
#         space += line.strip()  # Удаляем пробелы и добавляем строку к space
    
#     if "291006" in space:
#     	print("yes")
#     else:
#     	print("no")
#     print(len(space))

# with open("write.txt", 'w') as file:
# 	file.write("emneje\n")
# 	file.write("jfngejrg\n")

# with open("write.txt", 'w') as file:
# 	file.write("em\n")
# 	file.write("ngg\n")

# with open("write.txt", 'a') as file:
# 	file.write("emneje\n")
# 	file.write("jfngejrg\n")


# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print("crahs")


# def main():
# 	print("пошел нахуй!")

# def tihon_playboy():
# 	print("тишка иди нахуй")

# def tihon_huesos():
# 	print("hello world how are youx")




















