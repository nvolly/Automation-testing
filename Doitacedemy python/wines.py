import sqlite3
def menu():
    menu = """Alegeti una din optiunile de mai jos:
            1. Vizualizati lista de vinuri;
            2. Adaugati un vin;
            3. Stergeti un vin;
            4. Vinuri per an;
            5. Vinuri per soi
    """
    option = input(menu)
    return option

def visualise_all():
    con = sqlite3.connect("my_wines.db")
    cursor = con.cursor()
    query = """SELECT * from wines;"""
    cursor.execute(query)
    data = cursor.fetchall()
    print("Avem disponibil:")
    for item in date:
        print(f"Din crama {item[0]}, soiul {item[1]}, din anul {item[2]} culoarea {item[3]}")
    con.close()
def add_wine():
    pass

#choice = menu()
visualise_all()