import pygame
import datetime

pygame.init()
isDone = True
white = (255, 255, 255)
screen = pygame.display.set_mode((450, 400))
screen.fill(white)
clock = pygame.image.load("images/mickeyWithoutArms.png")
leftArmIMAGE = pygame.image.load("images/leftarm.png")
rightArmIMAGE = pygame.image.load("images/rightarm.png")
pygame.display.update()

leftArmAngle = 0
rightArmAngle = 0
leftArmSecondImage = pygame.transform.scale(leftArmIMAGE, (20, leftArmIMAGE.get_height() // 3 - 20))
rightArmMinuteImage = pygame.transform.scale(rightArmIMAGE, (rightArmIMAGE.get_width() // 3,rightArmIMAGE.get_height() // 3))
print(datetime.datetime.now())
while isDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
            pygame.quit()
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    leftArmAngle = second * (-6)
    rightArmAngle = (minute+10) * (-6)

    clock1 = pygame.transform.scale(clock, (clock.get_width() // 3, clock.get_height() // 3))
    screen.blit(clock1, (0, 0))

    left = pygame.transform.rotate(leftArmSecondImage, leftArmAngle)
    leftIMAGE = left.get_rect(center=(230, 175))

    right = pygame.transform.rotate(rightArmMinuteImage, rightArmAngle)
    rightIMAGE = right.get_rect(center=(230, 175))

    screen.blit(left, leftIMAGE.topleft)
    screen.blit(right, rightIMAGE.topleft)


    pygame.display.update()
    pygame.display.flip()
    
import pygame
pygame.mixer.init()
pygame.init()
running=True
screen=pygame.display.set_mode((800,750))
gopsygirl=pygame.transform.scale(pygame.image.load("images/gopsygirl.jpg"),(800,750))
life=pygame.transform.scale(pygame.image.load("images/life.jpg"),(800,750))
spiderman=pygame.transform.scale(pygame.image.load("images/spiderman.jpg"),(800,750))
arrP=[gopsygirl,life,spiderman]
arrM=[
"C:/Users/allmo/OneDrive/Documents/GUKASH CRASH/songs/Flashing light   Kany West.mp3",
"C:/Users/allmo/OneDrive/Documents/GUKASH CRASH/songs/kendrick-lamar-sza-luther.mp3",
"C:/Users/allmo/OneDrive/Documents/GUKASH CRASH/songs/14. The Weeknd & Kendrick Lamar - Pray for Me.mp3"
]
index=0
pygame.mixer.music.load(arrM[index])
pygame.mixer.music.play()
paused=False
while running:
    screen.blit(arrP[index], (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                index=(index+1)%3
                pygame.mixer.music.load(arrM[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_a:
                index = (index - 1) % 3
                pygame.mixer.music.load(arrM[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()

import pygame
pygame.init()
running=True
screen=pygame.display.set_mode((500,500))
fon=(255,255,255)
screen.fill(fon)
cordX=250
cordY=250
while running:
    screen.fill(fon)
    pygame.draw.circle(screen,"red",(cordX,cordY),25)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w and cordY>15:
                    cordY-=20
            if event.key==pygame.K_s and cordY<485:
                    cordY+=20
            if event.key==pygame.K_d and cordX<485:
                    cordX+=20
            if event.key==pygame.K_a and cordX>15:
                    cordX-=20
 