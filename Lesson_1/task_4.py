# 1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

choco_n = int(input("Введите ширину шоколадки: "))
choco_m = int(input("Введите длинну шоколадки: "))
choco_k = int(input("Сколько долек будут брать: "))
if choco_k < choco_n * choco_m and \
        ((choco_k % choco_n == 0) or (choco_k % choco_m == 0)):
    print("Ломай шоколадку смело!")
else:
    print("Сегодня без сладкого!")