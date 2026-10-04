# 💎 Amethyst — Cristallography software

![Java](https://img.shields.io/badge/Java-17-orange?logo=openapi-initiative)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-3.x-brightgreen?logo=springboot)
![React](https://img.shields.io/badge/React-18-blue?logo=react)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?logo=postgresql)
![License](https://img.shields.io/badge/License-MIT-green)

> **Amethyst** is a Python application, used to classify, model and extract cristallographic data provided by quantum computing.

---

## 🎯 Main goal

* **Issue :** Quantum computing in chemistry has led to an explosion of data produced either from existing calculations or from predictive algorithms. In order to correctly exploit and extract meaning from these data, it has become necessary to automatically classify them and arrange them accordingly.
* **Solution :** A software that can extract relevant data from quantum computing files and classify them in interactive plots.

## ⚙️ Features

- Reads, one or multiple, quantum chemistry files (cif, xyz, vasp, res and Poscar/USPEX).
- Extracts the relevant data.
- Generates energy/index or energy/generation plots (depending on the file).
- Classifies extracted data in these plots by making them clickable to view a 3D model of the corresponding structure.

---

## 🛠 Technical Stack

* **Language & Framework :** Python, Jupyter Notebook
* **IDE :** Visual Studio Code, Spyder
* **Versioning :** Git/GitHub

---

## 🏗 Architecture & Conception

[Décris brièvement tes choix d'architecture, c'est ce qui valorise le plus ta rigueur d'ingénieur.]

* **Architecture en couches :** Controller ➔ Service ➔ Repository (séparation stricte des responsabilités).
* **Sécurité :** Gestion des rôles (RBAC) et chiffrement des données sensibles.
* **Base de données :** Modèle relationnel normalisé avec requêtes optimisées (indexation).
