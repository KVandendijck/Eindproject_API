# **ReadMe Eindproject_API**
## Kobe Vandendijck 2CCS02


### Thema
In deze opdracht moest ik verder werken aan mijn vorige API en hem uitbreiden. Mijn eerste API was stond de gebruiker toe om de username van een persoon zijn/haar Twitter account in te geven in de POST endpoint. Daarna waren er 2 GET endpoints die informatie over deze persoon gaven, namelijk de hoeveelheid tweets dat deze persoon verstuurd had en dan ook nog eens 5 tweets van dit profiel. Wat ik tijdens dit project heb toegevoegd is dat de data niet zomaar getoond wordt, maar dat deze wordt opgeslagen in een database waaruit je de informatie later kon opvragen. Ik heb nog wat POST en GET endpoints toegevoegd en zoals gevraagd ook een DELETE en een PUT endpoint. Tot slot zit er deze keer ook security op de API, dus nu moet je een account maken en je inloggen om van de endpoints gebruik te kunnen maken.

Dit was met het gebruik van een database waarin 3 tabellen moesten aangemaakt worden.

de 3 tabellen zijn:
  - User: In deze tabel worden alle aangemaakte users opgeslagen, samen met hun hashed paswoord.
  - Searches: in deze tabel sla ik alle opzoekingen van Twitter usernames opgeslagen die vanuit mijn api gedaan worden. De concrete data die bijgehouden wordt is: de naam van de persoon, de id van het profiel, op welk uur van welke dag dit oopgezocht is en tot slot ook nog eens de hoeveelheid tweets dat deze persoon al gepost heeft.
  - Tweets: In deze tabel worden enkele tweets van het opgezochte profiel opgeslagen. Er wordt ook vooraleer dat er een nieuwe entry gemaakt wordt gecontroleerd of dat de tweet nog niet in de database staat. Dit gebeurt op basis van de id die Twitter aan de tweet gegeven heeft.




### Open API


### Postman



### Links

  - Front-end repository:
    <https://github.com/KVandendijck/KVandendijck.github.io>

  - API repository: <https://github.com/KVandendijck/API>

  - Okteto:
    
      - <https://api-service-kvandendijck.cloud.okteto.net>
    
      - <https://api-service-kvandendijck.cloud.okteto.net/user>
    
      - <https://api-service-kvandendijck.cloud.okteto.net/getNumberOfTweets>
    
      - <https://api-service-kvandendijck.cloud.okteto.net/gettweet>
