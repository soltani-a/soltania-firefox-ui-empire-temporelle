# Contribuer

Merci de contribuer à Empire temporelle, un plugin Firefox UI.

## Proposer un changement

1. Ouvrir une issue pour discuter d’une fonctionnalité importante.
2. Créer une branche dédiée à un changement précis.
3. Modifier les fichiers dans `src/` et, si nécessaire, l’aperçu dans `docs/`.
4. Exécuter `python scripts/build.py` avec Python 3.9 ou supérieur.
5. Charger `src/manifest.json` dans Firefox avec `about:debugging`.
6. Vérifier la lisibilité des onglets, des champs, des menus et de la barre latérale.
7. Mettre à jour `CHANGELOG.md`, puis ouvrir une pull request avec les vérifications réalisées.

Ne pas ajouter de scripts, de ressources distantes, de permissions ou de collecte de données au thème statique. Ne pas inclure de secrets, de profils de navigateur ni de captures contenant des données privées.

Les fichiers de `dist/` sont générés et ne doivent pas être commités. Les contributions sont proposées sous la licence MIT du projet.
