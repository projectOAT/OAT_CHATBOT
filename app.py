# app.py

from flask import Flask, request, jsonify
from agent import agent_executor

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query_db():
    user_question = request.json["question"]
    response = agent_executor.invoke(user_question)
    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(debug=True)
