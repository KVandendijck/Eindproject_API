# **ReadMe Eindproject_API**
## Kobe Vandendijck 2CCS02


### Thema
In deze opdracht moest ik verder werken aan mijn vorige API en hem uitbreiden. Mijn eerste API was stond de gebruiker toe om de username van een persoon zijn/haar Twitter account in te geven in de POST endpoint. Daarna waren er 2 GET endpoints die informatie over deze persoon gaven, namelijk de hoeveelheid tweets dat deze persoon verstuurd had en dan ook nog eens 5 tweets van dit profiel. Wat ik tijdens dit project heb toegevoegd is dat de data niet zomaar getoond wordt, maar dat deze wordt opgeslagen in een database waaruit je de informatie later kon opvragen. Ik heb nog wat POST en GET endpoints toegevoegd en zoals gevraagd ook een DELETE en een PUT endpoint. Tot slot zit er deze keer ook security op de API, dus nu moet je een account maken en je inloggen om van de endpoints gebruik te kunnen maken.

Dit was met het gebruik van een database waarin 3 tabellen moesten aangemaakt worden.

de 3 tabellen zijn:
  - User: In deze tabel worden alle aangemaakte users opgeslagen, samen met hun hashed paswoord.
  - Searches: in deze tabel sla ik alle opzoekingen van Twitter usernames opgeslagen die vanuit mijn api gedaan worden. De concrete data die bijgehouden wordt is: de naam van de persoon, de id van het profiel, op welk uur van welke dag dit oopgezocht is en tot slot ook nog eens de hoeveelheid tweets dat deze persoon al gepost heeft.
  - Tweets: In deze tabel worden enkele tweets van het opgezochte profiel opgeslagen, de informatie die wordt opgeslagen is de id van het profiel dat de tweet gepost heeft, de id van de tweet zelf en tot slot. Er wordt ook vooraleer dat er een nieuwe entry gemaakt wordt gecontroleerd of dat de tweet nog niet in de database staat. Dit gebeurt op basis van de id die Twitter aan de tweet gegeven heeft.

### Aanvullende functies

2.2 Met mijn API communiceer ik met een Twitter API. 

Ik niet echt een andere aanvulling gedaan, ik heb enkel 2 endpoints meer dan gevraagd.


## De endpoints met screenshots (OpenAPI, Postman)    

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
  ![image](https://user-images.githubusercontent.com/91118329/211167227-11e6e3f4-e77d-4c45-b01d-ab4dc6817229.png)
  ![image](https://user-images.githubusercontent.com/91118329/211167231-1834e1f2-d33e-4fc6-bbe9-f2d4a55dbc5e.png)
  ![image](https://user-images.githubusercontent.com/91118329/211167303-659a099d-7161-4e0a-9f76-01ca49a7ee92.png)
  - /allusers (GET): Dit endpoint toont alle gebruikers die aangemaakt zijn/in de database staan.
  ![image](https://user-images.githubusercontent.com/91118329/211167371-507f7906-0fdf-4860-88b5-675ca4f65d72.png)
  ![image](https://user-images.githubusercontent.com/91118329/211167415-f4e8e36f-58a7-4c6b-bf71-037785cfe517.png)
  - /users/{id} edit username (PUT): Dit endpoint staat je toe om de username van een van de users te veranderen op basis van de primary key.
  ![image](https://user-images.githubusercontent.com/91118329/211167469-e121b2f8-c759-40eb-858b-4c81c8cac7e5.png)
  ![image](https://user-images.githubusercontent.com/91118329/211167479-db0561dd-61bd-4148-ae08-f9d5fdad2a07.png)
  ![image](https://user-images.githubusercontent.com/91118329/211167536-4fca0b23-72af-46e3-ac8b-f5070d0ad43f.png)
  ![image](https://user-images.githubusercontent.com/91118329/211167558-8a9d8d34-0cd5-4985-b4ec-1548ea83008c.png)
  - /users/{id} delete user (DELETE): Dit endpoint laat je toe om users te verwijderen op basis van de primary key. Er wordt ook een bericht teruggegeven als de user verwijdert is.
  ![image](https://user-images.githubusercontent.com/91118329/211167623-bd510e63-5f7b-4253-b959-39a3543d75f5.png)
  ![image](https://user-images.githubusercontent.com/91118329/211167654-ab3bd92b-a870-4ae0-8ba1-f68a5bef227e.png)
  ![image](https://user-images.githubusercontent.com/91118329/211167671-3b1f4092-2aa4-4e91-b5c2-a79b0a7ca96d.png)

### Links

  - API repository: https://github.com/KVandendijck/Eindproject_API
  
  - Hosted API: https://system-service-kvandendijck.cloud.okteto.net

  - Okteto:
    
      - https://system-service-kvandendijck.cloud.okteto.net/profile
    
      - https://system-service-kvandendijck.cloud.okteto.net/alltweets
    
      - https://system-service-kvandendijck.cloud.okteto.net/allsearches
    
      - https://system-service-kvandendijck.cloud.okteto.net/token
     
      - https://system-service-kvandendijck.cloud.okteto.net/users
      
      - https://system-service-kvandendijck.cloud.okteto.net/allusers
      
      - https://system-service-kvandendijck.cloud.okteto.net/users/5
      
      - https://system-service-kvandendijck.cloud.okteto.net/users/5


