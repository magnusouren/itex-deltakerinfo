# ITEX assistent

Dette repoet ble laget for å forenkle oversikten over deltakere og påmeldinger til ITEX. Forhåpentligvis vil dette gjøre det enklere å holde oversikt over påmeldinger og deltakere. Særlig nødvendig for å unngå flere påmeldinger i samme parallell og for å sikre at alle er påmeldt i hver parallell.

> Lov å drømme om at noe slikt kan erstattes av en integrert løsning i OW på sikt, men det er nok langt frem i tid.

## Datagrunnlag

Alt av data er eksportert fra arrangementsidene på gamle OW og lagret lokalt i dette repoet i mappen `data_fra_ow`. Se mer om dette i [README.md](data_fra_ow/README.md) i mappen.

For å laste ned disse .json filene går du til arrangementsiden på old. Deretter trykker du "Administasjon" øverst i høyre hjørne. Deretter trykker du "Påmeldingsliste JSON". Filen som lastes ned legges i mappen `data_fra_ow/`i riktig mappe, og du bør endre navnet på filen til bedriftsnavn.json dersom det er for et av arrangementene. 


## Hvordan fungere dette?

Du må kjøre python scriptet `itex.py`for å generere filer med ulike oversikter over påmeldinger og deltakere.

Før du kjører må du sørge for at du legger inn korrekte filnavn på filene du har lastet ned fra ow og at du kobler hvert arrangement til riktig parallell. 

Se mer på kommentarene i koden for å forstå hvordan du kan gjøre dette.


## Gitignore

Alt av datafiler er lagt til i `.gitignore` for å unngå at sensitive data blir lastet opp til github. 

Per nå er dette for enkelhets skyld alle .txt og .json filer. Dersom dette er problematisk kan det endres i `.gitignore` filen slik at det kun er spesifikke filer som ignoreres.