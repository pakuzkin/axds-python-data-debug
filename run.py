def run():
    headers = [
        "time",
        "humidity",
        "salinity",
        "air_temperature",
        "water_temperature",
        "wind_speed"
    ]
    df = pd.read_csv('data.csv', header=None, names=headers)
    return {
        'humidity': df["humidity"].mean(),
        'salinity': df["salinity"].mean(),
        'air_temperature': df["air_temperature"].mean(),
        'water_temperature': df["water_temperature"].mean(),
        'wind_speed': df["wind_speed"].mean(),
    }


if __name__ == '__main__':
    import sys
    import time
    import math
    import pandas as pd

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
        'humidity': CORRECT_HUMIDITY,
        'salinity': CORRECT_SALINITY,
        'air_temperature': CORRECT_AIR_TEMPERATURE,
        'water_temperature':CORRECT_WIND_TEMPERATURE,
        'wind_speed': CORRECT_WIND_SPEED,
    }

    for column, value in ANSWERS.items():
        assert math.isclose(
            averages[column],
            value,
            rel_tol=1e-5,
        ), f"{column} should be {value}, instead {averages[column]}"

    print("Succesfully validated the data using {} in {} seconds".format(__file__, end - start))

    sys.exit(0)
