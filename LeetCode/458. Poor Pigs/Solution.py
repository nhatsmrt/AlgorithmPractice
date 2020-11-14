class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        num_tests = minutesToTest // minutesToDie

        # Given T test, each pig can have T + 1 possible states
        # (die in one of the T tests, or survive all)

        # If we have x pigs, then the number of possible states
        # is (T + 1)^x. We want to correspond each state
        # to only one case in testing the buckets
        # (i.e number of buckets <= (T + 1)^x)

        # We can think of each state as a vector of x dimension
        # each dimension can take (T + 1) values

        # Then these vectors form the vector space Z_{T + 1}^x
        # which has a basis of size x: the elementary basis

        # We can translate this basis to pigs testing based on its orthogonality as follows:
        # 1. Divide the (T + 1)^x buckets into (T + 1) group
        # One pig will test one group in each test
        # 2. For each of the (T + 1) groups, there are (T + 1)^{x - 1} buckets
        # Divide these buckets into (T + 1) subgroups, each with (T + 1)^{x - 2} buckets
        # Another pig will test all the first subgroups simultaenously in first test,
        # then second subgroups, etc.
        # At the end, if we arrive at the state (t_1, ..., t_x)
        # then we know that the bucket belong to group t_1, subgroup t_2, sub-subgroup t_3...
        # This will uniquely define the bucket.

        # In other word, each pig will need to check one "orthogonal dimension"
        # of the space of all buckets

        # if x = ceil(log_{T + 1}(N)), then (T + 1)^x >= N

        return math.ceil(log(buckets, num_tests + 1))
