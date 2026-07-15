from passlib.context import CryptContext
'''
Password(passlib.context)
   │
   ▼
CryptContext (Security machine)
   │
   ├── hash()   → Creates a hashed password
   └── verify() → Checks if a password matches the hash
'''
pwd_cxt = CryptContext(schemes=['bcrypt'],deprecated='auto') # deprecated means if in future bcrypt old or no longer recommended

class Hash():
    def bcrypt(password:str):
        return pwd_cxt.hash(password)    # hash ->method provided by passlib
    
    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password) # verify ->method provided by passlib
