class TimeOutException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Websocket is time out."
