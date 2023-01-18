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
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(270, 50, 601, 61))
        self.label_2.setStyleSheet("color:rgb(177, 177, 177);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 1131, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#000")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setIndent(1)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(50, 570, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color:rgb(79, 200, 255);\n"
                                      "color:#fff;\n"
                                      "font-weight:bold;\n"
                                      "border:5 px solid #eee;\n"
                                      "border-radius: 8px")
        self.pushButton.setCheckable(True)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 510, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#888")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 510, 181, 41))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color:rgb(79, 200, 255);\n"
                                        "color:#fff;\n"
                                        "font-weight:bold;\n"
                                        "border-radius: 5px;\n"
                                        "border:5 px solid #eee")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.upload)

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(740, 540, 200, 41))
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(50, 120, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:#888")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.hide()
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(50, 170, 391, 321))
        self.label_7.setStyleSheet("color:#888;")
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(230, 460, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(50, 460, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#888")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(50, 460, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:#888")
        self.label_9.setObjectName("label_9")
        self.label_7.hide()
        self.label_9.hide()
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(180, 460, 151, 31))
        self.label_10.setStyleSheet("color:#888;")
        self.label_10.setObjectName("label_10")
        self.label_10.setFont(font)
        self.label_10.hide()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#999")
        self.label_5.setAlignment(QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 420, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(50, 420, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:#888")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(50, 380, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color:#888")
        self.label_12.setObjectName("label_12")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 380, 181, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 340, 181, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(50, 340, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color:#888")
        self.label_13.setObjectName("label_13")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calcule de plus court chemin"))
        self.label_2.setText(_translate("Dialog",
                                        "L\'objectif du projet est de développer une application avec python permettant d’utiliser les algorithmes\n"
                                        "génétiques pour trouver la distance minimale du chemin effectué par le bus du ramassage scolaire."))
        self.label.setText(_translate("Dialog", "Projet Final"))
        self.pushButton.setText(_translate("Dialog", "Calculer le PCC"))
        self.label_3.setText(_translate("Dialog", "Upload le Dataset :"))
        self.pushButton_2.setText(_translate("Dialog", "Upload"))
        self.label_5.setText(_translate("Dialog", ""))
        self.label_6.setText(_translate("Dialog", ""))
        self.label_7.setText(_translate("Dialog", ""))
        self.lineEdit.setText('0.3')
        self.lineEdit_2.setText('500')
        self.lineEdit_3.setText('100')
        self.lineEdit_4.setText('10')
        self.label_8.setText(_translate("Dialog", "Taux de coisement:"))
        self.label_9.setText(_translate("Dialog", ""))
        self.label_10.setText(_translate("Dialog", ""))
        self.label_11.setText(_translate("Dialog", "nombre d\'iteration"))
        self.label_12.setText(_translate("Dialog", "Population"))
        self.label_13.setText(_translate("Dialog", "Le nombre d\'eleves"))
        coordinate = (37.8199286, -122.4782551)
        self.m = folium.Map(
            location=[48.8867, 2.3245], zoom_start=12
        )
        # save map data to data object
        self.webView = QWebEngineView(self.frame)
        self.webView.setHtml(self.m.get_root().render())
        self.webView.setGeometry(QtCore.QRect(520, 160, 501, 361))

    def upload(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self.frame, 'select dataset', '.', 'csv files(*.csv)')
        if fname:
            self.fname = str(fname[0])
            self.pushButton.setEnabled(True)
            self.pushButton.clicked.connect(self.main)
            print(self.fname)
    #verifier si s est un numbre
    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    def init_geo(self):
        # Initialiser le géolocalisateur en utilisant l'email de l'utilisateur comme agent
        geolocator = geocoders.Nominatim(user_agent="mail@myserver.com")
        # Initialiser une liste pour stocker les coordonnées
        self.label_6.setText("Le Plus cours Chemin :")
        self.label_9.setText("La distance total : ")
        self.label_10.setText("0 Km")
        self.label_6.update()
        self.label_9.update()
        self.label_10.update()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.label_8.hide()
        self.label_11.hide()
        self.label_12.hide()
        self.label_13.hide()
        self.label_6.show()
        self.label_9.show()
        self.label_10.show()
        QtCore.QCoreApplication.processEvents()
        coordinates_list = []
        self.n_cities = 10
        self.n_population = 100
        self.mutation_rate = 0.3
        self.nombre_iteration = 500
        # traitement sur le mutation_rate
        if self.is_number(self.lineEdit.text()):
            self.mutation_rate = float(self.lineEdit.text())
        else:
            self.mutation_rate = 0.3
            self.lineEdit.setText('0.3')
            self.lineEdit.update()
        # traitement sur le n_cities 
        if self.is_number(self.lineEdit_4.text()):
            self.n_cities = int(self.lineEdit_4.text())
        else:
            self.n_cities = 10
            self.lineEdit_4.setText('10')
            self.lineEdit_4.update()
        # traitement sur le n_population  
        if self.is_number(self.lineEdit_3.text()):
            self.n_population = int(self.lineEdit_3.text())
        else:
            self.n_population = 100
            self.lineEdit_3.setText('100')
            self.lineEdit_3.update()
            
        if self.is_number(self.lineEdit_2.text()):
            self.nombre_iteration = int(self.lineEdit_2.text())
        else:
            self.nombre_iteration = 500
            self.lineEdit_2.setText('500')
            self.lineEdit_2.update()
            QtCore.QCoreApplication.processEvents()
        df = pd.read_csv(self.fname)
        df = df.sample(frac=1, random_state=1).reset_index()
        # Récupérer la liste des noms de villes à partir d'un dataframe
        self.df = df[['Street', 'Full Name']].head(self.n_cities)
        self.names_list = np.array(self.df['Street'])
        # Boucler sur toutes les villes pour récupérer les coordonnées
        for city in self.names_list:
            location = geolocator.geocode(city)
            coordinates_list.append(list((location.latitude, location.longitude)))
        # Créer un dictionnaire pour stocker les noms de villes et les coordonnées
        self.cities_dict = {x: y for x, y in zip(self.names_list, coordinates_list)}
        self.names = {x: y for x, y in zip(self.df['Street'] , self.df['Full Name'])}
        self.distances ={}
        self.create_distance_dict()
        print(self.names)
    # Fonction pour calculer la distance entre deux points
    def create_distance_dict(self):
        for point1, coord1 in self.cities_dict.items():
            h3_coord1 = h3.geo_to_h3(coord1[0], coord1[1], 9)
            for point2, coord2 in self.cities_dict.items():
                if point1 != point2:
                    h3_coord2 = h3.geo_to_h3(coord2[0], coord2[1], 9)
                    distance = h3.h3_distance(h3_coord1, h3_coord2)
                    self.distances[(point1, point2)] = distance

    @functools.lru_cache(maxsize=None)
    def compute_city_distance_names(self, city_a, city_b):
        return self.distances[(city_a, city_b)]


    def genesis(self, city_list, n_population):
        # Initialiser une liste vide pour stocker les solutions générées
        population_set = []
        # Itérer à travers le nombre de population spécifié
        for i in range(n_population):
            # Génération aléatoire d'une nouvelle solution
            sol_i = city_list[np.random.choice(list(range(self.n_cities)), self.n_cities, replace=False)]
            population_set.append(sol_i)
        return np.array(population_set)

    def fitness_eval(self,city_list):
        # Initialiser une variable pour stocker la distance totale
        total = 0
        # Itérer à travers les villes dans la liste sauf la dernière
        for i in range(self.n_cities - 1):
            # Récupérer la ville actuelle et la prochaine
            a = city_list[i]
            b = city_list[i + 1]
            # Ajouter la distance entre les deux villes au total
            total += self.compute_city_distance_names(a, b)
        # Retourner la distance totale
        return total

    def get_all_fitnes(self, population_set, cities_dict):
        # Initialiser une liste pour stocker les valeurs de fitness
        fitnes_list = np.zeros(self.n_population)

        # Boucler sur toutes les solutions en calculant le fitness pour chaque solution
        for i in range(self.n_population):
            fitnes_list[i] = self.fitness_eval(population_set[i])

        # retourner la liste des fitness
        return fitnes_list



    def progenitor_selection(self, population_set, fitnes_list):
        # calculer la somme de tous les fitness
        total_fit = fitnes_list.sum()
        # calculer la probabilité pour chaque solution
        prob_list = fitnes_list / total_fit

        # Il y a une chance qu'un progéniteur s'accouple avec soi-même
        progenitor_list_a = np.random.choice(list(range(len(population_set))), len(population_set), p=prob_list,
                                             replace=True)
        progenitor_list_b = np.random.choice(list(range(len(population_set))), len(population_set), p=prob_list,
                                             replace=True)

        # selectionner les solutions progénitrices
        progenitor_list_a = population_set[progenitor_list_a]
        progenitor_list_b = population_set[progenitor_list_b]

        # retourner la liste des progénitrices
        return np.array([progenitor_list_a, progenitor_list_b])

    def mate_progenitors(self, prog_a, prog_b):
        # prendre les 5 premières villes de la solution progénitrice A
        offspring = prog_a[0:5]
        # Pour chaque ville de la solution progénitrice B
        for city in prog_b:
            # Si la ville n'est pas dans la descendance
            if not city in offspring:
                # Ajouter la ville à la descendance
                offspring = np.concatenate((offspring, [city]))

        # retourner la descendance
        return offspring

    def mate_population(self, progenitor_list):
        # Initialiser une liste pour stocker la nouvelle population
        new_population_set = []
        # Boucler sur toutes les solutions progénitrices
        for i in range(progenitor_list.shape[1]):
            # Récupérer les solutions progénitrices
            prog_a, prog_b = progenitor_list[0][i], progenitor_list[1][i]
            # Générer la descendance
            offspring = self.mate_progenitors(prog_a, prog_b)
            # Ajouter la descendance à la nouvelle population
            new_population_set.append(offspring)
        # retourner la nouvelle population
        return new_population_set

    def mutate_offspring(self, offspring):
        # Boucler sur un certain nombre de positions, déterminé par le taux de mutation
        for q in range(int(self.n_cities * self.mutation_rate)):
            # choisir aléatoirement deux positions
            a = np.random.randint(0, self.n_cities)
            b = np.random.randint(0, self.n_cities)

            # Echanger les villes à ces positions
            offspring[a], offspring[b] = offspring[b], offspring[a]

        # retourner l'enfant muté
        return offspring

    def mutate_population(self, new_population_set):
        # Initialiser une liste pour stocker la population mutée
        mutated_pop = []
        # Boucler sur tous les enfants
        for offspring in new_population_set:
            # Appliquer la mutation à chaque enfant
            mutated_pop.append(self.mutate_offspring(offspring))
        # retourner la population mutée
        return mutated_pop

    def plot_map(self):
        if self.iteration != 0:
            self.label_5.setText(f"iteration numero {self.iteration * 100}")

        self.label_10.setText(f"{round(self.best_solution[1], 3)} Km")
        str_fin = ''
        for ix,el in enumerate(self.best_road):
            str_fin += f'{ix+1}- {self.names[el]}, '
            if (ix+1)%2==0:
                str_fin += '\n'
        self.label_7.setText(str_fin)
        self.label_10.update()
        self.label_7.update()
        self.label_5.update()
        self.label_7.show()
        QtCore.QCoreApplication.processEvents()
        time.sleep(1)

    def main(self):

        import time
        import sys

        start_time = time.time()
        self.init_geo()
        population_set = self.genesis(self.names_list, self.n_population)
        fitnes_list = self.get_all_fitnes(population_set, self.cities_dict)
        progenitor_list = self.progenitor_selection(population_set, fitnes_list)
        new_population_set = self.mate_population(progenitor_list)
        mutated_pop = self.mutate_population(new_population_set)
        self.best_solution = [-1, np.inf, np.array([])]
        self.iteration = 0
        for i in range(self.nombre_iteration):
            # Saving the best solution
            if fitnes_list.min() < self.best_solution[1]:
                self.best_solution[0] = i
                self.best_solution[1] = fitnes_list.min()
                self.best_solution[2] = np.array(mutated_pop)[fitnes_list.min() == fitnes_list]
            progenitor_list = self.progenitor_selection(population_set, fitnes_list)
            new_population_set = self.mate_population(progenitor_list)
            mutated_pop = self.mutate_population(new_population_set)
            self.best_road = self.best_solution[2][0]
            if i % 100 == 0:
                self.iteration += 1
                print(i, fitnes_list.min(), fitnes_list.mean(), datetime.now().strftime("%d/%m/%y %H:%M"))
                self.plot_map()
            fitnes_list = self.get_all_fitnes(mutated_pop, self.cities_dict)

        self.m.location = self.cities_dict[self.best_road[0]]
        end_time = time.time()
        execution_time = end_time - start_time
        print("Execution time: ", execution_time)
        loc = []
        for el in self.best_road:

            loc.append(self.cities_dict[el])
            folium.Marker(
                self.cities_dict[el], popup=f"<i>{el}</i>").add_to(self.m)
        #loc.append(self.cities_dict[self.best_road[0]])
        folium.PolyLine(loc,
                        color='blue',
                        weight=4,
                        opacity=0.9).add_to(self.m)
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
