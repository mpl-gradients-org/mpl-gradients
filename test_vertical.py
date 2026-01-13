import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import to_rgba

class VerticalGradient:
    def __init__(self, color_top, color_bottom):
        self.color_top = np.array(to_rgba(color_top))
        self.color_bottom = np.array(to_rgba(color_bottom))

    def __call__(self, im, dpi):
        # im shape is (Height, Width, 4)
        height, width, depth = im.shape

        # 1. Create a mixing factor from 0 to 1 based on HEIGHT
        # We reshape it to (Height, 1, 1) so it can broadcast across Width and Channels
        factor = np.linspace(0, 1, height)[:, None, None]

        # 2. Calculate the Gradient Color
        # Formula: Color = Factor * (Bottom - Top) + Top
        gradient_color = factor * (self.color_bottom - self.color_top) + self.color_top

        # 3. Handle Transparency (The "Alpha" Fix)
        # We want the gradient color, but we MUST respect the original shape's transparency.
        # Original Image Alpha is at index 3.
        original_alpha = im[:, :, 3] 
        
        # New Alpha = Gradient's Alpha * Original Shape's Alpha
        final_alpha = gradient_color[:, :, 3] * original_alpha

        # 4. Apply changes
        im[:, :, :3] = gradient_color[:, :, :3] # Update RGB
        im[:, :, 3] = final_alpha               # Update Alpha

        return im, 0, 0

# --- TESTING IT OUT ---
fig, ax = plt.subplots()
bars = ax.bar([1, 2, 3], [5, 3, 8], color='blue')

# Apply our filter
grad = VerticalGradient(color_top="red", color_bottom="yellow")

for bar in bars:
    bar.set_agg_filter(grad)

print("Saving vertical_test.png...")
plt.savefig("vertical_test.png", dpi=100)
# plt.show() # Commented out so it doesn't freeze the terminal if no GUI is available