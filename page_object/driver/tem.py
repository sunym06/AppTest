from appium import webdriver

class AndroidClient():
    caps = {}
    caps["platformName"] = "Android"
    caps["platformVersion"] = "9"
    caps["deviceName"] = "b675c20"
    caps["appPackage"] = "com.great_mall.u4"
    caps["appActivity"] = "io.dcloud.PandoraEntryActivity"

    def __init__(self):
        self.driver = self.installAPP()

    @classmethod
    def installAPP(cls):

        # caps['noReset'] = True
        cls.caps["autoGrantPermissions"] = "true"
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub",cls.caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def restartAPP(cls):
        caps = {}
        caps["platformName"] = "Android"
        caps["platformVersion"] = "9"
        caps["deviceName"] = "b675c20"
        caps["appPackage"] = "com.great_mall.u4test"
        caps["appActivity"] = "io.dcloud.PandoraEntryActivity"
        caps['noReset'] = True

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        return cls.driver

a = AndroidClient()
a.driver.find_element_by_xpath('//*').click()