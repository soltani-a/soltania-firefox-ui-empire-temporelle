# Empire temporelle

**Plugin Firefox UI** — un thème statique pour Firefox de bureau, aux couleurs violet impérial et vert émeraude, avec des anneaux temporels et des circuits futuristes.

[![Build](https://github.com/soltani-a/soltania-firefox-ui-empire-temporelle/actions/workflows/package.yml/badge.svg)](https://github.com/soltani-a/soltania-firefox-ui-empire-temporelle/actions/workflows/package.yml)
[![Licence MIT](https://img.shields.io/badge/licence-MIT-emerald)](LICENSE)

Dépôt : `soltani-a/soltania-firefox-ui-empire-temporelle`.

![Fond panoramique du thème](src/temporal.svg)

## Fonctionnalités

- Onglets, barre d’adresse et barre d’outils sombres.
- Accents émeraude pour l’onglet actif et les éléments importants.
- Menus et barre latérale compatibles assortis.
- Préférence de mode sombre et couleurs du nouvel onglet natif.
- Aucun script, aucune collecte de données, aucune permission de navigation.

Le plugin utilise le format officiel des thèmes Firefox. Il personnalise l’interface compatible sans changer sa structure ni le contenu des sites. Le résultat peut varier selon le système et la version de Firefox.

## Essayer dans Firefox

1. Télécharger et extraire ce dépôt.
2. Ouvrir `about:debugging#/runtime/this-firefox` dans Firefox.
3. Choisir **Charger un module complémentaire temporaire…**.
4. Sélectionner `src/manifest.json`.

Ce chargement disparaît au redémarrage de Firefox. Pour changer de thème, ouvrir `about:addons`, puis **Thèmes**.

## Construire le paquet

Python 3.9 ou supérieur suffit, sans dépendance externe :

```sh
python scripts/build.py
```

Le script vérifie les fichiers et produit `dist/empire-temporelle-1.0.0.zip`. Le manifeste est à la racine de l’archive, comme demandé par Firefox. Le dossier `dist` reste hors de l’historique Git ; le workflow GitHub Actions fournit aussi le paquet comme artefact téléchargeable.

## Publication Mozilla

Le paquet est **non signé**. L’hébergement sur GitHub ne remplace pas la signature Mozilla nécessaire pour une installation durable dans Firefox standard. Envoyer le ZIP au [portail développeur Mozilla](https://addons.mozilla.org/developers/addon/submit/) et suivre les contrôles du portail.

Nom : **Empire temporelle**  
Résumé : **Plugin Firefox UI : thème sombre violet et émeraude, avec anneaux temporels et circuits futuristes.**

## Structure

```text
src/                     Manifeste et fond SVG du thème
docs/preview.html        Maquette illustrative locale
scripts/build.py         Vérification et création du ZIP
.github/workflows/       Vérification et paquet automatiques
CHANGELOG.md             Historique des versions
```

Ouvrir `docs/preview.html` dans un navigateur pour voir la maquette. Elle ne constitue pas une capture réelle de Firefox et n’est pas installée par le thème.

## Validation et contribution

Exécuter le script de construction après une modification, puis vérifier le thème dans Firefox. Les vérifications du paquet ne remplacent pas un essai visuel ni le validateur Mozilla. Le rendu dans Firefox n’a pas encore été vérifié pour cette première version.

Pour signaler un problème, préciser la version de Firefox, le système et les étapes pour le reproduire. Ne pas joindre de données personnelles dans les captures.

## Licence

[Licence MIT](LICENSE), copyright © 2026 Slim SOLTANI. Elle couvre les sources et les ressources graphiques du projet.

Voir aussi [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md) et le [code de conduite](CODE_OF_CONDUCT.md).

## Documentation

- [Thèmes Firefox — MDN](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/theme)
- [Publication sur Firefox Add-ons](https://extensionworkshop.com/documentation/publish/submitting-an-add-on/)
