
#windows size

frame_size_x = 800
frame_size_y = 600
speed = 15
FPS = 60

#colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#coordinates by the plain(x,y - start)
x = 400
y = 400

plain_coordinates = [[x, y], [x-30, y+80], [x-70, y+50], [x-80, y+10], [x-140, y+90], [x-130, y+130], [x-90, y+170], [x-30, y+170], [x, y+140],
                    [x+30, y+170], [x+90, y+170], [x+130, y+130], [x+140, y+90], [x+80, y+10], [x+70, y+50], [x+30, y+80], [x, y]]

#other settings
plain_speed = 7

plain_enemy_coord = []

for count, elem in enumerate(plain_coordinates):
    plain_enemy_coord.append([plain_coordinates[count][0], ((plain_coordinates[count][1]-y)*(-1)) + y-200])



