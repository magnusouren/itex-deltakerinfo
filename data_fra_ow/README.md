# Data fra OW

I denne mappen ligger det filer med oversikt over data fra OW. Listene er hentet fra arrangementsiden på gamle OW. old.online.ntnu.no/events/[id].

## Mappe- og filstuktur

```
data_fra_ow/
│
├── README.md
├── arrangement/
│   ├── bedriftsnavn.json
├── itex/
│   ├── itex_4_og_5.json
│   ├── itex_3.json

```

## Import av data

Dataene er lastet ned som .json manuelt fra gamle OW per arrangement.

## Eksempelformat på data 

```json
{
    "attendees": [
        {
            "first_name": "Ola",
            "last_name": "Nordmann",
            "year": 3,
            "email": "ola@mail.com",
            "phone_number": "12345678",
            "alleriges": "Nøtter og melk",
        },
        ...
        ,
    ],
    "Waitlist": [], "Reservations": []
}
```
