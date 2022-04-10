from tinydb import TinyDB

db = TinyDB('db.json', encoding='utf-8', ensure_ascii=False, indent=4)
professores = db.table('professores')
disciplinas = db.table('disciplinas')
salas = db.table('salas')
