from pygame.locals import *
import pygame
import sys
import random
from tkinter import messagebox


def gum():
    global r
    r = r + o

r = 0

def herasu():
    global r
    r = r - o

def herasu2():
    global r
    r = r - p

def zouka():
    global o
    o = o + 1

o = 1

def autolv():
    global au
    au = au * 1.3

au = 0.001

def auzouka():
    global r
    r = r + au

def hyouji():
    global m
    m = random.randint(1,3)

m = 0

def herasukazu():
    global p
    p = au * 4000

p = 1

def aulevelcount():
    global aul
    aul = aul + 1

aul = 1

def main():
    pygame.init()    # Pygameを初期化
    screen = pygame.display.set_mode((600, 600))    # 画面を作成
    pygame.display.set_caption("Gum Clicker")    # タイトルを作成
    
    button = pygame.Rect(30, 30, 70, 50)  # creates a rect object
    button2 = pygame.Rect(110, 30, 150, 50)  # creates a rect object
    button3 = pygame.Rect(280, 30, 150, 50)  # ボタンを作る

    #STEP1.フォントの用意  
    font = pygame.font.Font(None, 25)
    font2 = pygame.font.Font(None, 45)

    hyouji()



    #STEP2.テキストの設定
    text1 = font.render("Click", True, (0,0,0))
    text2 = font.render("Click level up", True, (0,0,0))
    text3 = font.render("Total gum", True, (255,255,255))
    text4 = font.render("Auto level up", True, (0,0,0))
    if m == 1:
        text5 = font2.render("Gums are perfect", True, (255,255,255))
    elif m == 2:
        text5 = font2.render("There are a lot of gums here", True, (255,255,255))
    elif m == 3:
        text5 = font2.render("Do you like gums?", True, (255,255,255))
    text6 = font2.render(str(r), True, (255,255,255))
    text7 = font.render(str(p), True, (255,255,255))
    text9 = font.render("Auto level", True, (255,255,255))
    
    running = True

    #メインループ
    while running:

        screen.fill((0,0,0))  #画面を黒で塗りつぶす
        text6 = font.render(str(('{:.0f}'.format(r))), True, (255,255,255))
        text7 = font.render(str(('{:.0f}'.format(p))), True, (255,255,255))
        text8 = font.render(str(aul), True, (255,255,255))

        pygame.draw.rect(screen, (255, 0, 0), button)
        pygame.draw.rect(screen, (0, 255, 0), button2)
        pygame.draw.rect(screen, (255, 255, 255), button3)

        screen.blit(text1, (40, 45))
        screen.blit(text2, (120,45))
        screen.blit(text3, (80, 90))
        screen.blit(text4, (290, 45))
        screen.blit(text5, (100, 300))
        screen.blit(text6, (90, 110))
        screen.blit(text7, (400, 120))
        screen.blit(text8, (400, 100))
        screen.blit(text9, (280, 100))

        # 左上座標(10,10)、幅80px、高さ50pxの長方形を線幅5pxの緑色(R=0, G=80, B=0)で描く
        pygame.draw.rect(screen,(255,255,255),Rect(0,250,1500,5))   # 四角形を描画(塗りつぶしなし)
        #pygame.draw.rect(screen,(0,80,0),Rect(10,10,80,50))    # 四角形を描画(塗りつぶし)

        auzouka()

        pygame.display.update() #描画処理を実行
        for event in pygame.event.get():
            if event.type == QUIT:  # 終了イベント
                running = False
                pygame.quit()  #pygameのウィンドウを閉じる
                sys.exit() #システム終了
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    gum()
                    print(r)
                if button2.collidepoint(event.pos):
                    if r >= o:
                        zouka()
                        herasu()
                        print(o)
                    else:
                        messagebox.showwarning("ガムが足りないようだ", "gum error")
                if button3.collidepoint(event.pos):
                    if r >= p:
                        autolv()
                        herasu2()
                        herasukazu()
                        aulevelcount()
                        print(au)
                    else:
                        messagebox.showwarning("ガムが足りないようだ", "gum error")
                    
if __name__=="__main__":
    main()
