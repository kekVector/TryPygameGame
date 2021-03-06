# Support func
def resize_list(coord, k):
    for count, i in enumerate(coord):
        for count2, j in enumerate(i):
            coord[count][count2] = int(float(j) * k)
    return coord


# Windows size

frame_size_x = 1000
frame_size_y = 800
speed = 15
FPS = 60

# Colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
enemy_plains_color = [(205, 92, 92), (240, 128, 128), (250, 128, 114),
                      (233, 150, 122), (255, 160, 122), (220, 20, 60),
                      (255, 0, 0), (178, 34, 34), (139, 0, 0)]

# Stats
plain_speed = 7
max_health_main_plain = 10
move_dirs = ['w', 'a', 's', 'd']
# Menu settings
start_button_color = (50, 205, 50)
start_button_text_color = start_button_color
exit_button_color = (178, 34, 34)
exit_button_text_color = exit_button_color
button_pause_resume_color = (255, 69, 0)
button_pause_resume_color_text = button_pause_resume_color
button_pause_restart_color = (255, 99, 71)
button_pause_restart_color_text = button_pause_restart_color
button_pause_main_menu_color = (255, 160, 122)
button_pause_main_menu_color_text = button_pause_main_menu_color
button_pause_exit_color = (255, 127, 80)
button_pause_exit_color_text = button_pause_exit_color

# Coordinates by the plain(x,y - start)
x = 400
y = 400

plain_coordinates = [[x, y], [x - 30, y + 80], [x - 70, y + 50], [x - 80, y + 10], [x - 140, y + 90],
                     [x - 130, y + 130], [x - 90, y + 170], [x - 30, y + 170], [x, y + 140],
                     [x + 30, y + 170], [x + 90, y + 170], [x + 130, y + 130], [x + 140, y + 90],
                     [x + 80, y + 10], [x + 70, y + 50], [x + 30, y + 80], [x, y]]

# Enemies settings


plain_enemy_coord_1 = []
for count, elem in enumerate(plain_coordinates):
    plain_enemy_coord_1.append([plain_coordinates[count][0], ((plain_coordinates[count][1] - y) * (-1)) + y - 200])

plain_enemy_coord_2 = [[10, 0], [20, -20], [40, -30], [50, -10], [50, 30],
                       [40, 50], [30, 60], [10, 70], [40, 75], [40, 100], [60, 60],
                       [80, 0], [90, -10], [90, 10], [100, -10], [110, -20], [110, -30],
                       [80, -30], [70, -20], [60, -50], [50, -65], [40, -90], [30, -90],
                       [30, -75], [0, -90], [-30, -75], [-30, -90], [-40, -90], [-50, -65],
                       [-60, -50], [-70, -20], [-80, -30], [-110, -30], [-110, -20], [-100, -10],
                       [-90, 10], [-90, -10], [-80, 0], [-60, 60], [-40, 100], [-40, 75], [-10, 70],
                       [-30, 60], [-40, 50], [-50, 30], [-40, -30], [-20, -20], [-10, 0]]

plain_enemy_coord_3 = [[0, 0], [30, -10], [50, -30], [70, -40], [70, -10], [75, 0], [80, -10], [80, -40], [100, -50],
                       [120, -50], [120, -30], [125, -20], [130, -30], [130, -50], [150, -60], [160, -70], [170, -90],
                       [160, -110], [150, -130], [130, -120], [120, -110], [100, -100], [90, -130], [120, -160],
                       [130, -180], [120, -200], [110, -210], [100, -200], [90, -180], [60, -160], [40, -170],
                       [30, -200], [20, -230], [0, -250], [-20, -230], [-30, -200], [-40, -170], [-60, -160],
                       [-90, -180],
                       [-100, -200], [-110, -210], [-120, -200], [-130, -180], [-120, -160], [-90, -130], [-100, -100],
                       [-120, -110], [-130, -120], [-150, -130], [-160, -110], [-170, -90], [-160, -70], [-150, -60],
                       [-130, -50], [-130, -30], [-125, -20], [-120, -30], [-120, -50], [-100, -50], [-80, -40],
                       [-80, -10],
                       [-75, 0], [-70, -10], [-70, -40], [-50, -30], [-30, -10], [0, 0]]

plain_enemy_coord_4 = [[0, 0], [10, -40], [20, -30], [30, -60], [50, -60], [30, -70], [30, -80], [60, -100], [90, -80],
                       [90, -70], [100, -60], [100, -70], [110, -70], [110, -60], [120, -70], [120, -80], [110, -90],
                       [100, -90], [90, -90], [60, -110], [30, -90], [20, -110], [40, -140], [70, -110], [60, -130],
                       [40, -150], [20, -140], [40, -160], [70, -140], [70, -130], [80, -120], [80, -130], [90, -130],
                       [90, -120], [100, -130], [100, -140], [90, -150], [70, -150], [40, -170], [10, -150], [10, -160],
                       [-10, -180], [0, -190], [10, -170], [20, -190], [20, -210], [30, -220], [30, -240], [20, -230],
                       [20, -210], [10, -190], [0, -210], [-20, -170], [-10, -160], [-10, -150], [-40, -170],
                       [-70, -150], [-90, -150], [-100, -140], [-100, -130], [-90, -120], [-90, -130], [-80, -130],
                       [-80, -120], [-70, -130], [-70, -140], [-40, -160], [-20, -140], [-40, -150], [-60, -130],
                       [-70, -110], [-40, -140], [-20, -110], [-30, -90], [-60, -110], [-90, -90], [-110, -90],
                       [-120, -80], [-120, -70], [-110, -60], [-110, -70], [-100, -70], [-100, -60], [-90, -70],
                       [-90, -80], [-60, -100], [-30, -80], [-30, -70], [-50, -60], [-30, -60], [-20, -30], [-10, -40],
                       [0, 0]]

# Resising start coord
plain_enemy_coord_1 = resize_list(plain_enemy_coord_1, 0.3)
plain_enemy_coord_2 = resize_list(plain_enemy_coord_2, 0.3)
plain_enemy_coord_3 = resize_list(plain_enemy_coord_3, 0.25)
plain_enemy_coord_4 = resize_list(plain_enemy_coord_4, 0.2)
plain_coordinates = resize_list(plain_coordinates, 0.5)
plain_enemy_coord_5 =[]

# for i in range(len(plain_enemy_coord_4)):
#     if plain_enemy_coord_4[i][0] > 0:
#         plain_enemy_coord_5.append(plain_enemy_coord_4[i][0] + 5)
#     elif plain_enemy_coord_4[i][0] < 0:
#         plain_enemy_coord_5.append(plain_enemy_coord_4[i][0] - 5)
#     else:
#         plain_enemy_coord_5.append(plain_enemy_coord_4[i][0])
# Dict enemy coord
main_plain = {'Coord': plain_coordinates, 'index_guns_coord': [0]}
plain_enemy_1 = {'Coord': plain_enemy_coord_1, 'index_guns_coord': [0]}
plain_enemy_2 = {'Coord': plain_enemy_coord_2, 'index_guns_coord': [9, 39]}
plain_enemy_3 = {'Coord': plain_enemy_coord_3, 'index_guns_coord': [5, 11, 55, 61]}
plain_enemy_4 = {'Coord': plain_enemy_coord_4, 'index_guns_coord': [0]}
