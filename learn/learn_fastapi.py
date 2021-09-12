"""
参考文档：
https://fastapi.tiangolo.com/
"""

from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    import logging
    import os
    import sys

    import uvicorn

    sys.path.append(os.getcwd())

    uvicorn.run(
        app="learn.learn_fastapi:app",
        host="0.0.0.0",
        port=8715,
        reload=True,
        debug=True,
        log_level=logging.DEBUG,
    )
