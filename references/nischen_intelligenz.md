# Nischen-Intelligenz: Branchenspezifische Onboarding-Logik

Dieses Dokument enthält das Branchen-Wissen, das der Onboarding-Skill nutzt, um für jede Nische die richtige Assistenten-Konfiguration abzuleiten. Lies dieses Dokument IMMER zu Beginn des Onboardings.

## Grundprinzip

Jede Branche hat unterschiedliche Anforderungen an einen Telefonassistenten. Die Komplexität variiert stark. Dein Job ist es, die Nische des Kunden zu erkennen und dann proaktiv die richtigen Folgefragen zu stellen, die genau für diese Nische relevant sind.

**Faustregel für Komplexität:**
- **Einfach** (1-2 Kernaufgaben): Immobilien, Handwerk, Steuerberater, Rechtsanwälte
- **Mittel** (3-4 Kernaufgaben): Arztpraxen, Restaurants, Autohäuser, Hotels
- **Komplex** (5+ Kernaufgaben, oft mit Terminlogik): Friseursalons, Beauty/Wellness, Fitnessstudios, Werkstätten, Tierarztpraxen

---

## Branchenprofile

### Friseur / Beauty / Nagelstudio / Barbershop

**Warum komplex:** Viele verschiedene Dienstleistungen mit unterschiedlichen Dauern und Preisen, mehrere Mitarbeiter mit unterschiedlichen Spezialgebieten, Stammkunden mit Präferenzen.

**Typische Aufgaben:**
- Terminbuchung (mit Dienstleistung, Dauer, Mitarbeiter-Präferenz)
- Preisauskunft für diverse Leistungen
- Absagen / Umbuchen
- Öffnungszeiten

**Proaktiv fragen:**
- "Habt ihr verschiedene Dienstleistungen mit unterschiedlichen Dauern? (z.B. Schneiden 30min, Färben 90min, etc.)"
- "Sollen Kunden einen bestimmten Mitarbeiter wählen können?"
- "Habt ihr ein Online-Buchungssystem, das wir per API anbinden können? Wenn ja, welches? (z.B. Shore, Treatwell, Timify)"
- "Gibt es Leistungen, die nur bestimmte Mitarbeiter anbieten?"

**Empfohlene Konfiguration:**
- Wissensdatenbank: JA (Preisliste, Dienstleistungen, Mitarbeiter, Öffnungszeiten)
- Wissensdatenbank-Modus: `function_call` (nicht jeder Anrufer fragt nach Preisen)
- Post-Call Schema: name, telefonnummer, dienstleistung, wunsch_mitarb, termin_wunsch, zusammenfassung
- Mid-Call Tool: Falls Buchungssystem-API vorhanden, Tool zum Termincheck einrichten
- Hintergrundgeräusch: `cafe` oder `off`

**System-Prompt Schwerpunkte:**
- Dienstleistungen aktiv anbieten wenn unklar
- Nach Mitarbeiterpräferenz fragen
- Zeitraum-Wunsch abfragen
- Wenn kein API-Zugriff: "Ich notiere den Terminwunsch und das Team meldet sich zurück"

---

### Immobilienmakler / Hausverwaltung

**Warum einfach-mittel:** Hauptsächlich Terminvereinbarung und allgemeine Auskunft, wenig Varianten.

**Typische Aufgaben:**
- Besichtigungstermine vereinbaren
- Allgemeine Fragen zu Objekten beantworten
- Leads qualifizieren (Budget, Suchkriterien)
- Exposés anfordern

**Proaktiv fragen:**
- "Soll der Bot Leads vorqualifizieren? (z.B. Budget-Rahmen, Kauf oder Miete, Region)"
- "Habt ihr eine Website mit Objektlisten, die als Wissensdatenbank dienen kann?"

**Empfohlene Konfiguration:**
- Wissensdatenbank: Optional (Website-Scraping der Objekte)
- Post-Call Schema: name, telefonnummer, email, anliegen, objekt_ref, termin_wunsch, zusammenfassung
- Hintergrundgeräusch: `office`

---

### Arztpraxis / Zahnarzt / Physiotherapie

**Warum mittel-komplex:** Verschiedene Terminarten, Versicherungsstatus relevant, Dringlichkeit einschätzen.

**Typische Aufgaben:**
- Terminvereinbarung (Ersttermin, Folgetermin, Akuttermin)
- Rezeptbestellungen
- Fragen zu Leistungen/Behandlungen
- Überweisungen

**Proaktiv fragen:**
- "Welche Terminarten gibt es? (Ersttermin, Kontrolltermin, Akuttermin, spezielle Behandlungen)"
- "Soll nach der Versicherungsart gefragt werden? (gesetzlich/privat)"
- "Soll bei Schmerzen/Akutfällen eine Dringlichkeitsstufe erfasst werden?"
- "Gibt es ein Praxisverwaltungssystem mit API-Zugang?"

**Empfohlene Konfiguration:**
- Wissensdatenbank: JA (Leistungsspektrum, Sprechzeiten, Ärzte/Therapeuten)
- Wissensdatenbank-Modus: `function_call`
- Post-Call Schema: name, telefonnummer, geb_datum, versicherung, termin_art, dringlichkeit, zusammenfassung
- Hintergrundgeräusch: `off` oder `office`

**System-Prompt Schwerpunkte:**
- NIEMALS medizinische Ratschläge geben
- Bei Notfällen sofort auf 112 verweisen
- Versicherungsstatus abfragen
- Datenschutz betonen

---

### Restaurant / Gastronomie / Lieferdienst

**Typische Aufgaben:**
- Tischreservierungen
- Öffnungszeiten & Speisekarte
- Bestellungen entgegennehmen (Lieferdienst)
- Allergien / Sonderwünsche

**Proaktiv fragen:**
- "Nimmt der Bot nur Reservierungen an oder auch Bestellungen?"
- "Soll nach Allergien / Unverträglichkeiten gefragt werden?"
- "Habt ihr ein Reservierungssystem? (z.B. OpenTable, Resmio)"

**Empfohlene Konfiguration:**
- Wissensdatenbank: JA (Speisekarte, Öffnungszeiten, Events)
- Wissensdatenbank-Modus: `prompt` bei Lieferdienst (braucht immer Menü-Zugriff), `function_call` bei reiner Reservierung
- Post-Call Schema: name, telefonnummer, personen_anz, datum_zeit, sonderwuensche, zusammenfassung
- Hintergrundgeräusch: `cafe` oder `off`

---

### Autohaus / KFZ-Werkstatt

**Typische Aufgaben:**
- Werkstatttermine (TÜV, Inspektion, Reifenwechsel, Reparatur)
- Probefahrt-Anfragen
- Fahrzeug-Anfragen (Gebraucht/Neu)
- Kostenvoranschläge

**Proaktiv fragen:**
- "Verkauf, Werkstatt, oder beides?"
- "Welche Fahrzeugmarken werden betreut?"
- "Gibt es ein DMS (Dealer Management System) mit API?"

**Empfohlene Konfiguration:**
- Wissensdatenbank: JA (Fahrzeugbestand, Werkstatt-Leistungen)
- Post-Call Schema: name, telefonnummer, fahrzeug, leistung, termin_wunsch, zusammenfassung
- Hintergrundgeräusch: `office`

---

### Handwerk (Elektriker, Sanitär, Maler, Dachdecker etc.)

**Warum einfach:** Meist ein klares Anliegen: "Ich brauche einen Termin für X"

**Typische Aufgaben:**
- Terminanfrage / Auftragsanfrage
- Notdienst-Weiterleitung
- Kostenvoranschlag anfragen

**Proaktiv fragen:**
- "Gibt es einen Notdienst? Wenn ja, an welche Nummer soll bei Notfällen weitergeleitet werden?"
- "Arbeitet ihr in einem bestimmten Einzugsgebiet?"

**Empfohlene Konfiguration:**
- Wissensdatenbank: Optional (Leistungsspektrum, Einzugsgebiet)
- Post-Call Schema: name, telefonnummer, adresse, anliegen, dringlichkeit, zusammenfassung
- Hintergrundgeräusch: `off`

**System-Prompt Schwerpunkte:**
- Bei Notfällen (Wasserrohrbruch, Stromausfall): sofort Notdienst-Info geben oder weiterleiten
- Adresse erfassen (Einsatzort)
- Dringlichkeit einschätzen

---

### Hotel / Pension

**Typische Aufgaben:**
- Zimmerreservierung
- Verfügbarkeitsanfragen
- Check-in/Check-out Zeiten
- Ausstattung & Sonderwünsche

**Proaktiv fragen:**
- "Welche Zimmertypen gibt es?"
- "Gibt es ein Buchungssystem? (z.B. Booking-Anbindung)"
- "Sollen Preise genannt werden?"

**Empfohlene Konfiguration:**
- Wissensdatenbank: JA (Zimmertypen, Preise, Ausstattung, Umgebungsinfos)
- Post-Call Schema: name, telefonnummer, checkin, checkout, zimmer_typ, personen, zusammenfassung
- Hintergrundgeräusch: `office`

---

### Fitnessstudio / Sportverein

**Typische Aufgaben:**
- Probetraining vereinbaren
- Mitgliedschafts-Infos
- Kursplan / Öffnungszeiten
- Kündigung / Vertragsfragen

**Proaktiv fragen:**
- "Soll der Bot Probetrainings direkt buchen können?"
- "Gibt es verschiedene Mitgliedschaftsmodelle?"

**Empfohlene Konfiguration:**
- Wissensdatenbank: JA (Kursplan, Preise, Mitgliedschaften)
- Post-Call Schema: name, telefonnummer, interesse, termin_wunsch, zusammenfassung
- Hintergrundgeräusch: `off`

---

### Rechtsanwalt / Steuerberater / Notar

**Warum einfach:** Meist reiner Terminvereinbarungs-Bot mit Anliegen-Erfassung.

**Typische Aufgaben:**
- Erstberatungstermin vereinbaren
- Rückrufbitten aufnehmen
- Fachgebiet erfragen

**Proaktiv fragen:**
- "Welche Fachgebiete / Schwerpunkte?"
- "Soll der Bot zwischen mehreren Anwälten/Beratern unterscheiden?"
- "Erstberatung kostenlos oder kostenpflichtig? (Bot soll informieren)"

**Empfohlene Konfiguration:**
- Wissensdatenbank: Optional (Fachgebiete, Team)
- Post-Call Schema: name, telefonnummer, fachgebiet, anliegen, dringlichkeit, zusammenfassung
- Hintergrundgeräusch: `office`

**System-Prompt Schwerpunkte:**
- KEINE Rechts-/Steuerberatung geben
- Datenschutz / Vertraulichkeit betonen
- Fachgebiet korrekt erfassen

---

### Tierarztpraxis

**Typische Aufgaben:**
- Terminvereinbarung
- Notfallweiterleitung
- Impftermine / Vorsorge
- Fragen zu Leistungen

**Proaktiv fragen:**
- "Gibt es einen tierärztlichen Notdienst? Nummer?"
- "Welche Tierarten behandelt ihr?"

**Empfohlene Konfiguration:**
- Wissensdatenbank: Optional (Leistungen, Notdienst-Info)
- Post-Call Schema: name, telefonnummer, tierart, tier_name, anliegen, dringlichkeit, zusammenfassung
- Hintergrundgeräusch: `off`

---

## Unbekannte / Sonstige Nischen

Wenn die Branche nicht oben aufgelistet ist, leite folgende universelle Fragen ab:

1. "Was sind die 3 häufigsten Gründe, warum Kunden bei euch anrufen?"
2. "Welche Informationen müsst ihr bei jedem Anruf unbedingt erfassen?"
3. "Gibt es Situationen, in denen sofort an einen Menschen weitergeleitet werden muss?"
4. "Habt ihr eine Website oder Dokumente, die der Bot als Wissensbasis nutzen kann?"
5. "Gibt es externe Systeme (Buchung, CRM, Kalender), die der Bot ansprechen soll?"

Aus diesen Antworten leitest du dann:
- Den System-Prompt ab
- Das Post-Call Schema
- Ob eine Wissensdatenbank nötig ist
- Welche Mid-Call Tools sinnvoll wären

---

## Voice-Mapping (vereinfacht)

| Wahl      | Voice Name       | Voice ID | Sprache | Geschlecht |
|-----------|-----------------|----------|---------|------------|
| Weiblich  | Susi            | 13       | Deutsch | female     |
| Männlich  | Christian Plasa | 1994     | Deutsch | male       |

Für den User wird nur "männliche Stimme" oder "weibliche Stimme" angeboten. Die Voice-ID wird automatisch gesetzt.

---

## Standardwerte (Defaults)

Diese Werte werden gesetzt, wenn der Kunde keine abweichende Präferenz äußert:

| Feld                      | Default                     | Hinweis                                      |
|---------------------------|-----------------------------|----------------------------------------------|
| mode                      | `pipeline`                  | Bestes Preis-Leistungs-Verhältnis            |
| llm_model_id              | `2` (GPT-4.1-mini)         | Schnell, günstig, gut genug für 90% der Fälle |
| timezone                  | `Europe/Berlin`             | Standard DACH                                |
| allow_interruptions       | `true`                      | Natürlicheres Gesprächsverhalten             |
| fillers                   | `true`                      | "Moment...", "Lass mich kurz schauen..."     |
| enable_noise_cancellation | `true`                      | Immer aktiv                                  |
| record                    | `true`                      | Für Qualitätskontrolle                       |
| post_call_evaluation      | `true`                      | Immer Daten extrahieren                      |
| speech_speed              | `1.0`                       | Normal                                       |
| max_duration              | `600`                       | 10 Minuten                                   |
| endpoint_type             | `vad`                       | Voice Activity Detection                     |
| ambient_sound             | Branchenabhängig (siehe oben) |                                             |
| synthesizer_provider_id   | `1` (ElevenLabs)            | Standard TTS                                 |
