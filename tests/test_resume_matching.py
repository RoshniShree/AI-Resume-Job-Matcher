import unittest

from src.job_matcher import compare_skills


class TestResumeMatching(unittest.TestCase):
    def test_finds_skill_gap(self):
        result = compare_skills(
            "I use Python and SQL for data analysis.",
            "Looking for Python, SQL, and Docker experience.",
        )
        self.assertIn("python", result["resume_skills"])
        self.assertIn("docker", result["skill_gaps"])
        self.assertNotIn("python", result["skill_gaps"])

    def test_empty_inputs(self):
        result = compare_skills("", "")
        self.assertEqual(result["resume_skills"], [])
        self.assertEqual(result["required_skills"], [])
        self.assertEqual(result["skill_gaps"], [])


if __name__ == "__main__":
    unittest.main()
