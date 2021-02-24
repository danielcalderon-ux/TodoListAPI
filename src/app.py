from flask import Flask,jsonify,request,json

#siempre arriba dice que trabajamos con flask
app = Flask(__name__)

todos =[
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
    
]

#decorador ayuda a facilitar el trabajo
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos) # lo que retorna a /todos


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):
        todos.pop(position)
    else:
        raise Exception("Sorry, no numbers below zero")
    return jsonify(todos)






# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True) #debug todo se ve reflejado aqui




"""@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):
        todos.pop(position) #pop Saca por el indice y remove saca por el valor
    else:
        raise Exception("Sorry, no numbers below zero")
    return jsonify(todos) , 200"""

