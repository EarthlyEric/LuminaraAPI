import configobj

class Config:
    def __init__(self):
        self.config = configobj.ConfigObj('./config.ini')
        self.version = self.config['version']

    