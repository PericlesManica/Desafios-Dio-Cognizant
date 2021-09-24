n = int(input())
while n:
    n -= 1
    placa = input().split('-')
    if len(placa) == 2 and placa[0].isupper() and len(placa[0]) == 3 \
            and placa[0].isalpha() and placa[1].isnumeric():
        try:
            r = int(placa[1]) % 10
            if r == 9 or r == 0:
                print('SEXTA')
            elif r > 6:
                print('QUINTA')
            elif r > 4:
                print('QUARTA')
            elif r > 2:
                print('TERCA')
            else:
                print('SEGUNDA')
        except:
            print('FALHA')
    else:
        print('FALHA')
