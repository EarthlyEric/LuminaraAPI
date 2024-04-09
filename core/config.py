import configobj
import os

class Config:
    def __init__(self):
        self.config = configobj.ConfigObj('./config.ini')
        self.version = self.config['version']
        self.buildid = os.getenv('NF_DEPLOYMENT_SHA') # For Northflank

    