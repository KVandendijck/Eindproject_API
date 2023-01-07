# **ReadMe Eindproject_API**
## Kobe Vandendijck 2CCS02


### Thema
In deze opdracht moest ik verder werken aan mijn vorige API en hem uitbreiden. Mijn eerste API was stond de gebruiker toe om de username van een persoon zijn/haar Twitter account in te geven in de POST endpoint. Daarna waren er 2 GET endpoints die informatie over deze persoon gaven, namelijk de hoeveelheid tweets dat deze persoon verstuurd had en dan ook nog eens 5 tweets van dit profiel. Wat ik tijdens dit project heb toegevoegd is dat de data niet zomaar getoond wordt, maar dat deze wordt opgeslagen in een database waaruit je de informatie later kon opvragen. Ik heb nog wat POST en GET endpoints toegevoegd en zoals gevraagd ook een DELETE en een PUT endpoint. Tot slot zit er deze keer ook security op de API, dus nu moet je een account maken en je inloggen om van de endpoints gebruik te kunnen maken.

Dit was met het gebruik van een database waarin 3 tabellen moesten aangemaakt worden.

de 3 tabellen zijn:
  - User: In deze tabel worden alle aangemaakte users opgeslagen, samen met hun hashed paswoord.
  - Searches: in deze tabel sla ik alle opzoekingen van Twitter usernames opgeslagen die vanuit mijn api gedaan worden. De concrete data die bijgehouden wordt is: de naam van de persoon, de id van het profiel, op welk uur van welke dag dit oopgezocht is en tot slot ook nog eens de hoeveelheid tweets dat deze persoon al gepost heeft.
  - Tweets: In deze tabel worden enkele tweets van het opgezochte profiel opgeslagen. Er wordt ook vooraleer dat er een nieuwe entry gemaakt wordt gecontroleerd of dat de tweet nog niet in de database staat. Dit gebeurt op basis van de id die Twitter aan de tweet gegeven heeft.

## De endpoints met screenshots (Open API, Postman)
  
  - /profile (POST): Met deze endpoint geef je een username in van een Twitter account, en deze endpoint verbind met een Twitter API om zo bepaalde informatie op te halen.
  ![image](https://user-images.githubusercontent.com/91118329/211166197-e698b2fb-aa07-4695-8708-2e098c0eb474.png)
  ![image](https://user-images.githubusercontent.com/91118329/211166241-4ed1c4d8-5102-405e-bec7-97b3a3a3f386.png)
  ![image](https://user-images.githubusercontent.com/91118329/211166367-3af3ff37-5289-4cc1-8ecf-415ab188af88.png)
  -  

### Links

  - API repository: <https://github.com/KVandendijck/API>

  - Okteto:
    
      - https://system-service-kvandendijck.cloud.okteto.net/profile
    
      - <https://api-service-kvandendijck.cloud.okteto.net/user>
    
      - <https://api-service-kvandendijck.cloud.okteto.net/getNumberOfTweets>
    
      - <https://api-service-kvandendijck.cloud.okteto.net/gettweet>
