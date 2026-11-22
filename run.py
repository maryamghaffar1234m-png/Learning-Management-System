from flask import Flask, render_template
from backend.routes.courses import course_bp

app = Flask(__name__)

app.register_blueprint(course_bp)

@app.route('/')
def home():
    return render_template('auth/login.html')

if __name__ == '__main__':
    app.run(debug=True)
    