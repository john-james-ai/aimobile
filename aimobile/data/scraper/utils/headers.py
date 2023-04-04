#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# ================================================================================================ #
# Project    : Enter Project Name in Workspace Settings                                            #
# Version    : 0.1.0                                                                               #
# Python     : 3.10.8                                                                              #
# Filename   : /aimobile/data/scraper/utils/headers.py                                             #
# ------------------------------------------------------------------------------------------------ #
# Author     : John James                                                                          #
# Email      : john.james.ai.studio@gmail.com                                                      #
# URL        : Enter URL in Workspace Settings                                                     #
# ------------------------------------------------------------------------------------------------ #
# Created    : Tuesday April 4th 2023 03:01:18 pm                                                  #
# Modified   : Tuesday April 4th 2023 06:12:24 pm                                                  #
# ------------------------------------------------------------------------------------------------ #
# License    : MIT License                                                                         #
# Copyright  : (c) 2023 John James                                                                 #
# ================================================================================================ #
"""Module responsible for producing HTTP Headers."""

HEADERS {
    "authority": "www.apple.com",
    "method": "GET",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",  # Client Hints go next
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


USER_AGENTS = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0",
"Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0",
"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.5563.101 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (iPad; CPU OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/111.0.5563.101 Mobile/15E148 Safari/604.1",
"Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.116 Mobile Safari/537.36"

]

VPN_SERVERS = [
    "ch-us-01a.protonvpn.net",
    "ch-us-01b.protonvpn.net",
    "ch-us-01c.protonvpn.net",
    "ch-us-01d.protonvpn.net",
    "ch-us-01g.protonvpn.net",
    "ch-us-01h.protonvpn.net",
    "ch-us-01i.protonvpn.net",
    "ch-us-01j.protonvpn.net",
    "ch-us-01k.protonvpn.net",
    "ch-us-01n.protonvpn.net",
    "ch-us-01p.protonvpn.net",
    "ch-us-01v.protonvpn.net",
    "ch-us-01w.protonvpn.net",
    "ch-us-01x.protonvpn.net",
    "ch-us-01y.protonvpn.net",
    "ch-us-01z.protonvpn.net",
    "ch-us-02a.protonvpn.net",
    "ch-us-02b.protonvpn.net",
    "ch-us-02c.protonvpn.net",
    "ch-us-02d.protonvpn.net",
    "ch-us-02e.protonvpn.net",
    "ch-us-02f.protonvpn.net",
    "ch-us-02g.protonvpn.net",
    "ch-us-02h.protonvpn.net",
    "ch-us-02i.protonvpn.net",
    "ch-us-02j.protonvpn.net",
    "ch-us-02k.protonvpn.net",
    "is-us-01a.protonvpn.net",
    "is-us-01b.protonvpn.net",
    "is-us-01c.protonvpn.net",
    "is-us-01d.protonvpn.net",
    "is-us-01f.protonvpn.net",
    "is-us-01g.protonvpn.net",
    "is-us-01h.protonvpn.net",
    "is-us-01i.protonvpn.net",
    "is-us-01j.protonvpn.net",
    "is-us-01k.protonvpn.net",
    "is-us-01l.protonvpn.net",
    "is-us-01q.protonvpn.net",
    "is-us-01r.protonvpn.net",
    "is-us-01s.protonvpn.net",
    "se-us-01a.protonvpn.net",
    "se-us-01b.protonvpn.net",
    "se-us-01c.protonvpn.net",
    "se-us-01d.protonvpn.net",
    "se-us-01e.protonvpn.net",
    "se-us-01f.protonvpn.net",
    "se-us-01g.protonvpn.net",
    "se-us-01h.protonvpn.net",
    "se-us-01i.protonvpn.net",
    "se-us-01j.protonvpn.net",
    "se-us-01l.protonvpn.net",
    "se-us-01m.protonvpn.net",
    "se-us-01n.protonvpn.net",
    "node-us-41.protonvpn.net",
    "node-us-119.protonvpn.net",
    "node-us-121.protonvpn.net",
    "node-us-59.protonvpn.net",
    "node-us-69.protonvpn.net",
    "node-us-129.protonvpn.net",
    "node-us-130.protonvpn.net",
    "node-us-135.protonvpn.net",
    "node-us-57.protonvpn.net",
    "node-us-108.protonvpn.net",
    "node-us-109.protonvpn.net",
    "node-us-125.protonvpn.net",
    "node-us-93.protonvpn.net",
    "node-us-94.protonvpn.net",
    "node-us-58.protonvpn.net",
    "node-us-74.protonvpn.net",
    "node-us-48.protonvpn.net",
    "node-us-49.protonvpn.net",
    "node-us-65.protonvpn.net",
    "node-us-66.protonvpn.net",
    "node-us-82.protonvpn.net",
    "node-us-95.protonvpn.net",
    "node-us-96.protonvpn.net",
    "node-us-97.protonvpn.net",
    "node-us-98.protonvpn.net",
    "node-us-99.protonvpn.net",
    "node-us-122.protonvpn.net",
    "node-us-51.protonvpn.net",
    "node-us-63.protonvpn.net",
    "node-us-64.protonvpn.net",
    "node-us-90.protonvpn.net",
    "node-us-100.protonvpn.net",
    "node-us-50.protonvpn.net",
    "node-us-101.protonvpn.net",
    "node-us-102.protonvpn.net",
    "node-us-103.protonvpn.net",
    "node-us-134.protonvpn.net",
    "node-us-46.protonvpn.net",
    "node-us-67.protonvpn.net",
    "node-us-68.protonvpn.net",
    "node-us-77.protonvpn.net",
    "node-us-104.protonvpn.net",
    "node-us-105.protonvpn.net",
    "node-us-106.protonvpn.net",
    "node-us-107.protonvpn.net",
    "node-us-144.protonvpn.net",
    "node-us-118.protonvpn.net",
    "node-us-126.protonvpn.net",
    "node-us-110.protonvpn.net",
    "node-us-111.protonvpn.net",
    "node-us-112.protonvpn.net",
    "node-us-120.protonvpn.net",
    "node-us-123.protonvpn.net",
    "node-us-124.protonvpn.net",
    "node-us-127.protonvpn.net",
    "node-us-31.protonvpn.net",
    "us-co-21-tor.protonvpn.net",
    "us-ga-29-tor.protonvpn.net"]
