import unittest
from linker import link


class LinkerTests(unittest.TestCase):
    def test_links_decision_to_code_reference(self):
        report = link([{ "id": "ADR-1" }], [{ "adr": "ADR-1", "type": "code", "path": "app.py" }])
        self.assertEqual(report["decisions"][0]["state"], "linked")

    def test_marks_missing_implementation(self):
        report = link([{ "id": "ADR-2" }], [])
        self.assertEqual(report["unimplemented"], ["ADR-2"])

    def test_marks_superseded_decision(self):
        report = link([{ "id": "ADR-3", "superseded_by": "ADR-4" }], [{ "adr": "ADR-3" }])
        self.assertEqual(report["decisions"][0]["state"], "superseded")


if __name__ == "__main__":
    unittest.main()
