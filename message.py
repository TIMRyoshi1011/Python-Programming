# Encoding: UTF-8
"""Message screen.

This is where the player receives their fortune.
"""
import json
import pathlib
import random

import arcade
import arcade.color as color

import fortune_cookie as game


class MessageView(arcade.View):
    def on_show_view(self):
        """Run once when we switch to this view."""
        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, self.window.width, 0, self.window.height)

    def setup(self):
        """Set up the "level" here."""
        self.ui = arcade.SpriteList(use_spatial_hash=True)

        #Randomly select a fortune to display.
        with pathlib.Path.open(pathlib.Path(f"{game.CFG}/dev.json")) as file:
            fortunes: list = json.load(file) ["fortunes"]

        self.fortune = random.choice (fortunes) # noqa: S311, DUO102

        #Display the paper
        paper = arcade.Sprite(f"{game.IMG}/message.png", 0.40)

        paper.center_x = self.window.width / 2 - 50
        paper.center_y = self.window.height / 2 + 75

        self.ui.append(paper)

        # TODO: Add sound effect to congratulate the player on their fortune

    def on_mouse_press(self, x: int, y: int, button: int, modiflers: int):
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
        # ? when clicked, should the game restart?
        pass

    def on_draw(self):
        """Render the screen.

        ### Notes
            This class instance method should not be called directly. It's for Arcade's 
            internal use only. but you may write code here to define what should be
            drawn on screen every frame.
        """
        self.clear()

        # Code to draw the screen goes here
        self.ui.draw()
        arcade.draw_text (
            self.fortune,
            self.window.width / 2,
            self.window.height / 2,
            color.BLACK,
            font_size=14,
            anchor_x="center",
        )
