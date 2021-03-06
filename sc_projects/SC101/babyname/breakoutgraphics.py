"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

Name: Po Kai Feng
File: breakoutgraphics.py
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.brr = brick_rows
        self.brc = brick_cols
        self.brw = brick_width
        self.brh = brick_height
        self.bro = brick_offset
        self.brs = brick_spacing

        # Create a paddle.
        self.pw = paddle_width
        self.ph = paddle_height
        self.po = paddle_offset
        self.peddle = GRect(self.pw, self.ph)
        self.peddle.filled = True
        self.peddle.fill_color = 'black'
        self.set_paddle()
        self.window.add(self.peddle)

        # Center a filled ball in the graphical window.
        self.br = ball_radius
        self.ball = GOval(self.br*2, self.br*2)
        self.ball.color = 'navy'
        self.ball.filled = True
        self.ball.fill_color = 'navy'
        self.set_ball()
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.__vx = 0
        self.__vy = 0

        # Initialize our mouse listeners.
        onmousemoved(self.move_paddle)
        onmouseclicked(self.move_ball)

        # Draw bricks.
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if j < 2:
                    self.brick.fill_color = 'red'
                elif j < 4:
                    self.brick.fill_color = 'orange'
                elif j < 6:
                    self.brick.fill_color = 'yellow'
                elif j < 8:
                    self.brick.fill_color = 'green'
                elif j < 10:
                    self.brick.fill_color = 'blue'
                elif j < 12:
                    self.brick.fill_color = 'navy'
                else:
                    self.brick.fill_color = 'purple'
                self.window.add(self.brick, x=i*(brick_width+brick_spacing), y=brick_offset+j*(brick_height+brick_spacing))

        # To note whether the ball has bounced peddle
        self.bouncing_peddle = False

    # Set the initial position of peddle
    def set_paddle(self):
        self.peddle.x = (self.window.width-self.pw)/2
        self.peddle.y = self.window.height-self.po-self.ph

    # Set the initial position of ball
    def set_ball(self):
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height)/2
        self.__vx = 0
        self.__vy = 0
        self.bouncing_peddle = False

    # Set the initial velocity and moving direction of ball
    def set_ball_velocity(self):
        self.__vx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__vx = -self.__vx
        self.__vy = INITIAL_Y_SPEED

    def move_paddle(self, mouse):
        if mouse.x < 0:
            self.peddle.x = 0
        elif mouse.x+self.peddle.width >= self.window.width:
            self.peddle.x = self.window.width-self.peddle.width
        else:
            self.peddle.x = mouse.x

    # Getter
    def get_vx(self):
        return self.__vx

    # Getter
    def get_vy(self):
        return self.__vy

    # Determine the state of ball when user click mouse, and set velocity when vy==0
    def move_ball(self, mouse):
        if self.__vy == 0:
            self.set_ball_velocity()

    def check_collapse(self, vy):
        """
        :param vy: the velocity of y-direction now
        :return: the direction of velocity should be changed
        """
        # Set segment amount of collapse-checkpoint
        seg = 1
        if self.pw > self.ph:
            if self.br*2 >= self.ph:
                seg = self.br*2 // self.ph
        else:
            if self.br * 2 >= self.pw:
                seg = self.br*2 // self.pw

        # Check whether the ball collapse and return which direction of velocity should change
        for i in range(seg+1):
            for j in range(seg+1):
                obj = self.window.get_object_at(self.ball.x+i*self.br*2/seg, self.ball.y+j*self.br*2/seg)
                if obj is not None and obj is not self.peddle and obj is not self.ball:
                    # Check 4 relative situation of the ball and brick: (up or down) and (left or right)
                    # In each situation, compare the contact area of x- and y- direction
                    # The bigger contact area means the direction of bouncing
                    if self.ball.x < obj.x:
                        if self.ball.y < obj.y:
                            if self.ball.x+self.ball.width-obj.x > self.ball.y+self.ball.height-obj.y:
                                self.window.remove(obj)
                                self.bouncing_peddle = False
                                return 'y'
                            elif self.ball.x+self.ball.width-obj.x < self.ball.y+self.ball.height-obj.y:
                                self.window.remove(obj)
                                self.bouncing_peddle = False
                                return 'x'
                            else:
                                self.window.remove(obj)
                                self.bouncing_peddle = False
                                return 'xy'
                        else:
                            if self.ball.x+self.ball.width-obj.x > obj.y+obj.height-self.ball.y:
                                self.window.remove(obj)
                                self.bouncing_peddle = False
                                return 'y'
                            elif self.ball.x+self.ball.width-obj.x < obj.y+obj.height-self.ball.y:
                                self.window.remove(obj)
                                self.bouncing_peddle = False
                                return 'x'
                            else:
                                self.window.remove(obj)
                                self.bouncing_peddle = False
                                return 'xy'
                    else:
                        if self.ball.y < obj.y:
                            if obj.x+obj.width-self.ball.x > self.ball.y+self.ball.height-obj.y:
                                self.window.remove(obj)
                                self.bouncing_peddle = False
                                return 'y'
                            elif obj.x+obj.width-self.ball.x > self.ball.y+self.ball.height-obj.y:
                                self.window.remove(obj)
                                self.bouncing_peddle = False
                                return 'x'
                            else:
                                self.window.remove(obj)
                                self.bouncing_peddle = False
                                return 'xy'
                        else:
                            if obj.x+obj.width-self.ball.x > obj.y+obj.height-self.ball.y:
                                self.window.remove(obj)
                                self.bouncing_peddle = False
                                return 'y'
                            elif obj.x+obj.width-self.ball.x > obj.y+obj.height-self.ball.y:
                                self.window.remove(obj)
                                self.bouncing_peddle = False
                                return 'x'
                            else:
                                self.window.remove(obj)
                                self.bouncing_peddle = False
                                return 'xy'
                # Bounced peddle, should change velocity if the ball hasn't bounced peddle
                elif obj is self.peddle:
                    if not self.bouncing_peddle:
                        self.bouncing_peddle = True
                        return 'y'
                    else:
                        return 0
                # Determine if peddle collapsed the round shape of ball
                elif self.peddle.x < self.ball.x < self.peddle.x+self.peddle.width and self.ball.y < self.peddle.y < self.ball.y+2*self.br:
                    if vy > 0:
                        if not self.bouncing_peddle:
                            self.bouncing_peddle = True
                            return 'y'
                        else:
                            return 0
                elif self.ball.x < self.peddle.x < self.ball.x+2*self.br and self.ball.y < self.peddle.y < self.ball.y+2*self.br:
                    if vy > 0:
                        if not self.bouncing_peddle:
                            self.bouncing_peddle = True
                            return 'y'
                        else:
                            return 0
        return 0

    # To check if the bricks are all cleared
    def brick_cleared(self):
        for i in range(self.brc):
            for j in range(self.brr):
                obj = self.window.get_object_at(x=i*(self.brw+self.brs), y=self.bro+j*(self.brh+self.brs))
                if obj is not None and obj is not self.ball and obj is not self.peddle:
                    return False
        return True
