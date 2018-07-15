#-*-coding:utf-8-*-
# Author: GISyang_china


# 建造者模式
'''
建造者模式：
    
'''

MINI4 = '1.4GHz Mac mini'

class AppleFactory:
    class MacMini14:
        def __init__(self):
            self.memory = 4  # 单位为GB
            self.hdd    = 500 # 单位为GB
            self.gup    = 'Inter HD Graphics 5000'

        def __str__(self):
            info = ('Model: {}'.format(MINI4),
                    'Memory: {}GB'.format(self.memory),
                    'Hard Disk: {}GB'.format(self.hdd),
                    'Graphics Card: {}'.format(self.gup)
            )
            return '\n'.join(info)

    def build_computer(self, model):
        if (model == MINI4):
            return self.MacMini14()
        else:
            print("I dont know how to build {}".format(model))

if __name__ == '__main__':
    afac = AppleFactory()
    mac_mini = afac.build_computer(MINI4)
    print(mac_mini)
