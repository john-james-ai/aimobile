#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : AI-Enabled Voice of the Mobile Technology Customer                                  #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.10                                                                             #
# Filename   : /aimobile/scraper/appstore/service/reviews.py                                       #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/aimobile                                           #
# ------------------------------------------------------------------------------------------------ #
# Created    : Saturday April 8th 2023 02:44:42 pm                                                 #
# Modified   : Monday April 10th 2023 06:38:10 am                                                  #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
"""AppStore Reviews Scraper Module"""
import logging
from datetime import datetime

from dependency_injector.wiring import Provide, inject

from aimobile.scraper.appstore.entity.project import AppStoreProject
from aimobile.scraper.appstore.repo.datacentre import DataCentre
from aimobile.scraper.appstore.http.reviews import AppStoreReviewRequest
from aimobile.scraper.base import AbstractAppDataScraper
from aimobile.scraper.appstore.container import AppStoreContainer
from aimobile.scraper.appstore.http.base import Handler


# ------------------------------------------------------------------------------------------------ #
class AppStoreReviewScraper(AbstractAppDataScraper):
    """App Store Reviews Scraper

    This class implements methods to retrieve information about iTunes App
    Store apps in various ways. Much has been adapted from the itunes-app-scraper,
    which can be found at  https://github.com/digitalmethodsinitiative/itunes-app-scraper

    Args:
        request (type[AppStoreReviewRequest]): A request object that specifies the request
            parameters and defines the process for parsing the request response.
        session_handler (Handler): Handles the session that performs the request, managing
            retries as defined in the session handler object.
        datacentre (AppStoreDataCentre): Manages the project, request and app data
            repositories under single database context.
    """

    @inject
    def __init__(
        self,
        request: type[AppStoreReviewRequest] = AppStoreReviewRequest,
        session_handler: Handler = Provide[AppStoreContainer.session.handler],
        datacentre: DataCentre = Provide[AppStoreContainer.datacentre.repo],
    ) -> None:
        self._request = request
        self._session_handler = session_handler
        self._datacentre = datacentre
        self._project = None

        self._logger = logging.getLogger(f"{self.__module__}.{self.__class__.__name__}")

    @property
    def project(self) -> AppStoreProject:
        return self._project

    def search(
        self, id: int, page: int, after: datetime, max_pages: int = None, limit: int = None
    ) -> None:
        """Executes a search of app data, and persists the results in the appstore appdate repository.

        Args:
            id (int): An appstore app id.
            max_pages (int): The maximum number of pages to return
            limit (int): The maximum number of results to return per page.

        """
        # Initialize the project.
        self._setup(id)

        # Iterate over our requests iterator
        for request in self._request(
            term=id,
            page=page,
            after=after,
            max_pages=max_pages,
            handler=self._session_handler,
        ):
            self._persist(request)

        # Close the project
        self._teardown()

    def _setup(self, id: int = None) -> None:
        """Some initialization"""
        self._project = AppStoreProject(name=id)
        self._project.start()
        self._datacentre.project_repository.add(project=self._project)

    def _persist(self, request: AppStoreReviewRequest) -> None:
        """Saves the app and project data to the database."""
        # Save review data
        self._datacentre.review_repository.add(data=request.result)

        # Update project and persist
        self._project.update(num_results=request.results, content_length=request.content_length)
        self._datacentre.project_repository.update(project=self._project)

        # Save request object
        self._datacentre.request_repository.add(request.request)
        self._datacentre.save()

    def _teardown(self) -> None:
        """Some final bookeeping."""
        self._project.end()
        # Set the status to success, unless an exception has occurred and
        # post the project to the database and release the resources.
        self._datacentre.project_repository.update(self._project)

    def summarize(self) -> None:
        """Prints a summary of the appdata scraping project."""
        print(self._project)
