import unittest

from phishing_risk_analyzer import calculate_risk_score, get_risk_rating


class PhishingRiskAnalyzerTests(unittest.TestCase):
    def test_low_rating_for_no_warning_signs(self):
        self.assertEqual(calculate_risk_score([False] * 6), 0)
        self.assertEqual(get_risk_rating(0), "low")

    def test_medium_rating_at_boundary(self):
        self.assertEqual(get_risk_rating(3), "medium")
        self.assertEqual(get_risk_rating(5), "medium")

    def test_high_rating_at_boundary(self):
        self.assertEqual(get_risk_rating(6), "high")
        self.assertEqual(get_risk_rating(12), "high")

    def test_yes_answers_are_scored(self):
        score = calculate_risk_score(["yes", "yes", "no", "no", "no", "no"])
        self.assertEqual(score, 5)


if __name__ == "__main__":
    unittest.main()
