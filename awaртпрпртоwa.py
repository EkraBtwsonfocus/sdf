x = int(input('Сколько денег вы хотите положить в банк? ')) 
p = int(input('Введите процент: ')) 
y = int(input('Какую сумму вы хотите получить?')) 
year = 1 

while x < y: 
  print(year, ' год') 
  year += 1 
  x = x * p/ 100 + x 
  print(int(x))