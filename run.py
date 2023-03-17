import sys
import time
import math
import pandas as pd

# Weather meta data
FILE_PATH = 'data.csv'
# Headers
TIME = "time",
HUMIDITY = "humidity",
SALINITY = "salinity",
AIR_TEMP = "air_temperature",
WATER_TEMP = "water_temperature",
WIND_SPEED = "wind_speed"


def run():
    headers = [
        TIME,
        HUMIDITY,
        SALINITY,
        AIR_TEMP,
        WATER_TEMP,
        WIND_SPEED
    ]
    df = pd.read_csv(FILE_PATH, header=None, names=headers)
    return {
        HUMIDITY: df[HUMIDITY].mean(),
        SALINITY: df[SALINITY].mean(),
        AIR_TEMP: df[AIR_TEMP].mean(),
        WATER_TEMP: df[WATER_TEMP].mean(),
        WIND_SPEED: df[WIND_SPEED].mean(),
    }


if __name__ == '__main__':
    '''
    +---------+--------------------+
    | Library | Run time (seconds) |
    +---------+--------------------+
    | CSV     | 0.407449           |
    | Pandas  | 0.087758           |
    +---------+--------------------+
    '''
    start = time.perf_counter()
    averages = run()
    end = time.perf_counter()

    CORRECT_HUMIDITY = 80.8129
    CORRECT_SALINITY = 36.1433
    CORRECT_AIR_TEMPERATURE = 19.7976
    CORRECT_WIND_TEMPERATURE = 34.1683
    CORRECT_WIND_SPEED = 5.6777

    ANSWERS = {
        HUMIDITY: CORRECT_HUMIDITY,
        SALINITY: CORRECT_SALINITY,
        AIR_TEMP: CORRECT_AIR_TEMPERATURE,
        WATER_TEMP: CORRECT_WIND_TEMPERATURE,
        WIND_SPEED: CORRECT_WIND_SPEED,
    }

    for column, value in ANSWERS.items():
        assert math.isclose(
            averages[column],
            value,
            rel_tol=1e-5,
        ), f"{column} should be {value}, instead {averages[column]}"

    print("Successfully validated the data using {} in {} seconds".format(__file__, end - start))

    sys.exit(0)
