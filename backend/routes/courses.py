from flask import Blueprint, render_template

course_bp = Blueprint('courses', __name__)

@course_bp.route('/courses')
def list_courses():
    return render_template('courses/list.html')