import unittest
from src.fingerprint import Fingerprint
from src.preprocess import enhance_image, binarize_image

class TestFingerprint(unittest.TestCase):

    def setUp(self):
        self.fingerprint = Fingerprint()

    def test_capture_fingerprint(self):
        # Assuming capture_fingerprint returns an image array
        image = self.fingerprint.capture_fingerprint()
        self.assertIsNotNone(image)
        self.assertGreater(len(image), 0)

    def test_process_image(self):
        # Assuming process_image returns a processed image
        raw_image = self.fingerprint.capture_fingerprint()
        processed_image = self.fingerprint.process_image(raw_image)
        self.assertIsNotNone(processed_image)

    def test_extract_features(self):
        raw_image = self.fingerprint.capture_fingerprint()
        features = self.fingerprint.extract_features(raw_image)
        self.assertIsNotNone(features)
        self.assertGreater(len(features), 0)

    def test_enhance_image(self):
        raw_image = self.fingerprint.capture_fingerprint()
        enhanced_image = enhance_image(raw_image)
        self.assertIsNotNone(enhanced_image)

    def test_binarize_image(self):
        raw_image = self.fingerprint.capture_fingerprint()
        binary_image = binarize_image(raw_image)
        self.assertIsNotNone(binary_image)

if __name__ == '__main__':
    unittest.main()