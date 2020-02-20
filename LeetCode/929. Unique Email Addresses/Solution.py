class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_set = set()
        for email in emails:
            emails_set.add(self.process(email))
        return len(emails_set)

    def process(self, email: str) -> str:
        ret = []

        local_name, domain_name = email.split('@')
        for i in range(len(local_name)):
            if local_name[i] != "." and local_name[i] != "+":
                ret.append(local_name[i])
            elif local_name[i] == "+":
                break

        ret.append("@")
        ret.append(domain_name)

        return ''.join(ret)
