from flask import Flask, render_template, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastroLivros.sqlite3'
db = SQLAlchemy(app)

class BancoLivro(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    livro = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    lido = db.Column(db.String(3), nullable=False)

    def __init__(self, id, livro, autor, lido):
        self.id = id
        self.livro = livro
        self.autor = autor
        self.lido = lido
        

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route('/Livros')
def index():
    livros = []
    for livro in BancoLivro.query.all():
        livros.append(livro.as_dict())
    return jsonify(livros)    


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        adic_livro = BancoLivro(request.form['id'], 
                                request.form['livro'],
                                request.form['autor'],  
                                request.form['lido'])
        db.session.add(adic_livro)
        db.session.commit()
        #aqui salvamos no banco
        #return jsonify(adic_livro)
        return redirect(url_for('index'))    
    return render_template('add.html')
        
        
        #id = request.form.get('id')
        #livro = request.form.get('titulo')
        #autor = request.form.get('autor')
        #lido = request.form.get('lido')
        #banco_livro = BancoLivro(id, livro, autor, lido)
        #db.session.add(banco_livro)
        #db.session.commit()
        #return jsonify({banco_livro.id: {
        #    'id': str(banco_livro.id),
        #    'livro': banco_livro.titulo,
        #    'autor': banco_livro.autor,
        #    'lido': banco_livro.lido            
        #}})
        #db.session.add()
        #aqui salvamos no banco
        #return jsonify(adic_livro)
        #return redirect(url_for('index'))    
    #return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    editalivrobanco = BancoLivro.query.get(id)
    if request.method == 'POST':
        editalivrobanco.id = request.form['id']
        editalivrobanco.livro = request.form['livro']
        editalivrobanco.autor = request.form['autor']
        editalivrobanco.lido = request.form['lido']
        db.session.commit()
        return jsonify(editalivrobanco)
        #return redirect(url_for('index'))
    return render_template('edit.html', editalivrobanco=editalivrobanco)


@app.route('/delete_/<int:id>')
def delete_(id):
    deleta_livro_banco = BancoLivro.query.get(id)
    db.session.delete(deleta_livro_banco)
    db.session.commit()
    return jsonify(deleta_livro_banco)
    #return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
