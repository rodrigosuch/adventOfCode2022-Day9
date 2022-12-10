import turtle as t


def init_knots(num):
    for _ in range(0,num):
        knot = t.Turtle()
        knot.shapesize(stretch_len=0.5, stretch_wid=0.5)
        knot.penup()
        knot.shape("circle")
        knot.color("red")
        knot.speed(0)
        knots.append(knot)
        knot.hideturtle()


def run_tail_step(h, t):
    if ((h.ycor() - t.ycor() >= 1 or h.ycor() - t.ycor() <= -1) and \
            (h.xcor() - t.xcor() > 1 or h.xcor() - t.xcor() < -1)) or \
        ((h.ycor() - t.ycor() > 1 or h.ycor() - t.ycor() < -1) and \
         (h.xcor() - t.xcor() >= 1 or h.xcor() - t.xcor() <= -1)):
        if h.ycor() - t.ycor() >= 1:
            t.sety(t.ycor() + 1)
        elif h.ycor() - t.ycor() <= -1:
            t.sety(t.ycor()-1)

        if h.xcor() - t.xcor() >= 1:
            t.setx(t.xcor() + 1)
        elif h.xcor() - t.xcor() <= -1:
            t.setx(t.xcor() - 1)

    elif h.ycor() - t.ycor() > 1 or h.ycor() - t.ycor() < -1:
        if h.ycor() - t.ycor() > 1:
            t.sety(t.ycor()+1)
        elif h.ycor() - t.ycor() < -1:
            t.sety(t.ycor()-1)
    elif h.xcor() - t.xcor() > 1 or h.xcor() - t.xcor() < -1:
        if h.xcor() - t.xcor() > 1:
            t.setx(t.xcor()+1)
        elif h.xcor() - t.xcor() < -1:
            t.setx(t.xcor()-1)


def run_head_step(direction, h):

    if direction == "U":
        h.sety(h.ycor() + 1)
    elif direction == "D":
        h.sety(h.ycor() - 1)
    elif direction == "R":
        h.setx(h.xcor() + 1)
    elif direction == "L":
        h.setx(h.xcor() - 1)


def run_head_line(direction, numsteps):

    for _ in range(0,int(numsteps)):
        run_head_step(direction, knots[0])
        for n in range(0, len(knots)-1):
            run_tail_step(knots[n], knots[n + 1])
        if (knots[9].xcor(), knots[9].ycor()) not in tailpositions:
            tailpositions.append((knots[9].xcor(), knots[9].ycor()))


knots = []
tailpositions = []
screen = t.Screen()
screen.setup(500, 500)
t.tracer(n=10, delay=1000)
file1 = open("commands.txt", "r")
lines = file1.readlines()
init_knots(10)

for l in lines:
    line = l.split(" ")
    run_head_line(line[0], line[1])

print(len(tailpositions))
