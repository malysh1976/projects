import random
import time

player={
    'name':'player',
    'hp':50,
    'dmg':1,
}


boss={
    'name':'boss',
    'hp':random.randint(50,100),
    'dmg':1,
}


locate=['мрачный','светлый','старый']
loc=["дом",'лес','особняк']
boss_names=["Ворон","Тень","Темный маг"]
boss['name']=random.choice(boss_names)
player['name']=input('Введите имя вашего игрока: ')


def fight():
    while player['hp']>0 and boss['hp']>0:
        time.sleep(2)
        dam_player=random.randint(15,30)
        boss['hp']-=dam_player
        dam_boss=random.randint(10,30)
        player['hp']-=dam_boss
        if player['hp']>0:
            print(f'Вам нанесли {dam_boss} урона!')
            time.sleep(0.8)
            print(f'Ваше здоровье {player["hp"]}')
            time.sleep(0.8)
        if boss['hp']>0:
            print(f'Вы нанесли {dam_player} урона!')
            time.sleep(0.8)
            print(f"Еще осталось {boss['hp']}")
            time.sleep(0.8)
        elif boss['hp']<0:
            print(f'Босс {boss["name"]} повержен!')

while True:
    print(f'Добро пожаловать в игру, {player["name"]}!')
    time.sleep(2)
    print(f'Вы попадаете в {random.choice(locate)} {random.choice(loc)}...')
    time.sleep(2)
    print(f'Перед вами появляется босс {boss["name"]}')
    fight()
    if boss['hp']<0:
        break
    elif player['hp']<0:
        print('Вы проиграли!')
        break


