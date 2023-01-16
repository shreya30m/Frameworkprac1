import logging

class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\Logs\\automation.log",
        #                 format='%(asctime)s :%(levelname)s : %(name)s :%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

        logger = logging.getLogger()
        fileHandler = logging.FileHandler('.\\Logs\\automation.log',mode='a')
        formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(name)s-%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
