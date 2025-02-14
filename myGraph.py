from graphics import *   #import the graphics.py module (must be in the same folder this file)

def chart():
    
    #OPEN THE WINDOW
    win = GraphWin("Histogram", 650,700)      
    win.setBackground("Mint Cream")          

    #main heading
    my_heading = Text(Point(100,30),'Histogram Results')
    my_heading.setSize(15)
    my_heading.draw(win)

    #headings
    text1 = Text(Point(100,625),'Progress')
    text1.draw(win)
    text1 = Text(Point(250,625),'Trailer')
    text1.draw(win)
    text1 = Text(Point(400,625),'Retriever')
    text1.draw(win)
    text1 = Text(Point(550,625),'Excluded')
    text1.draw(win)

    #line
    line = Line(Point(25,600),Point(625,600))
    line.draw(win)

    Pr_count = 20
    Tr_count = 15
    Re_count = 10
    Ex_count = 5

    max_height = 500
    max_count = max(Pr_count,Tr_count,Re_count,Ex_count)
    k = max_height/max_count
    Pr_height = Pr_count*k
    Tr_height = Tr_count*k
    Re_height = Re_count*k
    Ex_height = Ex_count*k


    #Rectangles          
    #box = Rectangle(Point(50,600),Point(150,600-Pr_height))
    #box.setFill('dark green')
    #box.draw(win)

    #box = Rectangle(Point(200,600),Point(300,600-Tr_height)) 
    #box.setFill('green')
    #box.draw(win)

    #box = Rectangle(Point(350,600),Point(450,600-Re_height))
    #box.setFill('light green')
    #box.draw(win)

    #box = Rectangle(Point(500,600),Point(600,600-Ex_height))
    #box.setFill('pink')
    #box.draw(win)


    #Rectangles
    space = 50
    def chart(height,color):
        box = Rectangle(Point(space,600),Point(space+100,600-height))
        box.setFill(color)
        box.draw(win)

    chart(Pr_height,'dark green')
    space += 150
    chart(Tr_height,'green')
    space += 150
    chart(Re_height,'light green')
    space += 150
    chart(Ex_height,'pink')


    #count text
    text = Text(Point(100,600-(Pr_height+20)),Pr_count)
    text.draw(win)
    text = Text(Point(250,600-(Tr_height+20)),Tr_count)
    text.draw(win)
    text = Text(Point(400,600-(Re_height+20)),Re_count)
    text.draw(win)
    text = Text(Point(550,600-(Ex_height+20)),Ex_count)
    text.draw(win)




    #win.getMouse()
    #win.close()

