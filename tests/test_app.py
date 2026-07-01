import os
import sys
import pytest

# Add the project root to Python's path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


@pytest.fixture
def dash_app(dash_duo):
    dash_duo.start_server(app)
    return dash_duo


def test_header_present(dash_app):
    assert dash_app.find_element("#dashboard-header")


def test_visualisation_present(dash_app):
    assert dash_app.find_element("#sales-chart")


def test_region_picker_present(dash_app):
    assert dash_app.find_element("#region-picker")