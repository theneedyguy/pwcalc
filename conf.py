#!/usr/bin/env python
import json
import os


def getConfigValue(key):
    config = None
    configPath = "config.json"
    if "PWCALC_CONFIG" in os.environ:
        configPath = os.environ["PWCALC_CONFIG"]
    with open(configPath, "r") as f:
        config = json.load(f)
        f.close()
    try:
        return config[key]
    except:
        return "Error"

