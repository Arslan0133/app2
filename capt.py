from captcha.image import ImageCaptcha
import random


def capgenerate():
    image = ImageCaptcha()

    strnum = '123456789'
    strsym = 'qwertyuiopasdfghjklzxcvbnm'
    strcont = strnum + strsym
    ls = list(strcont)
    random.shuffle(ls)
    capsym = ''.join([random.choice(ls) for x in range(6)])

    data = image.generate(capsym)
    image.write(capsym, 'out.png')
    return capsym
