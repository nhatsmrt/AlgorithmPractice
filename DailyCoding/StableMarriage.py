#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import defaultdict


def stable_marry(guy_preferences, gal_preferences):
    candidates = defaultdict(int)
    forward_map = {}
    backward_map = {}

    female_ranking = {}
    for women in gal_preferences:
        female_ranking[women] = {}
        for i, man in enumerate(gal_preferences[women]):
            female_ranking[women][man] = i
    unmarried_men = [guy for guy in guy_preferences]

    while unmarried_men:
        to_marry = unmarried_men.pop()

        while True:
            candidate = guy_preferences[to_marry][candidates[to_marry]]
            candidates[to_marry] += 1
            if candidate not in backward_map:
                backward_map[candidate] = to_marry
                forward_map[to_marry] = candidate
                break
            elif female_ranking[candidate][backward_map[candidate]] \
                > female_ranking[candidate][to_marry]:
                divorced = backward_map[candidate]
                backward_map[candidate] = to_marry
                unmarried_men.append(divorced)
                forward_map[to_marry] = candidate
                break


    return forward_map

guy_preferences = {'andrew': ['caroline', 'abigail', 'betty'],
                   'bill': ['caroline', 'betty', 'abigail'],
                   'chester': ['betty', 'caroline', 'abigail']}

gal_preferences = {'abigail': ['andrew', 'bill', 'chester'],
                   'betty': ['bill', 'andrew', 'chester'],
                   'caroline': ['bill', 'chester', 'andrew']}

# print(stable_marry(guy_preferences, gal_preferences))
