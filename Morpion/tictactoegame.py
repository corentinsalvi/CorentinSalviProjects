# -*- coding: iso-8859-15 -*-
# CrÃ©Ã© par cosalvi, le 01/04/2021 en Python 3.7

#--------------------#/Projet Jeu du Morpion\#-------------------------#


from tkinter import*
"""Définition des Variables Globales"""
tbl_grille=[[0,0,0],[0,0,0],[0,0,0]]
nbr_cases_pleines=0
nbr_clic=0
joueur=1
next_player=True
rep=False

def grille():
	"""La fonction grille() définit la grille de jeu à l'ouverture de la page"""
	cote=80
	for l in range (3):
		for c in range(3):
			carre=cnv_jeu.create_rectangle(30+l*cote,30+c*cote,110+l*cote,110+c*cote)

def initialisation():
	""""La fonction initialisation() permet de redéfinir la grille de
jeu ainsi que les variables globales. Elle communique aussi les label de départ"""
	global tbl_grille
	global joueur
	global nbr_clic
	global nbr_cases_pleines
	global cnv_jeu
	cote=80
	lbl_msg2['text']="Commencez à jouer"
	lbl_msg3['text']=" "
	tbl_grille=[[0,0,0],[0,0,0],[0,0,0]]
	joueur=1
	nbr_clic=0
	nbr_cases_pleines=0
	cnv_jeu.delete('all')
	grille()
	print("New Game")

def draw_cercle(x,y):
	"""La fonction cercle() est actionnée suivant les conditions de la fonction remplir_case().
	Elle permet de remplir la case selectionnée par un cercle aux bonnes dimensions"""
	global cnv_jeu
	r = 35
	color= 'orange'
	cnv_jeu.create_oval(x-r, y-r, x+r, y+r, outline=color, width=3.5)

def evaluation(tbl_grille,joueuractif):
	"""La fonction evaluation() permet d'évaluer la partie. Il teste à chaque nouvelle case
remplie si la partie est finie, donc si un joueur a gagné, si il ya eu égalité, ou si la partie est en cours.
Une fois la partie finie, la fonction va retourner des label de communication """
	global nbr_cases_pleines
	global rep
	a=int(tbl_grille[0][0])
	b=int(tbl_grille[0][1])
	c=int(tbl_grille[0][2])
	d=int(tbl_grille[1][0])
	e=int(tbl_grille[1][1])
	f=int(tbl_grille[1][2])
	g=int(tbl_grille[2][0])
	h=int(tbl_grille[2][1])
	i=int(tbl_grille[2][2])

	if (a, e, i)==(1,1,1) or (a, e, i)==(2,2,2):
		lbl_msg2['text']="Le joueur "+str(joueuractif)+" a gagné!"
		lbl_msg3['text']="Recommencez une partie"
		rep=True
	elif (g, e, c)==(1,1,1) or (g, e, c)==(2,2,2):
		lbl_msg2['text']="Le joueur "+str(joueuractif)+" a gagné!"
		lbl_msg3['text']="Recommencez une partie"
		rep=True
	elif (a, b, c)==(1,1,1) or (a, b, c)==(2,2,2):
		lbl_msg2['text']="Le joueur "+str(joueuractif)+" a gagné!"
		lbl_msg3['text']="Recommencez une partie"
		rep=True
	elif (d, e, f)==(1,1,1) or (d, e, f)==(2,2,2):
		lbl_msg2['text']="Le joueur "+str(joueuractif)+" a gagné!"
		lbl_msg3['text']="Recommencez une partie"
		rep=True
	elif (g, h, i)==(1,1,1) or (g, h, i)==(2,2,2):
		lbl_msg2['text']="Le joueur "+str(joueuractif)+" a gagné!"
		lbl_msg3['text']="Recommencez une partie"
		rep=True
	elif (a, d, g)==(1,1,1) or (a, d, g)==(2,2,2):
		lbl_msg2['text']="Le joueur "+str(joueuractif)+" a gagné!"
		lbl_msg3['text']="Recommencez une partie"
		rep=True
	elif (b, e, h)==(1,1,1) or (b, e, h)==(2,2,2):
		lbl_msg2['text']="Le joueur "+str(joueuractif)+" a gagné!"
		lbl_msg3['text']="Recommencez une partie"
		rep=True
	elif (c, f, i)==(1,1,1) or (c, f, i)==(2,2,2):
		lbl_msg2['text']="Le joueur "+str(joueuractif)+" a gagné!"
		lbl_msg3['text']="Recommencez une partie"
		rep=True
	elif nbr_cases_pleines==9 and rep==False :
		lbl_msg2['text']=" Egalité!"
		lbl_msg3['text']="Recommencez une partie !"
		rep=None
	return rep

def clicgauche(event):
	""""La fonction clicgauche est en interaction avec le clic gauche de la souris.
	Elle permettra de savoir si le clic concerné se trouve dans la grille de jeu,
	si la case cliquée est déjà occupée, quel joueur doit jouer.
	La fonction communique aussi des labels et fait appel à la fonction remplir_case() et evaluation()"""
	if rep==True:
		return
	else:
		global joueur
		global next_player
		global nbr_clic
		global Xsouris
		global Ysouris
		global nbr_cases_pleines
		Xsouris=event.x
		Ysouris=event.y
		if 30<Xsouris<270 and 30<Ysouris<270:
			nbr_clic+=1
			joueuractif=1
			if nbr_clic%2==0:
				joueuractif=2
			joueur=1
			if nbr_clic%2!=0:
				joueur=2
			remplir_case(Xsouris, Ysouris, joueuractif)
			nbr_cases_pleines+=1
			if evaluation(tbl_grille,joueuractif)==True:

				return
			if evaluation(tbl_grille,joueuractif)==None:
				return
			if not next_player:
				lbl_msg2['text']="La case est déjà occupée"
				nbr_clic-=1
				nbr_cases_pleines-=1
			else:
				lbl_msg2['text']="C'est au joueur "+ str(joueur)+" de jouer"
			print(Xsouris, Ysouris)
			print(nbr_cases_pleines)
		else:
			lbl_msg2['text']="Vous n'êtes pas sur la grille de jeu"



def remplir_case(a,b,joueuractif):
	"""La fonction remplir_case(), après chaque clic valide, va remplir la case concernée de tbl_grille avec le numéro du joueur ayant cliqué
	puis va dessiner une croix ou un rond dans la grille de jeu sur cnv_jeu """
	global tbl_grille
	global next_player
	global cnv_jeu
	if 30<a<110 and 30<b<110 and tbl_grille[0][0]==0:
		tbl_grille[0][0]=joueuractif
		next_player=True
		if joueuractif==1:
			cnv_jeu.create_line(35,35, 105,105, width=3.5, fill="red")
			cnv_jeu.create_line(35,105, 105,35, width=3.5, fill="red")
		else:
			centre_caseX=(35+105)//2
			centre_caseY=(35+105)//2
			draw_cercle(centre_caseX,centre_caseY)

	elif 30<a<110 and 110<b<190 and tbl_grille[1][0]==0:
		tbl_grille[1][0]=joueuractif
		next_player=True
		if joueuractif==1:
			cnv_jeu.create_line(35,115,105,185, width=3.5, fill="red")
			cnv_jeu.create_line(35,185,105,115, width=3.5, fill="red")
		else:
			centre_caseX=(35+105)//2
			centre_caseY=(115+185)//2
			draw_cercle(centre_caseX,centre_caseY)

	elif 30<a<110 and 190<b<270 and tbl_grille[2][0]==0:
		tbl_grille[2][0]=joueuractif
		next_player=True
		if joueuractif==1:
			cnv_jeu.create_line(35,195,105,265, width=3.5, fill="red")
			cnv_jeu.create_line(35,265,105,195, width=3.5, fill="red")
		else:
			centre_caseX=(35+105)//2
			centre_caseY=(195+265)//2
			draw_cercle(centre_caseX,centre_caseY)

	elif 110<a<190 and 30<b<110 and tbl_grille[0][1]==0:
		tbl_grille[0][1]=joueuractif
		next_player=True
		if joueuractif==1:
			cnv_jeu.create_line(115,35,185,105, width=3.5, fill="red")
			cnv_jeu.create_line(115,105,185,35, width=3.5, fill="red")
		else:
			centre_caseX=(115+185)//2
			centre_caseY=(35+105)//2
			draw_cercle(centre_caseX,centre_caseY)

	elif 110<a<190 and 110<b<190 and tbl_grille[1][1]==0:
		tbl_grille[1][1]=joueuractif
		next_player=True
		if joueuractif==1:
			cnv_jeu.create_line(115,115,185,185, width=3.5, fill="red")
			cnv_jeu.create_line(115,185,185,115, width=3.5, fill="red")
		else:
			centre_caseX=(115+185)//2
			centre_caseY=(115+185)//2
			draw_cercle(centre_caseX,centre_caseY)

	elif 110<a<190 and 190<b<270 and tbl_grille[2][1]==0:
		tbl_grille[2][1]=joueuractif
		next_player=True
		if joueuractif==1:
			cnv_jeu.create_line(115,195,185,265, width=3.5, fill="red")
			cnv_jeu.create_line(115,265,185,195, width=3.5, fill="red")
		else:
			centre_caseX=(115+185)//2
			centre_caseY=(195+265)//2
			draw_cercle(centre_caseX,centre_caseY)

	elif 190<a<270 and 30<b<110 and tbl_grille[0][2]==0:
		tbl_grille[0][2]=joueuractif
		next_player=True
		if joueuractif==1:
			cnv_jeu.create_line(195,35,265,105, width=3.5, fill="red")
			cnv_jeu.create_line(195,105,265,35, width=3.5, fill="red")
		else:
			centre_caseX=(195+265)//2
			centre_caseY=(35+105)//2
			draw_cercle(centre_caseX,centre_caseY)

	elif 190<a<270 and 110<b<190 and tbl_grille[1][2]==0:
		tbl_grille[1][2]=joueuractif
		next_player=True
		if joueuractif==1:
			cnv_jeu.create_line(195,115,265,185, width=3.5, fill="red")
			cnv_jeu.create_line(195,185,265,115, width=3.5, fill="red")
		else:
			centre_caseX=(195+265)//2
			centre_caseY=(115+185)//2
			draw_cercle(centre_caseX,centre_caseY)

	elif 190<a<270 and 190<b<270 and tbl_grille[2][2]==0:
		tbl_grille[2][2]=joueuractif
		next_player=True
		if joueuractif==1:
			cnv_jeu.create_line(195,195,265,265, width=3.5, fill="red")
			cnv_jeu.create_line(195,265,265,195, width=3.5, fill="red")
		else:
			centre_caseX=(195+265)//2
			centre_caseY=(195+265)//2
			draw_cercle(centre_caseX,centre_caseY)

	else:
		next_player=False
	print(tbl_grille)
	print(next_player)

#Fenetre
fn_principal=Tk()
fn_principal.title("Morpion")
fn_principal.geometry("450x450")

lbl_msg=Label(fn_principal,text="Morpion", font=("Arial",15), fg="black")

lbl_msg2=Label(fn_principal,text="Commencez à jouer", font=("Arial",15), fg="black")

lbl_msg3=Label(fn_principal,text=" ", font=("Arial",15), fg="black")

btn_quit=Button(fn_principal,text="Fermer",command=fn_principal.quit)

cnv_jeu=Canvas(fn_principal,width=300, height=300, bg='blue')

grille()

btn_reply=Button(fn_principal,text="Relancer",command=initialisation)

lbl_msg.pack()

cnv_jeu.pack()

lbl_msg2.pack()

lbl_msg3.pack()

btn_reply.pack(pady=10,padx=10, side=RIGHT)

btn_quit.pack(pady=10,padx=10, side=LEFT)

cnv_jeu.bind('<Button-1>',clicgauche)


fn_principal.mainloop()

