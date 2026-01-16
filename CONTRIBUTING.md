# Contributing to mpl-gradients

First off, thank you for considering contributing to `mpl-gradients`! It's people like you that make open source tools great.

## 🛠️ Development Setup

Since this library is designed to be **zero-dependency** (only relying on `matplotlib` and `numpy`), setting up the environment is very fast.

1.  **Fork** the repository on GitHub.
2.  **Clone** your fork locally:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/mpl-gradients.git](https://github.com/YOUR_USERNAME/mpl-gradients.git)
    cd mpl-gradients
    ```
3.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```
4.  **Install in editable mode** with test dependencies:
    ```bash
    pip install -e .
    pip install pytest
    ```

## 🧪 Running Tests

Please ensure all tests pass before submitting a Pull Request.

```bash
pytest
