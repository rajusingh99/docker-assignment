from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow cross-origin requests from frontend if direct posting

# Simple HTML template to show after submission
RESULT_HTML = """
<!doctype html>
<html>
  <head><meta charset="utf-8"><title>Submission Result</title></head>
  <body>
    <h1>Data received by Flask backend</h1>
    <ul>
      <li><strong>Name:</strong> {{ name }}</li>
      <li><strong>Email:</strong> {{ email }}</li>
      <li><strong>Message:</strong> {{ message }}</li>
    </ul>
    <a href="/">Back</a>
  </body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return "<h2>Flask backend is running. POST to /submit</h2>"

@app.route("/submit", methods=["POST"])
def submit():
    # Accept both JSON and form-encoded
    data = request.get_json(silent=True)
    if data is None:
        data = request.form.to_dict()
    name = data.get("name", "<no name>")
    email = data.get("email", "<no email>")
    message = data.get("message", "<no message>")

    # Here you can process the data: save to DB, validate, etc.
    # For demo, just return a simple HTML result page
    return render_template_string(RESULT_HTML, name=name, email=email, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
