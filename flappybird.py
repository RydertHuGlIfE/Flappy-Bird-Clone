import pygame
import sys
import pyttsx3


pygame.init()
pygame.mixer.get_init()
pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 2, buffer = 1024)


width = 287
height = 512
basex = 0
FPS = 70
pipex = 400
pipexx = 700
pipex3 = 1000
pipex4 = 1300
keys = pygame.key.get_pressed()
game_active = True
game_active = globals
game_paused = False
scorebird = 0 
high_score = 0
colorchange = True


def infinitybase(): #null parameter
    screen.blit(base, (basex, 400))
    screen.blit(base, (basex + 289, 400))
def looppipe1():
    screen.blit(pipe_good, pipe_rect) 
    screen.blit(pipe_ivt, pipe_rect_sec)

def looppipe2():
    screen.blit(pipe_good, pipe_rect_third)
    screen.blit(pipe_ivt, pipe_rect_four)
def looppipe3():
    screen.blit(pipe_good, pipe_rect_five)
    screen.blit(pipe_ivt, pipe_rect_six)
def looppipe4():
    screen.blit(pipe_good, pipe_rect_sev)
    screen.blit(pipe_ivt, pipe_rect_eght)
def collidecheck1():
    if bird_rect.colliderect(pipe_rect):
        diesound.play()      
        return False
    if bird_rect.colliderect(pipe_rect_sec):
        diesound.play()
        return False
    if bird_rect.colliderect(pipe_rect_third):
        diesound.play()
        return False
    if bird_rect.colliderect(pipe_rect_four):
        diesound.play()
        return False
    if bird_rect.colliderect(pipe_rect_five):
        diesound.play()
        return False
    if bird_rect.colliderect(pipe_rect_six):
        diesound.play()
        return False  
    if bird_rect.colliderect(pipe_rect_third):
        diesound.play()
        return False
    if bird_rect.colliderect(pipe_rect_third):
        diesound.play()
        return False
    if bird_rect.top <= -50 or bird_rect.bottom >= 400:
        diesound.play()
        return False
    return True
def scoresurface():
    score_surface = game_font.render(str(int(scorebird)),True,(255,255,255))
    score_rect = score_surface.get_rect(center = (150,80))
    screen.blit(score_surface,score_rect)
def blur_screen():
    blur_surface.blit(screen, (0, 0))
    screen.blit(pygame.transform.scale(blur_surface, (width, height)), (0, 0))
def rotate_bird(bird):
	new_bird = pygame.transform.rotozoom(bird,-bird_movement * 4,1)
	return new_bird
def bird_animation():
	new_bird = bird_frames[bird_index]
	new_bird_rect = new_bird.get_rect(center = (50,bird_rect.centery))
	return new_bird,new_bird_rect
def retstarting_game():
    if game_active == False:
        screen.blit(restartscreen, (50, 35))
def scorefisd():
    if game_active == False:
        score_surface = game_font.render(f'Score: {int(scorebird)}' ,True,(255,255,255))
        score_rect = score_surface.get_rect(center = (150,80))
        screen.blit(score_surface,score_rect) 

def bird_select():
    if game_active == False:
        print("Select Bird")
        a = str(input ("Please Select Bird"))
        print("1 - yellowbird")
        print("2 - bluebird")
        print("3 - redbird")
        if a == "1":
            birdupflap = pygame.image.load("Assets/sprites/yellowbird-upflap.png")
            birdmidflap = pygame.image.load("Assets/sprites/yellowbird-midflap.png")
            birddownflap = pygame.image.load("Assets/sprites/yellowbird-downflap.png")

        if a == "2":
            birdupflap = pygame.image.load("Assets/sprites/yellowbird-upflap.png")
            birdmidflap = pygame.image.load("Assets/sprites/redbird-midflap.png")
            birddownflap = pygame.image.load("Assets/sprites/bluebird-downflap.png")

        if a =="3":
            birdupflap = pygame.image.load("Assets/sprites/yellowbird-upflap.png")
            birdmidflap = pygame.image.load("Assets/sprites/redbird-midflap.png")
            birddownflap = pygame.image.load("Assets/sprites/bluebird-downflap.png")



screen = pygame.display.set_mode((width, height))
BIRDFLAP = pygame.USEREVENT + 1
birdupflap = pygame.image.load("Assets/sprites/yellowbird-upflap.png")
birdmidflap = pygame.image.load("Assets/sprites/redbird-midflap.png")
birddownflap = pygame.image.load("Assets/sprites/bluebird-downflap.png")
bird_frames = [birdupflap, birdmidflap, birddownflap]
bird_index = 0
windowname = pygame.display.set_caption("Flappy Bird 2.0")
back_img = pygame.image.load("Assets/sprites/background-day.png")
night_back_img = pygame.image.load("Assets/sprites/background-night.png")
blur_surface = pygame.Surface((width, height))
blur_amount = 5
blur_surface.set_alpha(blur_amount)
clock = pygame.time.Clock()
base = pygame.image.load("Assets/sprites/base.png")
bird = bird_frames[bird_index + 1]
pygame.time.set_timer(BIRDFLAP,200)
bird_rect = bird.get_rect(center = (50, 256))
pipe_good = pygame.image.load("Assets/sprites/pipe-green.png")
pipe_ivt = pygame.image.load("Assets/sprites/pipedown.png")
pipe_rect = pipe_good.get_rect(center = (pipex, 0))
pipe_rect_sec = pipe_ivt.get_rect(center = (pipex, 450))
pipe_rect_third = pipe_good.get_rect(center = (pipexx, -20))
pipe_rect_four = pipe_ivt.get_rect(center = (pipexx, 400))
pipe_rect_five = pipe_good.get_rect(center = (pipex3, -100))
pipe_rect_six = pipe_ivt.get_rect(center = (pipex3, 350))
pipe_rect_sev = pipe_good.get_rect(center = (pipex4, 350))
pipe_rect_eght = pipe_ivt.get_rect(center = (pipex4, 350))
game_over = pygame.image.load("Assets/sprites/gameover.png")
bird_flap_sound = pygame.mixer.Sound("Assets/audio/wing.wav")
diesound = pygame.mixer.Sound("Assets/audio/hit.wav")
pointsound = pygame.mixer.Sound("Assets/audio/point.wav")
restartscreen = pygame.image.load("Assets/sprites/message.png")
game_font = pygame.font.Font('04B_19.ttf',20)
BIRDFLAP = pygame.USEREVENT + 1
gravity = 0.20
bird_movement = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird,bird_rect = bird_animation()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                scorebird = 0
                bird_rect.centery = 150
                bird_movement = 0
                pipe_rect.centerx = 500 
                pipe_rect_sec.centerx = 500 
                pipe_rect_third.centerx = 800 
                #this code is made by varun chauhan :)   [before chatgpt so I am proud of it :D]
                pipe_rect_four.centerx = 800 
                pipe_rect_five.centerx = 1100 
                pipe_rect_six.centerx = 1100 
                pipe_rect_sev.centerx = 1400
                pipe_rect_eght.centerx = 1400
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_paused = not game_paused

        if scorebird > 50:
            FPS = 120
        if game_active == False:
            FPS = 70


        if scorebird > 90:
            FPS = 200
        if game_active == False:
            FPS = 70

    
        if event.type == BIRDFLAP:                          
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
                bird_surface,bird_rect = bird_animation()

    if game_active and not game_paused:
        screen.blit(back_img, (0, 0))
        
        screen.blit(base, (basex, 400))
        looppipe1()
        looppipe2()
        looppipe3()
        looppipe4()
        bird_select()
        scoresurface()
        scorefisd()
        rotated_bird = rotate_bird(bird)
        screen.blit(rotated_bird,bird_rect)
        collidecheck1()
        game_active = collidecheck1()
        

        if 95 < pipe_rect.centerx < 100:
            pointsound.play()
            scorebird += 1

        if 95 < pipe_rect_third.centerx < 100:
            pointsound.play()
            scorebird += 1

        if 95 < pipe_rect_five.centerx < 100:
            pointsound.play()
            scorebird += 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RALT:
                bird_movement = 0
                bird_movement -= 4.8
        bird_movement += gravity
        bird_rect.centery += bird_movement
        pipe_rect.centerx -= 3
        pipe_rect_sec.centerx -= 3
        pipe_rect_third.centerx -= 3
        pipe_rect_four.centerx -= 3
        pipe_rect_five.centerx -= 3
        pipe_rect_six.centerx -= 3

        FPS1 = clock.tick(FPS)

        if pipe_rect.centerx <= -300:
            pipe_rect.centerx = 500

        if pipe_rect_sec.centerx <= -300:
            pipe_rect_sec.centerx = 500

        if pipe_rect_third.centerx <= -300:
            pipe_rect_third.centerx = 500

        if pipe_rect_four.centerx <= -300:
            pipe_rect_four.centerx = 500

        if pipe_rect_five.centerx <= -300:
            pipe_rect_five.centerx = 500

        if pipe_rect_six.centerx <= -300:
            pipe_rect_six.centerx = 500

        if basex <= -289:
            basex = 0
            
        infinitybase()
#if game closes
    else:
        screen.blit(back_img, (0, 0))
        retstarting_game()
        high_score_surface = game_font.render(f'High score: {int(high_score)}',True,(0,0,0))
        high_score_rect = high_score_surface.get_rect(center = (75,355))   
        screen.blit(high_score_surface,high_score_rect)
        score_surface = game_font.render(f'Score: {int(scorebird)}' ,True,(0,0,0))
        score_rect = score_surface.get_rect(center = (240,355))
        screen.blit(score_surface,score_rect)
        pipe = pygame.image.load("Assets/sprites/pipe-green.png")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                if event.type == pygame.KEYDOWN:
                    birdupflap = pygame.image.load("Assets/sprites/bluebird-upflap.png")
                    birdmidflap = pygame.image.load("Assets/sprites/bluebird-upflap.png")
                    birddownflap = pygame.image.load("Assets/sprites/bluebird-upflap.png")
        
        if high_score < scorebird:
            high_score = scorebird

        if basex <= -289:
            basex = 0
            
        if game_paused:
            blur_screen()
            paused_text = game_font.render("Game Paused", True, (255, 255, 255))
            paused_rect = paused_text.get_rect(center=(width // 2, height // 2))
            screen.blit(paused_text, paused_rect)
      
 
    infinitybase()
    basex -= 1
    pygame.display.update()
