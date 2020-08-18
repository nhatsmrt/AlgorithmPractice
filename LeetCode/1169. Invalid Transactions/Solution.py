class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)

        processed_transactions = sorted(list(
            map(
                lambda trans: [trans[0], int(trans[1]), int(trans[2]), trans[3]],
                map(lambda trans: trans.split(","), transactions)
            )
        ), key=lambda trans: trans[1])

        # group by name:
        transactions_by_name = {}
        for transaction in processed_transactions:
            if transaction[0] not in transactions_by_name:
                transactions_by_name[transaction[0]] = []

            transactions_by_name[transaction[0]].append(transaction)

        ret = []
        for name, transactions in transactions_by_name.items():
            ret.extend(self.check_invalid_by_person(transactions))

        return ret

    def check_invalid_by_person(self, transactions: list) -> List[str]:
        ret = []
        added = set()

        cities_cnt = {transactions[0][-1]: 1}
        start = 0 # inclusive
        end = 0 # inclusive

        for i in range(len(transactions)):
            if transactions[i][2] > 1000:
                added.add(i)
                ret.append(self.list_to_trans_str(transactions[i]))

            while start < i and abs(transactions[i][1] - transactions[start][1]) > 60:
                cities_cnt[transactions[start][-1]] -= 1

                if not cities_cnt[transactions[start][-1]]:
                    cities_cnt.pop(transactions[start][-1])
                start += 1

            while end + 1 < len(transactions) and abs(transactions[end + 1][1] - transactions[i][1] <= 60):
                end += 1
                cities_cnt[transactions[end][-1]] = cities_cnt.get(transactions[end][-1], 0) + 1

            if i not in added and len(cities_cnt) >= 2:
                added.add(i)
                ret.append(self.list_to_trans_str(transactions[i]))

        return ret

    def list_to_trans_str(self, transaction: list) -> str:
        return ",".join([transaction[0], str(transaction[1]), str(transaction[2]), transaction[3]])
