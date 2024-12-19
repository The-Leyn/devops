from flask import Flask, request, redirect, url_for, render_template_string
import requests

app = Flask(__name__)

# local
# BACKEND_URL = "http://localhost:3000/tasks"

# container
BACKEND_URL = "http://backend:3000/tasks"

template = """
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo TP</title>
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"
    >
  </head>
  <body>
    <div class="container">
      <h1>TODO List</h1>
      <form method="POST" action="/add">
        <input type="text" name="title" placeholder="Ajouter une tache">
        <input type="submit" value="Ajouter">
      </form>
      <ul>
      {% for task in tasks %}
        <li>
          {{task.title}} - Fait: {{task.done}}
          <form method="POST" action="/done/{{ task._id }}" style="display:inline">
            <input type="submit" value="Marquer comme fait">
          </form>
          <form method="POST" action="/delete/{{ task._id }}" style="display:inline">
            <input type="submit" value="Supprimer">
          </form>
        </li>
      {% endfor %}
      </ul>
    </div>
  </body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    resp = requests.get(BACKEND_URL)
    tasks = resp.json()
    return render_template_string(template, tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    requests.post(BACKEND_URL, json={"title": title})
    return redirect(url_for('index'))

@app.route("/done/<task_id>", methods=["POST"])
def done(task_id):
    requests.put(f"{BACKEND_URL}/{task_id}", json={"done": True})
    return redirect(url_for('index'))

@app.route("/delete/<task_id>", methods=["POST"])
def delete(task_id):
    requests.delete(f"{BACKEND_URL}/{task_id}")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
