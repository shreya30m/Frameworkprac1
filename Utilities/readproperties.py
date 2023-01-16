import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:    #for every variable in config.ini file,we have to create one method for reading

    @staticmethod
    def getAppURL():
        url = config.get('INFO','baseURL')
        return url

    @staticmethod
    def getUseremail():
        mailid = config.get('INFO','email')
        return mailid

    @staticmethod
    def getUserPass():
        passwo = config.get('INFO','Passw')
        return passwo
