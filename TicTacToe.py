def cap(A):
    koor=[2,1,0]
    print('  ＿＿＿＿＿＿＿＿')
    for i in range(3):
        print(f'\033[94m{koor[i]}\033[0m',end=" │")
        for j in range(3):
            print('%2s' %A[i][j],end="│")
        print()
        print('  ─────────────')
    print(f'\033[94m    0   1   2\033[0m')
Matris=[["   " for j in range(3)] for i in range(3)]
cap(Matris)
sutun={0:["   ","   ","   "],1:["   ","   ","   "],2:['   ',"   ",'   ']}
setir={0:['   ','   ','   '],1:['   ','   ','   '],2:['   ','   ','   ']}
diaqonal={0:['   ','   ','   '],1:['   ','   ','   ']}
say=0;cavab=0
komp=input("Do you want to play with computer? (Yes or No): ")
while say<=9:
    say+=1
    for sutun1 in sutun:
        sayx=0;sayo=0
        for i in sutun[sutun1]:
            if i==' X ':
                sayx+=1
            elif i==' O ':
                sayo+=1
            if sayx==3:
                print("X won!")
                cavab+=1
                break
            elif sayo==3:
                print("O won!")
                cavab+=1
                break
    for setir1 in setir:
        sayx1 = 0;sayo1 = 0;
        for i in setir[setir1]:
            if i==' X ':
                sayx1+=1
            elif i==' O ':
                sayo1+=1
            if sayx1==3:
                print("X won!")
                cavab+=1
                break
            elif sayo1==3:
                print("O won!")
                cavab+=1
                break
    for dia in diaqonal.values():
        sayxd = 0;sayod = 0
        for i in dia:
            if i == ' X ':
                sayxd += 1
            elif i == ' O ':
                sayod += 1
            if sayxd == 3:
                print("X won!")
                cavab += 1
                break
            elif sayod == 3:
                print("O won!")
                cavab += 1
                break
    if cavab==1:
        break
    if say==10:
        break
    randomdaxilx=[]
    randomdaxily=[]
    koor=[2,1,0]
    from random import randint
    if say%2==0:
        x,y=map(int,input("Coordinates for symbol X: ").split())
        y=koor[y]
        if Matris[y][x]=="   ":
            Matris[y][x]=" X "
        else:
            print("This cell is taken!")
            say-=1
            continue
    else:
        if komp=="Yes":
            while True:
                x=randint(0,2);y=randint(0,2)
                if Matris[y][x]=="   ":
                    print(f'Coordinates for symbol O: {x} {koor[y]}')
                    break
        elif komp=="No":
            x,y=map(int,input("Coordinates for symbol O: ").split())
            y=koor[y]
        if Matris[y][x]=="   ":
            Matris[y][x]=" O "
        else:
            print("This cell is taken!")
            say-=1
            continue
    for i in range (3):
        for j in range (3):
            if setir[i][j]=="   ":
                setir[i][j]=Matris[i][j]
    for j in range (3):
        for i in range (3):
            if sutun[j][i]=="   ":
                sutun[j][i]=Matris[i][j]
    i2=-1
    for i in range (3):
        diaqonal[0][i]=Matris[i][i]
        diaqonal[1][i]=Matris[i][2-i]
    cap(Matris)
else:
    print("No winner!")