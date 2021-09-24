while True:
    try:
        x = int(input())
        if x >= 0 and x < 90 or x == 360:
            print('Bom Dia!!')
        elif x > 89 and x < 180:
            print('Boa Tarde!!')
        elif x > 179 and x < 270:
            print('Boa Noite!!')
        else:
            print('De Madrugada!!')
    except EOFError:
        break
