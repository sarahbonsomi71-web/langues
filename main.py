Try :
        Cursor.execute(« INSERT INTO dictionnaire VALUES ( ?, ?) », (fr, en))
        Conn.commit()
        Messagebox.showinfo(« Succès », « Mot ajouté ! »)
        Entree_fr.delete(0, tk.END)
        Entree_en.delete(0, tk.END)
    Except :
        Messagebox.showerror(« Erreur », « Mot déjà existant »)

