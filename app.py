import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Read data
df = pd.read_csv('formatted_output.csv')

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Create Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div(

    style={
        'backgroundColor': '#f4f4f4',
        'padding': '30px',
        'fontFamily': 'Arial'
    },

    children=[

        html.H1(
            children='Soul Foods Pink Morsel Sales Dashboard',

            style={
                'textAlign': 'center',
                'color': "#1e5f07",
                'marginBottom': '30px'
            }
        ),

        html.Div([

            html.Label(
                'Select Region:',
                style={
                    'fontWeight': 'bold',
                    'fontSize': '18px'
                }
            ),

            dcc.RadioItems(
                id='region-filter',

                options=[
                    {'label': 'All', 'value': 'all'},
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'}
                ],

                value='all',

                inline=True,

                style={
                    'marginTop': '10px',
                    'marginBottom': '20px'
                }
            )

        ]),

        dcc.Graph(id='sales-line-chart')

    ]
)

# Callback for updating chart
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)

def update_graph(selected_region):

    # Filter data
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['Region'].str.lower() == selected_region]

    # Group sales by date
    sales_by_date = (
        filtered_df
        .groupby('Date')['Sales']
        .sum()
        .reset_index()
        .sort_values('Date')
    )

    # Create chart
    fig = px.line(
    sales_by_date,
    x='Date',
    y='Sales',
    title=f'Sales Trend - {selected_region.title()} Region',
    color_discrete_sequence=['purple']
)

    # Style chart
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(size=14),
        title_font=dict(size=22),
        xaxis_title='Date',
        yaxis_title='Sales'
    )

    return fig

# Run app
if __name__ == '__main__':
    app.run(debug=True)