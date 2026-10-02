import logging

def get_logger(name="workflow"):
    if not logging.getLogger().handlers:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s" ,
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler("engine.log", encoding="utf-8"),
            ],
        )
    return logging.getLogger(name)

logger = get_logger("workflow")