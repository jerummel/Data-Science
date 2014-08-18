import scrapy
from wc.items import WcItem

class WCSpider(scrapy.Spider):
    name = "wc"
    allowed_domains = ["fifa.com"]
    start_urls = ['http://www.fifa.com/worldcup/matches/index.html']
    hosts = ('southafrica2010', 'germany2006', 'koreajapan2002', 'france1998', 'usa1994', 
        'italy1990', 'mexico1986', 'spain1982', 'argentina1978', 'germany1974', 'mexico1970', 'england1966', 
        'chile1962', 'sweden1958', 'switzerland1954', 'brazil1950', 'france1938', 'italy1934', 'uruguay1930')
    other_urls = [
        "http://www.fifa.com/tournaments/archive/worldcup/%s/matches/index.html" % host for host in hosts]
    start_urls.extend(other_urls)

    def findRoundBrazil(self, group):
        if(group == 'Final'):
            return 'Round 5'
        elif(group == 'Play-off for third place' or group == 'Semi-finals'):
            return 'Round 4'
        elif (group == 'Quarter-finals'):
            return 'Round 3'
        elif (group == 'Round of 16'):
            return 'Round 2'
        else:
            return 'Round 1'

    def findRound(self, year, idx):
        if(year > 1990):
            if(idx < 8):
                return 'Round 1'
            elif(idx == 8):
                return 'Round 2'
            elif (idx == 9):
                return 'Round 3'
            elif (idx < 12):
                return 'Round 4'
            else:
                return 'Round 5'
        elif(year > 1982):
            if(idx < 6):
                return 'Round 1'
            elif(idx == 6):
                return 'Round 2'
            elif(idx == 7):
                return 'Round 3'
            elif(idx < 10):
                return 'Round 4'
            else:
                return 'Round 5'
        elif(year == 1982):
            if(idx < 6):
                return 'Round 1'
            elif(idx < 10):
                return 'Round 2'
            elif(idx < 12):
                return 'Round 3'
            else:
                return 'Round 4'
        elif(year > 1970):
            if(idx < 4):
                return 'Round 1'
            elif(idx < 7):
                return 'Round 2'
            else:
                return 'Round 3'
        elif(year > 1950):
            if(idx < 4):
                return 'Round 1'
            elif(idx == 4):
                return 'Round 2'
            elif(idx < 7):
                return 'Round 3'
            else:
                return 'Round 4'
        elif(year == 1950):
            if(idx < 4):
                return 'Round 1'
            else:
                return 'Round 2'
        elif(year > 1930):
            if(idx == 0):
                return 'Round 1'
            elif(idx == 1):
                return 'Round 2'
            elif(idx < 4):
                return 'Round 3'
            else:
                return 'Round 4'
        else:
            if(idx < 4):
                return 'Round 1'
            elif(idx == 4):
                return 'Round 2'
            else:
                return 'Round 3'

    def parse(self, response):
        item = WcItem()
        pageTitle = response.xpath('//title/text()').extract()[0]
        if '2014 FIFA World Cup Brazil' in pageTitle:
            for table in response.xpath('//div[@class=\'match-list-date anchor\']'):
                for matchData in table.xpath('.//div[@class=\'col-xs-12 clear-grid \']'):
                    item['match'] = matchData.xpath('./div/a/div[1]/div[3]/text()').extract()[0][6:]
                    group = matchData.xpath('./div/a/div[1]/div[4]/text()').extract()[0]
                    item['wcRound'] = self.findRoundBrazil(group)
                    item['group'] = group
                    dateString = matchData.xpath('./div/a/div[1]/div[2]/text()').extract()[0]
                    dateList = dateString.rsplit(' ', 1)
                    item['date'] = dateList[0]
                    item['year'] = dateList[1]
                    item['venue'] = matchData.xpath('./div/a/div[1]/div[5]/div[2]/text()').extract()[0]
                    item['hometeam'] = matchData.xpath('./div/a/div[3]/div[1]/div[2]/span[1]/text()').extract()[0]
                    score = matchData.xpath('./div/a/div[3]/div[3]/div/div[3]/span/text()').extract()[0]
                    score = score.replace('-', ':')
                    ot = matchData.xpath('./div/a/div[3]/div[5]/span[1]/text()').extract()[0]
                    ot = ot.replace('-', ':')
                    if(ot != ' '):
                        if(ot[len(ot)-1] == ' '):
                            ot = ot[:-1] #get rid of the space at the end
                        item['results'] = "%s %s" % (score, ot)
                    else:
                        item['results'] = score
                    item['awayteam'] = matchData.xpath('./div/a/div[3]/div[2]/div[2]/span[1]/text()').extract()[0]
                    yield item
        else:
            groups = [caption.xpath('text()').extract()[0] for caption in response.xpath('//caption')]
            year = pageTitle[:4]
            year = int(year)
            item = WcItem()
            for idx, table in enumerate(response.xpath('//table[@class=\'fixture \']')):
                wcGroup= groups[idx]
                for tableRow in table.xpath('.//tr'):
                    if(len(tableRow.xpath('./th[1]/text()').extract()) > 0):
                        continue
                    item['match'] = tableRow.xpath('./td[1]/text()').extract()[0]
                    item['wcRound'] = self.findRound(year, idx)
                    item['group'] = wcGroup
                    item['date'] = tableRow.xpath('./td[2]/text()').extract()[0]
                    item['year'] = year
                    item['venue'] = tableRow.xpath('./td[3]/text()').extract()[0]
                    item['hometeam'] = tableRow.xpath('./td[5]/a/text()').extract()[0]
                    score = tableRow.xpath('./td[6]/a/text()').extract()
                    if(len(score) == 0):
                        score = tableRow.xpath('./td[6]/div/a/text()').extract()
                    item['results'] = score[0]
                    item['awayteam'] = tableRow.xpath('./td[7]/a/text()').extract()[0]
                    yield item