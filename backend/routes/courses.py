from flask import Blueprint, render_template, request, redirect, url_for
from backend.database import get_connection

course_bp = Blueprint('courses', __name__)

# 1. Read All (Course List)
@course_bp.route('/courses')
def list_courses():
    conn = get_connection()
    courses = conn.execute('SELECT * FROM courses').fetchall()
    conn.close()
    return render_template('courses/list.html', courses=courses)

# 2. Create Course
@course_bp.route('/courses/create', methods=['GET', 'POST'])
def create_course():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        teacher_name = request.form['teacher_name']
        
        conn = get_connection()
        conn.execute('INSERT INTO courses (title, description, teacher_name) VALUES (?, ?, ?)', 
                     (title, description, teacher_name))
        conn.commit()
        conn.close()
        return redirect(url_for('courses.list_courses'))
        
    return render_template('courses/create.html')

# 3. Update Course (Edit)
@course_bp.route('/courses/edit/<int:id>', methods=['GET', 'POST'])
def edit_course(id):
    conn = get_connection()
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        teacher_name = request.form['teacher_name']
        
        conn.execute('UPDATE courses SET title=?, description=?, teacher_name=? WHERE id=?', 
                     (title, description, teacher_name, id))
        conn.commit()
        conn.close()
        return redirect(url_for('courses.list_courses'))
        
    course = conn.execute('SELECT * FROM courses WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('courses/edit.html', course=course)

# 4. Delete Course
@course_bp.route('/courses/delete/<int:id>', methods=['POST'])
def delete_course(id):
    conn = get_connection()
    conn.execute('DELETE FROM courses WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('courses.list_courses'))

# 5. Course Detail (View Materials & Enrolled Students)
@course_bp.route('/courses/<int:id>')
def course_detail(id):
    conn = get_connection()
    course = conn.execute('SELECT * FROM courses WHERE id = ?', (id,)).fetchone()
    materials = conn.execute('SELECT * FROM materials WHERE course_id = ?', (id,)).fetchall()
    enrollments = conn.execute('SELECT * FROM enrollments WHERE course_id = ?', (id,)).fetchall()
    conn.close()
    return render_template('courses/detail.html', course=course, materials=materials, enrollments=enrollments)

# 6. Upload Material
@course_bp.route('/courses/<int:id>/upload', methods=['POST'])
def upload_material(id):
    material_title = request.form['material_title']
    file_type = request.form['file_type']
    
    conn = get_connection()
    conn.execute('INSERT INTO materials (course_id, title, file_type) VALUES (?, ?, ?)',
                 (id, material_title, file_type))
    conn.commit()
    conn.close()
    return redirect(url_for('courses.course_detail', id=id))

# 7. Enroll Student
@course_bp.route('/courses/<int:id>/enroll', methods=['POST'])
def enroll_student(id):
    student_name = request.form['student_name']
    
    conn = get_connection()
    conn.execute('INSERT INTO enrollments (student_name, course_id) VALUES (?, ?)',
                 (student_name, id))
    conn.commit()
    conn.close()
    return redirect(url_for('courses.course_detail', id=id))
