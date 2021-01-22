from src import db, ma

class Usuario(db.Model):

    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(200), nullable=False)
    dtNasc = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String(20), unique=True, nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    senha = db.Column(db.String(250), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    endereco = db.relationship('Endereco', uselist=False)

    def setNome(self, value):
        if value and len(value) > Usuario.nome.type.length:
            raise Exception("Value too long to 'nome' field")
        self.nome = value

    def setCpf(self, value):
        if value and len(value) > Usuario.cpf.type.length:
            raise Exception("Value too long to 'cpf' field")
        self.cpf = value

    def setCelular(self, value):
        if value and len(value) > Usuario.celular.type.length:
            raise Exception("Value too long to 'celular' field")
        self.celular = value

    def setEmail(self, value):
        if value and len(value) > Usuario.email.type.length:
            raise Exception("Value too long to 'email' field")
        self.email = value

    def setSenha(self, value):
        if value and len(value) > Usuario.senha.type.length:
            raise Exception("Value too long to 'senha' field")
        self.senha = value

class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nome', 'dtNasc', 'cpf', 'celular', 'email', 'senha', 'admin', 'status')

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
