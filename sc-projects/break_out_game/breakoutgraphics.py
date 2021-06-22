"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Width of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 15  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    # this is the constructor
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.window_width = self.brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (self.brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # create count
        self.count = brick_cols * brick_rows

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2,
                        y=self.window_height-paddle_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(self.ball_radius*2, self.ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width-self.ball_radius*2)/2,
                        y=(self.window_height-self.ball_radius*2)/2)

        # set ball velocity
        self.__dx = 0
        self.__dy = 0

        # Draw bricks
        brick_position_y = brick_offset
        for i in range(brick_rows):
            brick_position_x = 0
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i == 0:
                    self.brick.fill_color = 'peru'
                if i == 1:
                    self.brick.fill_color = 'peru'
                if i == 2:
                    self.brick.fill_color = 'orchid'
                if i == 3:
                    self.brick.fill_color = 'orchid'
                if i == 4:
                    self.brick.fill_color = 'tan'
                if i == 5:
                    self.brick.fill_color = 'tan'
                if i == 6:
                    self.brick.fill_color = 'ivory'
                if i == 7:
                    self.brick.fill_color = 'ivory'
                if i == 8:
                    self.brick.fill_color = 'teal'
                if i == 9:
                    self.brick.fill_color = 'teal'

                self.window.add(self.brick, x=brick_position_x, y=brick_position_y)
                brick_position_x = brick_position_x + brick_width + brick_spacing
            brick_position_y = brick_position_y + brick_height + brick_spacing

        # Initialize our mouse listeners
        onmousemoved(self.change_position)
        onmouseclicked(self.set_ball_velocity)

        # mouse switch
        self.click = True

    def get_dx(self):
        return self.__dx

    def set_dx(self, new_dx):
        self.__dx = new_dx

    def get_dy(self):
        return self.__dy

    def set_dy(self, new_dy):
        self.__dy = new_dy

    def change_position(self, event):
        if 0 + PADDLE_WIDTH/2 < event.x < self.window_width - PADDLE_WIDTH/2:
            self.paddle.x = event.x - PADDLE_WIDTH / 2

    def reset_ball(self):
        self.ball.x = (self.window_width - self.ball_radius * 2)/2
        self.ball.y = (self.window_height - self.ball_radius * 2)/2

    # 放在 onmouseckicked 裡面的 funciton，要拿一個變數去裝滑鼠資訊
    def set_ball_velocity(self, event):
        # 做一個開關確保滑鼠連續點擊不影響球的速度
        if self.click:  # self.click is a bool value, it is preset to be True
            self.click = False
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx
            if random.random() > 0.5:
                self.__dy = -self.__dy

    def ball_collide_paddle(self):
        collide_ball = self.window.get_object_at(self.ball.x, self.ball.y + self.ball_radius*2)
        if collide_ball is not None:
            self.__dy *= -1
            if collide_ball.y < self.window_height - (PADDLE_OFFSET + PADDLE_HEIGHT):
                self.window.remove(collide_ball)
                self.count = self.count - 1
                if self.count == 0:
                    self.you_win()

        else:
            collide_ball = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y +
                                                     self.ball_radius * 2)
            if collide_ball is not None:
                self.__dy *= -1
                if collide_ball.y < self.window_height - (PADDLE_OFFSET + PADDLE_HEIGHT):
                    self.window.remove(collide_ball)
                    self.count = self.count - 1
                    if self.count == 0:
                        self.you_win()

            else:
                collide_ball = self.window.get_object_at(self.ball.x, self.ball.y)
                if collide_ball is not None:
                    self.__dy *= -1
                    if collide_ball.y < self.window_height - (PADDLE_OFFSET + PADDLE_HEIGHT):
                        self.window.remove(collide_ball)
                        self.count = self.count - 1
                        if self.count == 0:
                            self.you_win()

                else:
                    collide_ball = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
                    if collide_ball is not None:
                        self.__dy *= -1
                        if collide_ball.y < self.window_height - (PADDLE_OFFSET + PADDLE_HEIGHT):
                            self.window.remove(collide_ball)
                            self.count = self.count - 1
                            if self.count == 0:
                                self.you_win()

                    else:
                        pass

    def game_over(self):
        game_over_label = GLabel(label='game over')
        self.window.add(game_over_label, x=(self.window_width - game_over_label.width)/2,
                        y=(self.window_height - game_over_label.height)/2)

    def you_win(self):
        you_win_label = GLabel(label='you win!')
        self.window.add(you_win_label, x=(self.window_width - you_win_label.width)/2,
                        y=(self.window_height - you_win_label.height)/2)

    def dead(self):
        # 滑鼠開關打開，準備執行下一run
        self.click = True
        # 速度歸零，才不會讓球一直動
        self.__dx = 0
        self.__dy = 0