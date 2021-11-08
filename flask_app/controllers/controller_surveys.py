from flask_app import app, render_template, request, redirect, session
from flask_app.models.model_survey import Survey

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def create_survey():
    data = {
        "name" : request.form['name'],
        "location" : request.form['location'],
        "language" : request.form['language'],
        "comments" : request.form['comments']
    }

    if not Survey.validate_survey(request.form):
        return redirect('/')
        
    id= Survey.save(data)
    return redirect(f"/result/{id}")
    

@app.route("/result/<int:id>")
def show_survey(id):
    print("Showing the User Info From the Form")
    data = {
        "id":id
        }
    survey=Survey.get_one(data)
    print(survey)
    return render_template("result.html", survey=survey )
