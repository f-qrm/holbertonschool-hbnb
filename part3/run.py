from app import create_app
from app.services import facade

def init_admin():
    admin_data = {
        "email": "admin@example.com",
        "first_name": "Admin",
        "last_name": "User",
        "password": "adminpass",  # mot de passe en clair, sera hashé dans create_user
        "is_admin": True
    }

    existing_admin = facade.get_user_by_email(admin_data["email"])
    if existing_admin:
        print(f"Admin user already exists: {existing_admin.email}")
    else:
        try:
            admin_user = facade.create_user(admin_data)
            if not getattr(admin_user, "is_admin", False):
                admin_user.is_admin = True
                facade.put_user(admin_user.id, {"is_admin": True})
            print(f"Admin user created: {admin_user.email}")
        except Exception as e:
            print(f"Error creating admin user: {e}")

app = create_app()

if __name__ == '__main__':
    init_admin()  # <-- ici on crée l'admin avant de lancer le serveur
    app.run(debug=True)
