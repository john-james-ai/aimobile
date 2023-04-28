#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : AI-Enabled Voice of the Mobile Technology Customer                                  #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.10                                                                             #
# Filename   : /tests/conftest.py                                                                  #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/aimobile                                           #
# ------------------------------------------------------------------------------------------------ #
# Created    : Monday March 27th 2023 07:01:48 pm                                                  #
# Modified   : Thursday April 27th 2023 03:35:59 am                                                #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
import os
import pytest
import random
import dotenv
import subprocess

from aimobile.infrastructure.io.local import IOService
from aimobile.container import AIMobileContainer

# ------------------------------------------------------------------------------------------------ #
collect_ignore = [""]

# ================================================================================================ #
#                                FRAMEWORK TEST FIXTURES                                           #
# ================================================================================================ #

DATAFRAME_FILEPATH = "tests/data/test.csv"
APPDATA_FILEPATH = "tests/data/appdata.csv"
APPDATA_HEALTH_FILEPATH = "tests/data/appstore_health.csv"
REVIEWS_FILEPATH = "tests/data/reviews.csv"
RATINGS_FILEPATH = "tests/data/appstore_ratings.csv"
RESET_SCRIPT = "tests/scripts/reset.sh"
APP_IDS = ["297606951", "544007664", "951937596", "310633997", "422689480"]
APPS = [
    {"id": "297606951", "name": "amazon", "category_id": 6024, "category": "SHOPPING"},
    {"id": "544007664", "name": "youtube", "category_id": 6005, "category": "SOCIAL_NETWORKING"},
    {"id": "951937596", "name": "outlook", "category_id": 6000, "category": "BUSINESS"},
    {"id": "422689480", "name": "gmail", "category_id": 6002, "category": "UTILITIES"},
    {"id": "310633997", "name": "whatsapp", "category_id": 6002, "category": "UTILITIES"},
]

STOREFRONTS = [
    {"country": "us", "headers": {"X-Apple-Store-Front": "143441-1,29"}},
    {"country": "au", "headers": {"X-Apple-Store-Front": "143460,29"}},
    {"country": "ca", "headers": {"X-Apple-Store-Front": "143455-6,29"}},
    {"country": "gb", "headers": {"X-Apple-Store-Front": "143444,29"}},
]

collect_ignore = ["test_database*.*"]


# ------------------------------------------------------------------------------------------------ #
#                                      APP IDS                                                     #
# ------------------------------------------------------------------------------------------------ #
@pytest.fixture(scope="module", autouse=False)
def apps():
    return APPS


# ------------------------------------------------------------------------------------------------ #
#                                   RESET TEST DB                                                  #
# ------------------------------------------------------------------------------------------------ #
@pytest.fixture(scope="module", autouse=False)
def reset():
    subprocess.run(RESET_SCRIPT, shell=True)


# ------------------------------------------------------------------------------------------------ #
#                                  SET MODE TO TEST                                                #
# ------------------------------------------------------------------------------------------------ #
@pytest.fixture(scope="module", autouse=True)
def mode():
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    os.environ["MODE"] = "test"
    dotenv.set_key(dotenv_file, "MODE", os.environ["MODE"])


# ------------------------------------------------------------------------------------------------ #
#                              DEPENDENCY INJECTION                                                #
# ------------------------------------------------------------------------------------------------ #
@pytest.fixture(scope="module", autouse=True)
def container():
    container = AIMobileContainer()
    container.init_resources()
    container.wire(packages=["aimobile.service.appstore"])

    return container


# ------------------------------------------------------------------------------------------------ #
#                                 DATABASE FIXTURES                                                #
# ------------------------------------------------------------------------------------------------ #
@pytest.fixture(scope="module", autouse=False)
def dataframe():
    df = IOService.read(DATAFRAME_FILEPATH)
    return df


# ------------------------------------------------------------------------------------------------ #
#                                        APPDATA                                                   #
# ------------------------------------------------------------------------------------------------ #
@pytest.fixture(scope="module", autouse=False)
def appdata():
    df = IOService.read(APPDATA_HEALTH_FILEPATH)
    return df


# ------------------------------------------------------------------------------------------------ #
#                                      APPDATA REPO                                                #
# ------------------------------------------------------------------------------------------------ #
@pytest.fixture(scope="module", autouse=False)
def appstore_appdata_repo(container):
    repo = container.data.appdata_repo()
    repo.delete_all()
    repo.save()
    return repo


# ------------------------------------------------------------------------------------------------ #
#                                  APPSTORE RATINGS REPO                                           #
# ------------------------------------------------------------------------------------------------ #
@pytest.fixture(scope="module", autouse=False)
def appstore_rating_repo(container):
    repo = container.data.rating_repo()
    try:
        repo.delete_all()
    except Exception:
        pass
    df = IOService.read(RATINGS_FILEPATH)
    repo.add(data=df)
    return repo


# ------------------------------------------------------------------------------------------------ #
#                                        REVIEWS                                                   #
# ------------------------------------------------------------------------------------------------ #
@pytest.fixture(scope="module", autouse=False)
def review():
    df = IOService.read(REVIEWS_FILEPATH)
    return df


# ------------------------------------------------------------------------------------------------ #
#                                        RATINGS                                                   #
# ------------------------------------------------------------------------------------------------ #
@pytest.fixture(scope="module", autouse=False)
def rating():
    df = IOService.read(RATINGS_FILEPATH)
    return df


# ------------------------------------------------------------------------------------------------ #
#                                      WEB FIXTURES                                                #
# ------------------------------------------------------------------------------------------------ #
@pytest.fixture(scope="module", autouse=False)
def request_appdata():
    d = {
        "url": "https://itunes.apple.com/search",
        "params": {
            "media": "software",
            "term": "health",
            "country": "us",
            "lang": "en-us",
            "explicit": "yes",
            "limit": 5,
            "offset": 0,
        },
    }
    return d


@pytest.fixture(scope="function", autouse=False)
def request_ratings():
    # Note: Taking '/json' of the end of the url. Want actual response object returned.
    storefront = random.choice(STOREFRONTS)
    d = {
        "url": f"https://itunes.apple.com/{storefront['country']}/customer-reviews/id{random.choice(APP_IDS)}?displayable-kind=11",
        "headers": storefront["headers"],
    }
    return d
