# Encoding: UTF-8
"""The title screen of the game."""
# ? Code written here does not get ran when imported but runs when it is ran via the
# ? commmand 'py-m fortune_cookie
# * Imports
import arcade
import arcade.csscolor as css

import fortune_cookie as game
import fortune_cookie.scene.select as select

# * Constants
SCREEN_WIDTH: int = 1080
SCREEN_HEIGHT: int = 720
SCREEN_TITLE: str = "Fortune Cookie"


# !README: https://api.arcade.academy/en/latest/get_started.html
class Game(arcade.Window):
    def __init__(self):
        """Initialize the game."""
        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE) #type: ignore

        arcade.set_background_color(css.LIGHT_BLUE)


class TitleView(arcade.View):
    """Main application class."""

    def __init__ (self):
        """Initialize the game."""
        # Call the parent class and set up the window
        super().init() # type: ignore

        arcade.set_background_color(css.LIGHT_BLUE)

    def on_show_view(self):
        """Set up the game here. Call this function to restart the game."""
        self.ui = arcade.Spritelist(use_spatial_hash=True)
        self.headers = arcade.Spritelist(use_spatial_hash=True)
        self.cookies = arcade.Spritelist()

        #Setup the title screen text [1]
        title = arcade.Sprite(f"{game.IMG}/title-text.png", 0.32)
        start = arcade.Sprite(f"{game.IMG}/start.png", 0.25)

        title.center_x = SCREEN_WIDTH / 2
        title.center_y = 620

        start.center_x = SCREEN_WIDTH / 2
        start.center_y = 50

        self.headers.append(title)
        self.headers.append(start)

        # Setup the fortune cookie
        title_cookie = arcade.Sprite(f"{game.IMG}/title-cookie.png", 0.32)

        title_cookie.center_x = SCREEN_WIDTH / 2
        title_cookie.center_y = SCREEN_HEIGHT / 2

        self.cookies.append(title_cookie)

    def on_draw(self):
        """Render the screen.

        ### Notes
            This class instance method should not be called directly. It's for Arcade's 
            internal use only, but you may write code here to define what should be 
            drawn on screen every frame.
        """
        self.clear()

        #Code to draw the screen goes here
        self.ui.draw()
        self.headers.draw()
        self.cookies.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        """Call if mouse is pressed.

        ### Parameters
            - x: int
                - X coordinates of the mouse upon press.
            - y: int
                - Y coordinates of the mouse upon press.
            - button: int
                - Which mouse button was used.
            - modifiers: int
                - Modifier keys such as Control, Alt, Shift, etc.

        ### Notes
            This class instance method should not be called directly. It's for Arcade's 
            internal use only, but you may write code here to define what behaviours 
            should occur when the user clicks on something.

            You may use this as a reference
            https://api.arcade.academy/en/latest/tutorials/card_game/index.html#mouse-button-pressed
        """
        start_now = arcade.get_sprites_at_point((x, y), self.cookies)

        if len(start_now) > 0 and button:
            #TODO: Provide the user with audio feedback when they open a cookie. Play
            #TODO: a sound effect basically.

            selection_view = select.SelectionView()
            selection_view.setup()
            self.window.show_view(selection_view)


# I've decided to split each scene of the game into modules. I personally find it's 
# easier to split them up into "levels" rather than as one giant file.
WINDOW = Game()


def main()-> None:
    """Game itself."""
    title = TitleView()
    WINDOW.show_view(title)
    arcade.run()


# [1]: Note that while Arcade can indeed use the fonts installed on the user's system
# instead, we do want to ensure the text gets rendered properly regardless of the fonts 
# installed on the user's PC so we instead use an image of the text.
# ///
