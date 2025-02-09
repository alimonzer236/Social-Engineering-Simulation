import unittest
from src.scenarios.phishing import PhishingScenario
from src.scenarios.pretexting import PretextingScenario
from src.scenarios.baiting import BaitingScenario

class TestScenarios(unittest.TestCase):
    def test_phishing(self):
        phishing = PhishingScenario()
        phishing.execute()

    def test_pretexting(self):
        pretexting = PretextingScenario()
        pretexting.execute()

    def test_baiting(self):
        baiting = BaitingScenario()
        baiting.execute()
