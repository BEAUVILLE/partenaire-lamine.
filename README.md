# Lamine — DIGIY DRIVER

Fiche publique autonome de **Lamine**, chauffeur privé à Saly, intégrée à la galerie **DIGIY DRIVER**.

## Adresse publique

```text
https://partenaire-lamine.digiylyfe.com/
```

## Positionnement

Lamine est classé uniquement dans le module **DRIVER** :

- chauffeur privé à Saly ;
- transfert AIBD ;
- courses locales ;
- trajets vers Dakar ;
- circuits Petite Côte ;
- mise à disposition ;
- course sur réservation confirmée directement sur WhatsApp.

La mention « sur réservation » décrit la manière de commander une course. Elle ne rattache pas Lamine au module DIGIY RESA.

## Contact direct

```text
Téléphone / WhatsApp : +221 78 441 36 80
```

Lien WhatsApp :

```text
https://wa.me/221784413680
```

## Doctrine DIGIYLYFE

- 0 % commission DIGIY ;
- contact direct entre le client et le chauffeur ;
- disponibilité et tarif confirmés par Lamine ;
- paiement direct au chauffeur ;
- aucune demande ni donnée de course stockée par cette fiche.

Le petit formulaire présent dans `index.html` prépare uniquement un message WhatsApp dans le navigateur du client.

## Fichiers du dépôt

```text
index.html
README.md
CNAME
```

## Déploiement sur GitHub Pages

1. Créer un dépôt GitHub, par exemple `partenaire-lamine`.
2. Ajouter les fichiers du présent pack à la racine.
3. Ouvrir **Settings → Pages**.
4. Choisir **Deploy from a branch**.
5. Sélectionner la branche `main` et le dossier `/root`.
6. Enregistrer.
7. Dans **Custom domain**, saisir :

```text
partenaire-lamine.digiylyfe.com
```

8. Activer **Enforce HTTPS** dès que GitHub le permet.

## DNS

Le sous-domaine doit pointer vers GitHub Pages :

```text
Type  : CNAME
Nom   : partenaire-lamine
Cible : beauville.github.io
TTL   : 300
```

## Liens DIGIYLYFE

- Galerie chauffeur : https://driver-client.digiylyfe.com/
- Maison DIGIYLYFE : https://digiylyfe.com/
- Fiche Lamine : https://partenaire-lamine.digiylyfe.com/

## Mise à jour du numéro ou des services

Rechercher dans `index.html` :

```text
221784413680
```

Puis remplacer toutes les occurrences si le numéro change.

Les services peuvent être modifiés dans la section HTML :

```text
Les services chauffeur
```

---

**DIGIY DRIVER — Le chauffeur garde son client, son paiement et sa route.**
