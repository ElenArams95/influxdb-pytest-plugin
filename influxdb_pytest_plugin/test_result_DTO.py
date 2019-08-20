class TestResultDTO:
    __run = None
    __test = None
    __status = None
    __project = None
    __version = None
    __screenshot = None
    __duration_sec = None
    __exception = None

    def get_run(self):
        return self.__run

    def set_run(self, run):
        self.__run = run

    def get_test(self):
        return self.__test

    def set_test(self, test):
        self.__test = test

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_project(self):
        return self.__project

    def set_project(self, project):
        self.__project = project

    def get_version(self):
        return self.__version

    def set_version(self, version):
        self.__version = version

    def get_screenshot(self):
        return self.__screenshot

    def set_screenshot(self, screenshot):
        self.__screenshot = screenshot

    def get_duration_sec(self):
        return self.__duration_sec

    def set_duration_sec(self, duration_sec):
        self.__duration_sec = duration_sec

    def get_exception(self):
        return self.__exception

    def set_exception(self, exception):
        self.__exception = exception
