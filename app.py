#!/usr/bin/python3
# coding: utf-8


from fastapi import FastAPI, staticfiles

from controller.match import router_match
from controller.matches import router_matches


app = FastAPI(
    title='Analytics Virtual Soccer',
    version='1.0.0',
    openapi_tags=[
        {
            'name': 'analytics_virtual_soccer',
            'description': ''
        }
    ]
)

app.mount("/src", staticfiles.StaticFiles(directory="./templates/src"), name="source")

app.include_router(
    router_match, prefix="/match", tags=['match']
)

app.include_router(
    router_matches, prefix="/matches", tags=['matches']
)
