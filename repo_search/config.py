import os


class BaseConfig:
    """Base configuration"""

    TESTING = False
    STATIC_VERSION = os.getenv("STATIC_VERSION", 12345)
    JSON_SORT_KEYS = False
    BASE_URL = ""
    PER_PAGE = 10
    ACCEPTED_PROVIDERS = ["gitlab"]


class LocalConfig(BaseConfig):
    """Development configuration"""

    Testing = False
