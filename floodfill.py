#Julian Balletshofer
#Matr.Nr: 03738853

#for the floodfill algorithm i used the breath-first-traversal form the lecture
#here i used the breath first traversal to go around that starting pixel by pixel and alway look at the four neighbours of the current pixel
#additionally i used an iterative solution to be aware of stack overflow if we have huge pictures
# the solution is linear with respect to width*height since we check for the old color and skip if it isnt the old color so we dont do any overhead
# and the max number of pixel we process would be width*height if we would have to process the whole picture


from PIL import Image

def checkColorValues(r,g,b):
  if r<0 or r>255 or b<0 or b>255 or g<0 or g>255:
    print("invalid color values")
    return False
  return True

def checkSurroundingPixel(x,y,lenRow,lenCol,preC,img):
    # check boundaries and if it has the oldColor otherwise we want to skip it
    if x<0 or x>lenRow-1 or y<0 or y>lenCol-1  or img.getpixel((x,y))!=preC:
        return False
    return True


def Floodfill(img, x,y, newColor):
    # take length colum and row of image
    # this will help us to check if we are still inside the picture
    lenRow,lenCol = img.size
    # initialize queue
    queue = []
    # append start value
    queue.append([x,y])
    # oldColor = img[x][y]
    oldColor = img.getpixel((x,y))
    # start Breath first traversial do as long queue is not empty which would mean we are finished
    # iterative process to avoid overflow
    while queue:
        # pop item and assign location of pixel to x and y
        curPixel = queue.pop()
        x = curPixel[0]
        y = curPixel[1]
        # assign new color
        img.putpixel((x,y),newColor)
        # put surrounding pixels in stack
        # check before if the neighbours(nodes) are:
        # out of Bounds, are oldColor
        # color them to avoid that we have the same pixel(node) mutiple time in the queue
        if checkSurroundingPixel(x, y+1,lenRow,lenCol,oldColor,img):
            queue.append([x,y+1])
            img.putpixel((x,y+1),newColor)
        if checkSurroundingPixel(x, y-1,lenRow,lenCol,oldColor,img):
            queue.append([x,y-1])
            img.putpixel((x,y-1),newColor)
        if checkSurroundingPixel(x+1, y,lenRow,lenCol,oldColor,img):
            queue.append([x+1,y])
            img.putpixel((x+1,y),newColor)
        if checkSurroundingPixel(x-1, y,lenRow,lenCol,oldColor,img):
            queue.append([x-1,y])
            img.putpixel((x-1,y),newColor)
        # now it goes back to the top and pops first element in queue
            

#open the image
imgg = Image.open('input.jpeg')
#confert into RGB data
rgb = imgg.convert("RGB")
#start point
x,y = 1,1
#color we want to assign
s_r = 200
s_g = 240
s_b = 0
#check if valid color values
if checkColorValues(s_r,s_g,s_b):
  newColor = (s_r,s_g,s_b)
  #starting the floodfill algorithm
  Floodfill(rgb,x,y,newColor)
#save new picture to a differen file
rgb.save('output.png','png')
