import pytest
import matplotlib.pyplot as plt
from mpl_gradients import gradient_fill  # Adjust this import if your function name is different!

def test_import():
    """Test that the library imports without crashing."""
    assert gradient_fill is not None

def test_run_without_error():
    """Test that the function runs on a dummy plot without crashing."""
    fig, ax = plt.subplots()
    ax.bar([1, 2, 3], [1, 2, 3])
    
    # Try running your function
    try:
        gradient_fill(ax) # Add arguments here if your function needs them!
        assert True
    except Exception as e:
        pytest.fail(f"gradient_fill raised an exception: {e}")
