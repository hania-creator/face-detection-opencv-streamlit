import unittest

import detector


class DetectorPathTests(unittest.TestCase):
    def test_model_paths_resolve_to_existing_files(self):
        prototxt_path, model_path = detector.get_model_paths()
        self.assertTrue(prototxt_path.exists(), f"Expected {prototxt_path}")
        self.assertTrue(model_path.exists(), f"Expected {model_path}")


if __name__ == "__main__":
    unittest.main()
