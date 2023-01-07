# **ReadMe Eindproject_API**
## Kobe Vandendijck 2CCS02


### Thema
In deze opdracht moest ik verder werken aan mijn vorige API en hem uitbreiden. Mijn eerste API was stond de gebruiker toe om de username van een persoon zijn/haar Twitter account in te geven in de POST endpoint. Daarna waren er 2 GET endpoints die informatie over deze persoon gaven, namelijk de hoeveelheid tweets dat deze persoon verstuurd had en dan ook nog eens 5 tweets van dit profiel. Wat ik tijdens dit project heb toegevoegd is dat de data niet zomaar getoond wordt, maar dat deze wordt opgeslagen in een database waaruit je de informatie later kon opvragen. Ik heb nog wat POST en GET endpoints toegevoegd en zoals gevraagd ook een DELETE en een PUT endpoint. Tot slot zit er deze keer ook security op de API, dus nu moet je een account maken en je inloggen om van de endpoints gebruik te kunnen maken.

Dit was met het gebruik van een database waarin 3 tabellen moesten aangemaakt worden.

de 3 tabellen zijn:
  - User: In deze tabel worden alle aangemaakte users opgeslagen, samen met hun hashed paswoord.
  - Searches: in deze tabel sla ik alle opzoekingen van Twitter usernames opgeslagen die vanuit mijn api gedaan worden. De concrete data die bijgehouden wordt is: de naam van de persoon, de id van het profiel, op welk uur van welke dag dit oopgezocht is en tot slot ook nog eens de hoeveelheid tweets dat deze persoon al gepost heeft.
  - Tweets: In deze tabel worden enkele tweets van het opgezochte profiel opgeslagen, de informatie die wordt opgeslagen is de id van het profiel dat de tweet gepost heeft, de id van de tweet zelf en tot slot. Er wordt ook vooraleer dat er een nieuwe entry gemaakt wordt gecontroleerd of dat de tweet nog niet in de database staat. Dit gebeurt op basis van de id die Twitter aan de tweet gegeven heeft.

## De endpoints met screenshots (Open API, Postman)    

![image](https://user-images.githubusercontent.com/91118329/211166460-e5f7bb8f-2730-448f-a32b-fee267e593b9.png)

  - /profile (POST): Met dit endpoint geef je een username in van een Twitter account, en deze endpoint verbind met een Twitter API om zo bepaalde informatie op te halen. En dan wordt deze informatie opgeslagen in 2 van de 3 tabellen namelijk de Tweets en de Searches tabellen. Verdere specificaties staan hierboven uitgelegd.
  ![image](https://user-images.githubusercontent.com/91118329/211166197-e698b2fb-aa07-4695-8708-2e098c0eb474.png)
  ![image](https://user-images.githubusercontent.com/91118329/211166241-4ed1c4d8-5102-405e-bec7-97b3a3a3f386.png)
  ![image](https://user-images.githubusercontent.com/91118329/211166367-3af3ff37-5289-4cc1-8ecf-415ab188af88.png)
  - /alltweets (GET): Dit endpoint toont alle tweets die zijn opgeslagen in de Tweets tabel van de database. Samen met de informatie die hierboven staat opgesomd.
  ![image](https://user-images.githubusercontent.com/91118329/211166708-cabf12eb-23b8-4117-b98a-0ec7bbce6ddc.png)
  ![image](https://user-images.githubusercontent.com/91118329/211166751-c0291bfd-fb50-4d31-845e-c2152bbac459.png)
  - /allsearches (GET): Dit endpoint toont alle opgeslagen searches die gebeurt zijn sinds de database gemaakt is.
  ![image](https://user-images.githubusercontent.com/91118329/211166811-92950378-0c66-433d-94e7-c49290cce3e4.png)
  ![image](https://user-images.githubusercontent.com/91118329/211166828-8b2ed167-f754-4057-920a-6ad7336dccff.png)
  - /token (POST): Met dit endpoint genereer je een bearer token dat kan meegestuurd worden van services die je niet op voorhand toestaan om in te loggen, een voorbeeld hiervan is Postman.
  ![image](https://user-images.githubusercontent.com/91118329/211166986-4d32579c-51d7-413e-9839-275f5b9fad64.png)
  ![image](https://user-images.githubusercontent.com/91118329/211167002-7cb6d127-dee2-4e0b-be75-2088750e5146.png)
  ![image](https://user-images.githubusercontent.com/91118329/211167068-bfb6665a-ce47-44d8-b583-4ac38449281d.png)
  - /users (POST): Dit endpoint laat jou een nieuwe user aanmaken en een wachtwoord. Dit wachtwoord wordt hierna gehashed.



### Links

  - API repository: <https://github.com/KVandendijck/API>

  - Okteto:
    
      - https://system-service-kvandendijck.cloud.okteto.net/profile
    
      - https://system-service-kvandendijck.cloud.okteto.net/alltweets
    
      - https://system-service-kvandendijck.cloud.okteto.net/allsearches
    
      - https://system-service-kvandendijck.cloud.okteto.net/token
     
      - 


