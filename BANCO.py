import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cdd2023",
    database="escola_turma_b"
)
print(banco)


meucursor=banco.cursor()
pesquisa = 'select * from alunos;'
meucursor.execute(pesquisa)
resultado=meucursor.fetchall()

for x in resultado:
    print(x)
#meucursor.close()
#banco.close()

#inserindo dados na tabela
nome1='Teste'
cpf='04123658974'
telefone='81994512365'
media=9.5
Fk_Turma=2
cursor=banco.cursor()
sql="insert into alunos (nome,cpf,Telefone,Media,FK_Turma) values(%s,%s,%s,%s,%s)"
data=(nome1,cpf,telefone,media,Fk_Turma)
cursor.execute(sql,data)
banco.commit()
userid=cursor.lastrowid
print(userid)
cursor.close()
banco.close()