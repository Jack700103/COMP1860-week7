import turtle, datetime
from itertools import islice

def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(50)
    drawGap()


def drawDigit(d):

    drawLine(True) if d[0] else drawLine(False)
    turtle.right(90)
    drawLine(True) if d[1] else drawLine(False)
    turtle.right(90)
    drawLine(True) if d[2] else drawLine(False)
    turtle.right(90)
    drawLine(True) if d[3] else drawLine(False)
    drawLine(True) if d[4] else drawLine(False)
    turtle.right(90)
    drawLine(True) if d[5] else drawLine(False)
    turtle.right(90)
    drawLine(True) if d[6] else drawLine(False)
    #turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def main():

    #each group has a code which defines how their segments align to the segments drwan by the turtle.
    #this is different for each group of students

    group_code = input("Enter your group code (on assignment sheet)")
    code = [eval(i) for i in group_code]

    turtle.speed("fastest")
    turtle.setup(800,350,200,200)
    turtle.penup()
    turtle.fd(-100)
    turtle.pensize(5)
    turtle.hideturtle()

    mapped_digit=[0,0,0,0,0,0,0]
    #read each line of file, one line per digit
   
    with open('Decoder.out','r') as fin:
        for line in list(islice(fin, 1, None)):
            segments = line.split("|")
            #remove leading "" then
            segments = segments[:-1]
            #skip input in
            segments = segments[2:]

            print(segments)

            #covert str to int
            digit = [eval(i) for i in segments]
            
            #reorder inputs to match turtles segments
            for i,d in enumerate(digit):
                mapped_digit[code[i]] = d
            
            #print(mapped_digit)
            turtle.hideturtle()

            drawDigit(mapped_digit)
            
            turtle.clearscreen()
            turtle.home()
            turtle.speed(10)
            turtle.penup()
            turtle.fd(-100)
            turtle.pensize(5)
            

    turtle.hideturtle()

main()