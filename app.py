import os
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Get the folder containing app.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build the full path to formatted_output.csv
csv_path = os.path.join(BASE_DIR, "formatted_output.csv")

# Read the processed data
df = pd.read_csv(csv_path)
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Read the processed data
df = pd.read_csv("formatted_output.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Aggregate sales by date
daily_sales = df.groupby("Date", as_index=False)["Sales"].sum()

# Create the figure
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales"
)

app = Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Soul Foods Pink Morsel Sales Dashboard",
        id="dashboard-header"
    ),
    dcc.Dropdown(
    id="region-picker",
    options=[
        {"label": region, "value": region}
        for region in sorted(df["Region"].unique())
    ],
    value=sorted(df["Region"].unique())[0],
    clearable=False
),

    dcc.Graph(
        id="sales-chart",
        figure=fig
    )

])

if __name__ == "__main__":
    app.run(debug=True)