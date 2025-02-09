from scenarios.phishing import PhishingScenario
from scenarios.pretexting import PretextingScenario
from scenarios.baiting import BaitingScenario

def run_simulation():
    print("Running Social Engineering Simulation...")
    phishing = PhishingScenario()
    phishing.execute()

    pretexting = PretextingScenario()
    pretexting.execute()

    baiting = BaitingScenario()
    baiting.execute()

if __name__ == "__main__":
    run_simulation()
