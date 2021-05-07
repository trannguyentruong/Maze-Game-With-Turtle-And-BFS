import turtle
from collections import deque

#Create turtle Object
cmd = turtle.Screen()
cmd.bgcolor('black')
cmd.title("Maze Game")
cmd.setup(700,700)

#Create array that will append block element
walls = []
lastPoint = []
ways = []

#Import gif for character and block
turtle.register_shape('Panda.gif') 
turtle.register_shape('Block.gif')
turtle.register_shape('Last.gif')
turtle.register_shape('Help.gif')
turtle.register_shape('Arrow.gif')

#Create Pen to draw graphic in terminal
class Draw(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.shape('Block.gif') 
        self.penup()
        self.speed(0)

#Create panda at the first point of maze
class Panda(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('Panda.gif')
        self.penup()
        self.speed(0)
    
    def go_up(self):
        move_to_x = panda.xcor()
        move_to_y = panda.ycor() + 24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    def go_down(self):
        move_to_x = panda.xcor()
        move_to_y = panda.ycor() - 24
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    def go_left(self):
        move_to_x = panda.xcor() -24
        move_to_y = panda.ycor()
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
    def go_right(self):
        move_to_x = panda.xcor() + 24
        move_to_y = panda.ycor() 
        if(move_to_x,move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

#Create a mark of the out point of maze
class outPoint(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.shape('Last.gif')
        self.penup()
        self.speed(0)

#draw help button for panda
class helpArrow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('Arrow.gif')
        self.penup()
        self.speed(0)
class helpButton(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape('Help.gif') 
        self.goto(-260,-268)
        if(self.xcor() == panda.xcor() and self.ycor() == panda.ycor()):
            self.hideturtle()

levels = [
    [1,'P',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],
    [1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],
    [1,1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1],
    [1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1],
    [1,1,1,0,1,1,0,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1],
    [1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1],
    [1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
    [1,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1],
    [1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,'L',1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)
            if(character == 1):
                pen.goto(screen_x,screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))
            if(character == 0 or character == 'L'):
                path.append((screen_x,screen_y))
            if(character =='P'):
                panda.goto(screen_x,screen_y)
            if(character == 'L'):
                outPoint.goto(screen_x,screen_y)
                outPoint.stamp()
                outX = screen_x
                outY = screen_y
                lastPoint.append((screen_x,screen_y))
def BFS(x,y):
    frontier.append((x,y))
    solution[(x,y)] = x,y
    space_x = [-24, 0, 24, 0, ]
    space_y = [0, -24, 0 , 24,]
    while frontier:
        x,y = frontier.popleft()
     # pop next entry in the frontier queue an assign to x and y location
        for i in range(4):
            if(x+space_x[i],y+space_y[i]) in path and (x+space_x[i], y+space_y[i]) not in visited:  # check the cell on the left
                cell = (x+space_x[i], y+ space_y[i])
                solution[cell] = x,y    # backtracking routine [cell] is the previous cell. x, y is the current cell
            #blue.goto(cell)        # identify frontier cells
            #blue.stamp()
                frontier.append(cell)   # add cell to frontier list
                visited.add((x+space_x[i],y+space_y[i]))  # add cell to visited list
                print(solution)

def backRoute(x, y):
    while (x, y) != (panda.xcor(), panda.ycor()):
        if((x,y) == (panda.xcor()-24,panda.ycor()) or (x,y) == (panda.xcor(),panda.ycor()-24) or (x,y) == (panda.xcor()+24,panda.ycor()) or (x,y) == (panda.xcor(),panda.ycor()+24)):
            break
        helpArrow.goto(solution[x, y])        # move the yellow sprite to the key value of solution ()
        helpArrow.stamp()
        x, y = solution[x, y]               # "key value" now becomes the new key
    helpArrow.clear()
def Finding(x,y):
    if(-272<=x <= -248):
        if(-278<=y<=-254):
            BFS(panda.xcor(),panda.ycor())
            backRoute(outPoint.xcor(),outPoint.ycor())
solution = {}
frontier = deque()
visited = set()
path = []

#Object oriented
pen = Draw()
panda = Panda()
outPoint = outPoint()
helpButton = helpButton()
helpArrow = helpArrow()
#Create maze
setup_maze(levels)
#Keyboard event
turtle.listen()
turtle.onkey(panda.go_left,'Left')
turtle.onkey(panda.go_right,'Right')
turtle.onkey(panda.go_up,'Up')
turtle.onkey(panda.go_down,'Down')


def main():
    turtle.onscreenclick(Finding)
    turtle.mainloop()
main()

cmd.tracer(0)
while True :
    cmd.update()

