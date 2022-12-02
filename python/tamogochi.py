from asyncio.windows_events import NULL
from distutils.command.install_egg_info import to_filename
import random, time
class Animals():
    
    def __init__(self,name):
        self.name=name
        self.hunger=0
        self.thirst=0
        self.hp=0
        self.happiness=0
        self.level=1
        self.ills=NULL
        self.exp=0
        

class Dog(Animals):
    def __init__(self,name):
        super().__init__(name)
        self.hp=100
        self.recEat=['корм','кость','мясо']
        self.recDrink=['вода фильтрованная','кефир']

        self.recGame=['апорт','палка-приманка']
        self.hunger=0
        self.level=1
        self.happiness=50
        self.thirst=0
        self.ills=NULL
        

class Cat(Animals):
    def __init__(self,name):
        super().__init__(name)
        self.hp=90
        self.exp=0
        self.recEat=['корм','куриное мясо','рыба']
        self.recDrink=['вода фильтрованная','молоко']
        
        self.recGame=['найди лакомство','удочка-дразнилка']
        self.hunger=0
        self.level=1
        self.happiness=50
        self.thirst=0
        self.ills=NULL

class Parrot(Animals):
    def __init__(self,name):
        super().__init__(name)
        self.hp=50
        self.exp=0
        self.recEat=['морковь','овёс','семечки']
        self.recDrink=['вода фильтрованная','сок манго']

        self.recGame=['найди лакомство','качели']
        self.hunger=0
        self.level=1
        self.happiness=50
        self.thirst=0
        self.ills=NULL

class Hamster(Animals): 
    def __init__(self,name):
        super().__init__(name)
        self.hp=15
        self.exp=0
        self.recEat=['корм','тыква','овёс']
        self.recDrink=['вода фильтрованная','роса']
        self.recGame=['колесо','лабиринт']
        self.hunger=0
        self.level=1
        self.happiness=50
        self.thirst=0
        self.ills=NULL

class Kapibara(Animals):
    def __init__(self,name):
        super().__init__(name)
        self.hp=150
        self.exp=0
        self.recEat=['корм','арбуз','бананы']
        self.recDrink=['вода фильтрованная']
        self.recGame=['найди лакомство','лабиринт']
        self.hunger=0
        self.level=1
        self.happiness=50
        self.thirst=0
        self.ills=NULL

class Poni(Animals):
    def __init__(self,name):
        super().__init__(name)
        self.hp=200
        self.exp=0
        self.recEat=['корм','сено','трава']
        self.recDrink=['вода фильтрованная','вода из под крана']
        self.recGame=['найди лакомство','покататься']
        self.ills=NULL
        self.hunger=0
        self.level=1
        self.happiness=50
        self.thirst=0

class Karakal(Animals):
    def __init__(self,name):
        super().__init__(name)
        self.hp=95
        self.exp=0
        self.recEat=['корм','мясо индейки','варёное мясо']
        self.recDrink=['вода фильтрованная','молоко']
        self.recGame=['найди лакомство','плетёный шарик']
        self.ills=NULL
        self.hunger=0
        self.level=1
        self.happiness=50
        self.thirst=0


    
def drinking(drank):


    Drink=['вода из под крана','молоко','вода фильтрованная','яблочный сок','кефир','сок манго','роса']
    print('Выберите питьё:',Drink)
    intDrink=input().lower()
    

    if intDrink==drank.recEat[0] or intDrink==drank.recDrink[1]:
            print("Вы напоили своего питомца","\n+5 к счастью", "\n+5 к здоровью","\n+8 к жажде")
            drank.happiness+=5
            drank.hp +=5
            drank.thirst+=8
            



    else:
        print("Вы неправильно напоили своего питомца","\n-5 к счастью", "\n-4 к здоровью","\n-8 к жажде")
        drank.happiness-=5
        drank.hp-=2
        drank.thirst-=8
    atil=random.randint(1,10)
    if atil<=4:
        print('Ваш питомец заболел','\nВам срочно нужно идти к ветиринару')
        print('1.Идти к ветеринару \n2.Не идти к ветeринару')
        di=int(input())
        if di==1:
            print("Вы сходили к ветeринару \n+4 к здоровью \n+4 к счастью")
            drank.hp +=4    
            drank.happiness+=4
        elif di==2:
            print("Вы не сходили ко врачу ваш питомец умер")
            drank.hp=0
        else:
            print('Вы неправильно ввели команду')
        
            

def eating(ate):
    
    Eat=['корм','кость','мясо','куриное мясо','рыба','морковь','овёс','семечки','крецкий орех','тыква','изюм','бананы','трава','арбуз','сено','мясо индейки','варёное мясо']
    print('Выберите еду:',Eat)
    intEat=str(input()).lower()
    

    if intEat==ate.recEat[0] or intEat==ate.recEat[1] or intEat==ate.recEat[2]:
        print("Вы покормили своего питомца","\n+5 к счастью", "\n+8 к здоровью","\n+8 к голоду")
        ate.happiness+=5
        ate.hp += 8
        ate.hunger+=8
        

    else:
        print("Вы неправильно покормили своего питомца","\n-5 к счастью", "\n-8 к здоровью","\n-8 к голоду")
        ate.happiness-=5    
        ate.hp-=8
        
        ate.hunger-=8
        atil=random.randint(1,10)
        if atil<=4:
            print('Ваш питомец заболел','\nВам срочно нужно идти к ветиринару')
            print('1.Идти к ветеринару \n2.Не идти к ветеринару')
            di=int(input())
            if di==1:
                print("Вы сходили к ветиринару \n+10 к здоровью \n+10 к счастью")
                ate.hp +=10

                ate.happiness+=10
            elif di==2:
                print("Вы не сходили ко врачу ваш питомец умер")
                ate.hp=0
            else:
                print('Вы неправильно ввели команду')    
        
def games(game):
    Game=['палка-приманка','колесо','апорт','найди лакомство','покататься','удочка-дразнилка','качели','плетёный шарик','лабиринт']
    print('Выбирите игру:',Game)
    intGame=input().lower()     
    if intGame==game.recGame[0] or intGame==game.recGame[1]:
        print("Вы поиграли со своим питомцем","\n+10 к счастью")
        game.happiness+=10
            
        

    else:
        print("Вы неправильно поиграли со своим питомцем","\n-10 к счастью")
        game.happiness-=10
            
        
    
def gamE(self):
    if self.happiness==100:
        self.level+=1
        self.happiness=0
    elif self.level==5:
        quit()
    elif self.hp<=0 or self.happiness<=0:
        quit()
ani=input('Выбирите питомца  ').lower()
nam=input('Назовите своего питомца  ').lower()
if ani=='karakal':
    anim=Karakal(nam)
    print('Вы выбрали питомца каракал')
elif ani=='dog':
    anim=Dog(nam)
    print('Вы выбрали питомца собаку')

elif ani=='cat':
    anim=Cat(nam)
    print('Вы выбрали питомца кошку')
elif ani=='parrot':
    anim=Parrot(nam)
    print('Вы выбрали питомца попугая')
elif ani=='kapibara':
    anim=Kapibara(nam)
    print('Вы выбрали питомца капибару')
elif ani=='hamster':
    anim=Hamster(nam)
    print('Вы выбрали питомца хомяка')
elif ani=='poni':
    anim=Poni(nam)
    print('Вы выбрали питомца пони')
else:
    print('Питомец выбран неправильно')
    quit()   

st=0


    
while True:
    
    time.sleep(5)
    doing=int(input("Выберите действие: \n1.Покормить \n2.Напоить \n3.Поиграть \n4.Статистика \n"))
    
    if doing==4:
        
        print(f'Здоровье питомца: {anim.hp}')
        print(f'Счастье питомца: {anim.happiness}')
        print(f'Голод питомца: {anim.hunger}')
        print(f'Жажда питомца: {anim.thirst}')
        print(f'Уровень питомца: {anim.level}')
        st+=1
    elif doing==1:
        st+=1
        eat=eating(anim)
        gamE(anim)
    elif doing==2:
        st+=1
        drink=drinking(anim)
        gamE(anim)
    elif doing==3:
        st+=1
        game=games(anim)
        gamE(anim)

    else:
        print('Неизвесная команда')    
    
    if st==6:
        time.sleep(10)
        st=0
        
        anim.hp-=5
        anim.hunger-=10
        anim.thirst-=10
        anim.happiness-=10
        
    if anim.hunger<0:
            print("Ваш питомец хочет кушать")
    if anim.thirst<0:
        print("Ваш питомец хочет пить")

           
    


          
