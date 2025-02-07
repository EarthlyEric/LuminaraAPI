import json
import os
import subprocess

def getCommitSHA():
    try:
        sha = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')
        return sha
    except subprocess.CalledProcessError as e:
        return None
    
def genSecretKey():
    if not os.path.exists('./core/secret'):
        with open('./core/secret', 'w') as f:
            key = str(os.urandom(32).hex())
            f.write(key)
            
    with open('./core/secret','r') as f:
        if f.read().strip() == '':
            key = str(os.urandom(32).hex())
            with open('./core/secret', 'w') as f:
                f.write(key)
        else:
            return f.read().strip()

class Config:
    def __init__(self,versionFile='./core/version'):
        with open(versionFile) as file:
            self.version = json.load(file)['version']
        
        # Get the build ID from the environment variable of Northflank or from the git commit SHA
        self.build_id = os.getenv('NF_DEPLOYMENT_SHA', getCommitSHA())
        
        # Database connection
        self.user = os.getenv('POSTGRES_USER')
        self.password = os.getenv('POSTGRES_PASSWORD')
        self.host = os.getenv('POSTGRES_HOST')
        self.port = os.getenv('POSTGRES_PORT')
        self.database = os.getenv('POSTGRES_DB')
        self.database_debug = bool(os.getenv('POSTGRES_DEBUG', False))
        
        self.jwt_secret_key = os.getenv('SECRET_KEY', genSecretKey())
        
config = Config()

if __name__ == '__main__':
    print(config.version)
    print(config.build_id)
    print(config.user)
    print(config.password)
    print(config.host)
    print(config.port)
    print(config.database)
    print(config.database_debug)
    print(config.jwt_secret_key)