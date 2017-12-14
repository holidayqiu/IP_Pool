from xicidaili import settings
from xicidaili.items import IPinfo
import pymysql

mysql_host=settings.MYSQL_HOST
mysql_uesr=settings.MYSQL_USER
mysql_psd=settings.MYSQL_PASSWORD
mysql_db=settings.MYSQL_DATABASE

db=pymysql.connect(mysql_host,mysql_uesr,mysql_psd,mysql_db)
cursor=db.cursor()

class SQL():

    @classmethod
    def insert_ip(cls,addr,port,location,is_uknow,type,speed,connect_time,survival,proving_date):
        sql='insert into ip_list(`addr`,`port`,`location`,`is_uknow`,`type`,`speed`,`connect_time`,`survival`,`proving_date`)VALUES' \
            ' (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql,(addr,port,location,is_uknow,type,speed,connect_time,survival,proving_date))
        db.commit()