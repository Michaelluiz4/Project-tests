from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/greeting', methods=['POST'])
def greenting():
    name = request.form.get('name')

    if not name:
        return jsonify({"Error": "Name is required"}), 400
    
    return render_template("greeting.html", name=name)    
   
if __name__ == '__main__':
    app.run(debug=True)