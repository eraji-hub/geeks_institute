from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

students = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "age": 20, "gender": "male"},
    {"id": 2, "name": "Jane Doe", "email": "jane.doe@example.com", "age": 21, "gender": "female"},
    {"id": 3, "name": "Jim Doe", "email": "jim.doe@example.com", "age": 22, "gender": "male"},
    {"id": 4, "name": "Jill Doe", "email": "jill.doe@example.com", "age": 23, "gender": "female"},
    {"id": 5, "name": "Jack Doe", "email": "jack.doe@example.com", "age": 24, "gender": "male"}
]

def get_student_by_id(student_id):
    return next((s for s in students if s['id'] == student_id), None)

def get_next_id():
    return max([s['id'] for s in students], default=0) + 1


@app.route("/students", methods=["GET"])
def get_students():
    """Get all students with pagination"""
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    start = (page - 1) * limit
    end = start + limit
    return jsonify({
        "students": students[start:end],
        "page": page,
        "limit": limit
    }), 200

@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    """Get a student by ID"""
    student = get_student_by_id(student_id)
    if not student:
        return jsonify(None), 404
    return jsonify(student), 200

@app.route("/students", methods=["POST"])
def create_student():
    """Create a new student"""
    data = request.get_json()
    new_student = {
        "id": get_next_id(),
        "name": data.get("name"),
        "email": data.get("email"),
        "age": data.get("age"),
        "gender": data.get("gender")
    }
    students.append(new_student)
    return jsonify(new_student), 201

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """Update an existing student"""
    student = get_student_by_id(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()
    student.update({
        "name": data.get("name", student["name"]),
        "email": data.get("email", student["email"]),
        "age": data.get("age", student["age"]),
        "gender": data.get("gender", student["gender"])
    })
    return jsonify(student), 200

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """Delete a student"""
    student = get_student_by_id(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    students.remove(student)
    return jsonify(student), 200



@app.errorhandler(404)
def handle_404(e):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.name, "message": e.description}), e.code
    return jsonify({"error": "An error occurred", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
