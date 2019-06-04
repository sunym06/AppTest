from page_object.driver.AndroidClient import AndroidClient

class basePage():

    def __init__(self):
        self.driver = self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver = AndroidClient.driver
        return cls.driver

    def find(self,kv):
        return self.driver.find_element(*kv)