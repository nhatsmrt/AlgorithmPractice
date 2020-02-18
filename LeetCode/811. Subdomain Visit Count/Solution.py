class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_cnt = {}

        for info in cpdomains:
            cnt, domain = info.split(" ")
            cnt = int(cnt)
            subdomains = domain.split(".")

            subdomain = ""
            for i in range(len(subdomains)):
                if len(subdomain) > 0:
                    subdomain = "." + subdomain
                subdomain = subdomains[len(subdomains) - 1 - i] + subdomain
                visit_cnt[subdomain] = visit_cnt.get(subdomain, 0) + cnt

        return [str(visit_cnt[subdomain]) + " " + subdomain for subdomain in visit_cnt]        
