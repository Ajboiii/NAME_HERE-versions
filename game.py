import time, random, pickle, os.path
inventory = []
equipped = []
player = [10, 1, 0, 5, 0, 0, 0]
chest_data = [True]
def shop1():
    global player
    decide_shop = "yes"
    print("")
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

print('Enter fullscreen or else some craaaaazy stuff will happen')
time.sleep(5)
print("MMMWWOc:oXWMMMMMMMMMMMMMMMMMMMMMM0,.;0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MWKkxxOOKNMMMMMMMNklllclOWMMMMMMMNOxdoloKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("XXkc;o0KXWMMMMWX0k;...,;kWMN00XWMMMM0;..o0KNMMMMMMMMMMMMMMWXKXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("ddl:;:ccdXMMMMXl.....oXNWMMx. :XMMMM0;....,OMMMMMMMMMMMMMWKl;lKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("ool::lxk0NMMMMX:..:ddKMMMMMd. ;XMMMM0;....'kMMMMMMMMMMMMMW0c'cKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOllkWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("ool::dXMMMMMMMX:..dXXXXXKKKl  ,OXXXXk,...';xKXNMMMMMMMMWXXk:':kKKKKKKKXNMMMMMNXKKKKKKKXWMMMMWNKKKKKKKKKNWMMMMMMMWXKKKKKKKXNMMMMMMMMMMMMMMMMMMMMMMMMMMWl  :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("ool::dXWMMMMMMX:...'''''...    .''''...'dX0:..dWMMMMMMW0l:;,,'.........dWMMMMk'.......;0MMMMXc.........lNMMMMMMM0;........dWMMMMMMMMMMMMMMMMMMMMMMMMMWl  :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("oolccokO0NMMMMNklllll'  |||            .kMX;  oWMMMMMMWO:,,,,.         oWMMMMd.       'OMMMMX;         .loOWMMMM0'        oWMMMMMMMMMMMMMMMMMMMMMMMMMWl  :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("oooool:;o0NWWMMMMMMMNc  .,;.           .dN0: .dWMWNNNNXk;,,,,.         oWMMMMd.       '0MMMMX;            ,0NNWM0'        oWMMMMMMMMMMMMMMMMMMMMMMMWNXc  :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("oooool:;:loxXWMMMMMMNc                  ..,d00XMWx''..''',;cl;.        oWMMMMd.       '0MMMMX;             .'cKMO'        oWMMMMMMMMMMMMMMMMMMMMMMWklc.  :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("ooooolcc::;lk0KNMMMMWx;,.                  :xxxxxl;;'...',;lo:.        oWMMMMd.       '0MMMMX;               .lxl.        oWMMMMXkxxxxxxxxxxxxxkXMNo..   ,xOKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("ddooooool:::::l0MMMMMWWNl                       .lNNk;'',,;lo:.        oWMMMMd.       '0MMMMX;                            oWMMMMd.             .xMNc     .',oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("OOxdooooollc:;l0WMMMMMMWKkkkkk:               ;xkKWWk;,;ccloo:.        oWMMMMd.       '0MMMMX;                            oWMMMWd.             .xMNc  .;;;,,oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("K0Oxxdoooool:;l0WMMMMMMMMMMMMMx.              :OO000d;,:looll;.        oWMMMWd.       '0MMMMX;          .'.               oWMMMMO;''''''''''''';xXK:  'ooc,,oXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("KKK00kdooool::l0WWMMMMMMMMMMMMx.                 .,;,,,:lol;,.         oWMMMWd.       '0MMMMX;         ;KNd.              oWMMMMWNNNNNNNNNNNNNNXkdo'  'ooc,,oXWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("KKKKKOdooool:::oxkXWMMMWX0Odc:'                  .',;:clooocc;'..      .:::::'     .cdkNMMMMX;         ,xOkdd:.           oWMMMMMMMN0OKNMMMMMMMNx:;.  ..''',:odkNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("KKKK0Oxdddolc:::;ckXXXXKkol,                     ..';loooooool;,'.               ..:KMWNXXXXO,         .clxKXk,..         oWMMMMMMWKxoxKXNNNNNXKl,'...   .,;,,'lKWMMMMMMMMMMMMMMMMMMMNK0KWMMMMMMMMMMMMMM")
print("KKKKK000Odoooolc::ccclccc::'                        'loooooool;,'''.            ,OKXWWKo::::;.         .',;::lOKx.        oWMMMMMMWKxodddddddddo:,,:lc'  .coc,'cKWMMMMMMMMMMMMMMMMMMMk. ;0MMMMMMMMMMMMMM")
print("KKKKKKKK0Okxdoolcccccccc::;,...                     .',:loooooc:::::;,''''''''''ck0Okxo;',;::;,''''',,,;::;,,:oxdollllllllx00000000kdodxkkkkxdoolc:;,'.  .',;:cok00000000000NMWOollll,  .:lxXMMMMMMMMMMM")
print("KKKKKKKKKKKOxdddddooooool:::::'.                       .cllooooooooooooolllllllllllc,'''',cdddoooooodoooooc;,,,'cOXNNNNXXKxllllllccccldOKKKK0kddddo'   ..   .:llddddoolllcclkKK:   ......  'OMMMMMMMMMMM")
print("KKKKKKKKKKK00OOOOOxooooooolllllcc,                      ..'cooooooooooo,............     .lOOxooooooooooooollc;,,:cccc:,..............,xKKKKK00000O;  ,xx:    .,x0Odol'........   ,OKKKKd. 'OMMMMMMMMMMM")
print("KKKKKKKKKKKKKKKKK0Okxxkxxkxxkxxkkd:;;;,;;;;;;;;;,.        .cooooo:,,,,,.  ...''.',;;;;'   ,cldxxxxxxxxxxxkkkxo'........   .,;;;;;;;.  .;ccccccccccc.  :0Kx:;;;;;ccc;,'.  .........cO0Odd:. 'OMMMMMMMMMMM")
print("KKKKKKKKKKKKKKKKKK0KKKKKK0KKKKKKKKKKKKKKKKKKKKKK0:        .:ooooc.        ,oddodx0KKKKx.    .l000000000000OOOo.          .c0KKKKKKKo.                .c0KKKKKKKd.       .:dddooolllll,     ,0MWWNNNNNNNN")
print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0kdoooo;   ......   ;oooodxOOOOO00KKKKOxoc.  .''''''''''''....  .cdddddddxOKKKKKKKKOxdddddddddddddddddOKKKKKKKKOxdddddddxkOOxdoooolll,  .dO0NMNxcccccccc")
print("ooooooooooooooooooooooooooooooooooooooooooooooooooooooo;            ,ooooooooooooooooooooc.                     .:ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooc;;;;;;,,'..:KMNKOkc,'......")
print("                                                                                                                                                                                     .:cdXWKl,;,,'.     ")
print("ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd;     .cddddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxo.  ,xxxxx:      ........'cxxxxxxxx:   ..:KMN0OOOOOkxd:..")
print("MMMMMNKK0000000000000XMMMMMMMMMMMNK00000000000000000XWMMMMNK0KWMWK0000000000Oc     '0MMMMWK00OO0NMMMMMMMMMMMMMMMMMMMMMWX00000000000000KWMMMMWK0x'  oWMX0Oc      ........,oO0XMMMMMk,..  '0MMMMMMMMMWNd,,")
print("MMMMMO:,'.          .dWMMMMMMMMMMO,                 cNMMMM0, ,0MX:                 '0MMMMX:    .dWMMMMMMMMMMMMMMMMMMMMX:              ,0MMMMX:     oWWo.                   .dWMMMMWNNd. '0MMMMMMMMMMNd,,")
print("dddddc'.......       'cllllkWMKol;                  :XMMMMO. .;l:.                 '0MMMMNkol.  oWMMMMMMMM0lcdXMMMMMMMX;              .;cdXMK;     .::.            ......   oWMMMMMMMx. '0MMMMMMMMMMNd,'")
print("................           ,OKo.        .........   :XMMMMO.      ..       .....   '0MMMMWXKO,  oWMMMMMMMMx. .xKXWMMMMX;   .....         .xKk'                     .,''..   c0KKKKNWMx. '0MMMMMMMMMMNd,'")
print("......   ............       ..         .oKKKKKKK0:  :XMMMMO.    .oKO,     :0KKKKo. '0MMMMXc..   oWMMMMMMMMx.  ..;0MMMMX;  cKKKKKl         ...                      .,'.      .....lNMx. '0MMMMMMMMMMNd,,")
print("......................                  ;oooooooolcckNMMMMXoc,  .kMX;     lWMMMMKolxXMMMMK,     oWMMMMMMMMx.    .OMNklc.  oWMMMWd. .:l;                            .''...;llllc.  :XMx. '0MMMMMMMMMMNd,,")
print("..................   ....                        cXNWMMMMMMMMO' .kMX;     lWMMMMMMMMMMMMMK,     oWMMMMMMMMx.    'OMK,     oWMMMMx. :XMO.                          ..,,,,:OWMMMWl  ;0Nd. '0MMMMMMMMMMNd,,")
print(".........  .................                     ..'oNMMMMMMMO' .kMX;     lWMMMMMMMMMMMMMK,     oWMMMMMMMMx.    '0MK,     oWMMMMN00XWMO.           :O00OOc.     ..'',,,,:OWMMMWl   ...  '0MMMMMMMMMMNd,,")
print(".......... ............':ooc;;.      ';,.  .;,.     'dx0WMMMMO' .kMX;     lWMMMMMMMMMMMMMK,     ,oxKWWMMMMx.    'OMK;     oWMMMMMMMMMMO.           ,dxKWMd.     ...',,,,;okkkOk:..     .'dOkkkkkOOOkxc,,")
print("   ..................'',dNWWWWd.    .OWK; .xWNc        ;XMMWWO. .xMX;     lNWMMMMMMMMMMMMK;        lXWMMMMx.    'OMK;     oWMMMMMMMMMMO'              lNWd.       ..,',',,,,,,,,''.  ..'',,,,,,,,,,,,,,,")
print("   ...............'',oOOo;;dNMx.    .:ooxxOXMNc        ;XMKl,'  .xMX;     .,;dNMMMMMMMMMMW0kd.     lXWMMMMx.    .OMK;     oWMMMMMMMMMMNOkl.           .,;cxk:      .'',',,,'''',,'.    ..',,',,''''',,''")
print("''............';c:;,;d00:  :XMO;'.   ..;OWMMMNc        'dkl.  .,:0MX;        :XMMMMMMMN0kONMX;     ;dxkkkkc     'OMK;     ;xkkkkKWMMMMMMM0'              'dkc      .,'''''',,,,,,'..    ..'',',,''',,,''")
print("NNo.     .....,kNKo,,;;;.  :XMWNNk.    .kMMMMNc              .OWWWMX;        :XMMMMMMM0' .kMX;                  .OMK;           :XMMMMMMM0'                        .'',,,,,,,,',,,'''.   .,'',,,,''''',,")
print("MMx..         .kMWKOk:..   :XMXxdc.     ':::::.        .lddddkNMMMMWOdo'     :XMMMMMMMO'  ':;.                  'OMNOdl.        .;::::dXM0'        ,oo'            ....,,,,',,,'',,''.   .,'',,,,,''''''")
print("MMk,..        .kMMMMWo..   ,OKd,..                   ..lXMMMMMMMMMMMMMNc     :XMWXKK00d.                      ..:KMMMMXl..            .d0d.  ...   oWWx'..            .........'',,''.   .,'',,,,'''''''")
print("MMk'.....     .xMMMMMNX0:   ...                     ;0NNMMMMMMMMMMMMMMNc     :XWOc;'..                       .kNNWMMMMMNNK:             .   .dX0,  oWMWNXo                     .','''.   .,'','','''''''")
print("MMk,...        ,ldKMMMMWOollllllllll;.     ,lc.  .,;dNMMMMMMMMMMMMMMMMNc     'oxxxxc.     ,lc.  'lc'      .clxXMMMMMMMMMMWOolllllllllllll;. .xMNklo0WMMMWd.                    .''....   .,,,,,,,'''''''")
print("NNx'..           .xMMMMMMMMMMMMMMMMM0;....'kMNo..;od0WMMMMMMMMMMMMMMMMNc      ..cOKx.  ..'OMXc..dWWd...   ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;.'OMMMMMMMMNXKo.                    .''.     ..',,,,,,'''''''")
print(";;.      ........'kMMMMMMMMMMMMMMMMMWXKKKKKNMMNK0c..cXMMMMMMMMMMMMMMMMNc         .....;kKKNMWXKKNMMNKKKl  ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKKWMMMMMMMWd'..      ..''''.'''...  .''.  ..''',,,',,''''''''")
print("...       .......,kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx,'oNMMMMMMMMMMMMMMMMWkc::::'     .cdkXMMMMMMMMMMMMMMWd. ;XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo.       ..,,'''',,,,'......   .',,,,,,',,''''''''")
print("......      .....'xNNNNNWMMMMMMMMMMMMMMMMMMMMMWWW0xx0WMMMMMMMMMMMMMMMMMMMMMMWx.    '0MMMMMMMMMMMMMMMMMMx. :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo.       ..,,,,,,,,,,,,,'.     .',,,,,',,,,'''''''")
print("  ......    ...   .'''',xWMMMMMMMMMMMMMMMMMMMWKOOKXXNMMMMMMMMMMMMMMMMMMMMMMMMN0Oc  '0MMMMMMMMMMMMMMMMMMN0OKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo.    ...''''',,,,,',,''''.....''',,,,,,''''''''''")
print("   ......   ...         lWMMMMMMMMMMMMMMMMMMMW0xx0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMx. '0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo     .',''''',,,,,,',,'',,,,,,,',,,,,,'''''''''''")

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

print(' You find yourself in a mysterious room\n a few torches dimly illuminate your surroundings\n random objects that you might see while playing a video game are also in the room.\n paranoid about where exactly you might be, you pick up a dusty sheild\n they both feel surprislingly real\n you decide to explore the place now that you have some protection')
print(" _______   _______\n|             |||||\n|             ¯¯¯¯|\n|		  |\n|_       	 _|\n<--SHOP  #   \n|      |/|\      |\n|_________________|\n")
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
