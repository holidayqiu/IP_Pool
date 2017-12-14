from xicidaili.items import IPinfo
from xicidaili.mylpipelines.SQL import SQL

class pipelines(object):
    def process_item(self,item,spider):
        if isinstance(item,IPinfo):
            addr = item['addr']
            port = item['port']
            location = item['location']
            is_uknow = item['is_uknow']
            type = item['type']
            speed = item['speed']
            connect_time = item['connect_time']
            survival = item['survival']
            proving_date = item['proving_date']



            SQL.insert_ip(addr, port, location, is_uknow, type, speed, connect_time, survival, proving_date)
            print('写入IP地址')



