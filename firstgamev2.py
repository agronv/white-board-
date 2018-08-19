import pygame
import random
pygame.init()


def hollow_rect(start_position, end_position, color, display):
# this function will be used in order to make hollow ractangles for my buttons
    size_list = [start_position,
                [end_position[0],start_position[1]],
                end_position,
                [start_position[0],end_position[1]],
                start_position]
    pygame.draw.lines(window,color,True,size_list)

def rainbowFunc():
#this is a rainbow function used to generate random colors
    c0 = random.randint(0,255)
    c1 = random.randint(0,255)
    c2 = random.randint(0,255)
    return [c0,c1,c2]

def transitionalFunc(color):
    if(len(color)==3):
        c0 = random.randint(0,255)
        c1 = random.randint(0,255)
        c2 = random.randint(0,255)
        c3 = random.randint(0,2)
        c4 = random.choice([-1,1])
        color = [c0,c1,c2,c3,c4,0]
        return color
    else:
        transitional_speed = 2
        if(color[5]==50):
            color[3] = random.randint(0,2)
            color[4] = random.choice([-1,1])
            color[5] = 0
        while(color[color[3]]+transitional_speed*color[4]>255 or
        color[color[3]]+transitional_speed*color[4]<0):
            color[3] = random.randint(0,2)
            color[4] = random.choice([-1,1])
            color[5] = 0
        color[color[3]] += transitional_speed*color[4]
        color[5] += 1
        return color

def buttons(window,color,shape):
#this is a function that will display my buttons
    #COLOR BUTTONS
    button_size = 50
    left_margin = 10
    upper_bound = 10
    left_bound = 75

    #COLORS
    black = [0,0,0]
    white = [255,255,255]
    red = [255,0,0]
    green = [0,255,0]
    blue = [0,0,255]
    grey = [200,200,200]

    if(color == white):
        color = grey

    #these are the buttons associated with color
    black_button = pygame.draw.rect(window,black,
    (left_margin,upper_bound,button_size, button_size))
    green_button = pygame.draw.rect(window,green,
    (left_margin,upper_bound+button_size,button_size, button_size))
    red_button = pygame.draw.rect(window,red,
    (left_margin,upper_bound+button_size*2,button_size, button_size))
    blue_button = pygame.draw.rect(window,blue,
    (left_margin,upper_bound+button_size*3,button_size, button_size))
    eraser_dime = [[left_margin,upper_bound+button_size*4],
                   [left_margin+button_size-1, upper_bound+button_size*5]]
    eraser = hollow_rect(eraser_dime[0],eraser_dime[1], black, window)
    eraser_inside = pygame.draw.rect(window,white,
    (left_margin+1,upper_bound+1+button_size*4,button_size-3, button_size-1))
    rainbow_button1 = pygame.draw.rect(window,blue,
    (left_margin,upper_bound+button_size*5+1,button_size*.34, button_size))
    rainbow_button2 = pygame.draw.rect(window,red,
    (left_margin+button_size*.34,upper_bound+button_size*5+1,button_size*.33, button_size))
    rainbow_button3 = pygame.draw.rect(window,green,
    (left_margin+button_size*.67,upper_bound+button_size*5+1,button_size*.34, button_size))
    for i in range(50):
        pygame.draw.rect(window,(255-5*i,255-5*i,255-5*i),
        (left_margin+button_size*.02*i, upper_bound+button_size*6+1,button_size*.02, button_size))

    #OPTION BUTTONS
    circle_dime = [[left_bound, upper_bound],
                  [left_bound+button_size, upper_bound+button_size]]
    circle_button =  hollow_rect(circle_dime[0],circle_dime[1], black, window)
    small_inside = pygame.draw.rect(window,white,(left_bound+1,upper_bound+1,button_size-1, button_size-1))
    circle_circle = pygame.draw.circle(window, [color[0],color[1],color[2]],
                    (left_bound+int(.5*button_size), upper_bound+int(.5*button_size)),int(.25*button_size))

    rect_dime = [[left_bound+button_size, upper_bound],
                 [left_bound+button_size*2, upper_bound+button_size]]
    rect_button =  hollow_rect(rect_dime[0],rect_dime[1], black, window)
    rect_inside = pygame.draw.rect(window,white,
    (left_bound+button_size+1,upper_bound+1,button_size-1, button_size-1))
    rect_rect = pygame.draw.rect(window,[color[0],color[1],color[2]],
                    (left_bound+button_size+int(.25*button_size), upper_bound+int(.25*button_size),
                     upper_bound+int(.35*button_size), upper_bound+int(.35*button_size)))

    # buttons associated with size
    small_dime = [[left_bound+button_size*2, upper_bound],
                 [left_bound+button_size*3, upper_bound+button_size]]
    small_button =  hollow_rect(small_dime[0],small_dime[1], black, window)
    small_inside = pygame.draw.rect(window,white,
    (left_bound+button_size*2+1,upper_bound+1,button_size-1, button_size-1))
    if(shape == 1):
        small_circle = pygame.draw.circle(window, [color[0],color[1],color[2]],
                   (left_bound+button_size*2+int(.5*button_size), upper_bound+int(.5*button_size)),3)
    else:
        small_rect = pygame.draw.rect(window, [color[0],color[1],color[2]],
                    (left_bound+button_size*2+int(.5*button_size)-1, upper_bound+int(.5*button_size)-1,3,3))

    med_dime = [[left_bound+button_size*3, upper_bound],
                 [left_bound+button_size*4, upper_bound+button_size]]
    med_button =  hollow_rect(med_dime[0],med_dime[1], black, window)
    med_inside = pygame.draw.rect(window,white,
    (left_bound+button_size*3+1,upper_bound+1,button_size-1, button_size-1))
    if(shape==1):
        med_circle = pygame.draw.circle(window, [color[0],color[1],color[2]],
                   (left_bound+button_size*3+int(.5*button_size), upper_bound+int(.5*button_size)),10)
    else:
        med_rect = pygame.draw.rect(window, [color[0],color[1],color[2]],
                   (left_bound+button_size*3+int(.5*button_size)-5, upper_bound+int(.5*button_size)-5,
                   10,10))

    big_dime = [[left_bound+button_size*4, upper_bound],
                 [left_bound+button_size*5, upper_bound+button_size]]
    big_button =  hollow_rect(big_dime[0],big_dime[1], black, window)
    big_inside = pygame.draw.rect(window,white,
    (left_bound+button_size*4+1,upper_bound+1,button_size-1, button_size-1))
    if(shape==1):
        big_circle = pygame.draw.circle(window, [color[0],color[1],color[2]],
                   (left_bound+button_size*4+int(.5*button_size), upper_bound+int(.5*button_size)),20)
    else:
        big_rect = pygame.draw.rect(window, [color[0],color[1],color[2]],
                   (left_bound+button_size*4+int(.5*button_size)-10, upper_bound+int(.5*button_size)-10,
                   20, 20))

def smallersize(size):
#this will be used to convert my size back to normal because the eraser sizes
# are larger than any other color
    if(size==11):
        return 3
    elif(size==31):
        return 10
    elif(size==75):
        return 20
    else:
        return size

def biggersize(size,color):
# the eraser size is bigger so we have to adjust
    if(color == [255,255,255]):
        if(size ==3):
            return 11
        elif(size ==10):
            return 31
        elif(size ==20):
            return 75
        else:
            return size
    else:
        return size


def printline(window, color,x,y,size,shape):
    if(shape==1):
        pygame.draw.circle(window,[color[0],color[1],color[2]],(x,y),size)
    else:
        pygame.draw.rect(window,[color[0],color[1],color[2]],(x-int(size*.5),y-(int(size*.5)),size, size))
################################################################################
################################################################################

#COLORS
black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
grey = [200,200,200]

#Window setting and display
screen_height = 750
screen_width = 1500
windowSize = [screen_width,screen_height]
window = pygame.display.set_mode(windowSize)
window.fill(white)
buttons(window,black,1)
pygame.display.set_caption("First Game")


#original size of line
size = 3
#original color
color = black
#this the the original shape of our line
shape = 1
#this will indicate whether or not anything has been drawn
action = 1
#original x and y coordinates
x = prevx = 50
y = prevy = 50
#speed at which or line travels
velocity = 1

#this will be used to create our buttons
button_size = 50
left_margin = 10
upper_bound = 10
left_bound = 75

#these will be used for the rainbow option notice that there are two different
#rainbows simply turn one true and the other one false to switch
rainbow = False
transitional = False


#this is our main loop
run = True
while run:
    # .002 seconds delay, makes the game less demanding while the performance isnt
    # affected that much
    pygame.time.delay(2)
    for event in pygame.event.get():
        #this occurs when we ht the x button
        if event.type == pygame.QUIT:
            run = False

        if(rainbow):
            color = rainbowFunc()
        #this event while occur when the left mouse button is clicked
        if pygame.mouse.get_pressed()[0]:
            x,y = event.pos
################################################################################
################################################################################
##this will check whether or not a button has been pressed, it is quit long
            if(((x>left_margin and x<left_margin+button_size) and
            (y>upper_bound and y<upper_bound+button_size*7)) or
              ((x>left_bound and x<left_bound+button_size*5) and
              (y>upper_bound and y<upper_bound+button_size))):

              # BLACK BUTTON
              if((x>left_margin and x<left_margin+button_size) and
              (y>upper_bound and y<upper_bound+button_size)):
                color = black
                size = smallersize(size)
                rainbow=False
                transitional = False
                action=1
                # GREEN BUTTON
              elif((x>left_margin and x<left_margin+button_size) and
              (y>upper_bound+button_size and y<upper_bound+button_size*2)):
                color = green
                size = smallersize(size)
                rainbow=False
                transitional = False
                action=1
                #RED BUTTON
              elif((x>left_margin and x<left_margin+button_size) and
              (y>upper_bound+button_size*2 and y<upper_bound+button_size*3)):
                color = red
                size = smallersize(size)
                rainbow=False
                transitional = False
                action=1
                # BLUE BUTTON
              elif((x>left_margin and x<left_margin+button_size) and
              (y>upper_bound+button_size*3 and y<upper_bound+button_size*4)):
                color = blue
                size = smallersize(size)
                rainbow=False
                transitional = False
                action=1
                # WHITE BUTTON. notice for the white button the size gets larger
              elif((x>left_margin and x<left_margin+button_size) and
              (y>upper_bound+button_size*4 and y<upper_bound+button_size*5)):
                color = white
                rainbow=False
                transitional = False
                action=1
                if(size==20):
                  size=75
                elif(size==10):
                  size=31
                else:
                  size=3
              #RAINBOW BUTTON
              elif((x>left_margin and x<left_margin+button_size) and
              (y>upper_bound+button_size*5 and y<upper_bound+button_size*6)):
                  rainbow = True
                  transitional = False
                  size = smallersize(size)
              #transitional Buttons
              elif((x>left_margin and x<left_margin+button_size) and
              (y>upper_bound+button_size*6 and y<upper_bound+button_size*7)):
                  transitional = True
                  rainbow = False
                  size = smallersize(size)

            #shape change buttons
              elif((x>left_bound and x<left_bound+button_size) and
              (y>upper_bound and y<upper_bound+button_size)):
                shape=1
                action=1
              elif((x>left_bound+button_size and x<left_bound+button_size*2) and
              (y>upper_bound and y<upper_bound+button_size)):
                shape=0
                action=1

            #size change buttons
              elif((x>left_bound+button_size*2 and x<left_bound+button_size*3) and
              (y>upper_bound and y<upper_bound+button_size)):
                size = 3
                size = biggersize(size,color)
              elif((x>left_bound+button_size*3 and x<left_bound+button_size*4) and
              (y>upper_bound and y<upper_bound+button_size)):
                  size = 10
                  size = biggersize(size,color)
              elif((x>left_bound+button_size*4 and x<left_bound+button_size*5) and
              (y>upper_bound and y<upper_bound+button_size)):
                size = 20
                size = biggersize(size,color)
              #we will not remember this event so our coordinates will go back to the previous one
              x = prevx
              y = prevy

################################################################################
################################################################################
#this will occur only when our mouse has not been clicked on a button or an arrow
# key has been pressed
            else:
                #we will indicate that an action has occured
                action = 1
                if(transitional):
                    color = transitionalFunc(color)
                # finally we will print the line
                printline(window, color,x,y,size,shape)


    if(pygame.key.get_pressed() and action==0):
        keys=pygame.key.get_pressed()
        # an action will only occur if we either press up,down,left, or right
        if keys[pygame.K_LEFT] and x>velocity:
            x-= velocity
            action = 1
        if keys[pygame.K_RIGHT] and x<screen_width-velocity:
            x+= velocity
            action = 1
        if keys[pygame.K_UP] and y>velocity:
            y -= velocity
            action = 1
        if keys[pygame.K_DOWN] and y<screen_height-velocity:
            y += velocity
            action = 1
        if(action == 1):
            if(transitional):
                color = transitionalFunc(color)
            printline(window,color,x,y,size,shape)

    if action ==1:
        # if we actually drew something than our window will update
        buttons(window,color,shape)
        pygame.display.update()
        prevx = x
        prevy = y
    action=0

pygame.quit()
