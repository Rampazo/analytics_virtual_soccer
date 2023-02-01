#!/usr/bin/python3
# coding: utf-8

from datetime import date, datetime, timedelta
from enum import Enum
from pydantic import BaseModel, Field, validator
from typing import Optional


TRUE = "●"
FALSE = "○"
HOME = "●"
AWAY = "○"
DRAW = "x"


class Cup(str, Enum):
    euro_cup = "Euro Cup"
    world_cup = "World Cup"
    premiership = "Premiership"
    super_league = "Superleague"


class Match(BaseModel):
    id: str
    code: str
    cup: str
    match_time: str
    match_datetime: datetime
    result_ft: str
    result_ht: str
    goals_home_team_ft: int
    goals_visitor_team_ft: int
    goals_home_team_ht: int
    goals_visitor_team_ht: int
    created_at: datetime

    total_goals_ft: Optional[int]
    under_0_5_ft: Optional[str]
    under_1_5_ft: Optional[str]
    under_2_5_ft: Optional[str]
    under_3_5_ft: Optional[str]
    over_0_5_ft: Optional[str]
    over_1_5_ft: Optional[str]
    over_2_5_ft: Optional[str]
    over_3_5_ft: Optional[str]
    over_4_5_ft: Optional[str]
    over_5_5_ft: Optional[str]
    both_score_ft: Optional[str]
    winner_ft: Optional[str]

    total_goals_ht: Optional[int]
    under_0_5_ht: Optional[str]
    under_1_5_ht: Optional[str]
    under_2_5_ht: Optional[str]
    under_3_5_ht: Optional[str]
    over_0_5_ht: Optional[str]
    over_1_5_ht: Optional[str]
    over_2_5_ht: Optional[str]
    over_3_5_ht: Optional[str]
    both_score_ht: Optional[str]
    winner_ht: Optional[str]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total_goals_ft = self.goals_home_team_ft + self.goals_visitor_team_ft
        self.total_goals_ht = self.goals_home_team_ht + self.goals_visitor_team_ht

        self.under_0_5_ft = self.check_under(0.5, 'ft')
        self.under_1_5_ft = self.check_under(1.5, 'ft')
        self.under_2_5_ft = self.check_under(2.5, 'ft')
        self.under_3_5_ft = self.check_under(3.5, 'ft')
        self.over_0_5_ft = self.check_over(0.5, 'ft')
        self.over_1_5_ft = self.check_over(1.5, 'ft')
        self.over_2_5_ft = self.check_over(2.5, 'ft')
        self.over_3_5_ft = self.check_over(3.5, 'ft')
        self.over_4_5_ft = self.check_over(4.5, 'ft')
        self.over_5_5_ft = self.check_over(5.5, 'ft')
        self.both_score_ft = self.check_both_score('ft')
        self.winner_ft = self.check_winner('ft')

        self.under_0_5_ht = self.check_under(0.5, 'ht')
        self.under_1_5_ht = self.check_under(1.5, 'ht')
        self.under_2_5_ht = self.check_under(2.5, 'ht')
        self.under_3_5_ht = self.check_under(3.5, 'ht')
        self.over_0_5_ht = self.check_over(0.5, 'ht')
        self.over_1_5_ht = self.check_over(1.5, 'ht')
        self.over_2_5_ht = self.check_over(2.5, 'ht')
        self.over_3_5_ht = self.check_over(3.5, 'ht')
        self.both_score_ht = self.check_both_score('ht')
        self.winner_ht = self.check_winner('ht')

    def check_under(self, value, part):
        total_goals = self.total_goals_ht if part == 'ht' else self.total_goals_ft
        return TRUE if total_goals < value else FALSE

    def check_over(self, value, part):
        total_goals = self.total_goals_ht if part == 'ht' else self.total_goals_ft
        return TRUE if total_goals > value else FALSE

    def check_both_score(self, part):
        if part == 'ht':
            goals_home_team = self.goals_home_team_ht
            goals_visitor_team = self.goals_visitor_team_ht
        else:
            goals_home_team = self.goals_home_team_ft
            goals_visitor_team = self.goals_visitor_team_ft
        return TRUE if goals_home_team and goals_visitor_team else FALSE

    def check_winner(self, part):
        if part == 'ht':
            goals_home_team = self.goals_home_team_ht
            goals_visitor_team = self.goals_visitor_team_ht
        else:
            goals_home_team = self.goals_home_team_ft
            goals_visitor_team = self.goals_visitor_team_ft

        if goals_home_team > goals_visitor_team:
            return HOME
        elif goals_home_team < goals_visitor_team:
            return AWAY
        else:
            return DRAW


def create_match_by_list(list_data):
    list_matches = []

    for match in list_data:
        list_matches.append(Match(
            id=match[0],
            code=match[1],
            cup=match[2],
            match_time=match[3],
            match_datetime=match[4],
            result_ft=match[5],
            result_ht=match[6],
            goals_home_team_ft=match[7],
            goals_visitor_team_ft=match[8],
            goals_home_team_ht=match[9],
            goals_visitor_team_ht=match[10],
            created_at=match[11]
            )
        )
    return list_matches
