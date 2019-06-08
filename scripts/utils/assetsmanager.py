import pygame as pg

pg.init()
pg.font.init()

title_frames = []
title_font = pg.font.Font('fonts/PetalGlyphV1.5.ttf', 42)
explanation_font = pg.font.Font('fonts/EndOfAnthropocene-Regular.ttf', 72)
title_img = pg.image.load('img/ecotitle.png')

for f in range(0, 97):
    frame = pg.image.load('img/title/frame_' + str(f) + '_delay-0.04s.gif').convert()
    title_frames.append(frame)

def get(assetname):

    if assetname == "TITLEGIF":
        return title_frames

    if assetname == 'TITLEFONT':
        return title_font

    if assetname == 'TITLEIMG':
        return title_img

    if assetname == 'EXPLANATION':
        return explanation_font