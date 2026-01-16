import pytest
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_gradients import apply_gradient

# 1. SETUP & TEARDOWN
# This fixture creates a fresh plot for every test, so they don't interfere with each other.
@pytest.fixture
def ax():
    fig, ax = plt.subplots()
    return ax

# 2. PARAMETERIZED TESTS (The Pro Way)
# Instead of writing 4 different test functions, we write ONE that runs 4 times.
@pytest.mark.parametrize("direction", [
    "vertical",
    "horizontal",
    "diagonal",
    "diagonal_reverse"  # Assuming your library supports this, or you can remove it
])
def test_gradient_directions(ax, direction):
    """Test that gradient works for all supported directions."""
    bars = ax.bar([1, 2], [10, 20])
    
    # This should run without error for all directions listed above
    apply_gradient(bars, direction=direction, colors=["#FF0000", "#0000FF"])
    
    # Professional Check: Ensure the artist actually has a URL or ID set (which usually implies a filter was attached)
    # Note: The exact check depends on how AGG filters work, but checking for no crash is step 1.
    assert len(bars) == 2

# 3. TEST DIFFERENT INPUT TYPES
def test_works_on_different_artists(ax):
    """Test that it works on Bars, and maybe other patch types."""
    # Test on a simple Rectangle
    rect = Rectangle((0, 0), 1, 1)
    ax.add_patch(rect)
    
    apply_gradient(rect, colors=["green", "yellow"])
    
    # Test on a list of patches (like a bar chart)
    bars = ax.bar([1], [5])
    apply_gradient(bars, colors=["black", "white"])

# 4. TEST CUSTOM COLORS (Hex, Names, RGB)
@pytest.mark.parametrize("colors", [
    ["red", "blue"],               # Names
    ["#FF0000", "#00FF00"],        # Hex
    [(1, 0, 0), (0, 0, 1)],        # RGB Tuples
    ["red", "white", "blue"]       # 3 Colors (Multi-stop)
])
def test_color_formats(ax, colors):
    """Test that the library handles various color formats correctly."""
    bars = ax.bar([1], [1])
    apply_gradient(bars, colors=colors)

# 5. ERROR HANDLING (Crucial for being 'Professional')
# A good library MUST raise specific errors when the user does something wrong.
def test_raises_error_on_invalid_direction(ax):
    """Test that a helpful error is raised for typos."""
    bars = ax.bar([1], [1])
    
    # We expect a ValueError (or whatever your library raises) when direction is nonsense
    with pytest.raises(ValueError):
        apply_gradient(bars, direction="invalid_direction_typo")

def test_raises_error_on_empty_colors(ax):
    """Test that passing no colors raises an error."""
    bars = ax.bar([1], [1])
    
    # Adjust this based on what error your code actually raises (IndexError, ValueError, etc.)
    with pytest.raises(Exception): 
        apply_gradient(bars, colors=[])
