def setup():
    size(400,400)
    textSize(70)
def draw():
    background(0)
    text("M", width/2-50, height/2)
    text("D", width/2, height/2)
    fill(120)
    print(mouseX,mouseY)
    if keyPressed:
        fill(120)
        if key == 'D' or key == 'd':
            fill(120,0,0)
            text("D",width/2,height/2)
            fill(120)
    if keyPressed:
        fill(120)
        if key == 'M' or key == 'm':
            fill(120,0,0)
            text("M", width/2-50,height/2)
            fill(120)
    if (mouseX>=155 and mouseX<=205 and mouseY>=147 and mouseY<=200):
        text("D",width/2, height/2)
        fill(0,120,135)
        if keyPressed:
            if keyCode == 39 and mouseX>=155 and mouseX<=205 and mouseY>=14 and mouseY<=200:
                fill(255,0,0)
                text("D", width/2,height/2)
                fill(120)
                print(keyCode)
    if (mouseX>=225 and mouseX<=260 and mouseY>=147 and mouseY<=200):
            text("M", width/2-50, height/2)
            fill(0,201,153)
            if keyPressed:
                fill(120)
                if keyCode == 37 and mouseX>=225 and mouse<=260 and mouse>=14 and mouseY<=200:
                    fill(0,255,0)
                    text("M", width/2-50, height/2)
                    fill(120)
                    print(keyCode)
