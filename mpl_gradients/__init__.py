import numpy as np
from matplotlib.colors import to_rgba

class LinearGradient:
    def __init__(self, start_color, end_color, direction="vertical"):
        self.start_color = np.array(to_rgba(start_color))
        self.end_color = np.array(to_rgba(end_color))
        self.direction = direction

    def __call__(self, im, dpi):
        h, w, _ = im.shape

        if self.direction == "vertical":
            factor = np.linspace(0, 1, h)[:, None, None]
        elif self.direction == "horizontal":
            factor = np.linspace(0, 1, w)[None, :, None]
        elif self.direction == "diagonal":
            y_indices = np.linspace(0, 1, h)[:, None]
            x_indices = np.linspace(0, 1, w)[None, :]
            factor = (x_indices + y_indices) / 2
            factor = factor[:, :, None]
        else:
            raise ValueError(f"Unknown direction: {self.direction}")

        gradient_color = factor * (self.end_color - self.start_color) + self.start_color

        original_alpha = im[:, :, 3]
        final_alpha = gradient_color[:, :, 3] * original_alpha

        im[:, :, :3] = gradient_color[:, :, :3]
        im[:, :, 3] = final_alpha

        return im, 0, 0