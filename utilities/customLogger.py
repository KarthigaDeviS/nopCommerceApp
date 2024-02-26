import logging

class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="D:\\nopCommerceApp\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%y %I:%M:%S %p', level=logging.DEBUG)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

logger = LogGen.loggen()
logger.info(("********** Test_003_AddCustomer ************"))