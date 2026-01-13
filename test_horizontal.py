import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgba

class HorizontalGradient:
    def __init__(self, color_left, color_right):
        self.color_left = np.array(to_rgba(color_left))
        self.color_right = np.array(to_rgba(color_right))

    def __call__(self, im, dpi):
        height, width, depth = im.shape

        # CHANGE IS HERE: 
        # We vary across WIDTH, so we create a list of size 'width'
        # Reshape to (1, Width, 1) so it repeats across Height
        factor = np.linspace(0, 1, width)[None, :, None]

        gradient_color = factor * (self.color_right - self.color_left) + self.color_left

        # Alpha logic is exactly the same
        original_alpha = im[:, :, 3]
        final_alpha = gradient_color[:, :, 3] * original_alpha

        im[:, :, :3] = gradient_color[:, :, :3]
        im[:, :, 3] = final_alpha

        return im, 0, 0

# --- TESTING IT OUT ---
fig, ax = plt.subplots()
# Horizontal bar chart (barh) is better for horizontal gradients!
bars = ax.barh([1, 2, 3], [5, 3, 8])

grad = HorizontalGradient(color_left="purple", color_right="cyan")

for bar in bars:
    bar.set_agg_filter(grad)

print("Saving horizontal_test.png...")
plt.savefig("horizontal_test.png", dpi=100)
