from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form.get('role')
        # Role ke hisaab se redirect karein
        if role == 'student':
            return redirect(url_for('student.dashboard'))
        elif role == 'teacher':
            return redirect(url_for('teacher.dashboard'))
        else:
            return redirect(url_for('courses.list_courses'))
    return render_template('auth/login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Signup logic baad mein
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html')

