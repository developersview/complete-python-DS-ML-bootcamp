from flask import Flask, render_template

'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
#WSGI application instance
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Hello Team. This is the first Flask application."

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    try:
        # Run the Flask application
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your Flask installation and try again.")
        print("If you are using a virtual environment, ensure it is activated.")