from utilities.logger import get_logger

logger = get_logger(__name__)


def test_logger():
    logger.info("Logger test started")
    logger.warning("This is a warning")
    logger.error("This is a test error")

    assert True