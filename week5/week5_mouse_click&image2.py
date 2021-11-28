# Image positioning problem

###################################################
# Student should enter code below

import simplegui

# global constants
scale = 3
# load test image
image = simplegui.load_image("https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg")
image_size = [image.get_width(), image.get_height()]
image_center = [image_size[0] // 2, image_size[1] // 2]

# canvas size
can_size = [image_size[0] // 3, image_size[1] // 3]
can_center = can_size[0] // 2, can_size[1] // 2

# draw handler
def draw(canvas):
    if image_size[0] > 0 and image_size[1] > 0:
        canvas.draw_image(image, image_center, image_size, 
                      can_center, can_size)

# create frame and register draw handler    
frame = simplegui.create_frame("Test image", can_size[0] , can_size[1])
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)

# start frame
frame.start()
    
                                       