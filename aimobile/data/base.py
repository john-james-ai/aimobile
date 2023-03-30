#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : AI-Enabled Voice of the Mobile Technology Customer                                  #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.10                                                                             #
# Filename   : /aimobile/data/base.py                                                              #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/aimobile                                           #
# ------------------------------------------------------------------------------------------------ #
# Created    : Wednesday March 29th 2023 05:57:04 pm                                               #
# Modified   : Wednesday March 29th 2023 06:34:09 pm                                               #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
from abc import ABC, abstractmethod

URLFORMAT = "https://itunes.apple.com/search?media=software&term=Health&country=us&lang=en-us&explicit=yes&limit=200&offset=0"


# ------------------------------------------------------------------------------------------------ #
class Scraper(ABC):
    """Abstract base class for all scrapers"""

    @property
    @abstractmethod
    def data(self) -> dict:
        """Returns the current data dictionary"""

    @abstractmethod
    def scrape(self, category: str, page: int = None, directory: str = None) -> None:
        """Scrapes data for the category and optionally, a page, and saves it in the designated directory.

        The filename is of the format <category_page_num>.py.

        Args:
            category (str): Single word search term for the category of interest.
            page (int): The page to scrape. Optional. Default [0:max_pages].
            directory (str): Optional. Defaults to the directory designated in the constructor.

        """

    @abstractmethod
    def load(self, category: str, page: int = 0, directory: str = None) -> None:
        """Loads app data for the designated category and page into the data attribute.

        Args:
            category (str): Single word search term for the category of interest.
            page (int): The page number for the category results
            directory (str): The directory into which the file shall be saved. Optional.
                Defaults to the directory established in the constructor.
        """

    @abstractmethod
    def save(self, data: dict, category: str, page: int, directory: str = None) -> None:
        """Saves the app data to file.

        Args:
            data (dict): Dictionary containing the app data.
            category (str): The category of the data
            page (int): The page number of the results
            directory (str): The directory into which the file shall be saved. Optional.
                Defaults to the directory established at object construction.

        """

    @abstractmethod
    def summary(self) -> None:
        """Prints a summary of app scrapes."""
