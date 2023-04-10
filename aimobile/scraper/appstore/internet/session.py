#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : AI-Enabled Voice of the Mobile Technology Customer                                  #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.10                                                                             #
# Filename   : /aimobile/scraper/appstore/internet/session.py                                      #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : https://github.com/john-james-ai/aimobile                                           #
# ------------------------------------------------------------------------------------------------ #
# Created    : Saturday April 8th 2023 03:15:52 am                                                 #
# Modified   : Sunday April 9th 2023 09:54:48 pm                                                   #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
import os
from types import SimpleNamespace
from datetime import datetime
import random
import time
import logging
from dotenv import load_dotenv
import requests
from urllib3.util import Retry

from aimobile.scraper.appstore.internet.adapter import TimeoutHTTPAdapter
from aimobile.scraper.appstore.internet.base import SERVERS, HEADERS, Handler


# ------------------------------------------------------------------------------------------------ #
class SessionHandler(Handler):
    """Handles HTTP Requests

    Args:
        config (SimpleNamespace): Contains the configuration for the request handler
    """

    def __init__(self, config: SimpleNamespace) -> None:
        self._config = config
        self._timeout = None
        self._url = None
        self._headers = None
        self._proxies = None
        self._content_length = 0
        self._sessions = 0
        self._response = None
        self._rotate_headers = True
        self._status_code = None
        self.configure()
        self._logger = logging.getLogger(f"{self.__module__}.{self.__class__.__name__}")

    @property
    def url(self) -> str:
        """Returns the url sent with the last request."""
        return self._url

    @property
    def headers(self) -> dict:
        """Returns the headers that were sent with the last request"""
        return self._headers

    @property
    def status_code(self) -> dict:
        """Returns status_code from the last request."""
        return self._status_code

    @property
    def proxy(self) -> dict:
        """Returns the proxy server"""
        return self._proxies.get("http")

    @property
    def sessions(self) -> dict:
        """Returns the number of sessions used during the last request."""
        return self._sessions + 1

    @property
    def content_length(self) -> int:
        """Size of content returned."""
        return self._content_length

    @property
    def requested(self) -> datetime:
        """Returns datetime request was made"""
        return self._requested

    @property
    def responded(self) -> datetime:
        """Returns datetime response was received"""
        return self._responded

    @property
    def response_time(self) -> dict:
        """Returns the response time in milliseconds."""
        return self._response_time

    @property
    def response(self) -> requests.Response:
        """Returns the response"""
        return self._response

    def configure(self) -> None:
        """Configures the timeout adapter with retries."""
        retry = Retry(
            total=self._config["retry"]["total_retries"],
            backoff_factor=self._config["retry"]["backoff_factor"],
            status_forcelist=self._config["retry"]["status_forcelist"],
            allowed_methods=self._config["retry"]["allowed_methods"],
            raise_on_redirect=self._config["retry"]["raise_on_redirect"],
            raise_on_status=self._config["retry"]["raise_on_status"],
        )
        self._timeout = TimeoutHTTPAdapter(
            timeout=self._config["time"]["timeout"], max_retries=retry
        )

    def get(self, url: str, headers: dict = None, params: dict = None) -> requests.Response:
        """Executes the http request and returns a Response object.

        Args:
            url (str): The base url for the http request
            params (dict): The parameters to be added to the url
            headers (dict): Dictionary containing the HTTP header. Optional. If not provided,
                the headers will be rotated.
        """
        self._sessions = 0
        self._headers = headers
        self._rotate_headers = True if headers is None or len(headers) == 0 else False
        self._requested = None
        self._params = params
        self._url = url
        while self._sessions < self._config["retry"]["sessions"]:
            session = requests.Session()
            session.mount("https://", self._timeout)
            session.mount("http://", self._timeout)

            try:
                self._wait()
                self._pre_request()
                self._response = session.get(
                    url=self._url, headers=self._headers, params=self._params, proxies=self._proxies
                )
                self._post_request()
                return self

            except requests.exceptions.Timeout as e:  # pragma: no cover
                self._sessions += 1
                msg = f"A {type(e)} exception occurred after {self._config['retry']['total_retries']} retries. Retrying with new session #{self._sessions}."
                self._logger.error(msg)
            except requests.exceptions.TooManyRedirects as e:  # pragma: no cover
                self._sessions += 1
                msg = f"A {type(e)} exception occurred. Likely a problem with the url: {url}. Aborting request."
                self._logger.error(msg)
                break
            except requests.exceptions.ConnectionError as e:  # pragma: no cover
                self._sessions += 1
                msg = f"A {type(e)} exception occurred after {self._config['retry']['total_retries']} retries. Retrying with new session #{self._sessions}."
                self._logger.error(msg)
            except requests.exceptions.JSONDecodeError as e:  # pragma: no cover
                self._sessions += 1
                msg = f"A {type(e)} exception occurred after {self._config['retry']['total_retries']} retries. Unable to decode response. Aborting request"
                self._logger.error(msg)
                break
            except requests.exceptions.InvalidURL as e:  # pragma: no cover
                self._sessions += 1
                msg = f"A {type(e)} exception occurred. Likely a problem with the url: {url}. Aborting request."
                self._logger.error(msg)
                break
            except requests.exceptions.InvalidHeader as e:  # pragma: no cover
                self._sessions += 1
                msg = f"A {type(e)} exception occurred. Check headers.\n{headers}. Retrying with new session #{self._sessions}."
                self._logger.error(msg)
            except requests.exceptions.RetryError as e:  # pragma: no cover
                self._sessions += 1
                msg = f"A {type(e)} exception occurred after {self._config['retry']['total_retries']} retries. Retrying with new session #{self._sessions}."
                self._logger.error(msg)

        self._logger.error(
            "All retry and session limits have been reached. Exiting."
        )  # pragma: no cover

    def _wait(self) -> None:
        """Waits a random number of seconds between delay min and delay max."""
        sleep = random.randint(self._config["time"]["delay_min"], self._config["time"]["delay_max"])
        time.sleep(sleep)

    def _pre_request(self, headers: dict = None) -> None:
        """Conducts pre-request initializations"""
        if self._rotate_headers is True:
            self._headers = self._get_headers()
        self._proxies = self._get_proxy()
        self._response = None
        self._responded = None
        self._response_time = None
        self._content_length = 0
        self._requested = datetime.now() if self._requested is None else self._requested

    def _post_request(self) -> None:
        """Conducts post-request housekeeping"""
        self._status_code = int(self._response.status_code)
        self._responded = datetime.now()
        self._response_time = (self._responded - self._requested).total_seconds()
        try:
            self._content_length = int(self._response.headers["Content-Length"])
        except KeyError:  # pragma: no cover
            self._content_length = int(self._response.headers["content-length"])
        self._logger.debug(
            f"\nRequest status code: {self._response.status_code}. Session: {self._sessions}"
        )

    def _get_headers(self) -> dict:
        """Returns a randomly selected header from available HEADERS"""
        return random.choice(HEADERS)

    def _get_proxy(self) -> dict:
        """Returns proxy servers"""
        load_dotenv()
        username = os.getenv("GEONODE_USERNAME")
        password = os.getenv("GEONODE_PWD")
        while True:
            dns = random.choice(SERVERS)
            proxy = {"http": f"http://{username}:{password}@{dns}"}
            if proxy != self._proxies:
                break
        return proxy
