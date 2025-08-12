---

### Endpoints d'Authentification (Django REST Framework Simple JWT)

Ces endpoints sont gérés par `djangorestframework-simplejwt` et sont définis dans votre `my_project/urls.py`.

* **`POST /api/token/`**
    * **Description :** Obtient une paire de tokens (access et refresh) en échange des identifiants (username et password).
    * **Permissions :** `AllowAny` (Aucune authentification requise).

* **`POST /api/token/refresh/`**
    * **Description :** Rafraîchit un token d'accès expiré en utilisant un token de rafraîchissement valide.
    * **Permissions :** `AllowAny` (Requiert un `refresh` token valide dans le corps de la requête).

* **`POST /api/token/verify/`**
    * **Description :** Vérifie la validité d'un token d'accès.
    * **Permissions :** `AllowAny` (Requiert un `access` token dans le corps de la requête).

---

### Application `users`

- **`GET /api/users/`**

  - **Description :** Liste tous les utilisateurs.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`POST /api/users/`**

  - **Description :** Crée un nouvel utilisateur.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`GET /api/users/{id}/`**

  - **Description :** Récupère les détails d'un utilisateur spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`PUT /api/users/{id}/`**

  - **Description :** Met à jour complètement un utilisateur spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`PATCH /api/users/{id}/`**

  - **Description :** Met à jour partiellement un utilisateur spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`DELETE /api/users/{id}/`**
  - **Description :** Supprime un utilisateur spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

---

### Application `departement`

- **`GET /api/departements/`**

  - **Description :** Liste tous les départements.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`POST /api/departements/`**

  - **Description :** Crée un nouveau département.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`GET /api/departements/{id}/`**

  - **Description :** Récupère les détails d'un département spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`PUT /api/departements/{id}/`**

  - **Description :** Met à jour complètement un département spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`PATCH /api/departements/{id}/`**

  - **Description :** Met à jour partiellement un département spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`DELETE /api/departements/{id}/`**
  - **Description :** Supprime un département spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

---

### Application `postes`

- **`GET /api/postes/`**

  - **Description :** Liste tous les postes.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`POST /api/postes/`**

  - **Description :** Crée un nouveau poste.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`GET /api/postes/{id}/`**

  - **Description :** Récupère les détails d'un poste spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`PUT /api/postes/{id}/`**

  - **Description :** Met à jour complètement un poste spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`PATCH /api/postes/{id}/`**

  - **Description :** Met à jour partiellement un poste spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`DELETE /api/postes/{id}/`**
  - **Description :** Supprime un poste spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

---

### Application `employees`

- **`GET /api/employes/`**

  - **Description :** Liste les profils d'employés. Les admins/RH voient tout. Les employés voient leur propre profil.
  - **Permissions :** `IsAuthenticated` (Authentifié).

- **`POST /api/employes/`**

  - **Description :** Crée un nouveau profil d'employé.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`GET /api/employes/{id}/`**

  - **Description :** Récupère les détails d'un profil d'employé spécifique.
  - **Permissions :** `IsEmployeeOwnerOrAdminOrRH` (Admin, RH, ou le propriétaire de l'employé).

- **`PUT /api/employes/{id}/`**

  - **Description :** Met à jour complètement un profil d'employé spécifique.
  - **Permissions :** `IsEmployeeOwnerOrAdminOrRH` (Admin, RH, ou le propriétaire de l'employé).

- **`PATCH /api/employes/{id}/`**

  - **Description :** Met à jour partiellement un profil d'employé spécifique.
  - **Permissions :** `IsEmployeeOwnerOrAdminOrRH` (Admin, RH, ou le propriétaire de l'employé).

- **`DELETE /api/employes/{id}/`**
  - **Description :** Supprime un profil d'employé spécifique.
  - **Permissions :** `IsEmployeeOwnerOrAdminOrRH` (Admin, RH, ou le propriétaire de l'employé).

---

### Application `recruitment`

- **`GET /api/offres-emploi/`**

  - **Description :** Liste toutes les offres d'emploi. Les utilisateurs non authentifiés et les employés voient uniquement les offres publiées et non expirées. Les admins/RH voient toutes les offres.
  - **Permissions :** `AllowAny` (Tout le monde).

- **`POST /api/offres-emploi/`**

  - **Description :** Crée une nouvelle offre d'emploi.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`GET /api/offres-emploi/{id}/`**

  - **Description :** Récupère les détails d'une offre d'emploi spécifique. Les utilisateurs non authentifiés et les employés voient uniquement les offres publiées et non expirées. Les admins/RH voient toutes les offres.
  - **Permissions :** `AllowAny` (Tout le monde).

- **`PUT /api/offres-emploi/{id}/`**

  - **Description :** Met à jour complètement une offre d'emploi spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`PATCH /api/offres-emploi/{id}/`**

  - **Description :** Met à jour partiellement une offre d'emploi spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`DELETE /api/offres-emploi/{id}/`**

  - **Description :** Supprime une offre d'emploi spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`GET /api/candidats/`**

  - **Description :** Liste toutes les candidatures. Les admins/RH/managers voient tout. Les employés voient leurs propres candidatures (basé sur l'email personnel).
  - **Permissions :** `IsAuthenticated` (Authentifié).

- **`POST /api/candidats/`**

  - **Description :** Crée une nouvelle candidature (permet de postuler).
  - **Permissions :** `AllowAny` (Tout le monde).

- **`GET /api/candidats/{id}/`**

  - **Description :** Récupère les détails d'une candidature spécifique.
  - **Permissions :** `IsCandidatOwnerOrAdminOrManagerOrRH` (Admin, RH, Manager, ou le propriétaire de la candidature).

- **`PUT /api/candidats/{id}/`**

  - **Description :** Met à jour complètement une candidature spécifique.
  - **Permissions :** `IsCandidatOwnerOrAdminOrManagerOrRH` (Admin, RH, Manager, ou le propriétaire de la candidature).

- **`PATCH /api/candidats/{id}/`**

  - **Description :** Met à jour partiellement une candidature spécifique.
  - **Permissions :** `IsCandidatOwnerOrAdminOrManagerOrRH` (Admin, RH, Manager, ou le propriétaire de la candidature).

- **`DELETE /api/candidats/{id}/`**

  - **Description :** Supprime une candidature spécifique.
  - **Permissions :** `IsCandidatOwnerOrAdminOrManagerOrRH` (Admin, RH, Manager, ou le propriétaire de la candidature).

- **`PATCH /api/candidats/{id}/accept/`**

  - **Description :** Accepte une candidature spécifique.
  - **Permissions :** `IsAdminOrManagerOrRH` (Admin, RH ou Manager).

- **`PATCH /api/candidats/{id}/reject/`**
  - **Description :** Rejette une candidature spécifique.
  - **Permissions :** `IsAdminOrManagerOrRH` (Admin, RH ou Manager).

---

### Application `stage`

- **`GET /api/stagiaires/`**

  - **Description :** Liste tous les stagiaires. Les admins/RH voient tout. Les encadreurs (employés) voient les stagiaires qu'ils encadrent.
  - **Permissions :** `IsAuthenticated` (Authentifié).

- **`POST /api/stagiaires/`**

  - **Description :** Crée un nouveau stagiaire.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`GET /api/stagiaires/{id}/`**

  - **Description :** Récupère les détails d'un stagiaire spécifique.
  - **Permissions :** `IsEncadreurOrAdminOrRH` (Admin, RH, ou l'encadreur du stagiaire).

- **`PUT /api/stagiaires/{id}/`**

  - **Description :** Met à jour complètement un stagiaire spécifique.
  - **Permissions :** `IsEncadreurOrAdminOrRH` (Admin, RH, ou l'encadreur du stagiaire).

- **`PATCH /api/stagiaires/{id}/`**

  - **Description :** Met à jour partiellement un stagiaire spécifique.
  - **Permissions :** `IsEncadreurOrAdminOrRH` (Admin, RH, ou l'encadreur du stagiaire).

- **`DELETE /api/stagiaires/{id}/`**

  - **Description :** Supprime un stagiaire spécifique.
  - **Permissions :** `IsEncadreurOrAdminOrRH` (Admin, RH, ou l'encadreur du stagiaire).

- **`GET /api/periodes-stage/`**

  - **Description :** Liste toutes les périodes de stage.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`POST /api/periodes-stage/`**

  - **Description :** Crée une nouvelle période de stage.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`GET /api/periodes-stage/{id}/`**

  - **Description :** Récupère les détails d'une période de stage spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`PUT /api/periodes-stage/{id}/`**

  - **Description :** Met à jour complètement une période de stage spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`PATCH /api/periodes-stage/{id}/`**

  - **Description :** Met à jour partiellement une période de stage spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

- **`DELETE /api/periodes-stage/{id}/`**
  - **Description :** Supprime une période de stage spécifique.
  - **Permissions :** `IsAdminOrRH` (Admin ou RH).

---
