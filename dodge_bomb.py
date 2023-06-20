import math
import random
import time
import sys
import pygame as pg


WIDTH, HEIGHT = 1200, 650

delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}

# roto = {"":,"":,"":,"":,"":,"":,}

def check_w(rect: pg.rect):
    """
    kk_rect もしくはbomb_rectが画面内にいるか判定する
    引数:kk_rect ,bomb_rect
    戻り値:横方向と縦方向の判定結果タプル(True:画面内 False:画面外)
    """
    w ,h =True,True
    if (rect.left <0 or WIDTH<rect.right):
        w = False
    if (rect.top <0 or HEIGHT<rect.bottom):
        h = False
    return w,h


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img0 = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img1 = pg.transform.rotozoom(kk_img, 45, 2.0)
    kk_img2 = pg.transform.rotozoom(kk_img, 90, 2.0)
    kk_img3 = pg.transform.rotozoom(kk_img, 135, 2.0)
    kk_img4 = pg.transform.rotozoom(kk_img, 180, 2.0)
    kk_img5 = pg.transform.rotozoom(kk_img, 225, 2.0)
    kk_img6 = pg.transform.rotozoom(kk_img, 270, 2.0)
    kk_img7 = pg.transform.rotozoom(kk_img, 315, 2.0)


    # 練習２こうかとんSurface（kk_img）からこうかとんRect（kk_rct）を抽出する
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    bomb= pg.Surface((20,20))  #練習1
    pg.draw.circle(bomb,(255,30,0),(10,10),10)
    bomb.set_colorkey((0,0,0))
    w = random.randint(0,WIDTH)  #乱数を発生させる
    h = random.randint(0,HEIGHT)  #乱数を発生させる
    bomb_rct = bomb.get_rect()  #bombのrectを取得
    bomb_rct.center = w,h  #bombの中心位置を設定する
    vw = +5  #縦方向の移動速度
    vh = +5  #横方向の移動速度
    accs = [a for a in range(1, 11)] #加速度listの追加
    
    fonto = pg.font.Font(None,80)
    moji = fonto.render("YOU_LOSE!",True,(50,200,50))


    clock = pg.time.Clock()
    tmr = 0
    while True:

        if kk_rct.colliderect(bomb_rct):  # 練習５
                screen.blit(bg_img, [0, 0])  #背景画像の更新
                select_img = random.randint(7,8)  #こうかとんの画像をランダムに選ぶ
                kk_img = pg.image.load(f"ex02/fig/{select_img}.png")
                kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)  #画像のサイズ設定
                screen.blit(kk_img, kk_rct) 
                screen.blit(moji,[80,80])
                pg.display.update()
                print("ゲームオーバー")
                time.sleep(2)  #画面を停止
                return   # ゲームオーバー

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 
            
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]  # 合計移動量
        for k, mv in delta.items():
            if key_lst[k]: 
                sum_mv[0] += mv[0]
                sum_mv[1] += mv[1]
        kk_rct.move_ip(sum_mv)
        if check_w(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0],-sum_mv[1])
    
        
        screen.blit(bg_img, [0, 0])
        #screen.blit(kk_img, [900, 400]) 下の行に変更
        screen.blit(kk_img, kk_rct)
        screen.blit(bomb,bomb_rct)
        avw, avh= vw*accs[min(tmr//500, 9)], vh*accs[min(tmr//500, 9)]#加速度の追加
        #print(avw, avh)  #加速確認
        #print(tmr)  #タイマー確認
        bomb_rct.move_ip(avw,avh)#bombを移動させる move_ip(vw,vh)vwとvhはそれぞれの成分の移動速度　
        Wid, Hei = check_w(bomb_rct)
        if not Wid:
            vw *= -1
        if not Hei:
            vh *= -1
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()