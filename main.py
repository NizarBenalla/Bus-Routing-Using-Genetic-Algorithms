import functools
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine
import sys
import numpy as np
import pandas as pd
from geopy import geocoders
import folium
from datetime import datetime
import time
import h3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Calcule de plus court chemin")
        Dialog.resize(1131, 678)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1131, 681))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.description = QtWidgets.QLabel(self.frame)
        self.description.setGeometry(QtCore.QRect(270, 50, 601, 61))
        self.description.setStyleSheet("color:rgb(177, 177, 177);")
        self.description.setObjectName("description")
        self.project_title = QtWidgets.QLabel(self.frame)
        self.project_title.setEnabled(True)
        self.project_title.setGeometry(QtCore.QRect(0, 0, 1131, 61))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.project_title.sizePolicy().hasHeightForWidth()
        )
        self.project_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.project_title.setFont(font)
        self.project_title.setStyleSheet("color:#000")
        self.project_title.setAlignment(QtCore.Qt.AlignCenter)
        self.project_title.setWordWrap(False)
        self.project_title.setIndent(1)
        self.project_title.setObjectName("label")
        self.calculate_button = QtWidgets.QPushButton(self.frame)
        self.calculate_button.setGeometry(QtCore.QRect(50, 570, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.calculate_button.setFont(font)
        self.calculate_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculate_button.setAutoFillBackground(False)
        self.calculate_button.setStyleSheet(
            "background-color:rgb(79, 200, 255);\n"
            "color:#fff;\n"
            "font-weight:bold;\n"
            "border:5 px solid #eee;\n"
            "border-radius: 8px"
        )
        self.calculate_button.setCheckable(True)
        self.calculate_button.setDefault(True)
        self.calculate_button.setObjectName("pushButton")
        self.calculate_button.setEnabled(False)
        self.project_title_3 = QtWidgets.QLabel(self.frame)
        self.project_title_3.setGeometry(QtCore.QRect(50, 510, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.project_title_3.setFont(font)
        self.project_title_3.setStyleSheet("color:#888")
        self.project_title_3.setObjectName("label_3")
        self.upload_btn = QtWidgets.QPushButton(self.frame)
        self.upload_btn.setGeometry(QtCore.QRect(230, 510, 181, 41))
        self.upload_btn.setAutoFillBackground(False)
        self.upload_btn.setStyleSheet(
            "background-color:rgb(79, 200, 255);\n"
            "color:#fff;\n"
            "font-weight:bold;\n"
            "border-radius: 5px;\n"
            "border:5 px solid #eee"
        )
        self.upload_btn.setObjectName("upload_btn")
        self.upload_btn.clicked.connect(self.upload)

        self.accumulated_nbr_iteration_label = QtWidgets.QLabel(self.frame)
        self.accumulated_nbr_iteration_label.setGeometry(
            QtCore.QRect(740, 540, 200, 41)
        )
        self.result_title = QtWidgets.QLabel(self.frame)
        self.result_title.setGeometry(QtCore.QRect(50, 120, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.result_title.setFont(font)
        self.result_title.setStyleSheet("color:#888")
        self.result_title.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.result_title.setObjectName("result_title")
        self.result_title.hide()
        self.result_label = QtWidgets.QLabel(self.frame)
        self.result_label.setGeometry(QtCore.QRect(50, 170, 391, 321))
        self.result_label.setStyleSheet("color:#888;")
        self.result_label.setObjectName("result_label")
        self.taux_croisement_entry = QtWidgets.QLineEdit(self.frame)
        self.taux_croisement_entry.setGeometry(QtCore.QRect(230, 460, 181, 31))
        self.taux_croisement_entry.setObjectName("lineEdit")
        self.taux_croisement_label = QtWidgets.QLabel(self.frame)
        self.taux_croisement_label.setGeometry(QtCore.QRect(50, 460, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.taux_croisement_label.setFont(font)
        self.taux_croisement_label.setStyleSheet("color:#888")
        self.taux_croisement_label.setObjectName("taux_croisement_label")
        self.tatal_distance_label = QtWidgets.QLabel(self.frame)
        self.tatal_distance_label.setGeometry(QtCore.QRect(50, 460, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.tatal_distance_label.setFont(font)
        self.tatal_distance_label.setStyleSheet("color:#888")
        self.tatal_distance_label.setObjectName("tatal_distance_label")
        self.result_label.hide()
        self.tatal_distance_label.hide()
        self.total_distance_value = QtWidgets.QLabel(self.frame)
        self.total_distance_value.setGeometry(QtCore.QRect(180, 460, 151, 31))
        self.total_distance_value.setStyleSheet("color:#888;")
        self.total_distance_value.setObjectName("total_distance_value")
        self.total_distance_value.setFont(font)
        self.total_distance_value.hide()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.accumulated_nbr_iteration_label.setFont(font)
        self.accumulated_nbr_iteration_label.setStyleSheet("color:#999")
        self.accumulated_nbr_iteration_label.setAlignment(QtCore.Qt.AlignLeft)
        self.accumulated_nbr_iteration_label.setObjectName(
            "accumulated_nbr_iteration_label"
        )
        self.accumulated_nbr_iteration_entry = QtWidgets.QLineEdit(self.frame)
        self.accumulated_nbr_iteration_entry.setGeometry(
            QtCore.QRect(230, 420, 181, 31)
        )
        self.accumulated_nbr_iteration_entry.setObjectName(
            "accumulated_nbr_iteration_entry"
        )
        self.nbr_iteration_entry = QtWidgets.QLabel(self.frame)
        self.nbr_iteration_entry.setGeometry(QtCore.QRect(50, 420, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.nbr_iteration_entry.setFont(font)
        self.nbr_iteration_entry.setStyleSheet("color:#888")
        self.nbr_iteration_entry.setObjectName("nbr_iteration_entry")
        self.population_label = QtWidgets.QLabel(self.frame)
        self.population_label.setGeometry(QtCore.QRect(50, 380, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.population_label.setFont(font)
        self.population_label.setStyleSheet("color:#888")
        self.population_label.setObjectName("population_label")
        self.population_entry = QtWidgets.QLineEdit(self.frame)
        self.population_entry.setGeometry(QtCore.QRect(230, 380, 181, 31))
        self.population_entry.setObjectName("population_entry")
        self.nbr_eleve_entry = QtWidgets.QLineEdit(self.frame)
        self.nbr_eleve_entry.setGeometry(QtCore.QRect(230, 340, 181, 31))
        self.nbr_eleve_entry.setObjectName("nbr_eleve_entry")
        self.nbr_eleve_label = QtWidgets.QLabel(self.frame)
        self.nbr_eleve_label.setGeometry(QtCore.QRect(50, 340, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.nbr_eleve_label.setFont(font)
        self.nbr_eleve_label.setStyleSheet("color:#888")
        self.nbr_eleve_label.setObjectName("nbr_eleve_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calcule de plus court chemin"))
        self.description.setText(
            _translate(
                "Dialog",
                "L'objectif du projet est de développer une application avec python permettant d’utiliser les algorithmes\n"
                "génétiques pour trouver la distance minimale du chemin effectué par le bus du ramassage scolaire.",
            )
        )
        self.project_title.setText(_translate("Dialog", "Projet Final"))
        self.calculate_button.setText(_translate("Dialog", "Calculer le PCC"))
        self.project_title_3.setText(_translate("Dialog", "Upload le Dataset :"))
        self.upload_btn.setText(_translate("Dialog", "Upload"))
        self.accumulated_nbr_iteration_label.setText(_translate("Dialog", ""))
        self.result_title.setText(_translate("Dialog", ""))
        self.result_label.setText(_translate("Dialog", ""))
        self.taux_croisement_entry.setText("0.3")
        self.accumulated_nbr_iteration_entry.setText("500")
        self.population_entry.setText("100")
        self.nbr_eleve_entry.setText("10")
        self.taux_croisement_label.setText(_translate("Dialog", "Taux de coisement:"))
        self.tatal_distance_label.setText(_translate("Dialog", ""))
        self.total_distance_value.setText(_translate("Dialog", ""))
        self.nbr_iteration_entry.setText(_translate("Dialog", "nombre d'iteration"))
        self.population_label.setText(_translate("Dialog", "Population"))
        self.nbr_eleve_label.setText(_translate("Dialog", "Le nombre d'eleves"))
        coordinate = (37.8199286, -122.4782551)
        self.m = folium.Map(location=[48.8867, 2.3245], zoom_start=12)
        # save map data to data object
        self.webView = QWebEngineView(self.frame)
        self.webView.setHtml(self.m.get_root().render())
        self.webView.setGeometry(QtCore.QRect(520, 160, 501, 361))

    def upload(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(
            self.frame, "select dataset", ".", "csv files(*.csv)"
        )
        if fname:
            self.fname = str(fname[0])
            self.calculate_button.setEnabled(True)
            self.calculate_button.clicked.connect(self.main)
            print(self.fname)

    # verifier si s est un numbre
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def init_geo(self):
        self.start_time = time.time()
        # Initialiser le géolocalisateur en utilisant l'email de l'utilisateur comme agent
        geolocator = geocoders.Nominatim(user_agent="mail@myserver.com")
        # Initialiser une liste pour stocker les coordonnées
        self.result_title.setText("Le Plus cours Chemin :")
        self.tatal_distance_label.setText("La distance total : ")
        self.total_distance_value.setText("0 Km")
        self.result_title.update()
        self.tatal_distance_label.update()
        self.total_distance_value.update()
        self.taux_croisement_entry.hide()
        self.accumulated_nbr_iteration_entry.hide()
        self.population_entry.hide()
        self.nbr_eleve_entry.hide()
        self.taux_croisement_label.hide()
        self.nbr_iteration_entry.hide()
        self.population_label.hide()
        self.nbr_eleve_label.hide()
        self.result_title.show()
        self.tatal_distance_label.show()
        self.total_distance_value.show()
        QtCore.QCoreApplication.processEvents()
        coordinates_list = []
        self.nbr_ville = 10
        self.n_population = 100
        self.mutation_rate = 0.3
        self.nombre_iteration = 500
        # traitement sur le mutation_rate
        if self.is_number(self.taux_croisement_entry.text()):
            self.mutation_rate = float(self.taux_croisement_entry.text())
        else:
            self.mutation_rate = 0.3
            self.taux_croisement_entry.setText("0.3")
            self.taux_croisement_entry.update()
        # traitement sur le n_cities
        if self.is_number(self.nbr_eleve_entry.text()):
            self.nbr_ville = int(self.nbr_eleve_entry.text())
        else:
            self.nbr_ville = 10
            self.nbr_eleve_entry.setText("10")
            self.nbr_eleve_entry.update()
        # traitement sur le n_population
        if self.is_number(self.population_entry.text()):
            self.n_population = int(self.population_entry.text())
        else:
            self.n_population = 100
            self.population_entry.setText("100")
            self.population_entry.update()

        if self.is_number(self.accumulated_nbr_iteration_entry.text()):
            self.nombre_iteration = int(self.accumulated_nbr_iteration_entry.text())
        else:
            self.nombre_iteration = 500
            self.accumulated_nbr_iteration_entry.setText("500")
            self.accumulated_nbr_iteration_entry.update()
            QtCore.QCoreApplication.processEvents()
        df = pd.read_csv(self.fname)
        df = df.sample(frac=1, random_state=1).reset_index()
        # Récupérer la liste des noms de villes à partir d'un dataframe
        self.df = df[["Street", "Full Name"]].head(self.nbr_ville)
        self.names_list = np.array(self.df["Street"])
        # Boucler sur toutes les villes pour récupérer les coordonnées
        for ville in self.names_list:
            location = geolocator.geocode(ville)
            coordinates_list.append(list((location.latitude, location.longitude)))
        # Créer un dictionnaire pour stocker les noms de villes et les coordonnées
        self.dictionnaire_villes = {
            x: y for x, y in zip(self.names_list, coordinates_list)
        }
        self.names = {x: y for x, y in zip(self.df["Street"], self.df["Full Name"])}
        self.dict_distances = {}
        self.cree_dictionnaire_distances()
        print(self.names)

    # Fonction pour calculer la distance entre deux points
    def cree_dictionnaire_distances(self):
        for point1, coord1 in self.dictionnaire_villes.items():
            h3_coord1 = h3.geo_to_h3(coord1[0], coord1[1], 9)
            for point2, coord2 in self.dictionnaire_villes.items():
                if point1 != point2:
                    h3_coord2 = h3.geo_to_h3(coord2[0], coord2[1], 9)
                    distance = h3.h3_distance(h3_coord1, h3_coord2)
                    self.dict_distances[(point1, point2)] = distance

    def calculer_distance_villes(self, city_a, city_b):
        return self.dict_distances[(city_a, city_b)]

    def genesis(self, city_list, n_population):
        # Initialiser une liste vide pour stocker les solutions générées
        population_set = []
        # Itérer à travers le nombre de population spécifié
        for i in range(n_population):
            # Génération aléatoire d'une nouvelle solution
            sol_i = city_list[
                np.random.choice(
                    list(range(self.nbr_ville)), self.nbr_ville, replace=False
                )
            ]
            population_set.append(sol_i)
        return np.array(population_set)

    def evaluer_fitness(self, city_list):
        # Initialiser une variable pour stocker la distance totale
        total = 0
        # Itérer à travers les villes dans la liste sauf la dernière
        for i in range(self.nbr_ville - 1):
            # Récupérer la ville actuelle et la prochaine
            a = city_list[i]
            b = city_list[i + 1]
            # Ajouter la distance entre les deux villes au total
            total += self.calculer_distance_villes(a, b)
        # Retourner la distance totale
        return total

    def get_all_fitnes(self, population_set, cities_dict):
        # Initialiser une liste pour stocker les valeurs de fitness
        fitness_liste = np.zeros(self.n_population)

        # Boucler sur toutes les solutions en calculant le fitness pour chaque solution
        for i in range(self.n_population):
            fitness_liste[i] = self.evaluer_fitness(population_set[i])

        # retourner la liste des fitness
        return fitness_liste

    def progenitor_selection(self, population_set, fitness_liste):
        # calculer la somme de tous les fitness
        total_fit = fitness_liste.sum()
        # calculer la probabilité pour chaque solution
        prob_list = fitness_liste / total_fit

        # Il y a une chance qu'un progéniteur s'accouple avec soi-même
        géniteurs_liste_a = np.random.choice(
            list(range(len(population_set))),
            len(population_set),
            p=prob_list,
            replace=True,
        )
        géniteurs_liste_b = np.random.choice(
            list(range(len(population_set))),
            len(population_set),
            p=prob_list,
            replace=True,
        )

        # selectionner les solutions progénitrices
        géniteurs_liste_a = population_set[géniteurs_liste_a]
        géniteurs_liste_b = population_set[géniteurs_liste_b]

        # retourner la liste des progénitrices
        return np.array([géniteurs_liste_a, géniteurs_liste_b])

    def mate_progenitors(self, prog_a, prog_b):
        # prendre les 5 premières villes de la solution progénitrice A
        offspring = prog_a[0:5]
        # Pour chaque ville de la solution progénitrice B
        for ville in prog_b:
            # Si la ville n'est pas dans la descendance
            if not ville in offspring:
                # Ajouter la ville à la descendance
                offspring = np.concatenate((offspring, [ville]))

        # retourner la descendance
        return offspring

    def mate_population(self, géniteurs_liste):
        # Initialiser une liste pour stocker la nouvelle population
        Nouvelle_population_etablie = []
        # Boucler sur toutes les solutions progénitrices
        for i in range(géniteurs_liste.shape[1]):
            # Récupérer les solutions progénitrices
            prog_a, prog_b = géniteurs_liste[0][i], géniteurs_liste[1][i]
            # Générer la descendance
            offspring = self.mate_progenitors(prog_a, prog_b)
            # Ajouter la descendance à la nouvelle population
            Nouvelle_population_etablie.append(offspring)
        # retourner la nouvelle population
        return Nouvelle_population_etablie

    def mutate_offspring(self, offspring):
        # Boucler sur un certain nombre de positions, déterminé par le taux de mutation
        for q in range(int(self.nbr_ville * self.mutation_rate)):
            # choisir aléatoirement deux positions
            a = np.random.randint(0, self.nbr_ville)
            b = np.random.randint(0, self.nbr_ville)

            # Echanger les villes à ces positions
            offspring[a], offspring[b] = offspring[b], offspring[a]

        # retourner l'enfant muté
        return offspring

    def mutate_population(self, Nouvelle_population_etablie):
        # Initialiser une liste pour stocker la population mutée
        mutated_pop = []
        # Boucler sur tous les enfants
        for offspring in Nouvelle_population_etablie:
            # Appliquer la mutation à chaque enfant
            mutated_pop.append(self.mutate_offspring(offspring))
        # retourner la population mutée
        return mutated_pop

    def plot_map(self):
        if self.iteration != 0:
            self.accumulated_nbr_iteration_label.setText(
                f"iteration numero {self.iteration * 100}"
            )

        self.total_distance_value.setText(f"{round(self.meilleur_solution[1], 3)} Km")
        str_fin = ""
        for ix, el in enumerate(self.plus_court_chemin):
            str_fin += f"{ix+1}- {self.names[el]}, "
            if (ix + 1) % 2 == 0:
                str_fin += "\n"
        self.result_label.setText(str_fin)
        self.total_distance_value.update()
        self.result_label.update()
        self.accumulated_nbr_iteration_label.update()
        self.result_label.show()
        QtCore.QCoreApplication.processEvents()
        time.sleep(1)

    def main(self):
        self.init_geo()
        population_set = self.genesis(self.names_list, self.n_population)
        fitness_liste = self.get_all_fitnes(population_set, self.dictionnaire_villes)
        géniteurs_liste = self.progenitor_selection(population_set, fitness_liste)
        Nouvelle_population_etablie = self.mate_population(géniteurs_liste)
        mutated_pop = self.mutate_population(Nouvelle_population_etablie)
        self.meilleur_solution = [-1, np.inf, np.array([])]
        self.iteration = 0
        for i in range(self.nombre_iteration):
            # Saving the best solution
            if fitness_liste.min() < self.meilleur_solution[1]:
                self.meilleur_solution[0] = i
                self.meilleur_solution[1] = fitness_liste.min()
                self.meilleur_solution[2] = np.array(mutated_pop)[
                    fitness_liste.min() == fitness_liste
                ]
            géniteurs_liste = self.progenitor_selection(population_set, fitness_liste)
            Nouvelle_population_etablie = self.mate_population(géniteurs_liste)
            mutated_pop = self.mutate_population(Nouvelle_population_etablie)
            self.plus_court_chemin = self.meilleur_solution[2][0]
            if i % 100 == 0:
                self.iteration += 1
                print(
                    i,
                    fitness_liste.min(),
                    fitness_liste.mean(),
                    datetime.now().strftime("%d/%m/%y %H:%M"),
                )
                self.plot_map()
            fitness_liste = self.get_all_fitnes(mutated_pop, self.dictionnaire_villes)

        self.m.location = self.dictionnaire_villes[self.plus_court_chemin[0]]
        end_time = time.time()
        execution_time = end_time - self.start_time
        self.accumulated_nbr_iteration_label.setText(
            f"Executer en {round(execution_time,2)}s"
        )
        location_finale = []
        for el in self.plus_court_chemin:

            location_finale.append(self.dictionnaire_villes[el])
            folium.Marker(self.dictionnaire_villes[el], popup=f"<i>{el}</i>").add_to(
                self.m
            )
        # location_finale.append(self.dictionnaire_villes[self.plus_court_chemin[0]])
        folium.PolyLine(location_finale, color="blue", weight=4, opacity=0.9).add_to(
            self.m
        )
        self.webView.setHtml(self.m.get_root().render())
        self.webView.update()
        QtCore.QCoreApplication.processEvents()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())