import random

def kampf():
    """Kampf zwischen Spieler und Monster
    return 0 wenn spieler gewinnt
    return 1 wenn spieler verliert"""
    print("Spiele Schere, Stein, Papier gegen das Monster")
    while True:
        print("Wähle Schere, Stein oder Papier")
        command= input("?")
        if command not in ("Schere","Stein","Papier"):
            return 1
        gegnerzug=random.choice(("Schere","Stein","Papier"))
        print("Du spielst {} Monster spielt {}".format(command,gegnerzug))
        if gegnerzug==command:
            print("Unentschieden, spiele nochmals")
            continue
        if (gegnerzug=="Schere" and command=="Papier") or (gegnerzug=="Stein" and command=="Schere") or (gegnerzug=="Papier" and command=="Stein"):
            print("Monster gewinnt!")
            return 1
        print("Du gewinnst!")
        return 0


def shop(geld,semmeln):
    """Tausche Geld gegen Essen"""
    print("Willkommen im Shop!")
    print("Eine Wurstsemmel kostet 3 Gold.")
    print("Wie viele Wurstsemmeln willst du kaufen?")
    menge=input("?")
    try:
        menge=int(menge)
    except:
        print("Auf Wiedersehen")
        return geld,semmeln
    # gültige zahl eingegeben
    if menge*3>geld:
        print("Nicht genug Gold")
        return geld,semmeln
    semmeln+=menge
    geld-=menge*3
    print("Vielen Dank für Ihren Einkauf")
    return geld,semmeln
    
    
def kiste():
    """Gib dem Hero ein Matherätsel"""
    while True:
        a=random.randint(1,10)
        b=random.randint(1,10)
        c=a*b
        antwort=input("Wie viel ist {} x{}?".format(a,b))
        try:
            antwort=int(antwort)
        except:
            print("Zahl eingeben")
            continue
        if antwort==c:
            print("Bravo")
            return
        print("Falsche Zahl")
        print(a,"x",b,"=",c)
        

dungeon1="""
########################################################################
#.M..s....#......#.#..########.#........#############.....#.........#.<#
####?####.#.#####...##........#.....##..#...........#.###.#.#######.d..#
#$/#$#$$#.#.##.........#.###..#.####/#..#.###.####..#...#.#......#..#.##
#..#$#..#.#.#........###.#k#..#.#ss#.#..#.#.#..#.#.###..#...######..#.##
#?M###M?#.#.#.......#**#.#.#..#.#ss#.#..#.#.#.#......##..####.......#.##
#.......M.###......#***#.#*.#...#ss#.#..#.#.#.##...##.##............#.##
####d########......#***#.#..#.###ss#.#..#.#.#.#.#..##....############.##
#k.#.#***#.........#***#.#..#.#ssss#..#.#.#.#.#.....#.###..............#
#..#.#.s.#.........#***#.#..#.######..#.#.#.#..#####.....#############.#
#..#.#...#.........#***#....#.........#......#.......##.#/.............#
#?##.###M#.#############################################################
#....M??M#....?.?........................#.............................#
#....#####....?.?........................#.............................#
#?.......#....?w?........................#.............................#
#..ww....#....?.?........................#.............................#
#..ww....#....?.?......................................................#
#........##########################################################....#
#........#..................k#.$.#.$.#.$.#.$.#.$.#.....................#
#........#...................#.#.#.#.#.#.#.#.#.#.#.#...................#
#M......M#.........###.......#.#.#.#.#.#.#.#.#.#.#.#...................#
#........#.........?s?.......#.#.#.#.#.#.#.#.#.#.#.#.......$s$.........#
#.....M............###.........#...#...#...#...#...#...................#
########################################################################
"""

dungeon2="""
########################################################################
#<...................................?...................<#>????.......#
#...................................##....................######.......#
#....................................#.......................MM#.......#
#....................................#........................M####d####
#....................................#.........................#.......#
#....................................#.........................#.......#
#....................................#.........................#.......#
#....................................#.....#####.#####.........#.......#
#....................................#M....#...#.#...#........M#.......#
#....................................#MM...#...#.#...#.......MM#.......#
#....................................###########d###############.....###
#....................................#/#M........#M..................#M#
#....................................#?#.........#.....................#
#....................................#?#.........#.....................#
#....................................#...........#.....................#
#....................................#...........#......../............#
#....................................#...........#.....................#
#....................................#...........#.....................#
#....................................#...........#.....................#
#....................................#...........#.....................#
#....................................#...........#.....................#
#....................................#M..........dM...................M#
########################################################################
"""

dungeon3="""
########################################################################
#.....................................................#.....#..........#
#.....................................................#.....#..........#
#.....................................................#.....#..........#
#.....................................................#######..........#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
#......................................................................#
########################################################################
"""

level=[]
for d in (dungeon1,dungeon2,dungeon3):
    dungeon=[]
    for line in d.splitlines():
        dungeon.append(list(line))
    level.append(dungeon)

        
    


hero="@"
herox=1
heroy=2
heroz=0
herogold=0
herow=0
herohunger=0
herokey=0
herohp=100
while True:
    for z,dungeon in enumerate(level):
        if z !=heroz:
            continue
        for y,line in enumerate(dungeon):
        #   if y !=heroy:
        #       print(line)
        #else:
            for x,b in enumerate(line):
                if x == herox and y == heroy:
                    print(hero,end="")
                else:
                    print(b,end="")
            print()
    #herox=int(input))
    command=input("Gold:{} Wurstsemmel {} Hunger {} Key {} HP {} ".format(herogold, herow, herohunger, herokey, herohp))
    #herohunger+=1
    #steigt der hunger? 20%
    if random.random()< 0.2:
        herohunger+=random.randint(5,10)
        print("Man hab ich hunger")
    #Bewegung
    dx=0
    dy=0
    if command=="a":
        dx=-1
    if command=="d":
        dx=1
    if command=="up":
        if level[heroz][heroy][herox]==">":
            heroz-=1
            continue
        else:
            print("Finde erst ein Stiegenhaus >")
    if command=="down":
        if level[heroz][heroy][herox]=="<":
            heroz+=1
            continue
        else:
            print("Finde erst ein Stiegenhaus <")
    if command=="s":
        dy=1
    if command=="w":
        dy=-1
    if command=="break":
        break
    #------cheats-------
    if command=="cheat-help":
        print()
        print()
        print("s-cheat = Schlüssel")
        print("j-cheat = Jump")
        print("k-cheat = Kaufhaus")
        print("w-cheat = Wurstsemmeln")
        print("g-cheat = Gold")
        print("HP-cheat = Hp")
        print()
        print()
    if command=="j-cheat":
        herox+=7
        herohunger+=1
    if command=="k-cheat":
        level[heroz][heroy][herox]="k"
    if command=="w-cheat":
        herow+=1000
    if command=="g-cheat":
        herogold+=1000
    if command=="s-cheat":
        herokey+=1000
    if command=="HP-cheat":
        herohp+=10000
    #--türe--
    ziel=level[heroz][heroy+dy][herox+dx]
    if ziel=="d":
        if herokey<1:
            dy=0
            dx=0
        if herokey>0:
            herokey-=1

    
    #In Mauer gelaufen?
    ziel=level[heroz][heroy+dy][herox+dx]
    if ziel =="#":
        print("AUA")
        dx=0
        dy=0
        
    #ziel=level[heroz][heroy+dy][herox+dx]
    if ziel =="M":
        print("Ein Monster blockiert deinen Weg")
        resultat=kampf()
        if resultat==0:
            level[heroz][heroy+dy][herox+dx]=random.choice(("s","s","s","s","s","s","k","$","?","?",".",".",".",".",".",".",".",".",".",".",".","#"))
        else:
            herohp-=random.randint(10,20)
            print("Das Monster tut dir weh")
            if herohp<1:
                print()
                print()
                print()
                print("Du wurdest getötet")
                break
        dx=0
        dy=0
    #Bewegung!
    herox+=dx
    heroy+=dy
    if command=="eat":
        if herow>0:
            herow-=1
            herohunger-=random.randint(10,20)
            herohp+=random.randint(5,10)
            if herohp>100:
                herohp=100
    if herohunger<0:
        print()
        print()
        print()
        print("Game Over! Du hast zu viel gegessen.")
        break
    if herohunger>50:
        print()
        print()
        print()
        print("Game Over! Du bist verhungert.")
        break
        
#-----------------Auswertung--------------------
    stuff=level[heroz][heroy][herox]
    if stuff=="$":
        print("HURA Geld gefunden")
        herogold+=random.randint(1,5)
        level[heroz][heroy][herox]="."
    if stuff=="?":
        print("OH Rätselkiste gefunden")
        kiste()
    if stuff=="p":
        print()
        print()
        print()
        print("Prinzessin gefunden! Du hast gewonnen!")
        break
    if stuff=="w":
        print("Mmmh lecker")
        herow+=1
        level[heroz][heroy][herox]="."
    if stuff=="*":
        print("Du hast einen Diamant gefunden")
        herogold+=random.randint(10,20)
        level[heroz][heroy][herox]="."
    if stuff=="s":
        print("Du hast eine Schokolade gefunden")
        herow+=5
        level[heroz][heroy][herox]="."
    if stuff=="k":
        herogold,herow=shop(herogold,herow)
    if stuff=="/":
        herokey+=1
        level[heroz][heroy][herox]="."
