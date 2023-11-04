import scrapy


class QuotesSpider(scrapy.Spider):
    name = "Data"
    start_urls = [
        "https://s.cafef.vn/Ajax/PageNew/DataHistory/ThongKeDL.ashx?Symbol=HDB&StartDate=&EndDate=&PageIndex=1&PageSize=20",
    ]

    def parse(self, response):
        resp = json.loads(response.body)
        data = resp.get('Data')
        print(data)
        for datum in data:
            yield{
                "date": datum.get("Date"),
                "ThayDoi": datum.get("ThayDoi"),
                "SoLenhMua": datum.get("SoLenhMua"),
                "KLDatMua": datum.get("KLDatMua "),
                "KLTB1LenhMua": datum.get("KLTB1LenhMua"),
                "SoLenhDatBan": datum.get("KLDatBan"),
                "KLTB1LenhBan": datum.get("KLTB1LenhBan"),
                "ChenhLechKL": datum.get("ChenhLechKL")
            }


if __name__ == "__main__":
    t = QuotesSpider()
    t.parse()