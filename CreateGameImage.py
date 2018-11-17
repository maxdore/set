from PIL import Image
import time

def card_to_path(c):
    colors = ['green', 'purple', 'red']
    shape = ['diamond', 'oval', 'squiggle']
    filling = ['empty', 'filled', 'shaded']

    return 'cards/' + colors[c[0]] + shape[c[1]] + filling[c[2]] + str(c[3] + 1) + '.jpg'

def save_game_image(cards):
    card_images = list(map(Image.open, map(card_to_path, cards)))
    game_image = Image.new('RGB', (600, 300))

    x_offset = 0
    y_offset = 0
    for i in range(len(card_images)):
        game_image.paste(card_images[i], (x_offset, y_offset))
        x_offset = (x_offset + 200) % 600
        y_offset = y_offset + 100 if (i + 1) % 3 == 0 else y_offset

    game_image.save('gen/' + str(int(time.time()*1000)) + '.jpg')
