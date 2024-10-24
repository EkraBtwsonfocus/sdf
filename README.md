place_list = int(input("Введите место в списке поступающих: ")) 
if place_list > 10: 
    print("К сожалению, вы не поступили.")  
elif place_list > 0 and place_list < 10: 
    scores = int(input("Введите количество баллов за экзамены: ")) 
    print("Поздравляем, Вы поступили!") 
    if scores >= 290: 
        print("Бонусом Вам будет начисляться стипендия") 
    else: 
        print("Но Вам не хватило баллов для стипендии")


x = int(input('Сколько денег вы хотите положить в банк? ')) 
p = int(input('Введите процент: ')) 
y = int(input('Какую сумму вы хотите получить?')) 
year = 1 

while x < y: 
  print(year, ' год') 
  year += 1 
  x = x * p/ 100 + x 
  print(int(x))
