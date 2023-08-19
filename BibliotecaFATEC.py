import sqlite3


biblioteca = sqlite3.connect('biblioteca.db')
cursor = biblioteca.cursor()
#cursor.execute(f'SELECT * FROM {biblioteca}')
# for row in cursor.fetchall():
#     print(row)
#     'aluno', 'CPF', 'E-mail', 'Livro alocado', 'Prazo de devoução' 
#cursor.execute("CREATE TABLE aluno(Aluno text, CPF integer, 'E-mail' text, 'Livro alocado' text, 'Prazo de devolução' text)")
#sql = (
    #f'INSERT INTO aluno VALUES(?,?,?,?,?)')
#cursor.execute(sql,('José','54897681232','josé.felipe@fatec.sp.gov.br','A ordem da IA','24/08/2023'))
#cursor.execute("DELETE from aluno WHERE CPF = '51184404836'")
biblioteca.commit()
cursor.close()
biblioteca.close()


