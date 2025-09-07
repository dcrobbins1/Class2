## import my dash library
from dash import Dash, html

## create my dash app
app = Dash(__name__)
app.title = "My First Dash App"

## define layout
app.layout = html.Div([
    html.H1("Hello Dash", style={'color':"#17459b",
                                 'fontSize':'20px',
                                 'backgroundColor':"#0F5E96"}),
    html.P("This is a simple dashboard", style={'border':'1px solid black',
                                                'padding':'20px',
                                                'margin':'50px'}),
    html.Br(),
    html.A("Click Here!", href="https://example.com")
    
])

## run the app
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)