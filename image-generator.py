from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def generate_image(template, eventname, matchname, score1, score2):
    # define main things
    W, H = 1125, 1400
    img = Image.open(template)
    I1 = ImageDraw.Draw(img)

    # regular font for subtitle
    myFont1 = ImageFont.truetype('fonts/Manrope-Regular.ttf', 46.54)
    # bold font for title
    myFont2 = ImageFont.truetype('fonts/Manrope-ExtraBold.ttf', 66)
    # bodl font for scores
    myFont3 = ImageFont.truetype('fonts/Manrope-ExtraBold.ttf', 128)

    # title
    I1.text((W/2, 735), eventname, font=myFont2, anchor="mm")
    # subtitle
    I1.text((W/2, 798), matchname, font=myFont1, anchor="mm")

    # team 1 score
    I1.text((374, 1240), score1, font=myFont3, anchor="mm")
    # team 2 score
    I1.text((750, 1240), score2, font=myFont3, anchor="mm")
    img.show()
    img.save("export.png")


generate_image('templates/rl_template.png', "RLCS Major 1",
               "Grand Final", "4", "3")
