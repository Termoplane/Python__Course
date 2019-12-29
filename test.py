import random

class Warrior:
    hp = 100
    dmg = 20

    def hit(self, enemy):
        if enemy.hp > 0:
            enemy.hp -= self.dmg
            print("-20, Left:", enemy.hp)
        else:
            print('Кто-то пукнул')


Anya = Warrior()
Lesha = Warrior()

while Anya.hp > 0 or Lesha.hp > 0:
    kek = random.random()
    if kek > 0.5:
        print('Ударили Лешу')
        Anya.hit(Lesha)
        continue
    else:
        print('Ударили Аню')
        Lesha.hit(Anya)
        continue

    if Anya.hp == 0:
        print("Lesha wins, Anya has died")
        break
    else:
        print("Anya wins, Lesha has died")
        break