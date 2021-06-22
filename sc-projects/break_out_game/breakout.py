"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 50  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add animation loop here!
    lives = NUM_LIVES
    while True:
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        graphics.ball_collide_paddle()

        if graphics.ball.x <= 0 or graphics.ball.x+graphics.ball.width > graphics.window.width:
            graphics.set_dx(graphics.get_dx()*-1)
        elif graphics.ball.y <= 0:
            graphics.set_dy(graphics.get_dy()*-1)
        else:
            pass
        pause(FRAME_RATE)

        if graphics.ball.y > graphics.window_height + graphics.ball_radius * 2:
            lives -= 1
            # 做一個開關，把滑鼠資訊打開，下次點擊才可以再發球
            graphics.dead()
            if lives > 0:
                graphics.reset_ball()
            else:
                graphics.game_over()


if __name__ == '__main__':
    main()



