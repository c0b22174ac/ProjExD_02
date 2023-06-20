import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900



def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    bomb= pg.Surface((20,20))  #練習1
    pg.draw.circle(bomb,(255,30,0),(10,10),10)
    bomb.set_colorkey((0,0,0))
    w = random.randint(0,WIDTH)  #乱数を発生させる
    h = random.randint(0,HEIGHT)  #乱数を発生させる
    bomb_rct = bomb.get_rect()  #bombのrectを取得
    bomb_rct.center = w,h  #bombの中心位置を設定する
    vw = +5  #縦方向の移動速度
    vh = +5  #横方向の移動速度

    clock = pg.time.Clock()
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return        
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(bomb,bomb_rct)
        bomb_rct.move_ip(vw,vh)#bombを移動させる move_ip(vw,vh)vwとvhはそれぞれの成分の移動速度
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()