from graphics import*
Jugadores = ['Draw', 'O', 'X']
DRAW = PLAYERS.index('Draw')
#Colores de las líneas, de las X y de los O
Colores = ['black', 'blue', 'red']
window = GraphWin("X y O", 700, 700)
Cuadro = 0
Line(Point(250, 50), Point(250, 650)).draw(window)
Line(Point(450, 50), Point(450, 650)).draw(window)
Line(Point(50, 250), Point(650, 250)).draw(window)
Line(Point(50, 450), Point(650, 450)).draw(window)
turno = Jugadores.index('X')
scores = [0] * len(Jugadores)
tokens = []
while sum(scores) < 10:
    for token in tokens:
        token.undraw()
    board = [[Cuadro, Cuadro, Cuadro], [Cuadro, Cuadro, Cuadro], [Cuadro, Cuadro, Cuadro]]