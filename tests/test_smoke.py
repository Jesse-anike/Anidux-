import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("project_main", ROOT / "main.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class AlertDeduplicatorTests(unittest.TestCase):
    def test_deduplicates_key_order_independently(self):
        data = '{"a":1,"b":2}\n{"b":2,"a":1}\n'
        result = module.analyze(data)
        self.assertEqual(result["input_events"], 2)
        self.assertEqual(result["unique_count"], 1)
        self.assertEqual(result["unique_alerts"][0]["occurrences"], 2)

    def test_counts_invalid_lines(self):
        result = module.analyze('{bad json}\n{"ok":true}\n')
        self.assertEqual(result["invalid_lines"], 1)
        self.assertEqual(result["input_events"], 1)


if __name__ == "__main__":
    unittest.main()
