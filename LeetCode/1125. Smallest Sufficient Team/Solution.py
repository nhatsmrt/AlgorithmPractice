class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # Let dp: 2^skills -> 2^ppl. dp(skill_set) the minimum set of people that master
        # the skil set

        # For a skill set, iterate through the list of people
        # For each such person, we can find the skills in the skil set
        # not mastered by that person. Find the smallest sufficient team for those skills
        # then combine the team and that person to form a (candidate) sufficient team
        # for the current skill set

        # Time Complexity: O(people * 2^skills)
        # Space Complexity O(2^skills + people)

        skills_index = {}
        for i in range(len(req_skills)):
            skills_index[req_skills[i]] = i

        people_skills = []
        for i in range(len(people)):
            skill_masks = 0
            for skill in people[i]:
                skill_masks |= 1 << (skills_index[skill])
            people_skills.append(skill_masks)

        dp = {}
        min_len = {}

        dp[0] = 0
        min_len[0] = 0

        for skill_masks in range(1, 1 << len(req_skills)):
            for i in range(len(people)):
                other_skills = skill_masks & (~people_skills[i])

                if other_skills < skill_masks:
                    candidate_mask = dp[other_skills] | (1 << i)
                    candidate_len = min_len[other_skills] + 1

                    if skill_masks not in dp or candidate_len < min_len[skill_masks]:
                        dp[skill_masks] = candidate_mask
                        min_len[skill_masks] = candidate_len

        ret = []
        for i in range(len(people)):
            if ((1 << i) & dp[(1 << len(req_skills)) - 1]) > 0:
                ret.append(i)

        return ret
                    
