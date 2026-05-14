import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Read formatted data
df = pd.read_csv('formatted_output.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Group sales by date
sales_by_date = df.groupby('Date')['Sales'].sum().reset_index()

# Sort by date
sales_by_date = sales_by_date.sort_values('Date')

# Create line chart
fig = px.line(
    sales_by_date,
    x='Date',
    y='Sales',
    title='Pink Morsel Sales Over Time'
)

# Create Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div(children=[

    html.H1(
        children='Soul Foods Sales Visualiser'
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )

])

# Run app
if __name__ == '__main__':
    app.run(debug=True)
