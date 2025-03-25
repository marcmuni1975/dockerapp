from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notas.db'
db = SQLAlchemy(app)

class Estudiante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    notas = db.relationship('Nota', backref='estudiante', lazy=True)

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asignatura = db.Column(db.String(100), nullable=False)
    calificacion = db.Column(db.Float, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiante.id'), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    estudiantes = Estudiante.query.all()
    return render_template('index.html', estudiantes=estudiantes)

@app.route('/agregar_estudiante', methods=['GET', 'POST'])
def agregar_estudiante():
    if request.method == 'POST':
        nombre = request.form['nombre']
        estudiante = Estudiante(nombre=nombre)
        db.session.add(estudiante)
        db.session.commit()
        flash('Estudiante agregado correctamente')
        return redirect(url_for('index'))
    return render_template('agregar_estudiante.html')

@app.route('/agregar_nota/<int:estudiante_id>', methods=['GET', 'POST'])
def agregar_nota(estudiante_id):
    estudiante = Estudiante.query.get_or_404(estudiante_id)
    if request.method == 'POST':
        asignatura = request.form['asignatura']
        calificacion = float(request.form['calificacion'])
        nota = Nota(asignatura=asignatura, calificacion=calificacion, estudiante_id=estudiante.id)
        db.session.add(nota)
        db.session.commit()
        flash('Nota agregada correctamente')
        return redirect(url_for('index'))
    return render_template('agregar_nota.html', estudiante=estudiante)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
