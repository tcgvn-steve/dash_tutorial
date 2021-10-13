import dash
import dash_html_components as html
import dash_admin_components as dac
from dash.dependencies import Input, Output
import dash_core_components as dcc

# =============================================================================
# Dash App and Flask Server
# =============================================================================
app = dash.Dash(__name__)

# =============================================================================
# Dash Admin Components
# =============================================================================
# Navbar
right_ui = dac.NavbarDropdown(
    badge_label="!",
    badge_color="danger",
    src="https://quantee.ai",
    header_text="2 Items",
    children=[
        dac.NavbarDropdownItem(
                children="message 1",
                date="today"
        ),
        dac.NavbarDropdownItem(
            children="message 2",
            date="yesterday"
        ),
    ]
)

navbar = dac.Navbar(color="white",
                    text="I can write text in the navbar!",
                    children=right_ui)

# Sidebar
sidebar = dac.Sidebar(
    dac.SidebarMenu(
        [
            dac.SidebarHeader(children="Members"),
            dcc.Link(children=dac.SidebarMenuItem(
                id='tab_cards', label='Users', icon='box'), href='/users'),
            dcc.Link(children=dac.SidebarMenuItem(id='tab_social_cards',
                                                  label='Groups', icon='id-card'), href='/groups'),
            dac.SidebarMenuItem(id='tab_tab_cards',
                                label='Permission', icon='image'),
            dac.SidebarHeader(children="Products"),
            dac.SidebarMenuItem(id='tab_basic_boxes',
                                label='products', icon='desktop'),
            dac.SidebarMenuItem(id='tab_value_boxes',
                                label='Categories', icon='suitcase')
        ]
    ),
    title='Dash Admin',
    skin="light",
    color="primary",
    brand_color="primary",
    url="https://quantee.ai",
    src="https://adminlte.io/themes/AdminLTE/dist/img/user2-160x160.jpg",
    elevation=3,
    opacity=0.8
)


def render_personal_page():
    return html.Div([
        html.H4(children='Here you are User Page'),
        html.Div([
            html.H1("Tutotials about ui"),
            html.P("This is p element"),
            html.P("This is p element")
        ]),
    ])


def render_company_page():
    return html.Div([
        html.H4(children='Here you are Groups Page'),
        html.Div([
            html.H1("Tutotials about ui"),
            html.P("This is p element"),
            html.P("This is p element")
        ]),
    ])


# Body
body = dac.Body([
    dcc.Location(id='url'),
    html.Div(id='content', children="")
])

# Controlbar
controlbar = dac.Controlbar(
    [
        html.Br(),
        html.P("Put different components here!"),
    ],
    title="My right sidebar",
    skin="light"
)

# Footer
footer = dac.Footer(
    html.A("@DawidKopczyk, Quantee",
           href="https://twitter.com/quanteeai",
           target="_blank",
           ),
    right_text="2019"
)

# =============================================================================
# App Layout
# =============================================================================
app.layout = dac.Page([navbar, sidebar, body, controlbar, footer])

# =============================================================================
# Run app
# =============================================================================


@app.callback(
    Output('content', 'children'),
    Input('url', 'pathname')
)
def display(pathname):
    if pathname == '/':
        return html.Div([
            html.Br(),
            html.H4(children='Here you are Home Page'),
        ])
    if pathname == '/users':
        return render_personal_page()

    if pathname == '/groups':
        return render_company_page()


if __name__ == '__main__':
    app.run_server(debug=True)
