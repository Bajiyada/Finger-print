# Fingerprint Recognition using OpenCV

This project implements a fingerprint recognition system using OpenCV in Python. The system captures fingerprint images, processes them, extracts features, and matches fingerprints based on their features.

## Project Structure

```
fingerprint-opencv-python
├── src
│   ├── main.py               # Entry point of the application
│   ├── fingerprint.py        # Fingerprint processing class
│   ├── preprocess.py         # Image preprocessing functions
│   ├── match.py              # Fingerprint matching functions
│   ├── utils
│   │   └── __init__.py       # Utility functions
│   └── models
│       └── __init__.py       # Machine learning models
├── notebooks
│   └── exploration.ipynb      # Jupyter notebook for data exploration
├── tests
│   └── test_fingerprint.py    # Unit tests for fingerprint processing
├── requirements.txt           # Project dependencies
├── pyproject.toml            # Project configuration
├── .gitignore                 # Files to ignore in version control
└── README.md                  # Project documentation
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd fingerprint-opencv-python
pip install -r requirements.txt
```

## Usage

1. **Capture Fingerprint**: Use the `capture_fingerprint` method from the `Fingerprint` class in `fingerprint.py` to capture a fingerprint image.
2. **Process Image**: Call the `process_image` method to enhance the captured image.
3. **Extract Features**: Use the `extract_features` method to obtain fingerprint features.
4. **Match Fingerprints**: Utilize the `match_fingerprints` function in `match.py` to compare two sets of features and get a similarity score.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.