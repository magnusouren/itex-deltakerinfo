import json


class itex:
    attendees = []
    parallels = []
    events = []

    def __init__(self, *filenames):
        for filename in filenames:
            with open("data_fra_ow/itex/" + filename) as json_file:
                data = json.load(json_file)
            for p in data['Attendees']:
                self.attendees.append({'name': p['first_name'] + ' ' + p['last_name'], 'year': p['year'],
                                      'email': p['email'], 'allergies': p['allergies'], 'phone': p['phone_number'], 'events': {}})

    def register_event(self, filename, parallell):
        eventname = filename.split('.')[0]
        self.events.append(eventname)
        self.add_event_to_parallel(eventname, parallell)

        with open('data_fra_ow/arrangement/'+filename) as json_file:
            data = json.load(json_file)
        for p in data['Attendees']:
            for deltaker in self.attendees:
                if deltaker['email'] == p['email']:
                    deltaker['events'][eventname] = True
                elif not eventname in deltaker['events'].keys():
                    deltaker['events'][eventname] = False

    def add_event_to_parallel(self, eventname, parallell):
        while len(self.parallels) < parallell:
            self.parallels.append([])
        self.parallels[parallell-1].append(eventname)

    def print_attendees(self):
        for attendee in self.attendees:
            print(attendee)

    def amount_of_attendees(self):
        return len(self.attendees)

    def amount_of_attendees_per_event(self, eventname):
        amount = 0
        for deltaker in self.attendees:
            if deltaker['events'][eventname]:
                amount += 1
        return amount

    def intersection_between_events(self, event1, event2):
        res = []
        for deltaker in self.attendees:
            if deltaker['events'][event1] and deltaker['events'][event2]:
                res.append(deltaker)
        return res

    def intersection_in_parallel(self, *events):
        res = []

        for event_a in events:
            for event_b in events:
                if event_a != event_b:
                    intersection = self.intersection_between_events(
                        event_a, event_b)
                    for attendee in intersection:
                        if not attendee in res:
                            res.append(attendee)

        return res

    def get_attendees_not_in_parallel(self, *events):
        res = []
        for attendee in self.attendees:
            in_parallel = False
            for event in events:
                if attendee['events'][event]:
                    in_parallel = True
            if not in_parallel:
                res.append(attendee)
        return res

    def get_allergies_per_event(self, eventname):
        res = []
        for attendee in self.attendees:
            if attendee['events'][eventname] and attendee['allergies']:
                res.append(attendee)
        return res

    def parallel_status(self, num):
        with open('./paralleller/parallell'+str(num)+'.txt', 'w', encoding='utf-8') as f:
            events = self.parallels[num-1]
            f.write("Status for parallell: " + str(num) +
                    " med bes?k til: " + ", ".join(map(str, events)) + ":\n")

            f.write("\n---------------------------------\n\n")

            for event in events:
                f.write("Status " + event + ":\n")
                f.write("Antall p?meldte: " +
                        str(self.amount_of_attendees_per_event(event)) + "\n")

                f.write("\n---------------------------------\n\n")

            intersection = self.intersection_in_parallel(events)

            f.write("Overlapp mellom p?meldte i parallell:\n")

            if len(intersection) == 0:
                f.write("Ingen overlapp i parallell " + str(num) + "\n")
            else:
                f.write("Overlapp i parallell " + str(num) + ":\n")
                for attendee in intersection:
                    intersection = []
                    for event in attendee['events']:
                        if attendee['events'][event] and event in events:
                            intersection.append(event)

                    f.write(" - " + attendee['name'] + "er p?meldt: " +
                            ", ".join(map(str, intersection)) + "\n")

            f.write("\n---------------------------------\n\n")

            f.write(
                "Deltakere som ikke er p?meldt noen arrangement i parallell " + str(num) + ":\n")
            for attendee in self.get_attendees_not_in_parallel(*events):
                f.write(" - " + attendee['name'] + "\n")

    def write_deltakerliste_to_file(self, eventname, filename):
        with open(filename, 'w') as f:
            for i in range(6):  # for 5 klasser
                for attendee in self.attendees:
                    if attendee['events'][eventname] and attendee['year'] == i:
                        f.write(attendee['name'] + ", " +
                                str(attendee['year']) + ". klasse\n")

    def write_attendees_to_file(self, filename):
        with open(filename, 'w') as f:
            for i in range(6):  # for 5 klasser
                for attendee in self.attendees:
                    if attendee['year'] == i:
                        f.write(attendee['name'] + ", " +
                                str(attendee['year']) + ". klasse\n")

    def write_kontaktinfo_to_file(self, filename):
        with open(filename, "w") as f:
            for attendee in self.attendees:
                f.write(attendee['name'] + ", " +
                        str(attendee['phone']) + "\n")

    def write_allergies_to_file(self, filename):
        with open(filename, "w") as f:
            for attendee in self.attendees:
                if attendee['allergies']:
                    f.write("%s, %s\n" %
                            (attendee['name'], attendee['allergies']))

    def write_email_to_file(self, filename):
        with open(filename, "w") as f:
            for attendee in self.attendees:
                f.write(attendee['email'] + "\n")

    def write_allergies_per_event_to_file(self, filename, eventname):
        with open(filename, "w") as f:
            for attendee in self.get_allergies_per_event(eventname):
                f.write("%s, %s\n" %
                        (attendee['name'], attendee['allergies']))

    def write_reports(self):
        self.write_attendees_to_file('generelt/deltakere.txt')
        self.write_kontaktinfo_to_file('generelt/kontaktinfo.txt')
        self.write_allergies_to_file('generelt/allergier.txt')
        self.write_email_to_file('generelt/eposter.txt')

    def write_deltakerlister(self):
        for event in self.events:
            self.write_deltakerliste_to_file(
                event, 'deltakerlister/'+event+'.txt')

    def write_allergies(self):
        for event in self.events:
            self.write_allergies_per_event_to_file(
                'allergier/'+event+'.txt', event)

    def write_events_per_deltaker(self, filename):
        with open(filename, 'w') as f:
            for deltaker in self.attendees:
                f.write(deltaker['name'] + ":\n")
                for event in deltaker['events']:
                    if deltaker['events'][event]:
                        f.write(" - " + event + "\n")
                f.write("\n")


# Oppretter et itex-objekt med påmeldingsdata fra filene itex_3.json, itex_4_og_5.json som er hentet fra OW for den generelle p?meldingen.
# Filene må ligge i mappen data_fra_ow/itex/
# Legg til filnavn for alle arrangementene som gjelder for ITEX generelt.
# Eks:
# i = itex('itex_3.json', 'itex_4_og_5.json')
# i = itex('itex_3.json', 'itex_4_og_5.json', 'itex_6.json')
# i = itex('itex.json')

i = itex('itex_3.json', 'itex_4_og_5.json')

# Legger til events med filnavn og parallellnummer
# Filene må ligge i mappen data_fra_ow/arrangement/
# Eks:
# i.register_event('bedriftnavn.json', 1)
i.register_event('bekk.json', 1)
i.register_event('fremtind.json', 2)
i.register_event('bouvet.json', 2)
i.register_event('sopra.json', 2)
i.register_event('knowit.json', 3)
i.register_event('noa.json', 3)
i.register_event('geodata.json', 4)
i.register_event('dnv.json', 4)
i.register_event('cgi.json', 4)
i.register_event('twoday.json', 5)
i.register_event('accenture.json', 5)

# Printer påmeldingsstatus for paralleller
i.parallel_status(1)
i.parallel_status(2)
i.parallel_status(3)
i.parallel_status(4)
i.parallel_status(5)

# Printer allergier, deltakere og kontaktinfo for itex generelt
i.write_reports()

# Skriver deltakerlister for hvert event
i.write_deltakerlister()

# Skriver allergier for hvert event
i.write_allergies()

# Skriver hvilke events hver deltaker er påmeldt i en fil
i.write_events_per_deltaker('generelt/events_per_deltaker.txt')
