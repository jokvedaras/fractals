import graphics

#generally use numbers between -1 and 1 for randomiser
#remember to change the window scale and offset

#try : randomiser = -0.5 : y_offset = 1.114499259 : x_offset = 0.50015705

randomiser = 1
precision = 100
win_max = 200
scale = 100
y_offset = 0
x_offset = 0

#Create Graphics Window called "window" using size of win_max
win = graphics.GraphWin("window", win_max, win_max)

#iterate over size of graphics window
for num_y in range(0, win_max + 1):
    
    #We use this equation to get an offset and scale to the input of y
    y = (num_y/(scale)) - ((win_max/2)/scale) + y_offset

    #iterate again over size of graphics window for every pixel 200 * 200
    for num_x in range(0, win_max + 1):

        #Initiate check and count for every pixel on the Graphics Window
        count = 0
        check = 0

        #We use this equation to get an offset and scale to the input of x
        x = (num_x/(scale)) - ((win_max/2)/scale) + x_offset

        #This is the equation to calculate the magnitude of the point
        z = complex(x,y)**2 - randomiser

        #Run this while loop as many times as we put into precision
        while count < precision:

            #Use graphics Module to create a Point at x = num_x, y = num_y
            point = graphics.Point(num_x, num_y)

            #This is the equation to iterate over
            z = z**2 - randomiser

            #This value here effects the precision, increase it for better picture (careful you change the colours)
            if abs(z) > 1000000000000:

                #Store the number of counts required to reach this number **representing precision**
                check = count
                
                #count = precision to break the while loop
                count = precision

            #UPDATE WHILE LOOP
            count += 1
            
        #This first value is used to colour the the standard Mandelbrot set black
        if abs(z) <= 1:
            point.setFill("black")

        #These colors effect points by how quickly point escapes using the iteration
        elif check > 50:
            point.setFill("purple")           
            
        elif check > 40:
            point.setFill("blue")           
            
        elif check > 32:
            point.setFill("cyan")
            
        elif check > 26:
            point.setFill("white")

        elif check > 18:
            point.setFill("yellow")

        elif check > 15:
            point.setFill("orange")    
            
        elif check > 12:
            point.setFill("red")
            
        elif check > 9:
            point.setFill("orange")
            
        elif check > 7:
            point.setFill("yellow")

        elif check > 6:
            point.setFill("white")
            
        elif check > 4:
            point.setFill("cyan")

        else:
            point.setFill("blue")

        point.draw(win)
