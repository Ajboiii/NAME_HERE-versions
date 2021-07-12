print(' You find yourself in a mysterious room\n a few torches dimly illuminate your surroundings\n random objects that you might see while playing a video game are also in the room.\n paranoid about where exactly you might be, you pick up a dusty sheild\n they both feel surprislingly real\n you decide to explore the place now that you have some protection')
print(" _______   _______\n|             |||||\n|             ¯¯¯¯|\n|		  |\n|_       	 _|\n<--SHOP  #   \n|      |/|\      |\n|_________________|\n")
import random, pickle, os.path
inventory = []
equipped = []
player = [10, 1, 0, 5, 0, 0, 0]
chest_data = [True]
def shop1():
    global player
    decide_shop = "yes"
    print('Welcome to my shop')
    potion_cost = 10
    sword_cost = 5
    while decide_shop == 'yes':
        buying = input('What would you like to buy? \nSword\nPotion ')
        if buying == 'potion':
            if potion_cost > player[4]:
                print("you don't have enough money to buy this!")

            else:
                print('Are you sure you want to spend', potion_cost, 'dollars and buy a potion?')
                decide_shop = input()

                if decide_shop == 'yes':
                    player[4] = player[4] - potion_cost
                    inventory.append('potion')

        if buying == 'sword':
            if sword_cost > player[4]:
                print("you don't have enough money to buy this!")

            else:
                print('Are you sure you want to spend', sword_cost, 'dollars and buy a sword?')
                decide_shop = input()

                if decide_shop == 'yes':
                    player[4] = player[4] - sword_cost
                    inventory.append('sword')
        
        decide_shop = input('Buy anything else? ')
                    
        if decide_shop == 'no':
            print('These are the items you bought.')

            for x in inventory:
                print(x)

def battle1():
    monster1 = [10, 1, 1, 6]
    monster2 = [10, 1, 2, 6]
    monster3 = [11, 1, 3, 6]
    monster4 = [12, 2, 5, 7.5]
    monster_chance = random.randrange(1, 4)
    if monster_chance == 4:
        monster_chance = random.randrange(1, 2)

    if monster_chance == 2:
        print('you found a BOSS enemy!!')

    elif monster_chance == 1:
        print('you found a weak enemy!')

    elif monster_chance == 2:
        print('you found an enemy!')

    elif monster_chance == 3:
        print('you found a strong enemy!')

crack = 'bad'
while crack != 'still bad':
    save_load = input('new game or load?\nload\nnew game\n')
    
    if save_load == 'load':
        directory = './save/'
        filename = "player.dat"
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        file = open(file_path, 'rb')
        player = pickle.load(file)
        file.close()

        directory = './save/'
        filename = "inventory.dat"
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        file = open(file_path, 'rb')
        inventory = pickle.load(file)
        file.close()

        directory = './save/'
        filename = "equipped.dat"
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        file = open(file_path, 'rb')
        equipped = pickle.load(file)
        file.close()

        directory = './save/'
        filename = "chest_data.dat"
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        file = open(file_path, 'rb')
        player = pickle.load(file)
        file.close()

        crack = 'still bad'

    if save_load == 'new game':
        directory = './save/'
        filename = "player.dat"
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        file = open(file_path, 'wb')
        pickle.dump(player, file)
        file.close()

        directory = './save/'
        filename = "inventory.dat"
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        file = open(file_path, 'wb')
        pickle.dump(inventory, file)
        file.close()

        directory = './save/'
        filename = "equipped.dat"
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        file = open(file_path, 'wb')
        pickle.dump(equipped, file)
        file.close()

        directory = './save/'
        filename = "chest_data.dat"
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        file = open(file_path, 'wb')
        pickle.dump(chest_data, file)
        file.close()

        crack = 'still bad'

while True:
    if player[5] == 0 and player[6] == 0:
        print('There is a chest here')
        chesthere = True
    waiting_event = input('Which direction should you go?\nor open the menu? ')

    if waiting_event == 'menu':
        menu_decision = input('inventory\nmoney\nequip\nequipped\nsave ')
            
        if menu_decision == 'money':
            print('you have', player[4], 'dollars')

        elif menu_decision == 'inventory':
            for x in inventory:
                print(x)

        elif menu_decision == 'equipped':
            for x in equipped:
                print(x)

        elif menu_decision == 'equip':
            print('equip what?')
            for x in inventory:
                print(x)
                equip = input()
                if equip == 'sword':
                    if not 'sword' in equipped:
                        equipped.append('sword')
                        inventory.remove('sword')
                        player[2] = player[2] + 2

                    else:
                        print('you already have a sword equipped')

        elif menu_decision == 'save':
            directory = './save/'
            filename = "player.dat"
            file_path = os.path.join(directory, filename)
            if not os.path.isdir(directory):
                os.mkdir(directory)
            file = open(file_path, 'wb')
            pickle.dump(player, file)
            file.close()

            directory = './save/'
            filename = "inventory.dat"
            file_path = os.path.join(directory, filename)
            if not os.path.isdir(directory):
                os.mkdir(directory)
            file = open(file_path, 'wb')
            pickle.dump(inventory, file)
            file.close()

            directory = './save/'
            filename = "equipped.dat"
            file_path = os.path.join(directory, filename)
            if not os.path.isdir(directory):
                os.mkdir(directory)
            file = open(file_path, 'wb')
            pickle.dump(equipped, file)
            file.close()

            directory = './save/'
        filename = "chest_data.dat"
        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
            file = open(file_path, 'wb')
        pickle.dump(chest_data, file)
        file.close()
        

        if waiting_event == 'left':
                shop1()

        elif waiting_event == 'right':
            battle1()

        elif waiting_event == 'chest':
            if chesthere == True:
                if chest_data[0] == True:
                    chestget = random.randrange(5, 15)
                    print('You found',chestget,'dollars!')
                    player[4] = player[4] + chestget
                    chest_data[0] = False
