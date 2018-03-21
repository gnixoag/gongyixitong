import configparser

config = configparser.ConfigParser()
config.read('gongyixitong/init/db.cfg.txt')


config.write(open('gongyixitong/init/db.cfg.txt','w'))

