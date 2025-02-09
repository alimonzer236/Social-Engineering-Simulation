from utils.logger import setup_logger

logger = setup_logger()

class BaitingScenario:
    def execute(self):
        logger.info("Baiting Scenario: Offering a free USB drive...")
        # Simulate baiting attack
        offer = "Free USB drive! Plug it into your computer to claim your gift."
        logger.info(f"Offer: {offer}")
