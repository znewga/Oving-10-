#Import
import csv

#Klasser
class Studieplan_ny:
    def __init__(self, id, navn):
        self.id = id
        self.navn = navn
            
        self.studieplan = [     #En liste for hvert semester, med lagret objekter
            [],
            [],
            [],
            [],
            [],
            []
        ]

    def __str__(self):
        return f"{self.navn} har id: {self.id}"

    #Skriver ut alle emner i studieplanen
    def skriv_ut_studieplan(self):
        i = 1
        print(f"{self.navn}")
        for sem in self.studieplan:
            output = ""
            for fag in sem:
                output += fag.kode + ", "
            print(f"{i}. semester:", output)
            i += 1

    #Menyvalg 7: Sjekk om gyldig studieplan. Antall studiepoeng
    def gyldig_studieplan(self):
        for idx, semester in enumerate(self.studieplan, start=1):
            total_sp = 0
            for fag in semester:
                total_sp += fag.poeng
            if total_sp != 30:
                print(f"Semester {idx} har {total_sp} studiepoeng, og er dermed ugyldig.")
            else:
                print(f"Semester {idx} er gyldig med {total_sp} studiepoeng.")
    
class Emne:
    def __init__(self, navn:str, kode:str, semester:str, poeng:float ):
        self.navn= navn
        self.kode= kode
        self.semester= semester
        self.poeng= poeng
        
#FUNKSJONER
#Menyvalg 1
def lag_et_emne():   
    navn = input("Skriv inn emnenavn: ")
    while True:
            kode = input("Skriv inn emnekode: ")
            if len(kode) !=6:
                print("Ugyldig lengde. Emnekoden må være nøyaktig 6 tegn.")
                continue
            bokstaver = kode[:3]
            tall = kode[3:]
            if bokstaver.isalpha() and tall.isdigit():
                print("Gyldig emnekode!")
                break
            else:
                print("Feil format. De første 3 tegnene må være bokstaver og de siste 3 må være tall.")
    while True:
            semester = input("Hvilket semester (HØST/VÅR): ").upper()
            if semester in ["H", "V"]:
                break
            else:
                print("Ugyldig valg, du må skrive HØST eller VÅR")
    while True:
            sp = float(input("Antall studiepoeng: "))
            if sp>0 and sp<31:
                break
            else:
                print("Ugyldig sum, du må skrive et tall mellom 0 og 31.")
    print(f"Emnet '{navn}' ({kode}) ble lagt til.")

    emner.append( Emne(navn, kode, semester, sp) )

#Menyvalg 2
def emne_til_studieplan(): 
    print("Legg et emne til en studieplan. Velg en studieplan under: ")
    #Bruker velger en studieplan fra listen stuieplaner
    valgt_studieplan = velg_studieplan()

    #Skriver ut navn på alle emner i semesterene
    valgt_studieplan.skriv_ut_studieplan()

    #Velger ut semester
    p = len(valgt_studieplan.studieplan)
    while True:
        try:
            input_semester = int(input(f"Hvilket semester vil du legge emnet til(skriv 1-{p})? ") )
            if input_semester > 0 and input_semester <= p:
                break
            else:
                print(f"Du må skrive inn et tall mellom 1 og {p}.")
        except:
            print(f"Du må skrive inn et tall mellom 1 og {p}.")
    valgt_semester = valgt_studieplan.studieplan[input_semester-1] #En liste av emner(objekter)
       
    #Velger et emne
    print("Hvilket emne vil du legge til?")
    valgt_emne = velg_emne() #Velger objektet

    #Legger emnet til studieplanen
    legg_til_emne(valgt_emne, valgt_studieplan, input_semester) #De to første er objekter, den tredje er et tall

def legg_til_emne(input_emnet:object, input_studieplanen:object, input_semester:int): #De to første er objekter, den tredje er et tall
    emnetKode = input_emnet.kode
    emnetSemester = input_emnet.semester

    duplikat = False
    max_sp = False
    feil_semester = False

    #Sjekk duplikat
    i = 0
    for semester in input_studieplanen.studieplan:
        i += 1
        for emne in semester:
            if emne.kode == emnetKode:
                duplikat = True
                sem = i
                break
    
    #Sjekk semester høst eller vår
    if input_semester in (1, 3, 5) and emnetSemester == "V":
        feil_semester = True
        output_sem1 = "vår"
        output_sem2 = "høst"
    elif input_semester in (2, 4, 6) and emnetSemester == "H":
        feil_semester = True
        output_sem1 = "høst"
        output_sem2 = "vår"

    #Sjekk studiepoeng
    total_sp = 0
    fag_sp = 0
    emnet_sp = input_emnet.poeng
    valgt_semester = input_studieplanen.studieplan[input_semester-1]
    for emne in valgt_semester:
        for fag in emner:
            if fag.kode == emne.kode:
                fag_sp = fag.poeng       #Henter ut studiepoeng for emnet
                total_sp += fag_sp         #Legger til studiepoeng i total for semester
    #print(total_sp)
    if total_sp >= 30.0:
        max_sp = True

    #Sjekker feilmelding
    if duplikat:
        print(f"{emnetKode} finnes allerede i {sem}. semester.")
    elif max_sp:
        print(f"Det er {total_sp} sp i dette semesteret. Å legge til {emnet_sp} sp vil overskride 30.0 sp.")
    elif feil_semester:
        print(f"{emnetKode} er et {output_sem1} emne og kan ikke legges til i {output_sem2} semester.")
    else: #Legger til semesteret i studieplanen
        input_studieplanen.studieplan[input_semester-1].append(input_emnet)
        print("Success")

        #TEST
        #input_studieplanen.skriv_ut_studieplan()

# Menyvalg 3: Fjern et emne fra studieplan
def fjern_emne_fra_studieplan():
    print("Fjern et emne fra en studieplan. Velg en studieplan under:")
    
    # Bruker velger en studieplan
    valgt_studieplan = velg_studieplan()  # Objektet Studieplan_ny

    # Skriver ut emnene i alle semestre
    valgt_studieplan.skriv_ut_studieplan()

    # Velg hvilket semester
    p = len(valgt_studieplan.studieplan)
    while True:
        try:
            input_semester = int(input(f"Hvilket semester vil du fjerne et emne fra (1-{p})? "))
            if 1 <= input_semester <= p:
                break
            else:
                print(f"Skriv et tall mellom 1 og {p}.")
        except ValueError:
            print("Ugyldig input, skriv et tall.")

    # Hent ut valgt semester (liste med emne-objekter)
    valgt_semester = valgt_studieplan.studieplan[input_semester - 1]

    # Sjekk om det finnes emner i semesteret
    if not valgt_semester:
        print("Dette semesteret er tomt. Ingenting å fjerne.")
        return

    # Skriv ut emnene i semesteret
    print(f"\nEmner i {input_semester}. semester:")
    for i, fag in enumerate(valgt_semester, start=1):
        print(f"{i}. {fag.kode} - {fag.navn}")

    # Velg hvilket emne som skal slettes
    while True:
        try:
            input_emne = int(input(f"Hvilket emne vil du fjerne (1-{len(valgt_semester)})? "))
            if 1 <= input_emne <= len(valgt_semester):
                break
            else:
                print("Ugyldig valg.")
        except ValueError:
            print("Skriv inn et tall.")

    # Fjern valgt emne
    slettet_emne = valgt_semester.pop(input_emne - 1)
    print(f"Emnet {slettet_emne.kode} ({slettet_emne.navn}) ble fjernet fra {input_semester}. semester.")

         
#Menyvalg 4: Skriv ut en liste over alle registrerte emner
#Siden semmesterene er allerede er lagt inn i lister simpliserer vi denne koden med å bare skrive inn semesterne i en ny liste som hjelper
def registrerte_emner():
    if not emner:
        print("Ingen emner er registert.")
        return
    print("De registrerte emnene er:")
    for emne in emner:
        print(f" - {emne.kode:}: {emne.navn}, {emne.semester}, {emne.poeng} sp")


#Menyvalg 5: Lag en tom studieplan
def lag_tom_studieplan():
    navn = input("Hva skal studieplanen hete? ")
    id = input("Hva er ID på studieplanen? ")
    stud_plan = Studieplan_ny(id, navn)
    studieplaner.append(stud_plan)
    print(f"{navn} ble lagt til.")

#Menyvalg 6: skriv ut en studieplan
def skriv_ut_studieplan():
    print("Skriv ut en studieplan. Velg en studieplan under: ")
    #Bruker velger en studieplan
    valgt_studieplan = velg_studieplan() #Objektet Studieplan
    
    valgt_studieplan.skriv_ut_studieplan()

#Menyvalg 7: Sjekk om en studieplan er gyldig eller ikke
def gyldig_studieplan():
    print("Sjekker om studieplanen er gyldig eller ikke. Velg studieplan under:")
    #Bruker velger en studieplan
    valgt_studieplan = velg_studieplan()

    valgt_studieplan.gyldig_studieplan()

#Menyvalg 8: finn et emnet
def finn_emnet_i_studieplaner():
    print("Søk etter hvilke studieplaner som inneholder et emne.")
    print("Velg et emne å søke etter: ")
    #Skriver ut alle tilgjengelige emner
    t = 1
    for fag in emner:
        print(t, fag.navn, fag.kode)
        t += 1
    i = len(emner)
    input_emne = input("Oppgi emnekode: ")

    ingen_resultat = True
    for studieplan in studieplaner: #Går gjennom alle studieplaner
        for semester in studieplan.studieplan: #Går gjennom alle semester
            for fag in semester:    #Går gjennom alle fag i semesterene
                if fag.kode == input_emne: #Hvis faget i semester er lik input_emnet
                    print(f"{studieplan.navn} bruker emnet {fag.kode}")
                    ingen_resultat = False
    if ingen_resultat:
        print(f"Ingen studieplaner inneholder {input_emne}")

#Menyvalg 9: Lagre emner og studieplaner til fil
def skriv_emner_til_filer(): #Lagrer emner til fil emnefil.csv
    try:
        with open("emner_csv.txt", "w", encoding="utf-8") as fil:
            fil.write("Navn;Kode;Semester;Studiepoeng\n")
            for fag in emner:
                rad = str(fag.navn) + ";"
                rad += str(fag.kode) + ";"
                rad += str(fag.semester) + ";"
                rad += str(fag.poeng) + "\n"
                fil.write(rad)
            print("Success: Lagret emner til fil.")
    except:
         print("Feilmelding: Feil ved skriving til fil.")

def skriv_studieplaner_til_filer():
    try:
        with open("studieplanfil_csv.txt", "w", encoding="utf-8") as fila:
            for stud in studieplaner: #Itererer gjennom hver studieplan i studieplanlista
                stud_list = []
                for semester in stud.studieplan: #Iererer gjennom hver semester i studieplanene
                    semester_list = []
                    for fag in semester: #Itererer gjennom hvert fag i semestrene
                        semester_list.append(fag.kode) #Liste over fagkodene
                    semester_str = ",".join(semester_list) #Lager string med fagkode seperert med ",": "DAT120,ELE100"
                    stud_list.append(semester_str) #Legger stringen/semestrene til en liste over hele studieplanen
                raden = ";".join([stud.id, stud.navn] + stud_list) + "\n" #Hele stuideplanen blir gjort om fra list til string hvor semestrene er separeert med ";"
                fila.write(raden)
            print("Success: lagret studieplaner til fil")
    except FileNotFoundError:
        print("Fant ingen fil å åpne.")

#Menyvalg 10: Les inn emnene og studieplanen
def les_studieplaner_fra_filer():
    try:
        with open("studieplanfil_csv.txt", "r", encoding="utf-8") as fila:
            ny_studieplaner = []
            for linje in fila:
                linje = linje.strip()
                raden = linje.split(";") #Liste over id, navn, og alle semestrene der hvert semester er en string

                stud_id = raden[0]
                stud_navn = raden[1]

                stud_plan = raden[2:] #Studieplanen: en liste hvor hvert semester er en string: "DAT120,ELE100"

                studieplanen = Studieplan_ny(stud_id, stud_navn)
                print(f"Lest inn {stud_navn} med id {stud_id}.")

                for i, semester in enumerate(stud_plan):
                    semester_liste = semester.split(",") #Liste med fagkoder
                    semester_obj = [] #Liste med objekter for hvert semester
                    for emne in semester_liste: #emne = "DAT120"
                        #Finner rette objekt fra fagkode
                        for fag in emner: #Itererer gjennom liste over alle registrerte emner fra lista emner
                            if fag.kode == emne:
                                emne_obj = fag #Definerer rette emne objekt
                                semester_obj.append(emne_obj)
                                break

                    studieplanen.studieplan[i] = semester_obj
                ny_studieplaner.append(studieplanen)
            if ny_studieplaner:
                global studieplaner
                studieplaner = ny_studieplaner
    except FileNotFoundError:
        print("Hjelp")
                    
def les_emner_fra_filer():
    try:
        with open("emner_csv.txt", "r", encoding="utf-8") as fil:
            fil.readline()
            ny_emner = []
            for linje in fil:
                    linje = linje.strip()
                    linje = linje.split(";")
    
                    if len(linje) != 4:
                        print("Feil antall data på rad.")
                        continue
                    
                    data1 = str(linje[0])
                    data2 = str(linje[1])
                    data3 = str(linje[2])
                    data4 = float(linje[3])
                    ny_emner.append(Emne(data1, data2, data3, data4))
                    return
            if ny_emner:
                global emner
                emner = ny_emner
    except FileNotFoundError:
       print(f"Filen {fil} ikke funnet. Ingen emner ble lastet.")

             
#Andre funksjoner
def velg_studieplan(): #Her skrives ut alle studieplaner og brukeren velger en. Retureres studieplan som objekt
    #Skriver ut navn på alle studieplaner
    t = 1
    for studieplan in studieplaner:
        print(t, studieplan.navn)
        t += 1

    #Velger ut studieplanen
    p = len(studieplaner)
    while True:
        try:
            input_studieplan = int(input(f"Velg en studieplan(skriv 1-{p})? ") )
            if input_studieplan > 0 and input_studieplan <= p:
                break
            else:
                print(f"Du må skrive inn et tall mellom 1 og {p}.")
        except:
            print(f"Du må skrive inn et tall mellom 1 og {p}.")
    return studieplaner[input_studieplan-1] #Objektet Studieplan returneres

def velg_emne():
    #Skriver ut alle tilgjengelige emner
    t = 1
    for fag in emner:
        print(t, fag.navn, fag.kode)
        t += 1
    i = len(emner)

    #Velger ut emne
    while True:
        try:
            input_emne = int(input(f"Velg et emne(skriv 1-{i})? ") )
            if input_emne > 0 and input_emne <= i:
                break
            else:
                print(f"Du må skrive inn et tall mellom 1 og {i}.")
        except:
            print(f"Du må skrive inn et tall mellom 1 og {i}.")
    return emner[input_emne-1] #Returnerer objektet
      
#Globale variabler
studieplaner = []   #Mange objekter
emner = []          #Objekter
meny = ["Lag et nytt emne", 
        "Legg til et emne i en studieplan",
        "Fjern et emne fra en studieplan",
        "Skriv ut ei liste over alle registrerte emner",
        "Lag en tom studieplan",
        "Skriv ut studieplanen med hvilke emner som er i hvert semester",
        "Sjekk om studieplanen er gyldig",
        "Finn hvilke studieplaner som bruker et oppgitt emne",
        "Lagre emnene og studieplanen til fil",
        "Les inn emnene og studieplanen",
        "Avslutt"]

#Meny
def hovedmeny():
    while True:
        i = 0
        for m in meny:
            i += 1
            print(i, m)

        try:
            valg = int(input("Skriv inn et valg (1-11): "))
        except:
            print("Feil")

        if valg == 1: #Lag et nytt emne
            lag_et_emne()
        elif valg == 2: #Legg til et emne i studieplan
            emne_til_studieplan()
        elif valg == 3: #Fjern et emne fra studieplan
            fjern_emne_fra_studieplan()
        elif valg == 4: #Skriv ut ei liste over alle registrerte emner
            registrerte_emner() 
        elif valg == 5: #Lag en tom studieplan
            lag_tom_studieplan()
        elif valg == 6: #Skriv ut en studieplan med hvilke emner som er med i hver semester
            skriv_ut_studieplan()
        elif valg == 7: #Sjekk om en studieplan er gydig eller ikke
            gyldig_studieplan()
        elif valg == 8: #Fubb hvilke studieplaner som bruker et oppgitt emne
            #finn_emnet(input("Skriv inn emnekode du vil finne: "))
            finn_emnet_i_studieplaner()
        elif valg == 9: #Lagre emnene og studieplaner til fil
            skriv_emner_til_filer()
            skriv_studieplaner_til_filer()
        elif valg == 10: #Les inn emner og studieplaner fra fil
            les_emner_fra_filer()
            les_studieplaner_fra_filer()
        elif valg == 11: #Avslutter
            print("Avslutter...")
            break
        else:    
            print("FEIL VALG")

#Test
studieplaner.append( Studieplan_ny("B-ELEKTRO", "Elektroteknikk") ) #Elektro
studieplaner.append( Studieplan_ny("B-BYGG", "Byggteknikk") )
emner.append( Emne("Elektronikk", "ELE100", "H", 10) )
emner.append( Emne("Matematikk", "MAT100", "H", 10) )
emner.append( Emne("Grunnleggende Prog", "DAT120", "H", 10) )
emner.append( Emne("Statistikk", "STA100", "V", 10) )
studieplaner[0].studieplan[0].append(emner[0])
studieplaner[0].studieplan[1].append(emner[1])
studieplaner[0].studieplan[2].append(emner[2])
studieplaner[0].studieplan[2].append(emner[3])

studieplaner[1].studieplan[1].append(emner[0])
studieplaner[1].studieplan[2].append(emner[1])
studieplaner[1].studieplan[3].append(emner[2])
studieplaner[1].studieplan[4].append(emner[3])

hovedmeny()

"""
for stud in studieplaner:
    stud.skriv_ut_studieplan()
    print("")"""
#emne_til_studieplan()
#fjern_emne_fra_studieplan()
#skriv_ut_studieplan()
#finn_emnet_i_studieplaner()
#emne_til_studieplan()