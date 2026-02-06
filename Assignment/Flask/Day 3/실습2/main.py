from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__)

# 임시 데이터 저장소
todos = {
    1: "공부하기",
    2: "자기"
}
#####################
# DB 설정
#####################
BASE_DIR = os.path.dirname(__file__)
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)

DATABASE_URL = F'sqlite:///{os.path.join(INSTANCE_DIR, "todos.db")})'


engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

#####################
# 모델 정리
#####################
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, Index=True)
    task = Column(String, nullable=False)

    def __repr__(self):
        return f"<Todo_id={self.id}, task={self.task}>"

Base.metadata.create_all(engine)


#####################
# CRUD
#####################

# READ: 전체 항목 조회
@app.route("/todos", methods=["GET"])
def get_todos():
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()
    return jsonify([{"id": t.id, "task": t.task} for t in todos])


# READ: 특정 항목 조회
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    db = SessionLocal()
    todo = todos.get(todo_id).get(todo_id)
    db.colose()

    if not todo:
        return jsonify({'error': '해당 할 일이 없습니다.'}), 404
    return jsonify({'id': todo.id, 'task': todo.task})


# CREATE: 새로운 항목 조회
@app.route("/todos", method=["POST"])
def create_todo():
    data = request.get_json()

    db = SessionLocal()
    todo = Todo(task=data.get("task"))
    db.add(todo)
    db.commit()
    db.refresh(todo) # commit 후 자동 생성된 id 불러오기
    db.close()

    return jsonify({'id': todo.id, 'task': todo.task}), 201


# UPDATE: 특정 항목 수정
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    db = SessionLocal()

    todo = db.query(Todo).get(todo_id)
    if todo_id not in todos:
        db.close()
        return jsonify({'error': '해당 할 일이 없습니다.'}), 404
    

    data = request.get_json()
    todo.task = data['task']
    db.commit()
    updated = {'id': todo.id, 'task': todo.task}
    db.close()
    return jsonify(updated)


# DELETE: 특정 항목 삭제
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    db = SessionLocal()
    todo = db.query(Todo).get(todo_id)
    if not todo:
        db.close()
        return jsonify({'error': '해당 할 일이 없습니다.'}), 404
    
    db.delete(todo)
    db.commit()
    db.close()
    return jsonify({'deleted': todo_id})























# READ: 전체 항목 조회
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


# READ: 특정 항목 조회
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    task = todos.get(todo_id)
    if not task:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify({todo_id: task})


# CREAT: 새로운 항목 조회
@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    new_id = max(todos.keys()) + 1 if todos else 1
    todos[new_id] = data["task"]
    return jsonify({new_id: todos[new_id]}), 201


# UPDATE: 특정 항목 수정
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    if todo_id not in todos:
        return jsonify({"error": "Todo not found"}), 404
    data = request.get_json()
    todos[todo_id] = data["task"]
    return jsonify({todo_id: todos[todo_id]})


# DELETE: 특정 항목 삭제
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    if todo_id not in todos:
        return jsonify({"error": "Todo not found"}), 404
    todos.pop(todo_id)
    return jsonify({"deleted": "deleted"})


if __name__ == "__main__":
    app.run(debug=True, port=2000)