import random


def reset_():
    global mass_plant
                
    mass_plant = [['++','++','++','++','++','++','++','++','++','++','++','++'],
                  ['++','00','00','00','00','00','00','00','00','00','00','++'],
                  ['++','00','00','00','00','00','00','00','00','00','00','++'],
                  ['++','00','00','00','00','00','00','00','00','00','00','++'],
                  ['++','00','00','00','00','00','00','00','00','00','00','++'],
                  ['++','00','00','00','00','00','00','00','00','00','00','++'],
                  ['++','00','00','00','00','00','00','00','00','00','00','++'],
                  ['++','00','00','00','00','00','00','00','00','00','00','++'],
                  ['++','00','00','00','00','00','00','00','00','00','00','++'],
                  ['++','00','00','00','00','00','00','00','00','00','00','++'],
                  ['++','00','00','00','00','00','00','00','00','00','00','++'],
                  ['++','++','++','++','++','++','++','++','++','++','++','++']]

def serch_position(length_ship, name, xx, yy):
    global mass_plant
    global neext
    # xx = random.randint(1, 11)
    # yy = random.randint(1, 11)
    tempROT = ['vertical','horizontal']
    rotation = random.choice(tempROT)
    #print('NEXT')
    
    if rotation == 'vertical':
        for y in range(yy ,yy + length_ship + 2):
            for x in range(xx ,xx + 3):
                if mass_plant[y][x] == '00' or mass_plant[y][x] == '--' :
                    #print(y, x, 'vertical', name)
                    pass
                else:
                    return False
        setup = [True, yy, xx, length_ship, name]
        set_mass_vertical(setup)
        return True
                    
    if rotation == 'horizontal':
        for y in range(yy , yy + 3):
            for x in range(xx , xx + length_ship + 2):
                if mass_plant[y][x] == '00' or mass_plant[y][x] == '--' :
                    #print(y, x, 'horizontal', name)
                    pass
                else:
                    return False
        setup = [True, yy, xx, length_ship, name]
        set_mass_horizontal(setup)
        return True
        
def set_mass_vertical(setup):
    global mass_plant
    yy = setup[1]
    xx = setup[2]
    length_ship = setup[3]
    name = setup[4]
    ship_yy = yy + 1
    ship_xx = xx + 1
    
    for y in range(yy ,yy + length_ship + 2):
        for x in range(xx ,xx + 3):
            if x == ship_xx and( ship_yy <= y <= ship_yy + length_ship - 1 ):
                mass_plant[y][x] = name
            else:
                mass_plant[y][x] = '--'

def set_mass_horizontal(setup):
    global mass_plant
    yy = setup[1]
    xx = setup[2]
    length_ship = setup[3]
    name = setup[4]
    ship_yy = yy + 1
    ship_xx = xx + 1
    
    for y in range(yy , yy + 3):
        for x in range(xx , xx + length_ship +2):
            if y == ship_yy and( ship_xx <= x <= ship_xx + length_ship - 1 ):
                mass_plant[y][x] = name
            else:
                mass_plant[y][x] = '--'


def temp_sas(length_ship, name):

    # mas = [0] * 10 
    # for nn in range(len(mas)): 
    #     mas[nn] = [0] * 10
    # print(mas)
    
    # for ii in range(10):
    #     i = random.randint(1, 11)
    #     n = random.randint(1, 11)
    #     if serch_position(length_ship, name, i, n) == True:
    #         return True
    #     if ii == 10:
    #         start_game()
        
    for i in range(11):
        for n in range(11):
            if serch_position(length_ship, name, i, n) == True:
                return True
            if i == 10 and n == 10:
                start_game()
        
def change_ship(temp):
    for i in range(len(temp)):
        t = random.choice(temp)
        while temp_sas(t[0], t[1]) == True:
            temp.remove(t)
            break

def start_game():
    reset_()
    global mass_plant
    
    temp = [(4, '41'),
            #(3, '31'),
            (3, '32'),
            (3, '33'),
            (2, '21'),
            (2, '22'),
            (2, '23'),
            (1, '11'),
            (1, '12'),
            (1, '13'),
            (1, '14')]
    
    change_ship(temp)
    
    return mass_plant
    
    # for i in range(1,11):
    #     for n in range(1,11):
    #         print(mass_plant[i][n], end = ' ')
    #     print()
    
    
    # input()
         
# start_game()
# print(start_game())
# input()

