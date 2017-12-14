import scrapy
from scrapy.http import request,Request
from xicidaili.items import IPinfo



class xicidaili(scrapy.Spider):
    name = 'xicidaili'
    base_url='http://www.xicidaili.com/nn/'
    def start_requests(self):
        header={
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
        }
        for page in range(1,2):
            yield Request(self.base_url+str(page),self.iplist,headers=header)
    def iplist(self,response):
        table=response.xpath('//table[@id="ip_list"]')[0]
        trs=table.xpath('//tr')[1:]
        for tr in trs:
            new_ip=IPinfo()
            new_ip['addr']=tr.xpath('td[2]/text()').extract()[0]
            new_ip['port'] = tr.xpath('td[3]/text()').extract()[0]
            new_ip['location'] = tr.xpath('string(td[4])').extract()[0].strip()
            new_ip['is_uknow'] = tr.xpath('td[5]/text()').extract()[0]
            new_ip['type'] = tr.xpath('td[6]/text()').extract()[0]
            new_ip['speed'] = tr.xpath('td[7]/div/@title').extract()[0]
            new_ip['connect_time'] = tr.xpath('td[8]/div/@title').extract()[0]
            new_ip['survival'] = tr.xpath('td[9]/text()').extract()[0]
            new_ip['proving_date'] = tr.xpath('td[10]/text()').extract()[0]
            yield new_ip

