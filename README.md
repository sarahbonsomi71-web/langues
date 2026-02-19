import tkinter as tk
from tkinter import messagebox
import sqlite3
# Connexion base de données
conn = sqlite3.connect("traduction.db")
cursor = conn.cursor()

# Création table
cursor.execute("""
CREATE TABLE IF NOT EXISTS dictionnaire (
    francais TEXT PRIMARY KEY,
    anglais TEXT
)
""")

conn.commit()

# Fonction ajouter mot
def ajouter_mot():
    fr = entree_fr.get().lower()
    en = entree_en.get().lower()

    if fr == "" or en == "":
        messagebox.showwarning("Attention", "Remplir les deux champs")
        return

    try:
        cursor.execute("INSERT INTO dictionnaire VALUES (?, ?)", (fr, en))
        conn.commit()
        messagebox.showinfo("Succès", "Mot ajouté !")
        entree_fr.delete(0, tk.END)
        entree_en.delete(0, tk.END)
    except:
        messagebox.showerror("Erreur", "Mot déjà existant")

# Fonction traduire
def traduire():
    mot = zone_texte.get().lower()

    cursor.execute("SELECT anglais FROM dictionnaire WHERE francais=?", (mot,))
    resultat = cursor.fetchone()

    if resultat:
        label_resultat.config(text=resultat[0])
    else:
        label_resultat.config(text="Mot non trouvé")

# Fenêtre
app = tk.Tk()
app.title("Mon Traducteur Personnel")
app.geometry("500x400")
app.configure(bg="#0B3D91")

# Titre
tk.Label(app, text="Traducteur avec Base de Données",
         bg="#0B3D91", fg="yellow",
         font=("Arial", 16, "bold")).pack(pady=10)

# Ajouter mot
tk.Label(app, text="Français", bg="#0B3D91", fg="yellow").pack()
entree_fr = tk.Entry(app)
entree_fr.pack()

tk.Label(app, text="Anglais", bg="#0B3D91", fg="yellow").pack()
entree_en = tk.Entry(app)
entree_en.pack()

tk.Button(app, text="Ajouter",
          command=ajouter_mot,
          bg="yellow").pack(pady=5)

# Zone traduction
tk.Label(app, text="Mot à traduire",
         bg="#0B3D91", fg="yellow").pack(pady=10)

zone_texte = tk.Entry(app)
zone_texte.pack()

tk.Button(app, text="Traduire",
          command=traduire,
          bg="yellow").pack(pady=5)

label_resultat = tk.Label(app,
                          text="",
                          bg="#0B3D91",
                          fg="yellow",
                          font=("Arial", 14))
label_resultat.pack(pady=10)

app.mainloop()# langues
ce projet consiste à créer un traducteur(une application capable de traduire les mots français en anglais)
