'''
Created on 2018年2月3日

@author: gaoxing
'''
import os, base64
from hashlib import sha512
from hmac import HMAC

class Encrypt():
    '''
    classdocs
    '''
    

    def __init__(self ):
        '''
        Constructor
        '''
        pass
    
    def encrypt(self,password, salt=None):
        """Hash password on the fly."""
        if salt is None:
            salt = os.urandom(8)
    
        #如果指定 salt， 进行 salt 检查
        assert 8 == len(salt)
        assert isinstance(salt, bytes)
        assert isinstance(password, str)
        
        if isinstance(password, str):
            password = password.encode('UTF-8')
    
        assert isinstance(password, bytes)
    
        result = password 
        
        #使用 sha512 进行20次随机加密
        for i in range(20):
            result = HMAC(result, salt, sha512).digest()
            
        #返回utf-8加密字符（把salt加入用于验证加密）
        return str(base64.b64encode(salt + result),encoding="utf-8") 
    
    def validate(self,hashed, input_password):
        salt=base64.b64decode(bytes(hashed, encoding = "utf8"))
        return hashed == self.encrypt(input_password, salt[:8])