import re


class Solution:
    def maskPII(self, S: str) -> str:
        name_pattern = r'[a-zA-Z]{2,}'
        email_pattern = name_pattern + r'@' + name_pattern + r'\.' + name_pattern
        local_mask = "***-***-"


        if re.search(email_pattern, S):
            S = S.lower()
            first_name = re.search(name_pattern, S).group(0)
            return first_name[0] + "*****" + first_name[-1] + S[len(first_name):]
        else:
            # must be a phone number
            S = re.sub(r"[\(\) ]", "", S)
            digits = list(filter(lambda c: c in "0123456789", S))
            is_local = len(digits) == 10

            if is_local:
                return local_mask + "".join(digits[-4:])
            else:
                return "+" + "".join(["*"] * (len(digits) - 10)) + "-" + local_mask + "".join(digits[-4:])
