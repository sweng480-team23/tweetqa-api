from datetime import datetime


def read():
    return {
        "model_name": "First Model",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
