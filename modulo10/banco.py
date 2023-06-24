import psycopg2

print("Testando...")

try:
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="teste",
        password="123456"
    )
    print('VOCÊ ESTÁ CONECTADO............')

except Exception:
    print('VOCÊ ESTÁ SEM CONEXÃO..........')

if conn is not None:
    print('Sua conexão está estabelecida!')
    cursor = conn.cursor()
    
    insert_query = "INSERT INTO usuarios (nome, nickname, senha) VALUES (%s, %s, %s)"
    values = ("jose", "josedev", "123456")
    
    cursor.execute(insert_query, values)
    
    conn.commit()
    cursor.close()
    conn.close()
