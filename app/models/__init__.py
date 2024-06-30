from app import app
from app import db
from datetime import datetime
from app.models.sql.sqlite3.auth import Users
from app.models.sql.mysql.law.processos import Processos

with app.app_context():

    db.create_all()
    root = Users.query.filter_by(login = 'nicholas@robotz.dev').first()
    
    if root is None:
        
        root_license = "55eb3f3d94c530373c9bfc5d035050eb5e4e36c125bfafb5d4c7216a688f93859c9dfe705f1b644d5b510d67df108539172f16e88cf8f67f5f9a635b42cfca08"
        usuario = Users(
                    login = 'nicholas@robotz.dev',
                    nome_usuario = "Nicholas Silva",
                    senhacrip = "12345678",
                    email = 'nicholas@robotz.dev',
                    type_user = "super_admin",
                    license_key = root_license)
        
        db.session.add(usuario)
        
    proc = Processos.query.filter(Processos.processo == "0600305-93.2022.8.04.6300").first()
    
    if proc is None:
        
        date_string = '28-01-2022'
        format_string = '%d-%m-%Y'

        try:
            date_obj = datetime.strptime(date_string, format_string)
            print(date_obj)  # This will print: 2022-01-28 00:00:00
        except ValueError as e:
            print("Error:", e)
        
        processo = Processos(
            processo = "0600305-93.2022.8.04.6300",
            autor = "PORFIRIA ANEZIA CONCEICAO BARB",
            reu = "AMAZONAS DISTRIBUIDORA DE ENERGIA S.A",
            status = "ARQUIVADO",
            distribuicao_data = date_obj,
            valor_causa = "21000.00"  
        )
        
        db.session.add(processo)
        
    db.session.commit()