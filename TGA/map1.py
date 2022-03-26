import beta_Jogo_15
import enemy


##      A B C          1  2  3
##      D E F    R     4  5  6      18
##    M G H I O  Q  13 7  8  9  15  17
##    N J K L P  S  14 10 11 12 16  19
##              T U               20 21

def mapa1(enemygroup):
    
    global mymap
    mymap = [
        "F                                                                                                                                                                                                                                                                                                                                           t                                               D",#6
        "F                                                                                                                                                                                                t      t                                                                                                                                JKKKKKKKKKKL                                       D",#7
        "F                                                                                                                                                                                            JKKBBBBBBBBBBKKL                                                                                                                                                                               D",#8
        "F                                                                                                                                                                                               NHTEEEEUHP                                                                                                                    JKKKKL                ABBBBBBBBBBBC                           D",#9
        "F                                                                                                                                                                                    ABC          NHTUHP                                                                                                   JKKKKKKKKKKKKL                           DEEEEEEEEEEEF                           D",#10
        "F                                                                                                                         X                                                          DEF            NP              ABBBBBBBBBBBC                                                                                                                   DEEEEEEEEEEEF                           D",#11
        "F                                                            R                                                   ABBBBBBBBBBBBBBBBBBBBBBBC                                 ABC       DEF                            DEEEEEEEEEEEIOC                                                                    R                                            DEEEEEEEEEEEF                           D",#12
        "F                           R                          R     Q                                                   DEEEEEEEEEEEEEEEEEEEEEEEF                                 DEF       DEF                            DEEEEEEEEEEEEEIOC                                                          R       Q                                            DEEEEEEEEEEEF                           D",#13
        "F              t      R     Q                    R     Q     Q                  R                       R        DEEEEEEEEEEEEEEEEEEEEEEEF               XXX               DEF       DEFXXXXXXXXXXXXXXXXXXXXXXXXXXXXDEEEEEEEEEEEEEEEIOC              t                            R            QXXXXXXXQXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXDEEEEEEEEEEEF                          ZD",#14
        "IOBBBBBBBBBBBBBBBBBBBMSOBBBMSOBBBBBBBBBBBBBBBBBBMSOBBBMSOBBBMSOBBBBBBBBBBBBBBBBMSOBBBBBBBBBBBBBBBBBBBBBMSOBBBBBBMGEEEEEEEEEEEEEEEEEEEEEEEF    ABBBBBBBBBBBBBBBBBBBBBBBBBBBMGEIOBBBBBMGEIOBBBBBBBBBBBBBBBBBBBBBBBBBBMGEEEEEEEEEEEEEEEEEIOC     JBBBBBBBBBBXBBBBBBL     ABBBBBBBBBBMSOBBBBBBBBBBMSOBBBBBMSOBBBBBBBBBBBBBBBBBBBBBBBBBBC   ABBBBBBBBBBBMGEEEEEEEEEEEIOBBBBBBBBBBBBBBBC   ABBBBBBG",#15
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF    DEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEIOC      NHEEEEEIBGEEHP     AMGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF   DEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF    DEEEEEE",#16
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF    DEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEIOC      NHEEEEEEHP     AMGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF   DEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEP   DEEEEEE",#17
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF    DEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEIOC      NHHHHP     AMGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF   DEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF   NEEEEEEE",#18
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEFXXXXDEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEIOC             AMGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF   NHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHEEEEEEEEEEEF    DEEEEEE",#19
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEIOBBMGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEIOBBBBBBBBBBBMGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF                                  TEEEEEEEEEEEP   DEEEEEE",#20
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF     tttttttttt                   DEEEEEEEEEEF   NEEEEEEE",#21
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF     tttttttttt         ABBBBBC   DEEEEEEEEEEF    DEEEEEE",#22
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF                      AMGEEEEEF   NHHHHHHHHHHHP   DEEEEEE",#23
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEIOBBBBBBBBBBBBBBBBBBBBMGEEEEEEEF                  DEEEEEEE",#24
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF                  DEEEEEEE",#25
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEIOBBBBBBBBBBBBBBBBMGEEEEEEE"] #26

    enemygroup.add(enemy.enemy_1(32 * 90, 32 * 7))
    enemygroup.add(enemy.enemy_1(32 * 363, 32 * 19))
    enemygroup.add(enemy.enemy_2(32 * 25, 32 * 7))


def mapa2(enemygroup):

    global mymap
    mymap = [
        "EHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHE",  # 0
        "F                                                                                                                                               Qt                         t                                                             t        D",  # 1
        "F                                                                NHHHHP         NHHHHP                                 NHHHHP                   DP   EP          t         H                                       NHHHP                 H        D",  # 2
        "F                                         NHHHHP                                                     NHHHP                                      Q   NF           H                    t                                                           D",  # 3
        "F                                                       NHHHHP                                                                                  Q    Q                             NHHHHHHP           NHHHP               NHHHHHHHHHP             D",  # 4
        "F                                  NHHHHP                                             NHHHHP                                       NHHHHHP      DP   Q                 H                                                                          Z",  # 5
        "F                                                                     NHHHHP                                 NHHHHHP                            Q   NF     H                                              t                                       D",  # 6
        "EHHHHHHHHHHEEF             NHHHHF                  NHHHP                                                                                        Q    Q                                      NHHHHP        H           NHHHP      H       NHHHHP   D",  # 7
        "F          DEF                  Q                                                                 GEEEEI                   GEEEEEEEEI                Q   H                    H                                                                   D",  # 8
        "F   t      DEEHHHHHHP           NHHHHHHEHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHP     NF                                                                                            D",  # 9
        "F          NHP                         H                                                            t                                                Q           H                                           NHHP             NHHHHP              D",  # 10
        "F                      NHHHP                H       H     H                        H                   H     X    X   X                 X  X H  DXXXXQ                                                                               t            D",  # 11
        "F                                   NHHHP       H            t     H     H     H                  H          NHP  NP  NP       X H     NHHHP    DEEEEF          H        H              NHHHHHHHHHHP                               NHHP           D",  # 12
        "F          DEF    DEEEEEEEEEEEEF                             Q                        Q     Q          Q                     DEF    XDF         DEEEEFt   Q                                                 DEEEEEF                               D",  # 13
        "F          DEFXXXXDEEEEEEEEEEEEFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXQXXXXXXXXXXXXXXXXXXXXXXXXQXXXXXQXXXXXXXXXXQXXXXXXXXXXXXXXXXXXXXXDEFXXXXDEFXXXXXXXXXDEEEEEFXXXQXXXXXXXXXXXXXXXXDEEEEEEEEEEEEEEEEEEEEEFXXXXXXXXXXDEEEEEFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXD",  # 14
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEESEEEEEEEEEEEEEEEEEEEEEEEESEEEEESEEEEEEEEEESEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"] # 15

    enemygroup.add(enemy.enemy_1(32 * 46, 32 * 7))
    enemygroup.add(enemy.enemy_1(32 * 73, 32 * 7))
    enemygroup.add(enemy.enemy_1(32 * 116, 32 * 7))
    enemygroup.add(enemy.enemy_1(32 * 8, 32 * 13))


def mapa3(enemygroup):

    global mymap
    mymap = [
        "EHHHHEEEEEEEEEEEEHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHEHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHEEEEEEEHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHE",#0
        "F    DEEEEEEEEEEP                              Q                                                                DEEEEEF                    ttt                                                                                           tt    D",#1
        "F    DHHHHHHHHHP                          H    Q                                 t   NEEEEEEEEHHHHHHHHHHHHHHHP  DEEEEEF    t     H    DEEHHHHHHP        X                                                                       X       NHHHHF D",#2
        "F    Q                Q   X     Q              Q                                 H    DEEEEEEF                  DEEEEEF    H          DEF           NHHHHHHHP          X    X                                       XX       NHHHHP          Q D",#3
        "F    Q          NP   NHHHHHHHHHHF      H       Q                                      DEEEEEEEHHP NHHHHHHHHHHHHEEEEEEEF               DEF                          NHHHHHHHHHHP      X    XX   t                  NHHHHP                     Q D",#4
        "F    Q  NHP                     Q              Q                               H      DEEEEEEF                 NEEEEEEF  H            DEF                                            NHHHHHHHHHP         XXX                                 Q D",#5
        "F    Q               NP         Q H       H    Q           NP                         DEEEEEEF       X    X     DEEEEEF              NEEF                                                             DEEEEEEEF                              Q D",#6
        "F    Q     Q                    Q              Q                  Q     Q   H         DEEEEEEEHHHHEHHHHHHHHHHP  DEEEEEF  NHP          DEFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXDEEEEEEEFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXQ D",#7
        "F    DHHHHHHP                   Q     H        Q    NP            NHHHHHP             DEEEEEEF    Q             DEEEEEF               DEEHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHP D",#8
        "F    Q                          Q           t  Q                                      DEEEEEEF    Q    Q        DEEEEEF    NP        NEEF                         Q     Q                                                                      D",#9
        "F    Q   NHHHHP      X     H    Q           H  Q       DP                             DEEEEEEFt   Q    Q    Q   DEEEEEF               DEF                         Q     Q                                                                      D",#10
        "F    Q            NHHHHP        Q     X        Q       Q   t     Q                    DEEEEEEF         Q    Q   DEEEEEF               DEF                         Qt                                                                     t     D",#11
        "F    Q      X                   Q     H        Q       NHHHHHHHHHP   H                DEEEEEEF         QXXXXQ   DEEEEEF             DEEEF                         Q                                            Q                        DHHHHP D",#12
        "F    Q    NHHHHHP               Q           H  Q                          NP          DEEEEEEEEF  NHHHHHHHHHHHHHHHHHHHP           DEEEEEF                         Q XX  Q                                      Q                        Q      D",#13
        "F    Qt                 t       Q              Q                                  NP  DEEEEEEEEF                             XXDEEEEEEEEF                           NHHHSHHHHHP                                Q      Q                 Q      D",#14
        "F    DHHP             NHHHHP    Q        H     Q                                      DEEEEEEEEF              NEEEEHHHHHHHHHHHHHHHHHHHHHP                                          Q                           Q      Q                 Q      D",#15
        "F    Q                          Q    X         Q   t                         t       NEEEEEEEEEF           H   DEEF                                                                Q                           Q      Q      Q          Q      D",#16
        "F    NHHHHHHHHP   H             Q    H         Q NHHHHP                  NHHHHHHP     DEEEEEEEEF     H         DEEF        t                                       Q               QX                          Q      Q      Q          Q      D",#17
        "F                   X           Q              Q                    NP                DEEEEEEEEF               DEEF      NHHEP                          Q          Q               DHHP                        Q      Q      Q          Q      D",#18
        "F                 NHHHHP      NHF          H   Q                                      DEEEEEEEEF               DEEF         Q                  Q        Q          Q               Q                    Q      Q      Q      Q          Q      D",#19
        "F          NHHP                 Q       X                    NHHHP                    DEEEEEEEEF           H   DEEF         Q     X  X         Q        Q          Q               Q       Q            Q      Q      Q      Q          Q      D",#20
        "F                               Q       H                                             DEEEEEEEEF   t   H       DEEF         NHHHHHHHHHHP       Q        Q          Q               Q       Q            Q      Q      Q      Q          Q      D",#21
        "F                  NHHHHP   NHHHF                      NHP                            DEEEEEEEEF   H           DEEF                            Q        Q          Q               Q       Q      Q     Q      Q      Q      Q          Q      D",#22
        "F                               Q   Q                                                 DEEEEEEEEF        XX     DEEFXXXXXX  Z   XXXXXXXXXXXXXXXXQXXXXXXXXQXXXXXXXXXXQXXXXXXXXXXXXXXXQXXXXXXXQXXXXXXQXXXXXQXXXXXXQXXXXXXQXXXXXXQXXXXXXXXXXQXXXXXXD",#23
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEESEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEESEEEEEEEESEEEEEEEEEESEEEEEEEEEEEEEEESEEEEEEESEEEEEESEEEEESEEEEEESEEEEEESEEEEEESEEEEEEEEEESEEEEEEE"]#24

    enemygroup.add(enemy.enemy_1(32 * 12, 32 * 21))
    enemygroup.add(enemy.enemy_1(32 * 10, 32 * 6))
    enemygroup.add(enemy.enemy_1(32 * 70, 32 * 6))
    enemygroup.add(enemy.enemy_1(32 * 62, 32 * 10))
    enemygroup.add(enemy.enemy_1(32 * 75, 32 * 21))

def mapa4(enemygroup):
    global mymap
    mymap = [
        "EHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",# 1
        "F                                                                                                                       DEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",# 2
        "F                                                                                                                       DEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",# 3
        "EHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHEHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHEEEEEEEEEEEEEEEF   NHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHE",# 4
        "F                               Q                                                                    DEEEEEEEEEEEEEEF                                                                                                             D",# 5
        "F                               Q                H                             NHHHP NEEEEEEF        DEEEEEEEEEEEEEEF                            H                                                                  H             D",# 6
        "Z                         H     Q   Q NHHHP       Q       Q                           DEEEEEF  NHP   DEEEEEEEEEEEEEEF                                                    H                       H                                D",# 7
        "F                               DP  Q             NHHHHHHHP           NHHHHP        NHEEEEEEF        NHHHHHHHHHEEEEEF                                           t                           t                   H                 D",# 8
        "F    NHHP                    H  Q   Q                             XX                  DEEEEEF                  DEEEEF                 H              H      H   H                           H                                     D",# 9
        "F                  X            Q  ND      H                   NHHHHHP           NP   DEEEEEF   NHHHP     NHHP DEEEEF                             X                              NP                                      H   H    D",# 10
        "F       NHP     NHHHP           Q   Q                                                 DEEEEEF                  DEEEEF           H                 Q                                    Q            H   H       H                 D",# 11
        "F                            H  Q   Q        NHHP                                   NHEEEEEEF                  DEEEEFXXXDEFXXXXXXXXXXXXXXXXXXXXXXXQXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXQXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  D",# 12
        "F           NHP                 DP  Q                                   NHHHP         DEEEEEF               DEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF  D",# 13
        "F                          H    Q   Q                 NHHHP                      NP   DEEEEEF            NHHEEEEEHHHHHHHHHHHHEHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHEEF  D",# 14
        "F                               Q   Q       X                                         DEEEEEF   XX          DEEEF            Q                                                     t                                         DEF  D",# 15
        "F                     H            NF   NHHHP                                       NHEEEEEEF   NHHP        DEEEF      Q    NQ                                                     H                         NHHHEEEEF       DEF  D",# 16
        "F                               Q   Q                        NHHHP                    DEEEEEF               DEEEF      Q     Q                                     NHHHHHHP                                      DEEEEEEEEP  DEF  D",# 17
        "F        X     NHHHP            Q   Q                                            NP   DEEEEEF               DEEEF      Q     Q     NHHHHHP         t                                                             DEEEEEEEF   DEF  D",# 18
        "F     NHHHP                     DP  Q                                               NHEEEEEEFXX     NHHP    DEEEF      Q    NQ                 NHHHHHHHHHP                         H                             DEEEEEEEF   DEF  D",# 19
        "F                               Q   Q           NHHHP                                 DEEEEEEHHP            DEEEF      Q     Q                                                              NHHHHHHHHP           DEEEEEEEEP  DEF  D",# 20
        "EP                              Q   Q                                            NP   DEEEEEF             DEEEEEF      Q     Q   Q                                                                               DEEEEEEEF   DEF  D",# 21
        "F                      Q     Q  Q  NF                        NHHHHHHHHHP              DEEEEEF           XXDEEEEEF      Q    NQ   Q                                                                               DEEEEEEEF   DEF  D",# 22
        "F                      NHHHHHP  Q   Q                                               NHEEEEEEF      NHHHHHHHHHHHHP      Q     Q   Q                                                                               DEEEEEEEEF  NHP  D",# 23
        "EF           XXXX               Q   Q                                                 DEEEEEFXXXXX                   XXQ         Q                                                                               DEEEEEEEEF       D",# 24
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEF      DEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEESEEEEEEEEESXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXDEEEEEEEEEEEEEEEEE",# 25
        "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"]# 26

    enemygroup.add(enemy.enemy_1(32 * 55, 32 * 6))
    enemygroup.add(enemy.enemy_1(32 * 27, 32 * 21))
    enemygroup.add(enemy.enemy_1(32 * 42, 32 * 21))
    enemygroup.add(enemy.enemy_2(32 * 141, 32 * 7))
    enemygroup.add(enemy.enemy_2(32 * 165, 32 * 8))

# ««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««««
def maps(level, enemygroup):

    if level == 1:
        mapa1(enemygroup)

    elif level == 2:
        mapa2(enemygroup)

    elif level == 3:
        mapa3(enemygroup)

    elif level == 4:
        mapa4(enemygroup)

    else:
        beta_Jogo_15.menu_intro()
