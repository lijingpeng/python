import logging
import logging.config

logging.config.fileConfig('log.config')
main_logger = logging.getLogger('main')
main_logger.debug("test")
main_logger.info("info")
