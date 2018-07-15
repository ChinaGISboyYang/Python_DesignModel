#-*-coding:utf-8-*-
# Author: GISyang_china

# 抽象工厂
# 是抽象方法的一种泛化，抽象工厂是一组工厂方法，其中每个工厂方法负责产生不同种类的对象
#
'''
工厂模式使用场景：
    追踪对象的创建时
    将对象的创建和使用解耦时
    优化应用的性能和资源占用时
'''
class Frog:
    def __init__(self, name): 
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Forg encounters {} an {}'.format(self, obstacle, obstacle.action()))


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t-----forgWorld-----'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()



class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Wizard battles agains {} and {}!'.format(
            self, obstacle, obstacle.action()))


class Ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it!'

class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t-----WizardWorld-----'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()

class GameEnvironment:
    def __init__(self, factory):
        self.hero     = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input('Welcome{}.How old are you?'.format(name))
        age = int(age)

    except ValueError as err:
        print("Age{} is invalid, please try again...".format(age))
        return (False, age)
    return (True,age)

def main():
    name        = input("hello.what`s your name?")
    vaild_input = False
    while not vaild_input:
        vaild_input, age = validate_age(name)
    game        = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()


