if __name__ == "__main__":
    import logging

    import uvicorn

    uvicorn.run(
        app="server.app:app",
        host="0.0.0.0",
        port=8715,
        reload=True,
        debug=True,
        log_level=logging.DEBUG,
    )
