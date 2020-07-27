CREATE TABLE positions (
    position_id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitudeE7 INTEGER NOT NULL,
    altitude INTEGER NOT NULL,
    longitudeE7 INTEGER NOT NULL,
    timestampMs VARCHAR(15) NOT NULL,
    verticalAccuracy INTEGER NOT NULL,
    accuracy INTEGER NOT NULL
);