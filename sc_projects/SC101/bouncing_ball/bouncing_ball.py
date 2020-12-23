"""
File: bouncing_ball.py
Name: Po Kai Feng
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Constant
VX = 3
# The speed at x-direction (plus as moving right)
# Constant
DELAY = 10
# The period of pause
# Constant
GRAVITY = 1
# To simulate the gravity when the ball moves at y-direction
# Constant
SIZE = 20
# The diameter of the ball
# Constant
REDUCE = 0.9
# To note how much bouncing affects the y-direction speed
# Constant
X_START = 30
Y_START = 40
# The ball's initial location is (X_START, Y_START)

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
is_moving = False
# To note whether the ball is moving
reset_times = 0
# To note how many times has the code be executed


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, X_START, Y_START)
    onmouseclicked(move_ball)


def move_ball(mouse):
    global is_moving, reset_times
    if reset_times == 3:
        is_moving = True
    if not is_moving:
        # The ball was not moving and should move now
        is_moving = True
        # Assign True to is_moving
        vy = GRAVITY
        # The speed at y-direction (plus as moving down)
        while True:
            if ball.x-SIZE/2 >= window.width:
                # The ball is out of window and should be put at the initial location
                is_moving = False
                # Assign False to is_moving and break the while loop
                reset_times += 1
                break

            ball.move(VX, vy)
            vy += GRAVITY
            pause(DELAY)
            if ball.y + SIZE / 2 >= window.height:
                # The ball hit the ground and should bounce back
                vy *= -REDUCE
                # vy should times -1 and times REDUCE
        window.add(ball, X_START, Y_START)
        # Add the ball at the initial location


if __name__ == "__main__":
    main()
