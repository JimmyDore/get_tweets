# Des tweets pour s'amuser

## Les twittos choisis
- EmmanuelMacron : président 
- murielpenicaud : ministre du travail 
- pyduan : un startupper "révolutionnaire"
- Cyrilhanouna : lui il met plein d'emojis, ça peut être sympa pour l'algo
- rudygobert27 : sportif reconnu, et twittos enflammé
- MLP_officiel : une autre politicienne pour comparer
- benoithamon : un autre politicien pour comparer
- JLMelenchon : encore un 
- UrbanLePharaon : un twittos plus dans l'air du temps 

## Format des données
Le dossier `output/` contient 2 dossiers : 
- `csv/` qui contient:
  - un fichier ALL_TWEETS étant un CSV récapitulatif de tous les tweets de tous les users twitter identifiés.
  - un fichier par twittos, car le csv récapitulatif n'est pas sûr d'avoir une bonne délimitation. Le séparateur utilisé est "|", mais si le tweet contient ce caractère, pas sûr que ça fonctionne...
    
- `pickle/` qui contient :
    - un fichier ALL_TWEETS qui correspond au pickle du dataframe récapitulant tous les tweets
    - un fichier par twittos parce que pourquoi pas, c'est qu'une ligne de code en plus
    - Pour charger le dataframe pandas à partir du pickle : 
        ```
        import pandas as pd
        df = pd.read_pickle(f"tweets_from_users-{date.today()}.pickle")
        ```

