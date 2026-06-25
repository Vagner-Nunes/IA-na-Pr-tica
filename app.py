from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados simulado em memória
tasks = [
    {"id": 1, "title": "Configurar Repositório", "completed": False},
    {"id": 2, "title": "Criar Pipeline CI", "completed": False}
]

# Gerado com o prompt do GitHub Copilot: 
# "Crie uma função em Python/Flask para uma rota POST '/tasks' que adicione uma nova tarefa. A tarefa deve conter id, title (obrigatório) e completed (padrão False). Retorne erro 400 se o título faltar."
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json() or {}
    if 'title' not in data:
        return jsonify({"error": "O título é obrigatório"}), 400
    
    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "completed": data.get('completed', False)
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

if __name__ == '__main__':
    app.run(debug=True)
