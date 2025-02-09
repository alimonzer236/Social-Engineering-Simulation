from utils.logger import setup_logger

logger = setup_logger()

class PretextingScenario:
    def execute(self):
        logger.info("Pretexting Scenario: Creating a fabricated scenario...")
        # Simulate pretexting attack
        scenario = "Hello, this is IT support. We need your password to fix an issue."
        logger.info(f"Scenario: {scenario}")
