from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

# pressing a key
k.press_key('H')
# which you then follow with a release of the key
k.release_key('H')
# or you can 'tap' a key which does both
k.tap_key('e')
# note that that tap_key does support a way of repeating keystrokes with a interval time between each
k.tap_key('l',n=2,interval=1)
# and you can send a string if needed too
k.type_string('o World!')

# move the mouse to int x and int y (these are absolute positions)
m.move(200, 200)

# click works about the same, except for int button possible values are 1: left, 2: right, 3: middle
m.click(600, 900, 1)

# get the screen size
m.screen_size()
# (1024, 768)

# get the mouse positionHello World!Hello World!
m.position()
# (500, 300)lo World!