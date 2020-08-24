# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

def get_host_name(url: str) -> str:
    return url.split("/")[2]


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        ret = []
        to_visit = collections.deque()
        to_visit.append(startUrl)
        host_name = get_host_name(startUrl)
        added = set([startUrl])

        while len(to_visit) > 0:
            url = to_visit.popleft()
            ret.append(url)

            suburls = filter(lambda u: get_host_name(u) == host_name, htmlParser.getUrls(url))

            for suburl in suburls:
                if suburl not in added:
                    added.add(suburl)
                    to_visit.append(suburl)

        return ret


        
