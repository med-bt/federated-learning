from flask import Flask, render_template, request, redirect, url_for
from forms import MLTypeForm,AlgorithmForm,HyperparametersForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/', methods=['GET', 'POST'])
def select_type():
    form = MLTypeForm()
    if form.validate_on_submit():
        return redirect(url_for('select_algorithm', ml_type=form.ml_type.data))
    return render_template('select_type.html', form=form)

@app.route('/algorithm/<ml_type>', methods=['GET', 'POST'])
def select_algorithm(ml_type):
    form = AlgorithmForm()
    if ml_type == 'regression':
        form.algorithm.choices = [('linear_regression', 'Linear Regression')]
    elif ml_type == 'classification':
        form.algorithm.choices = [('decision_tree', 'Decision Tree Classifier')]
    elif ml_type == 'clustering':
        form.algorithm.choices = [('kmeans', 'KMeans')]
    if form.validate_on_submit():
        return redirect(url_for('hyperparameters', ml_type=ml_type, algorithm=form.algorithm.data))
    return render_template('select_algorithm.html', form=form)

@app.route('/hyperparameters/<ml_type>/<algorithm>', methods=['GET', 'POST'])
def hyperparameters(ml_type, algorithm):
    form = HyperparametersForm()
    if form.validate_on_submit():
        param1 = form.param1.data
        param2 = form.param2.data
        batch_size = form.batch_size.data

        if algorithm == 'linear_regression':
            code = f"""
from sklearn.linear_model import LinearRegression
model = LinearRegression()
# No hyperparameters required for LinearRegression.
"""
        elif algorithm == 'decision_tree':
            code = f"""
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(max_depth={param1}, min_samples_split={param2})
"""
        elif algorithm == 'kmeans':
            code = f"""
from sklearn.cluster import KMeans
model = KMeans(n_clusters={param2}, max_iter={param1})
"""

        code += f"""
# Train model (dummy example with X, y for supervised or X only for clustering)
# X, y = ...  # Load your dataset here
# model.fit(X[:{batch_size}])
"""
        return render_template('generated_code.html', code=code)
    return render_template('hyperparameters.html', form=form)

@app.route('/generated_code.html')
def generated_code():
    return """<html><body><pre>{{ code }}</pre></body></html>"""

if __name__ == '__main__':
    app.run(debug=True)
