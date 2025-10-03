import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Color scheme (colorblind-friendly)
colors = {'member': '#1f77b4', 'casual': '#ff7f0e'}  # Blue and orange

# Load summaries
avg_ride_by_type = pd.read_csv('data/excel_copies/avg_ride_by_type.csv', index_col=0)
rides_by_day = pd.read_csv('data/excel_copies/rides_by_day.csv', index_col=0)
rides_by_type_day = pd.read_csv('data/excel_copies/rides_by_type_day.csv', index_col=0)

# Plot 1: Avg ride length by user type
fig1 = px.bar(avg_ride_by_type, x=avg_ride_by_type.index, y='ride_length_sec',
              color=avg_ride_by_type.index, color_discrete_map=colors,
              labels={'ride_length_sec': 'Average Ride Length (seconds)', 'index': 'User Type'},
              title="Members ride shorter, focused trips; Casuals enjoy longer adventures.")
fig1.update_layout(yaxis_title="Seconds", xaxis_title="")
fig1.write_html('docs/avg_ride_by_type.html')

# Plot 2: Number of rides by day of week
fig2 = px.bar(rides_by_day, x=rides_by_day.index, y='ride_id',
              color_discrete_sequence=['#2ca02c'],
              labels={'ride_id': 'Number of Rides', 'day_of_week': 'Day of Week'},
              title="Weekday peaks for members (commutes); Weekends for casuals (leisure).")
fig2.update_xaxes(tickvals=list(range(1,8)), ticktext=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
fig2.write_html('docs/rides_by_day.html')

# Plot 3: Rides by user type and day of week (stacked bar)
fig3 = px.bar(rides_by_type_day.T, barmode='stack',
              color_discrete_map=colors,
              labels={'value': 'Number of Rides', 'day_of_week': 'Day of Week'},
              title="Stacked view: Members dominate weekdays; Casuals own weekends.")
fig3.update_xaxes(tickvals=list(range(1,8)), ticktext=['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
fig3.write_html('docs/rides_by_type_day.html')

print("Interactive visualizations created as HTML.")
