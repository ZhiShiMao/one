"""
参考文档：
https://toml.io/cn/v1.0.0
https://github.com/hukkin/tomli
"""

import toml
import json

config = {}
with open("pyproject.toml") as toml_file:
    config = toml.load(toml_file)
with open("temp.json", "w+") as json_file:
    json.dump(config, json_file)
