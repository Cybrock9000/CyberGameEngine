
NAME = 'template'
VERSION = 1

RES = (1200, 800)
FPS = 60
FOV = 1000

rayDist = 500 #raycast dist and render dist
rayAmount = 30 #amount of rays, the more = laggier but accurate, the less = fast but could miss a lot of walls
SHADOW_DIST = rayDist / 30
DARK = 1

SKY_COLOR = (0,0,0)

MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = RES[0] - MOUSE_BORDER_LEFT
MOUSE_SENSITIVITY = 0.15
MOUSE_SENSITIVITY_UD = 0.1
MOUSE_MAX_REL = 40

EHUD = True