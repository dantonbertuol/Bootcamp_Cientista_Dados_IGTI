import mysql.connector
import csv

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    auth_plugin='mysql_native_password'
)


#print(mydb)

#mycursor = mydb.cursor()

# Para criar um banco de dados use o comando abaixo
# mycursor.execute("CREATE DATABASE mydatabase")

# Retorna todos os esquemas criados no seu servidor de Banco de Dados
#mycursor.execute("SHOW DATABASES")

#for db in mycursor:
#    print(db)

# Conectar ao MySQL Server selecionand um banco de dados específico
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bootcamp'
)


mycursor = mydb.cursor()


# Retorna todas as tabelas criados no seu esquema de Banco de Dados
#mycursor.execute("SHOW TABLES")

#for db in mycursor:
#    print(db)

# Inserir dados em uma tabela

query = "INSERT INTO caracteristicasgerais (idcaracteristicasGerais, dsccaracteristicasGerais) VALUES (%s, %s)"
values = (1, "Portaria 24 horas")

mycursor.execute(query, values)

# Fazer a confirmação da inserção
mydb.commit()

print(mycursor.rowcount, "registro(s) inserido(s).")

# Inserindo multiplos valores
values = [(2, "Elevador"), (3, "Piscina")]

mycursor.executemany(query, values)

mydb.commit()

print(mycursor.rowcount, "registro(s) inserido(s).")

# Consultar a tabela
#mycursor.execute("SELECT * FROM caracteristicasgerais")

#myresult = mycursor.fetchall()  # todos os registros

#for mydata in myresult:
#    print(mydata)

#mycursor.execute("SELECT idcaracteristicasGerais, dsccaracteristicasGerais FROM caracteristicasgerais")

#myresult = mycursor.fetchone()  # apenas primeiro registro

#print(myresult)

# Incluir Caracteristicas Gerais
filename = 'caracteristicasgerais.csv'

#Abrir arquivo e inserir cada linha do arquivo na tabela cidade

with open(filename, 'r') as incsvfile:
    reader = csv.reader(incsvfile, delimiter=',')
    next(reader, None)  # skip the headers
    for line in reader:
        mycursor.execute ("INSERT INTO caracteristicasgerais (idcaracteristicasGerais, dsccaracteristicasGerais)\
                  VALUES (%s, %s)",line)
mydb.commit()

#db.close()
incsvfile.close() #Fechar arquivo



# Incluir estados
filename = 'estados.csv'

#Abrir arquivo e inserir cada linha do arquivo na tabela cidade

with open(filename, 'r') as incsvfile:
    reader = csv.reader(incsvfile, delimiter=',')
    next(reader, None)  # skip the headers
    for line in reader:
        mycursor.execute ("INSERT INTO estado\
                  VALUES (%s, %s, %s, %s)",line)
mydb.commit()

#db.close()
incsvfile.close() #Fechar arquivo



# Incluir cidades
filename = 'cidades.csv'

#Abrir arquivo e inserir cada linha do arquivo na tabela cidade

with open(filename, 'r') as incsvfile:
    reader = csv.reader(incsvfile, delimiter=',')
    next(reader, None)  # skip the headers
    for line in reader:
        mycursor.execute ("INSERT INTO cidade\
                  VALUES (%s, %s, %s, %s)",line)
mydb.commit()

#db.close()
incsvfile.close() #Fechar arquivo



# Incluir imoveis
filename = 'imoveis.csv'

#Abrir arquivo e inserir cada linha do arquivo na tabela cidade

with open(filename, 'r') as incsvfile:
    reader = csv.reader(incsvfile, delimiter=',')
    next(reader, None)  # skip the headers
    for line in reader:
        mycursor.execute ("INSERT INTO imovel\
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",line)
mydb.commit()

#db.close()
incsvfile.close() #Fechar arquivo


# Incluir caracteristica geral imovel
filename = 'caracteristicageralimovel.csv'

#Abrir arquivo e inserir cada linha do arquivo na tabela cidade

with open(filename, 'r') as incsvfile:
    reader = csv.reader(incsvfile, delimiter=',')
    next(reader, None)  # skip the headers
    for line in reader:
        mycursor.execute ("INSERT INTO caracteristicageralimovel (idcaracteristicasGerais, idImovel, temCaracteristica)\
                  VALUES (%s, %s, %s)",line)
mydb.commit()

#db.close()
incsvfile.close() #Fechar arquivo