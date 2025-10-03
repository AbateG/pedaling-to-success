import pandas as pd
import os
from datetime import timedelta

# Directory paths
data_dir = 'data/csv_originals'
excel_dir = 'data/excel_copies'

# Column mappings for each quarter
column_maps = {
    'Divvy_Trips_2019_Q2.csv': {
        '01 - Rental Details Rental ID': 'ride_id',
        '01 - Rental Details Local Start Time': 'started_at',
        '01 - Rental Details Local End Time': 'ended_at',
        '03 - Rental Start Station Name': 'start_station_name',
        '02 - Rental End Station Name': 'end_station_name',
        'User Type': 'member_casual'
    },
    'Divvy_Trips_2019_Q3.csv': {
        'trip_id': 'ride_id',
        'start_time': 'started_at',
        'end_time': 'ended_at',
        'from_station_name': 'start_station_name',
        'to_station_name': 'end_station_name',
        'usertype': 'member_casual'
    },
    'Divvy_Trips_2019_Q4.csv': {
        'trip_id': 'ride_id',
        'start_time': 'started_at',
        'end_time': 'ended_at',
        'from_station_name': 'start_station_name',
        'to_station_name': 'end_station_name',
        'usertype': 'member_casual'
    },
    'Divvy_Trips_2020_Q1.csv': {
        'trip_id': 'ride_id',
        'start_time': 'started_at',
        'end_time': 'ended_at',
        'from_station_name': 'start_station_name',
        'to_station_name': 'end_station_name',
        'usertype': 'member_casual'
    }
}

# Load and process each file
dfs = []
for file, col_map in column_maps.items():
    path = os.path.join(data_dir, file)
    df = pd.read_csv(path)
    df = df.rename(columns=col_map)
    # Keep only relevant columns
    df = df[['ride_id', 'started_at', 'ended_at', 'start_station_name', 'end_station_name', 'member_casual']]
    # Convert to datetime
    df['started_at'] = pd.to_datetime(df['started_at'])
    df['ended_at'] = pd.to_datetime(df['ended_at'])
    # Calculate ride_length
    df['ride_length'] = df['ended_at'] - df['started_at']
    # Format to HH:MM:SS
    df['ride_length_str'] = df['ride_length'].apply(lambda x: str(timedelta(seconds=x.total_seconds())).split('.')[0] if pd.notnull(x) else None)
    # Day of week (1=Sunday to 7=Saturday)
    df['day_of_week'] = df['started_at'].dt.weekday + 1
    dfs.append(df)

# Combine all
combined_df = pd.concat(dfs, ignore_index=True)

# Clean: remove invalid rides
combined_df = combined_df[combined_df['ride_length'] > timedelta(0)]
combined_df = combined_df[combined_df['ride_length'] < timedelta(days=1)]  # assume no rides >1 day
combined_df = combined_df.dropna(subset=['start_station_name', 'end_station_name'])

# Standardize member_casual
combined_df['member_casual'] = combined_df['member_casual'].str.lower().map({'member': 'member', 'subscriber': 'member', 'customer': 'casual'})

# Save to csv
combined_df.to_csv(os.path.join(excel_dir, 'combined_trips.csv'), index=False)

print("Data processing complete. Combined data saved to combined_trips.csv.")
