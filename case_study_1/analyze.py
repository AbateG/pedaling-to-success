import pandas as pd

# Load combined data
df = pd.read_csv('data/excel_copies/combined_trips.csv')

# Convert ride_length to timedelta for seconds
df['ride_length_td'] = pd.to_timedelta(df['ride_length'])
df['ride_length_sec'] = df['ride_length_td'].dt.total_seconds()

# Descriptive stats
desc_stats = df.groupby('member_casual')['ride_length_sec'].agg(['mean', 'max', 'median', 'count'])
print("Descriptive stats:")
print(desc_stats)

# Avg ride length by type
avg_ride_by_type = df.groupby('member_casual')['ride_length_sec'].mean()
print("\nAvg ride length by type:")
print(avg_ride_by_type)

# Avg ride length by day
avg_ride_by_day = df.groupby('day_of_week')['ride_length_sec'].mean()
print("\nAvg ride length by day:")
print(avg_ride_by_day)

# Rides by day
rides_by_day = df.groupby('day_of_week')['ride_id'].count()
print("\nNumber of rides by day:")
print(rides_by_day)

# Rides by type and day
rides_by_type_day = df.groupby(['member_casual', 'day_of_week'])['ride_id'].count().unstack()
print("\nRides by type and day:")
print(rides_by_type_day)

# Save summaries
desc_stats.to_csv('data/excel_copies/desc_stats.csv')
avg_ride_by_type.to_csv('data/excel_copies/avg_ride_by_type.csv')
avg_ride_by_day.to_csv('data/excel_copies/avg_ride_by_day.csv')
rides_by_day.to_csv('data/excel_copies/rides_by_day.csv')
rides_by_type_day.to_csv('data/excel_copies/rides_by_type_day.csv')

print("Analysis complete.")
