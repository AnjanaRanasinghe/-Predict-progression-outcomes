    # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
    
    # Any code taken from other sources is referenced within my code soluƟon.
    
    # Student ID: 20231160

    # Date: 2023/12/01

    
from graphics import *   #import the graphics.py module (must be in the same folder this file)


def staff():

    Pr_count = 0
    Tr_count = 0
    Re_count = 0
    Ex_count = 0
    count = 0
    list = []

    def Histogram():
        
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

        try:
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
            total = Text(Point(150,650),(f"{(Pr_count+Tr_count+Re_count+Ex_count)} outcomes in total"))
            total.setSize(15)
            total.draw(win)

        except ZeroDivisionError:
             print('Count gets Zero') 

        #win.getMouse()
        #win.close()

    c = open("Scores.txt","w")
    c.close()

        
    while count>=0:
        while True:
            try:
                a1 = int(input('Please enter your PASS credits: '))
                if a1 not in range(0,121,20):
                    print("Out of range !")
                else:
                    break
            except ValueError:
                print('Enter valid integer')


        while True:
            try:
                a2 = int(input('Please enter your DEFER credits: '))
                if a2 not in range(0,121,20):
                    print("Out of range !")
                else:
                    break
            except ValueError:
                print('Enter valid integer')


        while True:
            try:
                a3 = int(input('Please enter your FAIL credits: '))
                if a3 not in range(0,121,20):
                    print("Out of range !")
                else:
                    break
            except ValueError:
                print('Enter valid integer')

                    
                
        if a1+a2+a3!=120:
            print('Total Incorrect !')
        else:      
            if a1==120:
                p = 'Progress'
                print(p)
                Pr_count +=1
                
            elif a1==100:
                p = 'Progress (module trailer)'
                print(p)
                Tr_count +=1
                
            elif a3>=80:
                p = 'Exclude'
                print(p)
                Ex_count +=1
                
            else:
                p = 'Do not progress – module retriever'
                print(p)
                Re_count +=1

        f = open("Scores.txt","a")
        b = (f"{p} - {a1}, {a2}, {a3}\n")
        f.write(b)
        f.close()


                                   
        print('\nWould you like to enter another set of data ?') 
        value = input("Enter 'y' for yes or 'q' to quit and view results: ")
        print()
        if value.lower() == 'q':
            count = -1
            Histogram()
            r = open("Scores.txt","r")
            print(r.read())
            
        elif value.lower() == 'y':
            count=count
        else:
            print('Invalid Option')
            count = -1
                    



            

            
def student():
    
        while True:
            try:
                a1 = int(input('Please enter your PASS credits: '))
                if a1 not in range(0,121,20):
                    print("Out of range !")
                else:
                    break
            except ValueError:
                 print('Enter valid integer')


        while True:
            try:
                a2 = int(input('Please enter your DEFER credits: '))
                if a2 not in range(0,121,20):
                    print("Out of range !")
                else:
                    break
            except ValueError:
                 print('Enter valid integer')


        while True:
            try:
                a3 = int(input('Please enter your FAIL credits: '))
                if a3 not in range(0,121,20):
                    print("Out of range !")
                else:
                    break
            except ValueError:
                 print('Enter valid integer')

                
            
        if a1+a2+a3!=120:
            print('Total Incorrect !')
        else:      
            if a1==120:
                print('\nProgress')
                
            elif a1==100:
                print('\nProgress (module trailer)')
                
            elif a3>=80:
                print('\nExclude')             
                
            else:
                print('\nDo not progress – module retriever')

                

count1 = 0
while count1>=0:
        try:
            n1 = input("This program allows to student & staff. What do you want to progress? 'student' or 'staff':  ")
            if n1 == 'student':
                count1 = -1
                student()
            elif n1 == 'staff':
                count1 = -1
                staff()
            else:
                print('Invalid Option !')
                count1 = count1
        except ValueError:
            print('Enter valid integer !')    
               





