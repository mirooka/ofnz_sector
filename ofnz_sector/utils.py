import os
import sys


def is_production():
    return os.getenv('APP_ENVIRONMENT') == 'Production'


def is_test():
    return len(sys.argv) > 1 and sys.argv[1] == 'test'
