# Задача 7. Вариант 14.
# Разработайте систему начисления очков для задачи 6, в соответствии 
# с которой игрок получал бы большее количество баллов за меньшее количество попыток.
# 23.03.2017
import random,string
cityes =  ["Заяц","Мишка","Тигр",]
rightAnswer = random.choice(cityes)
money = 10000
answer = ""
print("Программа загадывает название одного из трех символов СОЧИ 2014")
print ('(Заяц или Мишка или Тигр)')
print("Чем меньше попыток вы используете, тем больше баллов вы заработаете.\n")
while answer != rightAnswer:
	answer = input("Назовите один из символов олимпиады в СОЧИ 2014 --------> ")
	if answer == rightAnswer:
		print("\nВсе верно!")
		print("Вам начислено", money,"баллов.")

	else:
		money-=1000
		print("\nВы не угадали!!!\nПопробуйте еще раз\n\n")
input("\n\nНажмите Enter для выхода")