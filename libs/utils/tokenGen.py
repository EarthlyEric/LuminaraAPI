import secrets
import jwt
import datetime
from datetime import datetime,timedelta
from typing import Optional

SECRET_KEY ="mysecretkey"
ALGORITHM = "HS256"
DEFAULT_ACCESSTOKEN_EXPIRE_DAY= 30

def createAccessToken(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta if expires_delta else timedelta(days=DEFAULT_ACCESSTOKEN_EXPIRE_DAY))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verifyAccessToken(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False
    
def generateAPIKey():
    parts = [secrets.token_hex(4) for _ in range(5)]
    return "-".join(parts)
