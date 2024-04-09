import configobj
import os

class Config:
    def __init__(self):
        self.config = configobj.ConfigObj('./config.ini')
        self.version = self.config['version']
        self.buildid = os.getenv('BUILD_ID')

    