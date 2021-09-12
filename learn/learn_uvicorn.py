"""
参考文档：
https://www.uvicorn.org/
https://github.com/encode/uvicorn
https://github.com/MagicStack/uvloop
https://github.com/MagicStack/httptools
https://asgi.readthedocs.io/en/latest/index.html
"""

import uvicorn


async def app(scope, receive, send):
    print(scope)
    print(receive)
    print(send)


if __name__ == "__main__":
    uvicorn.run(
        "test_uvicorn:app",
        host="127.0.0.1",
        port=5000,
        log_level="info",
        reload=True,
        debug=True,
    )
