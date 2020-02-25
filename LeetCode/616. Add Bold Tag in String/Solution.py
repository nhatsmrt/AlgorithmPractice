class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        occurences = [self.find(s, word) for word in dict]
        events = []
        for i in range(len(occurences)):
            for occurence in occurences[i]:
                events.append((occurence, True))
                events.append((occurence + len(dict[i]), False))

        events.sort(key=lambda t: t[0])
        num_opening = 0
        text_ind = 0
        ret = []
        for i in range(len(events)):
            event = events[i]
            if event[1]:
                if num_opening == 0:
                    for j in range(text_ind, event[0]):
                        ret.append(s[j])
                    if i == 0 or events[i - 1][0] != events[i][0]:
                        ret.append("<b>")
                    text_ind = event[0]
                num_opening += 1
            else:
                if num_opening == 1:
                    for j in range(text_ind, event[0]):
                        ret.append(s[j])
                    if i == len(events) - 1 or events[i + 1][0] != events[i][0]:
                        ret.append("</b>")
                    text_ind = event[0]
                num_opening -= 1

        ret.append(s[text_ind:])
        return ''.join(ret)

    def find(self, text: str, pattern: str):
        ret = []
        i = 0
        while i < len(text) and i >= 0:
            occur = text[i:].find(pattern)
            if occur >= 0:
                ret.append(occur + i)
                i = occur + i + 1
            else:
                break
        return ret
