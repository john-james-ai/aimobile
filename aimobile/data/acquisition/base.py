#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : AI-Enabled Voice of the Mobile Technology Customer                                  #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.11                                                                             #
# Filename   : /aimobile/data/acquisition/base.py                                                  #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/aimobile                                           #
# ------------------------------------------------------------------------------------------------ #
# Created    : Sunday April 30th 2023 06:49:10 pm                                                  #
# Modified   : Thursday June 1st 2023 01:57:33 pm                                                  #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
from __future__ import annotations
import os
from dotenv import load_dotenv
from abc import ABC, abstractmethod
from dataclasses import dataclass


# ------------------------------------------------------------------------------------------------ #
class Controller(ABC):
    """Defines the Abstract Base Class for Controller subclasses

    Controllers are responsible for the data acquisition process, taking a list of terms
    or categories to process, they orchestrate the data acquisition through scraper objects,
    and directly manage persistence of the results, as well as Project and Task objects.
    """

    @abstractmethod
    def scrape(self, *args, **kwargs) -> None:
        """Entry point for scraping operations."""
        load_dotenv()
        return os.getenv(self.__class__.__name__, False) in (True, "true", "True")


# ------------------------------------------------------------------------------------------------ #
@dataclass
class Result:
    scraper: type[Scraper]  # The class type of the Scraper


# ------------------------------------------------------------------------------------------------ #
class Scraper(ABC):
    """Defines the Scraper interface for app scraper objects returning app data in batch pages"""

    @abstractmethod
    def __iter__(self) -> Scraper:
        """Returns a RequestGenerator object"""

    @abstractmethod
    def __next__(self) -> Result:
        """Generates the next Request object and returns a Result object."""
