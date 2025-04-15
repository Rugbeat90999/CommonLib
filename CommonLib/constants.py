from CommonLib.classes import debase_float, OutputColors


HEX_COLOR_LIBRARY = {"black":{"name":"black", "hex":"#000000"},
"white":{"name":"white", "hex":"#ffffff"},
"light gray":{"name":"light gray", "hex":"#bfbfbf"},
"gray":{"name":"gray", "hex":"#7f7f7f"},
"dark gray":{"name":"dark gray", "hex":"#404040"},
"blue":{"name":"blue", "hex":"#0000ff"},
"red":{"name":"red", "hex":"#ff0000"},
"crimson":{"name":"crimson", "hex":"#9c0000"},
"green":{"name":"green", "hex":"#00ff00"},
"orange":{"name":"orange", "hex":"#fa6400"},
"yellow":{"name":"yellow", "hex":"#ffff00"},
"cyan":{"name":"cyan", "hex":"#00ffff"},
"teal":{"name":"teal", "hex":"#00ffae"},
"pink":{"name":"pink", "hex":"#ff9696"},
"purple":{"name":"purple", "hex":"#6407b0"},
"maroon": {"name": "maroon", "hex": "#800000"},
"olive": {"name": "olive", "hex": "#808000"},
"navy": {"name": "navy", "hex": "#000080"},
"lime": {"name": "lime", "hex": "#bfff00"},
"magenta": {"name": "magenta", "hex": "#ff00ff"},
"indigo": {"name": "indigo", "hex": "#4b0082"},
"gold": {"name": "gold", "hex": "#ffd700"},
"silver": {"name": "silver", "hex": "#c0c0c0"},
"coral": {"name": "coral", "hex": "#ff7f50"},
"salmon": {"name": "salmon", "hex": "#fa8072"},
"plum": {"name": "plum", "hex": "#dda0dd"},
"orchid": {"name": "orchid", "hex": "#da70d6"},
"turquoise": {"name": "turquoise", "hex": "#40e0d0"},
"peach": {"name": "peach", "hex": "#ffcc99"},
"mint": {"name": "mint", "hex": "#98ff98"},
"lavender": {"name": "lavender", "hex": "#e6e6fa"},
"amber": {"name": "amber", "hex": "#ffbf00"},
"rose": {"name": "rose", "hex": "#ff007f"},
"khaki": {"name": "khaki", "hex": "#f0e68c"},
"cerulean": {"name": "cerulean", "hex": "#007ba7"},
"chartreuse": {"name": "chartreuse", "hex": "#7fff00"},
"periwinkle": {"name": "periwinkle", "hex": "#ccccff"},
"sienna": {"name": "sienna", "hex": "#a0522d"},
"wisteria": {"name": "wisteria", "hex": "#c9a0dc"},
"azure": {"name": "azure", "hex": "#007fff"},
"lavender blush": {"name": "lavender blush", "hex": "#fff0f5"},
"emerald": {"name": "emerald", "hex": "#50c878"},
"cobalt": {"name": "cobalt", "hex": "#0047ab"},
"russet": {"name": "russet", "hex": "#80461b"},
"scarlet": {"name": "scarlet", "hex": "#ff2400"},
"violet": {"name": "violet", "hex": "#8a2be2"},
"mauve": {"name": "mauve", "hex": "#e0b0ff"},
"tan": {"name": "tan", "hex": "#d2b48c"},
"sepia": {"name": "sepia", "hex": "#704214"},
"coral pink": {"name": "coral pink", "hex": "#f88379"},
"ivory": {"name": "ivory", "hex": "#fffff0"},
"taupe": {"name": "taupe", "hex": "#483c32"},
"jade": {"name": "jade", "hex": "#00a86b"}} # type: ignore


BLACK = (00, 00, 00)
WHITE = (255, 255, 255)
LIGHT_GRAY = (191, 191, 191)
GRAY = (127, 127, 127)
DARK = (40, 40, 40)
BLUE = (00, 00, 255)
RED = (255, 00, 00)
CRIMSON = (156, 00, 00)
GREEN = (00, 255, 00)
ORANGE = (156, 64, 00)
YELLOW = (255, 255, 00)
CYAN = (00, 255, 255)
TEAL = (00, 255, 156)
PINK = (255, 96, 96)
PURPLE = (64, 7, 176)
MAROON = (80, 00, 00)
OLIVE = (80, 80, 00)
NAVY = (00, 00, 80)
LIME = (191, 255, 00)
MAGENTA = (255, 00, 255)
INDIGO = (75, 00, 82)
GOLD = (255, 215, 00)
SILVER = (192, 192, 192)
CORAL = (255, 127, 50)
SALMON = (250, 80, 72)
PLUM = (221, 160, 221)
ORCHID = (218, 70, 214)
TURQUOISE = (40, 224, 208)
PEACH = (255, 204, 99)
MINT = (98, 255, 98)
LAVENDER = (230, 230, 250)
AMBER = (255, 191, 00)
ROSE = (255, 0, 127)
KHAKI = (240, 230, 140)
CERULEAN = (0, 123, 167)
CHARTREUSE = (127, 255, 00)
PERIWINKLE = (204, 204, 255)
SIENNA = (160, 52, 45)
WISTERIA = (201, 160, 220)
AZURE = (0, 127, 255)
LAVENDER = (255, 240, 245)
EMERALD = (50, 200, 78)
COBALT = (00, 47, 171)
RUSSET = (80, 46, 27)
SCARLET = (255, 24, 00)
VIOLET = (138, 43, 226)
MAUVE = (224, 176, 255)
TAN = (210, 180, 140)
SEPIA = (70, 42, 14)
CORAL_PINK = (248, 83, 79)
IVORY = (255, 255, 240)
TAUPE = (48, 60, 32)
JADE = (0, 168, 107)




de = debase_float(0)
dafe = debase_float(1)
fiso = debase_float(2)
mido = debase_float(3)
zeba = debase_float(4)
nono = debase_float(5)
nino = debase_float(6)
fitu = debase_float(7)
vifi = debase_float(8)
gobo = debase_float(9)

class Output:
  DEFA = str(OutputColors())
  TITLE = str(OutputColors(font="bold", color="red"))
  COL = str(OutputColors(color="magenta")) + ":" + str(DEFA)
  CON = str(OutputColors(color="green"))
  VAR = str(OutputColors(color="cyan"))
  CBO = str(OutputColors(color="yellow")) + "\u007b" + str(DEFA)
  CBC = str(OutputColors(color="yellow")) + "\u007d" + str(DEFA)
  SBO = str(OutputColors(color="yellow")) + "[" + str(DEFA)
  SBC = str(OutputColors(color="yellow")) + "]" + str(DEFA)
  COM = str(OutputColors(color="red")) + ", " + str(DEFA)
  ERR = str(OutputColors(color="magenta"))
  CLS = str(OutputColors(color="green", font="bold"))