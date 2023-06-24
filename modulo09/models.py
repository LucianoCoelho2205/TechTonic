from main import db
class Carros(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(40), nullable=False)
    cor = db.Column(db.String(20), nullable=False)
    ano = db.Column(db.String(20), nullable=False)
    placa = db.Column(db.String(20), nullable=False)
    preco = db.Column(db.String(20), nullable=False)
    

    def __repr__(self):
        return '<Name %r>' % self.name


class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name