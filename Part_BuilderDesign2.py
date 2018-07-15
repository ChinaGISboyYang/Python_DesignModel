#-*-coding:utf-8-*-
# Author: GISyang_china

from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough    = Enum('PizzaDough', 'thin thick')
PizzaSauce    = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping  = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')
STEP_DELAY    = 3

class Pizza:
    def __init__(self, name):
        self.name   = name
        self.dough  = None
        self.sauce  = None
        self.toppin = None

    def __str__(self):
        return self.name

    def prepar_dough(self,dough):
        self.dough  = dough
        print('preparing the {} dough of your{}...'.format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))
'''
两个建造者之一的，玛格丽塔披萨
'''
class MargaritaBuilder:
    def __init__(self):
        self.pizza       = Pizza('margarita')
        self.progrss     = PizzaProgress.queued
        self.baking_time = 5
    #准备面团
    def prepar_dough(self):
        self.progrss     = PizzaProgress.preparation
        self.pizza.prepar_dough(PizzaDough.thin)

    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the toamto sauce')

    def add_topping(self):
        print('adding the topping (double mozzarella, oregano) to your margarita')
        self.pizza.topping.append([i for i in
                                   (PizzaTopping.double_mozzarella, PizzaTopping.oregano)
                                   ])
        time.sleep(STEP_DELAY)
        print('done with the topping (double mozzarrella, oregano)')

    def bake(self):
        self.progrss     = PizzaProgress.baking



