#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from src.utilities.logging import get_logger
from datetime import datetime

logger = get_logger(__name__)

def get_today_date():
    today = datetime.now().date()
    return today

def pprint(d):
    print(json.dumps(d, indent=4))
