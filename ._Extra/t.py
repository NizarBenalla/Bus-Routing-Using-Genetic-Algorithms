from PyQt5 import QtCore, QtGui, QtWidgets , QtCore
from PyQt5.QtWebEngineWidgets import QWebEngineView # pip install PyQtWebEngine
import sys
import io
import numpy as np
import random
import pandas as pd
from geopy import distance,geocoders,Nominatim # to calculate distance on the surface
import folium
from datetime import datetime

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
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
"border:5 px solid #eee")
        self.pushButton.setCheckable(True)
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 470, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(113, 113, 113)")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 470, 181, 41))
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("background-color:rgb(79, 200, 255);\n"
"color:#fff;\n"
"font-weight:bold;\n"
"border:5 px solid #eee")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.upload)

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(740, 540, 200, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#999")
        self.label_5.setAlignment(QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "L\'objectif du projet est de développer une application avec python permettant d’utiliser les algorithmes\n"
"génétiques pour trouver la distance minimale du chemin effectué par le bus du ramassage scolaire."))
        self.label.setText(_translate("Dialog", "Final Projet"))
        self.pushButton.setText(_translate("Dialog", "Calculer le PCC"))
        self.label_3.setText(_translate("Dialog", "Upload le Dataset :"))
        self.pushButton_2.setText(_translate("Dialog", "Upload"))
        self.label_5.setText(_translate("Dialog", "1ere iteration"))
        coordinate = (37.8199286, -122.4782551)
        self.m = folium.Map(
            location=[53.073635, 8.806422], zoom_start=15, tiles='Stamen Terrain'
        )
        # save map data to data object
        data = io.BytesIO()
        self.m.save(data, close_file=False)

        self.webView = QWebEngineView(self.frame)
        self.webView.setHtml(data.getvalue().decode())
        self.webView.setGeometry(QtCore.QRect(520, 160, 501, 361))

    def upload(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self.frame,'select dataset','.','csv files(*.csv)')
        if fname:
            self.fname = str(fname[0])
            self.pushButton.setEnabled(True)
            self.pushButton.clicked.connect(self.main)
            print(self.fname)
    
    
    def init_geo(self):
            # Initialiser le géolocalisateur en utilisant l'email de l'utilisateur comme agent
        geolocator = geocoders.Nominatim(user_agent="mail@myserver.com")
        # Initialiser une liste pour stocker les coordonnées
        
        coordinates_list=[]
        self.n_cities = 10
        self.n_population = 50
        self.mutation_rate = 0.3
        df = pd.read_csv(self.fname)
        # Récupérer la liste des noms de villes à partir d'un dataframe
        self.names_list = np.array(df['Street'].head(self.n_cities))
        # Boucler sur toutes les villes pour récupérer les coordonnées
        for city in self.names_list:
            location = geolocator.geocode(city)
            coordinates_list.append(list((location.latitude, location.longitude)))
        # Créer un dictionnaire pour stocker les noms de villes et les coordonnées
        self.cities_dict = { x:y for x,y in zip(self.names_list,coordinates_list)}
        

    # Fonction pour calculer la distance entre deux points
    def compute_city_distance_coordinates(self,a,b):
        return distance.distance((a[0], a[1]), (b[0],b[1])).km

    # Fonction pour calculer la distance entre deux villes en utilisant les coordonnées stockées dans le dictionnaire
    def compute_city_distance_names(self,city_a, city_b, cities_dict):
        return self.compute_city_distance_coordinates(cities_dict[city_a], cities_dict[city_b])
    
    
    def genesis(self,city_list, n_population):
        # Initialiser une liste vide pour stocker les solutions générées
        population_set = []
        # Itérer à travers le nombre de population spécifié
        for i in range(n_population):
            # Génération aléatoire d'une nouvelle solution
            sol_i = city_list[np.random.choice(list(range(self.n_cities)), self.n_cities, replace=False)]
            population_set.append(sol_i)
        return np.array(population_set)
    
    
    def fitness_eval(self,city_list, cities_dict):
        # Initialiser une variable pour stocker la distance totale
        total = 0
        # Itérer à travers les villes dans la liste sauf la dernière
        for i in range(self.n_cities-1):
            # Récupérer la ville actuelle et la prochaine
            a = city_list[i]
            b = city_list[i+1]
            # Ajouter la distance entre les deux villes au total
            total += self.compute_city_distance_names(a,b, cities_dict)
        # Retourner la distance totale
        return total
    
    
    def get_all_fitnes(self,population_set, cities_dict):
        # Initialiser une liste pour stocker les valeurs de fitness
        fitnes_list = np.zeros(self.n_population)

        # Boucler sur toutes les solutions en calculant le fitness pour chaque solution
        for i in  range(self.n_population):
            fitnes_list[i] = self.fitness_eval(population_set[i], self.cities_dict)

        # retourner la liste des fitness
        return fitnes_list
    
    
    def progenitor_selection(self,population_set,fitnes_list):
        # calculer la somme de tous les fitness
        total_fit = fitnes_list.sum()
        # calculer la probabilité pour chaque solution
        prob_list = fitnes_list/total_fit

        # Il y a une chance qu'un progéniteur s'accouple avec soi-même
        progenitor_list_a = np.random.choice(list(range(len(population_set))), len(population_set),p=prob_list, replace=True)
        progenitor_list_b = np.random.choice(list(range(len(population_set))), len(population_set),p=prob_list, replace=True)

        # selectionner les solutions progénitrices
        progenitor_list_a = population_set[progenitor_list_a]
        progenitor_list_b = population_set[progenitor_list_b]

        # retourner la liste des progénitrices
        return np.array([progenitor_list_a,progenitor_list_b])
    
    
    def mate_progenitors(self,prog_a, prog_b):
        # prendre les 5 premières villes de la solution progénitrice A
        offspring = prog_a[0:5]

        # Pour chaque ville de la solution progénitrice B
        for city in prog_b:
            # Si la ville n'est pas dans la descendance
            if not city in offspring:
                # Ajouter la ville à la descendance
                offspring = np.concatenate((offspring,[city]))

        # retourner la descendance
        return offspring

    
    def mate_population(self,progenitor_list):
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


    def mutate_offspring(self,offspring):
        # Boucler sur un certain nombre de positions, déterminé par le taux de mutation
        for q in range(int(self.n_cities*self.mutation_rate)):
            # choisir aléatoirement deux positions
            a = np.random.randint(0,self.n_cities)
            b = np.random.randint(0,self.n_cities)

            # Echanger les villes à ces positions
            offspring[a], offspring[b] = offspring[b], offspring[a]

        # retourner l'enfant muté
        return offspring

    
    def mutate_population(self,new_population_set):
        # Initialiser une liste pour stocker la population mutée
        mutated_pop = []
        # Boucler sur tous les enfants
        for offspring in new_population_set:
            # Appliquer la mutation à chaque enfant
            mutated_pop.append(self.mutate_offspring(offspring))
        # retourner la population mutée
        return mutated_pop
    
    
    def plot_map(self):
        self.m = folium.Map(
            location=self.cities_dict[self.names_list[0]], zoom_start=15, tiles='Stamen Terrain'
        )
        loc = []
        for el in self.best_road:
            loc.append(self.cities_dict[el])
            folium.Marker(
              self.cities_dict[el], popup=f"<i>{el}</i>").add_to(self.m)
        loc.append(self.cities_dict[self.best_road[0]])
        # save map data to data object
        data = io.BytesIO()
        self.m.save(data, close_file=False)
        self.webView.setHtml(data.getvalue().decode())
        
        
    def main(self):
        self.init_geo();
        population_set = self.genesis(self.names_list, self.n_population)
        fitnes_list = self.get_all_fitnes(population_set,self.cities_dict)
        progenitor_list = self.progenitor_selection(population_set,fitnes_list)
        new_population_set = self.mate_population(progenitor_list)
        mutated_pop = self.mutate_population(new_population_set)
        self.best_solution = [-1,np.inf,np.array([])]
        
        for i in range(1000):
            #Saving the best solution
            if fitnes_list.min() < self.best_solution[1]:
                self.best_solution[0] = i
                self.best_solution[1] = fitnes_list.min()
                self.best_solution[2] = np.array(mutated_pop)[fitnes_list.min() == fitnes_list]
            progenitor_list = self.progenitor_selection(population_set,fitnes_list)
            new_population_set = self.mate_population(progenitor_list)
            mutated_pop = self.mutate_population(new_population_set)
            self.best_road = self.best_solution[2][0]  
            if i%100==0: 
                print(i, fitnes_list.min(), fitnes_list.mean(), datetime.now().strftime("%d/%m/%y %H:%M"))
                self.plot_map()
                print('hiii')
            fitnes_list = self.get_all_fitnes(mutated_pop,self.cities_dict)

            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
