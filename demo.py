import matplotlib.pyplot as plt
import numpy as np
from gradients import LinearGradient

def plot_gradient_demo():
    # Use a wider figure to give bars breathing room
    fig, axes = plt.subplots(1, 3, figsize=(12, 5))
    
    # Standard data for all plots
    x = np.arange(2)  # [0, 1]
    heights = [0.8, 0.8] # Uniform height
    
    # --- 1. Vertical Gradient (Red -> Yellow) ---
    axes[0].bar(x, heights, color="white", edgecolor="black") # clearer borders
    axes[0].set_title("Vertical\n(Red $\\to$ Yellow)")
    
    grad_v = LinearGradient("red", "gold", direction="vertical")
    for bar in axes[0].containers[0]:
        bar.set_agg_filter(grad_v)

    # --- 2. Horizontal Gradient (Purple -> Cyan) ---
    # We use 'barh' here. 
    # Note: For barh, the "height" parameter controls the thickness of the bar.
    axes[1].barh(x, heights, color="white", edgecolor="black")
    axes[1].set_title("Horizontal\n(Purple $\\to$ Cyan)")
    
    grad_h = LinearGradient("rebeccapurple", "cyan", direction="horizontal")
    for bar in axes[1].containers[0]:
        bar.set_agg_filter(grad_h)

    # --- 3. Diagonal Gradient (Blue -> Lime) ---
    # Changing colors to avoid the "muddy gray" middle
    axes[2].bar(x, heights, color="white", edgecolor="black")
    axes[2].set_title("Diagonal\n(Navy $\\to$ Lime)")
    
    grad_d = LinearGradient("navy", "lime", direction="diagonal")
    for bar in axes[2].containers[0]:
        bar.set_agg_filter(grad_d)

    # --- Global Styling for Consistency ---
    for ax in axes:
        # Remove axis junk to focus on the gradients
        ax.set_xticks([])
        ax.set_yticks([])
        # Remove spines (borders)
        for spine in ax.spines.values():
            spine.set_visible(False)

    plt.tight_layout()
    print("Saving polished_demo.png...")
    plt.savefig("polished_demo.png", dpi=120)
    plt.show()

if __name__ == "__main__":
    plot_gradient_demo()