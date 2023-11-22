

import scrapy
import json

class CafefSpider(scrapy.Spider):
    name = "GDTuDoanh"
    # Symbol  mã chứng khoán của các công ti
    # PageSize kích thước tập dữ liệu cần crawl
    start_urls = "https://s.cafef.vn/Ajax/PageNew/DataHistory/GDTuDoanh.ashx?Symbol=HDB&StartDate=&EndDate=&PageIndex=&PageSize=10000"

    def parse(self, response):
        resp = json.loads(response.body)
        print(resp)
        data = resp.get('Data').get("Data")
        print("Data: ",data)
        for datum in data:
            yield{
                "date": datum.get("Date"),
                "KLcpMua": datum.get("KLcpMua"),
                "KLcpBan": datum.get("KLcpBan"),
                "GtMua": datum.get("GtMua"),
                "GtBan": datum.get("GtBan"),
            }
