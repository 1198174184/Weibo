from scrapy import Request, Spider


class WeiboSpider(Spider):
    name = 'weibocn'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['http://m.weibo.cn/']
    
    user_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&value={uid}&containerid=100505{uid}'
    
    follower_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_{uid}&uid={uid}&page={page}'
    
    fan_url = 'https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_{uid}&uid={uid}&page={page}'
    
    weibo_url = 'https://m.weibo.cn/api/container/getIndex?uid={uid}&type=uid&page={page}&containerid=107603{uid}'
    
    comment_url = 'https://m.weibo.cn/api/comments/show?id={id}&page={page}'
    
    repost_url = 'https://m.weibo.cn/api/statuses/repostTimeline?id={id}&page={page}'
    
    start_users = ['3217179555', '1742566624', '2282991915', '1288739185', '3952070245', '5878659096']
    
    def start_requests(self):
        for uid in self.start_users:
            yield Request(self.user_url.format(uid=uid), callback=self.parse_user, priority=3)
    
    def parse_user(self, response):
        self.logger.debug(response)
