from types import SimpleNamespace

__all__ = ['config']


class _Config:
    def __init__(self):
        self.test_size = .33
        self.target = 'trip_duration'

        self.features = SimpleNamespace(
            hours_bins=4,
        )


config = _Config()
