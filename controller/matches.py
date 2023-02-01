#!/usr/bin/python3
# coding: utf-8

from fastapi import APIRouter, HTTPException, Request, status, templating
from datetime import date

from domain.domain import create_match_by_list
from service.service import get_matches

router_matches = APIRouter()

templates = templating.Jinja2Templates(directory="templates")

EUROCUP = 'Euro Cup'
PREMIERSHIP = 'Premiership'
SUPERLEAGUE = 'Superleague'
WORLDCUP = 'World Cup'


def get_matches_wp(cup=None, search_date=str(date.today())):
    res = get_matches(cup, search_date)
    return create_match_by_list(res)


@router_matches.get('/euro_cup')
async def euro_cup_matches(request: Request):
    try:
        matches = get_matches_wp(cup=EUROCUP)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    return templates.TemplateResponse(
        "matches.html",
        {'request': request, 'matches': matches}
    )


@router_matches.get('/premiership')
async def premiership_matches(request: Request):
    try:
        matches = get_matches_wp(cup=PREMIERSHIP)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    return templates.TemplateResponse(
        "matches.html",
        {'request': request, 'matches': matches}
    )


@router_matches.get('/super_league')
async def super_league_matches(request: Request):
    try:
        matches = get_matches_wp(cup=SUPERLEAGUE)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    return templates.TemplateResponse(
        "matches.html",
        {'request': request, 'matches': matches}
    )


@router_matches.get('/world_cup')
async def world_cup_matches(request: Request):
    try:
        matches = get_matches_wp(cup=WORLDCUP)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    return templates.TemplateResponse(
        "matches.html",
        {'request': request, 'matches': matches}
    )


@router_matches.get('/world_cup2')
async def world_cup2_matches(request: Request):
    try:
        matches = get_matches_wp(cup=WORLDCUP)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    return templates.TemplateResponse(
        "new_matches.html",
        {'request': request, 'matches': matches}
    )
