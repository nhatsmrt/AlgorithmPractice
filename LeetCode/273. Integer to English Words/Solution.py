class Solution(object):
    def __init__(self):
        self.numDict = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen",
            19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
        }

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if (num == 0):
            return "Zero"
        ret = []
        while num > 0:
            if (num >= 1000000000):
                ret.append(self.numDict[num // 1000000000])
                ret.append("Billion")
                num %= 1000000000
            elif (num >= 1000000):
                millionPart = self.numberToWordsLess1000(num // 1000000)
                ret += millionPart
                num %= 1000000
                if len(millionPart) > 0:
                    ret.append("Million")
            elif (num >= 1000):
                thousandPart = self.numberToWordsLess1000(num // 1000)
                ret += thousandPart
                num %= 1000
                if len(thousandPart) > 0:
                    ret.append("Thousand")
            else:
                ret += self.numberToWordsLess1000(num)
                num = 0
        return " ".join(ret)

    def numberToWordsLess1000(self, num):
        if num in self.numDict:
            return [self.numDict[num]]
        elif num >= 100:
            return [self.numDict[num // 100], "Hundred"] + self.numberToWordsLess1000(num % 100)
        elif num > 0:
            return [self.numDict[num - num % 10], self.numDict[num % 10]]
        else:
            return []
