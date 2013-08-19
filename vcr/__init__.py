# Import Cassette to make it available at the top level
from .cassette import Cassette

# Also, make a 'load' function available
def use_cassette(path, **kwargs):
    return Cassette.load(path, **kwargs)
