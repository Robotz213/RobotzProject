# from app import app
# from app import db


# with app.app_context():

#     db.create_all()
#     root = Users.query.filter_by(login = 'nicholas@robotz.dev').first()
    
#     if root is None:
        
#         root_license = "55eb3f3d94c530373c9bfc5d035050eb5e4e36c125bfafb5d4c7216a688f93859c9dfe705f1b644d5b510d67df108539172f16e88cf8f67f5f9a635b42cfca08"
#         usuario = Users(
#                     login = 'nicholas@robotz.dev',
#                     nome_usuario = "Nicholas Silva",
#                     senhacrip = "12345678",
#                     email = 'nicholas@robotz.dev',
#                     type_user = "super_admin",
#                     license_key = root_license)
        
#         db.session.add(usuario)
#         db.session.commit()