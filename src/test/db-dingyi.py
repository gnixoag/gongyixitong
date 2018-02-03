# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 20:56:56 2018

@author: gaoxing
"""

from sqlalchemy import create_engine,Column,String,Integer,ForeignKey,Sequence,event,DDL
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from numpy import integer
from sqlalchemy.orm import relationship,sessionmaker,scoped_session



engine=create_engine("sqlite:///users.db",echo=True)

Base=declarative_base()
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


class Users(Base):
    __tablename__="dbt_user"
    
    uid=Column(Integer,Sequence('user_id_seq'),primary_key=True)
    name=Column(String(20))
    email=Column(String)
    password=Column(String)
    address=Column(String)
    group_name=Column(String,ForeignKey("dbt_group.gid"))


class Group(Base):
    __tablename__="dbt_group"
    gid=Column(Integer,primary_key=True)
    group_name=Column(String)
    users=relationship("Users")
    
class UsersDB(object):

    def initDB(self):
        '''
        1. 用DDL方式，为unique键添加自动增长
        2. 初始化数据库,找到BaseModel的所有子类,并在数据库中建立这些表,models里面的数据,bind绑定一个会话链接
        '''
#        event.listen(
#            Users.__table__,
#            'after_create',
#            DDL("alter table log MODIFY id INT AUTO_INCREMENT;")
#        )
        Base.metadata.create_all(bind=engine)

    def insert(self, element):
        '''
        单条插入mysql数据库
        '''
        flag = False
        try:
            session.add(element)
            session.commit()
            flag = True
        except:
            print ('\nerror element:'+element.getSelf()+'\t插入数据库失败,请查看主键以及唯一键约束!')
            session.rollback()
            session.flush()  # for resetting non-commited .add()
        finally:
            return flag

    def insertBatch(self, element_list):
        '''
        批量插入数据库
        '''
        successNum = 0
        failNum = 0
        for element in element_list:
            if self.insert(element):
                successNum += 1
            else:
                failNum += 1
        return successNum, failNum

    def insertLogtBulk(self, element_list, batch_num, type):
        '''
        批量插入mysql数据库Log表,一次批量插入batch_num条数据
        '''
        mysql_batch_list = []
        mysql_batch_num = batch_num
        for element in element_list:
            # 先检查在mysql中是否存在该条记录, 不存在则插入mysql
            follow_item_exist = getattr(m_models, type).query.filter_by(id=element.id).first()
            if not follow_item_exist:
                mysql_batch_list.append(element)
                mysql_batch_num -= 1
            else:
                print ("数据库Log表,已经存在记录:", element.getSelf())
            # 如果mysql_batch_num 自减到0,则提交到数据库
            if not mysql_batch_num:
                session.add_all(mysql_batch_list)
                session.commit()
                mysql_batch_num = batch_num
                mysql_batch_list = []
        session.add_all(mysql_batch_list)
        session.commit()


DBSession = sessionmaker(bind=engine)
session=DBSession()


a=Users(name='高星',email="gnix.oag@gmail.com",password="12345",address="galj",group_name="管理员")

userdb=UsersDB()

userdb.initDB()

userdb.insert(a)






