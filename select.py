# Encoding: UTF-8
"""Selection screen.

This is where the player can select which fortune to bless themself with.
"""
import arcade

import fortune_cookie as game
from fortune_cookie.scene.message import MessageView


class SelectionView(arcade.View):
    def on_show_view(self):
        """Run once when we switch to this view."""
        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def setup(self):
        """Set up the "level" here."""
        self.ui = arcade.SpriteList(use_spatial_hash=True)
        self.cookies = arcade.Spritelist()

        # Cookies
        cookie1, cookie2, cookie3 = (
            arcade.Sprite(f"{game.IMG}/fortune-cookie_closed.png", 0.25),
            arcade.Sprite(f"{game.IMG}/fortune-cookie_closed.png", 0.25),
            arcade.Sprite(f"{game.IMG}/fortune-cookie_closed.png", 0.25),
        )

        cookie1.center_x = 360 - 125
        cookie2.center_x = 720 - 125
        cookie3.center_x = 1080 - 125

        cookie1.center_y = 360
        cookie2.center_y = 360
        cookie3.center_y = 360

        self.cookies.append(cookie1)
        self.cookies.append(cookie2)
        self.cookies.append(cookie3)

        # Text
        choose = arcade.Sprite(f"{game.IMG}/choose.png", 0.32)

        choose.center_x = 1080 / 2
        choose.center_y = 620

        self.ui.append(choose)

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
        clicked = arcade.get_sprites_at_point((x, y), self.cookies)

        if len(clicked) > 0 and button:
            # TODO: Provide the user with audio feedback when they open a cookie. Play
            # TODO: a sound effect basically.

            message_view= MessageView()
            message_view.setup()
            self.window.show_view(message_view)

    def on_draw(self):
        """Render the screen.

        ### Notes
            This class instance method should not be called directly. It's for Arcade's 
            internal use only, but you may write code here to define what should be 
            drawn on screen every frame.
        """
        self.clear()

        # Code to draw the screen goes here
        self.ui.draw()
        self.cookies.draw()
