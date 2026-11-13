# Kokemukset ai-tehtävästä login

Ensimmäisellä yrityksellä agentti yritti lukea kaikenlaista login-hakemiston ulkopuolelta, vaikka minulla oli vain se auki VS Codessa. Keskeytin lopulta yrityksen. Sitten pyysin agenttia tekemään sen, mitä /init tekisi, mutta pysymään tämän hakemiston sisällä. Se onnistui. Jouduin korjaamaan vain python-komennon python3-komennoksi.

Testejä luodessa agentti yritti ensin ajaa testejä "robotcode"-komennolla, ja sitten olisi halunnut asentaa sen. Valitsin kuitenkin vaihtoehdon, että tehdään testit suoraan robot frameworkillä eikä asennella mitään. Näin jälkikäteen huomaan, että AGENTS.md-tiedostoon olisi kannattanut lisätä suoraan se komento, jolla haluaa testit ajettavan. Tämä oli näköjään tehtävänannossakin, mutta missasin sen.

Loppu menikin suunnitellusti, testit toimivat ja ominaisuudet myös, ja testit hajosivat kun muutin koodia.
