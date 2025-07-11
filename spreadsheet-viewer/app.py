from flask import Flask, render_template, request, redirect, url_for, send_file, flash
import os
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "secret_key"
app.config['UPLOAD_FOLDER'] = "uploads"

ALLOWED_EXTENSIONS = {"xlsx"}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            flash("Nenhum arquivo enviado!")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("Nenhum arquivo selecionado!")
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash("Formato inválido! Use arquivos .xlsx")
            return redirect(request.url)

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Salva filename na sessão para usar depois
        return redirect(url_for("table", filename=filename))
    return render_template("index.html")

@app.route("/table/<filename>")
def table(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if not os.path.exists(filepath):
        flash("Arquivo não encontrado!")
        return redirect(url_for("index"))

    df = pd.read_excel(filepath)

    # Exemplo simples: converter para lista de dicionários para renderizar na tabela
    data = df.to_dict(orient="records")
    columns = df.columns.values

    return render_template("table.html", data=data, columns=columns)

if __name__ == "__main__":
    app.run(debug=True)
