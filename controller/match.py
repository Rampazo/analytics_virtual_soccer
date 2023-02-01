#!/usr/bin/python3
# coding: utf-8

import collections

from fastapi import APIRouter, HTTPException, Request, status, templating
from datetime import date

from domain.domain import Cup, Match, create_match_by_list
from service.service import get_matches


router_match = APIRouter()

templates = templating.Jinja2Templates(directory="templates")


@router_match.get('/')
async def get_match(cup: Cup = None, match_date: date = None):
    res = get_matches(cup, match_date)
    return create_match_by_list(res)


@router_match.get("/matches", status_code=status.HTTP_200_OK)
async def get_matches_list(request: Request):
    try:
        res = get_matches()
        matches = create_match_by_list(res)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    return templates.TemplateResponse(
        "matches.html",
        {'request': request, 'matches': matches}
    )
