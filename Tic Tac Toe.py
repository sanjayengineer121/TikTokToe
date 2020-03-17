data = {
    'T1': ' ', 'T2': ' ', 'T3': ' ',
    'M1': ' ', 'M2': ' ', 'M3': ' ',
    'D1': ' ', 'D2': ' ', 'D3': ' '
}


def chk():
    if data['T1'] == "X" and data['T2'] == 'X' and data['T3'] == 'X':
        print("player One Won")
        return 1
    if data['M1'] == 'X' and data['M2'] == 'X' and data['M3'] =='X':
        print("player one won")
        return 1
    if data['D1'] == 'X' and data['D2'] + 'X' and data['D3'] == 'X':
        print("player one won")

    if data['D1'] == 'X' and data['M2'] == 'X' and data['T3'] =='X':
        print("player one won")
        return 1
    if data['T1'] == 'X' and data['M2'] =='X' and data['D3'] == 'X':
        print("player one Won")
        return 1
    #player2


    if data['T1'] == "Y" and data['T2'] == 'Y' and data['T3'] == 'Y':
        print("player One Won")
        return 1
    if data['M1'] == 'Y' and data['M2'] == 'Y' and data['M3'] == 'Y':
        print("player Two won")
        return 1
    if data['D1'] == 'Y' and data['D2'] + 'Y' and data['D3'] == 'Y':
        print("player Two won")
        return 1
    if data['D1'] == 'Y' and data['M2'] == 'Y' and data['T3'] == 'Y':
        print("player Two won")
        return 1
    if data['T1'] == 'Y' and data['M2'] =='Y' and data['D3'] == 'Y':
        print("player two Won")
        return 1
player = 1
tot_mov = 0
print('T1|T2|T3')
print('- +- +-')
print('M1|M2|M3')
print('- +- +-')
print('D1|D2|D3')
print("*********************************************************")
while True:
    print(data['T1'] + '|' + data['T2'] + '|' + data['T3'])
    print('- +- +-')
    print(data['M1'] + '|' + data['M2'] + '|' + data['M3'])
    print('- +- +-')
    print(data['D1'] + '|' + data['D2'] + '|' + data['D3'])
    end=chk()
    if tot_mov == 9:
        break
    while True:
        if player == 1:
            p1_input = input('player1')
            if p1_input.upper() in data and data[p1_input.upper()] == ' ':
                data[p1_input.upper()] = 'X'
                player = 2
                break
            else:
                print("Invalid Input")
                continue
        else:
            p2_input = input('player2')
            if p2_input.upper() in data and data[p2_input.upper()] == ' ':
                data[p2_input.upper()] = 'Y'
                player = 1
                break
            else:
                print('Invalid Input , try again')
                continue
    tot_mov += 1
    print('***************************************************************')
    print()
