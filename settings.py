
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

# Menu settings
start_button_color = (50, 205, 50)
start_button_text_color = start_button_color
exit_button_color = (178, 34, 34)
exit_button_text_color = exit_button_color
button_pause_resum_color = (255, 69, 0)
button_pause_resum_color_text = button_pause_resum_color
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

# Other settings


plain_enemy_coord_2 = []
for count, elem in enumerate(plain_coordinates):
    plain_enemy_coord_2.append([plain_coordinates[count][0], ((plain_coordinates[count][1] - y) * (-1)) + y - 200])

plain_enemy_coord_3 = [[10, 0], [20, -20], [40, -30], [50, -10], [50, 30],
                       [40, 50], [30, 60], [10, 70], [40, 75], [40, 100], [60, 60],
                       [80, 0], [90, -10], [90, -10], [100, -10], [110, -20], [110, -30],
                       [80, -30], [70, -20], [60, -50], [50, -65], [40, -90], [30, -90],
                       [30, -75], [0, -90], [-30, -75], [-30, -90], [-40, -90], [-50, -65],
                       [-60, -50], [-70, -20], [-80, -30], [-110, -30], [-110, -20], [-100, -10],
                       [-90, 10], [-90, -10], [-80, 0], [-60, 60], [-40, 100], [-40, 75], [-10, 70],
                       [-30, 60], [-40, 50], [-50, 30], [-40, -30], [-20, -20], [-10, 0]]

plain_enemy_coord_4 = [[0, 0], [30, -10], [50, -30], [70, -40], [70, -10], [75, 0], [80, -10],
                       [80, -40], [100, -50], [120, -50], [120, -30], [125, -20], [130, -30], [130, -50],
                       [150, -60], [160, -70], [170, -90], [160, -110], [150, -130], [130, -120], [120, -110],
                       [100, -100], [90, -130], [120, -160], [130, -180], [120, -200], [110, -210], [100, -200],
                       [90, -180], [60, -160], [40, -170], [30, -200], [20, -230], [0, 250], [-20, -230],
                       [-30, -200], [-40, -170], [-60, -160], [-90, -180], [-100, -200], [-110, -210], [-120, -200],
                       [-130, -180], [-120, -160], [-90, -130], [-100, -100], [-120, -110], [-130, -120], [-150, -130],
                       [-160, -110], [-170, -90], [-160, -70], [-150, -60], [-130, -50], [-130, -30], [-125, -20],
                       [120, -30], [120, -50], [100, -50], [80, -40], [80, -10], [75, 0], [70, -10],
                       [70, -40], [50, -30], [30, -10], [0, 0]]

plain_enemy_coord = [[0, 0], [30, -10], [50, -30], [70, -40], [70, -10], [75, 0], [80, -10], [80, -40], [100, -50],
                     [120, -50], [120, -30], [125, -20], [130, -30], [130, -50], [150, -60], [160, -70], [170, -90],
                     [160, -110], [150, -130], [130, -120], [120, -110], [100, -100], [90, -130], [120, -160],
                     [130, -180], [120, -200], [110, -210], [100, -200], [90, -180], [60, -160], [40, -170], [30, -200],
                     [20, -230], [0, -250], [-20, -230], [-30, -200], [-40, -170], [-60, -160], [-90, -180],
                     [-100, -200], [-110, -210], [-120, -200], [-130, -180], [-120, -160], [-90, -130], [-100, -100],
                     [-120, -110], [-130, -120], [-150, -130], [-160, -110], [-170, -90], [-160, -70], [-150, -60],
                     [-130, -50], [-130, -30], [-125, -20], [120, -30], [120, -50], [100, -50], [80, -40], [80, -10],
                     [75, 0], [70, -10], [70, -40], [50, -30], [30, -10], [0, 0]]
