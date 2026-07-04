from flask import Flask, request, redirect, render_template
from models import db, Task
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Prometheus Counter
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests",
    ["method", "endpoint"]
)


@app.before_request
def before_request():
    REQUEST_COUNT.labels(request.method, request.path).inc()


@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")

    if title:
        task = Task(title=title)
        db.session.add(task)
        db.session.commit()

    return redirect("/")


@app.route("/complete/<int:id>")
def complete(id):
    task = Task.query.get_or_404(id)
    task.completed = True
    db.session.commit()
    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")


@app.route("/health")
def health():
    return {
        "status": "UP",
        "application": "DevOpsX 2.0",
        "database": "Connected"
    }, 200


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
