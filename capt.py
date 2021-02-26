from captcha.image import ImageCaptcha

image = ImageCaptcha()

data = image.generate('1234')
image.write('34авы', 'out.png')
