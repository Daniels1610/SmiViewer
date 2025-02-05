#
# Imports
#
from flask.views import MethodView
from flask import Blueprint
#
# Testing
#
from app.blueprints.ml.services import dashboard_service

ml = Blueprint(
    'ml', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/ml/static',
    url_prefix='/ml'
)


class Dashboard(MethodView):
    '''
    Machine Learning Models Metrics
    render_template('dashboard.html', title='Dashboard', subtitle='Machine Learning Models Metrics', all_models=all_models)
    '''
    def get(self): 
        all_models = dashboard_service.get_dashboard_data()
        return all_models 


ml.add_url_rule('/dashboard', view_func=Dashboard.as_view("dashboard"))