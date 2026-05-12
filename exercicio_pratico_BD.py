


import sqlite3



conn = sqlite3.connect('exercicio_pratico_BD.db')


cursor = conn.cursor()







cursor.execute('''

    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )

''')


cursor.execute('''

    INSERT INTO clientes (nome, email) VALUES 
    ('João Silva', 'joao.silva@mail.com'),
    ('Maria Oliveira', 'maria.oliveira@mail.com'),
    ('Carlos Santos', 'carlos.santos@mail.com')

''')

conn.commit()



cursor.execute('SELECT * FROM clientes')



clientes = cursor.fetchall()

print("Clientes:")
for cliente in clientes:
    print(cliente)



cursor.execute('''

    UPDATE clientes SET email = 'novo_email@dominio.com' WHERE id = 1

''')

conn.commit()



cursor.execute('''

    DELETE FROM clientes WHERE id = 2

''')
conn.commit()

cursor.execute('SELECT * FROM clientes')

clientes = cursor.fetchall()

print("Clientes após as alterações:")
for cliente in clientes:
    print(cliente)


cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY,
        cliente_id INTEGER,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )

''')



cursor.execute('''
    INSERT INTO pedidos (cliente_id, produto, quantidade) VALUES (1, 'Produto A', 2)
''')
conn.commit()



cursor.execute('''
    SELECT pedidos.id, clientes.nome, pedidos.produto, pedidos.quantidade
    FROM pedidos
    JOIN clientes ON pedidos.cliente_id = clientes.id
''')

pedidos = cursor.fetchall()

print("Pedidos:")
for pedido in pedidos:
    print(pedido)



cursor.execute('''
    UPDATE pedidos SET quantidade = 5 WHERE id = 1
''')

conn.commit()

