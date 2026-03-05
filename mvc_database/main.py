from models.database import Database
from view.atm_view import ATMView

db = Database()
db.setup_database()

view = ATMView()
view.run()