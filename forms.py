from wtforms import SelectField, StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired


class MLTypeForm(FlaskForm):
    ml_type = SelectField('Choose ML Type', choices=[('regression', 'Regression'), ('classification', 'Classification'), ('clustering', 'Clustering')], validators=[DataRequired()])
    submit = SubmitField('Next')

class AlgorithmForm(FlaskForm):
    algorithm = SelectField('Choose Algorithm', choices=[], validators=[DataRequired()])
    submit = SubmitField('Next')

class HyperparametersForm(FlaskForm):
    param1 = FloatField('Parameter 1 (e.g., max_iter for KMeans)', validators=[DataRequired()])
    param2 = FloatField('Parameter 2 (e.g., n_clusters for KMeans)', validators=[DataRequired()])
    batch_size = IntegerField('Batch Size', validators=[DataRequired()])
    submit = SubmitField('Generate Code')