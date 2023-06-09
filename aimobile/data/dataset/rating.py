#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : AI-Enabled Voice of the Mobile Technology Customer                                  #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.11                                                                             #
# Filename   : /aimobile/data/dataset/rating.py                                                    #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/aimobile                                           #
# ------------------------------------------------------------------------------------------------ #
# Created    : Sunday May 21st 2023 03:53:33 am                                                    #
# Modified   : Saturday June 24th 2023 01:49:35 am                                                 #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
from functools import cached_property

from dependency_injector.wiring import Provide, inject
import pandas as pd

from aimobile.data.repo.base import Repo
from aimobile.data.dataset.base import Dataset
from aimobile.container import AIMobileContainer

# ------------------------------------------------------------------------------------------------ #
DTYPES = [
    "Nominal",
    "Nominal",
    "Categorical",
    "Categorical",
    "Interval",
    "Discrete",
    "Discrete",
    "Discrete",
    "Discrete",
    "Discrete",
    "Discrete",
    "Discrete",
]


# ------------------------------------------------------------------------------------------------ #
class RatingDataset(Dataset):
    """An in-memory dataset containing app data

    Args:
        repo (Repo): The dataset repository
    """

    @inject
    def __init__(self, repo: Repo = Provide[AIMobileContainer.data.rating_repo]) -> None:
        super().__init__(repo=repo)

    @cached_property
    def structure(self) -> pd.DataFrame:
        """Describes dataset structure, in terms of shape, size, and data type."""
        return super().structure

    @cached_property
    def dtypes(self) -> pd.DataFrame:
        """Summarizes the data types in the dataset."""

        d = {
            "Number of Nominal Data Types": 2,
            "Number of Categorical Data Types": 2,
            "Number of Discrete Data Types": 7,
            "Number of Interval Data Types": 1,
        }
        dtypes = pd.DataFrame.from_dict(data=d, orient="index").reset_index()
        dtypes.columns = ["Data Type", "Number of Features"]
        return dtypes

    @cached_property
    def quality(self) -> pd.DataFrame:
        """Provides statistical information at the variable level."""
        quality = self._df.dtypes.to_frame().reset_index()
        quality.columns = ["Column", "Format"]
        quality["Data Type"] = DTYPES
        quality["Valid"] = self._df.count().values
        quality["Null"] = self._df.isna().sum().values
        quality["Validity"] = quality["Valid"] / self._df.shape[0]
        quality["Cardinality"] = self._df.nunique().values
        quality["Percent Unique"] = self._df.nunique().values / self._df.shape[0]
        quality["Size"] = self._df.memory_usage(deep=True, index=False).to_frame().reset_index()[0]
        quality = round(quality, 2)
        return quality

    @cached_property
    def summary(self) -> None:
        """Summarizes the data"""

        summary = self._df["category"].value_counts().reset_index()
        summary.columns = ["category", "Examples"]
        df2 = self._df.groupby(by="category")["id"].nunique().to_frame()
        df3 = self._df.groupby(by="category")["rating"].mean().to_frame()
        df4 = self._df.groupby(by="category")["ratings"].sum().to_frame()
        df5 = self._df.groupby(by="category")["reviews"].sum().to_frame()

        summary = summary.join(df2, on="category")
        summary = summary.join(df3, on="category")
        summary = summary.join(df4, on="category")
        summary = summary.join(df5, on="category")
        summary.columns = [
            "Category",
            "Examples",
            "Apps",
            "Average Rating",
            "Rating Count",
            "Review Count",
        ]
        return summary
