import psycopg2

print("Testando...")

try:
    conn = psycopg2.connect(host = "localhost",
    port ="5432",
    database = "postgres", 
    user="teste", password = "123456")
    print('VOCE ESTA CONECTADO............')

except Exception:
    print('VOCE ESTA SEM CONEXAO..........')


if conn is not None:
    
    print('Sua Conexao está estabilizada!')

    cursor = conn.cursor()
    
    cursor.execute('CREATE TABLE  carro (id serial, marca VARCHAR(15)NOT NULL, modelo VARCHAR(15)NOT NULL, ano varchar(15) NOT NULL, cor varchar(15) NOT NULL, placa varchar(15) NOT NULL, preco varchar(15) NOT NULL, PRIMARY KEY(id));')
    print('Sua tabela de carros foi criada!')

    cursor.execute('CREATE TABLE usuarios  (nome VARCHAR(15) NOT NULL, nickname VARCHAR(30)NOT NULL, senha VARCHAR(30)NOT NULL,  PRIMARY KEY(nickname) );')
    print('Sua tabela usuario foi criada!')

    conn.commit()
    cursor.close()
    conn.close()