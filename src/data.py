import pandas as pd
from sklearn.model_selection import train_test_split as _train_test_split

from src.config import config
from src.directories import directories
from src.schemas import TaxiColumn, WeatherColumn

TRAIN_TAXI_DATA_FILENAME = 'train-2015.csv'
LIVE_TAXI_DATA_FILENAME = 'live-2015.csv'
WEATHER_DATA_FILENAME = 'nyc-weather-2015.csv'


def get_train_dataset():
    return _get_dataset(TRAIN_TAXI_DATA_FILENAME)


def get_live_dataset():
    return _get_dataset(LIVE_TAXI_DATA_FILENAME)


def _get_dataset(filename):
    return pd.read_csv(
        directories.taxi_data_dir / filename,
        parse_dates=[TaxiColumn.PICKUP_TIME, TaxiColumn.DROPOFF_TIME]
    )


def get_weather_data():
    return pd.read_csv(
        directories.weather_data_dir / WEATHER_DATA_FILENAME,
        parse_dates=[WeatherColumn.DATE]
    ).assign(**{WeatherColumn.DATE: lambda x: x[WeatherColumn.DATE].dt.date})


def train_test_split(data):
    return _train_test_split(
        data.sort_values(TaxiColumn.PICKUP_TIME),
        test_size=config.test_size,
        shuffle=False
    )


def get_target(data):
    """Target is the total duration of trip, in seconds"""
    target = (
        data[TaxiColumn.DROPOFF_TIME] - data[TaxiColumn.PICKUP_TIME]
    ).dt.seconds
    return target.rename(config.target)
