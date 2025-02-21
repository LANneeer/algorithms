import pandas as pd
import numpy as np
import plotly.express as px
import webbrowser
import os

# Load the dataset
file_path = "AirQualityUCI.csv"
df = pd.read_csv(file_path, sep=",", decimal=".", header=0)

# Clean and process the data
# Combine 'Date' and 'Time' into a one datetime column
df["DateTime"] = pd.to_datetime(
    df["Date"] + " " + df["Time"], format="%m/%d/%Y %H:%M:%S", errors="coerce"
)

# Now DateTime are index
df.set_index("DateTime", inplace=True)

# Drop unnecessary ('Date', 'Time') with NaN
df.drop(columns=["Date", "Time"], inplace=True)
df.replace(-200, np.nan, inplace=True)

# Compute statistics for CO concentration
pollutant = "CO_GT"

# Monthly statistics
monthly_stats = {
    "mean": df[pollutant].resample("ME").mean().tolist(),
    "max": df[pollutant].resample("ME").max().tolist(),
    "min": df[pollutant].resample("ME").min().tolist(),
}

# Yearly statistics
yearly_stats = {
    "mean": df[pollutant].resample("YE").mean().tolist(),
    "max": df[pollutant].resample("YE").max().tolist(),
    "min": df[pollutant].resample("YE").min().tolist(),
}

# Overall maximum and minimum
overall_max = df[pollutant].max()
overall_min = df[pollutant].min()

# Visualization with Plotly
# Monthly median CO levels
fig_monthly = px.line(
    x=df[pollutant].resample("ME").mean().index,
    y=monthly_stats["mean"],
    labels={"x": "Month", "y": "CO Mean (mg/m³)"},
)
fig_monthly.update_traces(line=dict(width=2))
# Monthly maximum CO levels
fig_monthly_max = px.line(
    x=df[pollutant].resample("ME").mean().index,
    y=monthly_stats["max"],
    labels={"x": "Month", "y": "CO Mean (mg/m³)"},
)
fig_monthly_max.update_traces(line=dict(width=2))
# Monthly minimum CO levels
fig_monthly_min = px.line(
    x=df[pollutant].resample("ME").mean().index,
    y=monthly_stats["min"],
    labels={"x": "Month", "y": "CO Mean (mg/m³)"},
)
fig_monthly_min.update_traces(line=dict(width=2))

# Yearly median CO levels
fig_yearly = px.bar(
    x=df[pollutant].resample("YE").mean().index.year,
    y=yearly_stats["max"],
    labels={"x": "Year", "y": "CO Mean (mg/m³)"},
)
fig_yearly.update_traces(marker=dict(line=dict(width=1)))

# Save dashboards as HTML
fig_monthly.write_html("monthly_co_levels.html")
fig_monthly_min.write_html("monthly_co_levels_min.html")
fig_monthly_max.write_html("monthly_co_levels_max.html")
fig_yearly.write_html("yearly_co_levels.html")

# Creating a HTML page
html_report = f"""
<!DOCTYPE html>
<html>
<head>
<title>AQI by Temir</title>
<style>
    body {{
        font-family: Arial, sans-serif;
        margin: 20px;
        background-color: #f4f4f9;
        color: #333;
    }}
    h1, h2 {{
        color: #2c3e50;
    }}
    table {{
        border-collapse: collapse;
        width: 100%;
        margin-top: 20px;
    }}
    th, td {{
        border: 1px solid #ddd;
        padding: 8px;
        text-align: center;
    }}
    th {{
        background-color: #2c3e50;
        color: white;
    }}
    tr:nth-child(even) {{
        background-color: #f9f9f9;
    }}
</style>
</head>
<body>
    <h1>Air Quality Monitoring & Analysis By Ilik Temirlan</h1>
    <h2>statistics</h2>
    <table>
        <tr>
            <th>Metrics</th>
            <th>Values</th>
        </tr>
        <tr>
            <td>Total maximum CO</td>
            <td>{overall_max:.2f}</td>
        </tr>
        <tr>
            <td>Total minimum CO</td>
            <td>{overall_min:.2f}</td>
        </tr>
    </table>
    <table>
        <tr>
            <th>
                Monthly median CO Levels
                <iframe src="monthly_co_levels.html" style="width:100%; height:500px; border:none;"></iframe>
            </th>
            <th>
                Monthly minimums CO Levels
                <iframe src="monthly_co_levels_min.html" style="width:100%; height:500px; border:none;"></iframe>
            </th>
            <th>
                Monthly maximums CO Levels
                <iframe src="monthly_co_levels_max.html" style="width:100%; height:500px; border:none;"></iframe>
            </th>
        </tr>
    </table>
    <h2>Yearly median CO Levels</h2>
    <iframe src="yearly_co_levels.html" style="width:100%; height:500px; border:none;"></iframe>
</body>
</html>
"""

# Save reports
report_path = "air_quality_report.html"
with open(report_path, "w") as f:
    f.write(html_report)
report_path = os.path.abspath("air_quality_report.html")

# Open report in browser
webbrowser.open("file://" + report_path)

print("HTML report ready")
