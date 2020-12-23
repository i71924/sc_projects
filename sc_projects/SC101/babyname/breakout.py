"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

Name: Po Kai Feng
File: breakout.py
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    while True:
        pause(FRAME_RATE)
        graphics.ball.move(vx, vy)
        if vx == 0:
            vx = graphics.get_vx()
            vy = graphics.get_vy()
        if graphics.ball.x < 0 or graphics.ball.x+graphics.ball.width >= graphics.window.width:
            vx = -vx
        if graphics.ball.y < 0:
            vy = -vy
            graphics.bouncing_peddle = False
        v_change = graphics.check_collapse(vy)
        # Get which direction should change velocity
        if v_change == 'x':
            vx = -vx
        elif v_change == 'y':
            vy = -vy
        elif v_change == 'xy':
            vx = -vx
            vy = -vy
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            lives -= 1
            if lives == 0:
                # Lives is zero, user lose
                break
            graphics.set_ball()
            vx = 0
            vy = 0
        if graphics.brick_cleared():
            # Bricks cleared, user win
            break


if __name__ == '__main__':
    main()
