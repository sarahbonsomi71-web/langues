 Validation des champs (champs vides)
 Ici :
if fr == "" or en == "":
    messagebox.showwarning("Attention", "Remplir les deux champs")
    return
Gestion d’erreur lors de l’insertion (mot déjà existant)
 Ici :
try:
    cursor.execute("INSERT INTO dictionnaire VALUES (?, ?)", (fr, en))
    conn.commit()
    messagebox.showinfo("Succès", "Mot ajouté !")
    entree_fr.delete(0, tk.END)
    entree_en.delete(0, tk.END)
except:
    messagebox.showerror("Erreur", "Mot déjà existant")
Gestion du cas "mot non trouvé"
 Ici :       
if resultat:
    label_resultat.config(text=resultat[0])
else:
    label_resultat.config(text="Mot non trouvé")
