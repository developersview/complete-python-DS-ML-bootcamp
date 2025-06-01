### Building Url Dynamically
## Variable Rule
### Jinja 2 Template Engine

### Jinja2 Template Engine
'''
{{  }} expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
'''
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello Team. This is the first Flask application."

@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}, welcome to the Flask application!"
    else:
        return render_template("form.html")
    

@app.route("/result1/<int:score>")
def result1(score):
    res = ""
    return render_template("result1.html", score=score, result=res)

@app.route("/result2/<int:score>")
def result2(score):
    res = ""
    if score >= 90:
        res = "Excellent"
    elif score >= 80:
        res = "Very Good"
    elif score >= 70:
        res = "Good"
    elif score >= 60:
        res = "Average"
    elif score >= 50:
        res = "Poor"
    else:
        res = "Fail"
    
    exp={'score':score,"res":res}

    return render_template("result2.html", results=exp)

if __name__ == '__main__':
    try:
        # Run the Flask application
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your Flask installation and try again.")
        print("If you are using a virtual environment, ensure it is activated.")