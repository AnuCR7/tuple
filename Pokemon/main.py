import pgzrun
from random import randint
WIDTH=500
HEIGHT=500
TITLE='Ash and Pikachu'

score= 0
gameover=False
startscreen=True

Sprite= Actor ('ash')
Sprite1= Actor ('pikachu')
def draw ():
    if startscreen:
        screen.fill('blue')
        screen.draw.text('Catch Pikachu',center=(WIDTH/2,HEIGHT/2),fontsize=30,color='white')
        screen.draw.text('Press SPACE to start',center=(WIDTH/2,HEIGHT/2+50),fontsize=25,color='white')
    else:
        screen.clear()
        screen.blit('background',(0,0))
        Sprite.draw()
        Sprite1.draw()
        screen.draw.text('score= '+str(score),midtop=(WIDTH/2,10),fontsize=40,color='WHITE')
        if gameover==True:
            screen.fill('blue')
            screen.draw.text('time up your final score is '+str(score),midtop=(WIDTH/2,10),fontsize=40,color='WHITE')
            timeup()

def placeash ():
    Sprite.x=randint(50,(WIDTH-50))
    Sprite.y=randint(50,(HEIGHT-50))
placeash()

def placepikachu ():
    Sprite1.x=randint(50,(WIDTH-50))
    Sprite1.y=randint(50,(HEIGHT-50))
placepikachu()

def timeup():
    global gameover
    gameover=True

def update():
    global score
    global startscreen
    if startscreen:
        if keyboard.space:
            startscreen=False
    if keyboard.left:
        Sprite.x=Sprite.x-5
    if keyboard.right:
        Sprite.x=Sprite.x+5
    if keyboard.up:
        Sprite.y=Sprite.y-5
    if keyboard.down:
        Sprite.y=Sprite.y+5
        
    if Sprite.colliderect(Sprite1):
        placepikachu()
        score=score+1
    


clock.schedule(timeup,60.0) 
    

pgzrun.go()