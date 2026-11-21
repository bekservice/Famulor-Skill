# Full Duplex reception

An illustrative design for German and English appointment intake. Test with a synthetic calendar and caller before using this pattern for actual bookings.

## Configure the assistant

- Select **Realtime → Full Duplex (Beta)** when the workspace offers it. List compatible native voices and play their previews. Compare them in the languages the assistant will actually speak. A voice's recommended language is useful for shortlisting.
- Set German as primary and English as secondary. A foreign name is ordinary conversation data. The assistant switches when the caller clearly chooses the supported language.
- Configure a separate greeting, such as “Guten Tag, hier ist der digitale Empfang der Praxis Lindenhof. Wie kann ich Ihnen helfen?” Configure the consent feature separately when required.
- Connect the test calendar and assign availability and booking capabilities. Map their exact accepted inputs and outcomes. Use the live schema and the assigned tool descriptions.

## Example prompt

```text
## Rolle und Ziel
Du bist der digitale Empfang der Praxis Lindenhof. Hilf Anrufern, einen Termin zu finden.

## Sprechweise
Sprich ruhig und freundlich und verwende Sie. Stelle eine Frage pro Gesprächsschritt.
Sprich „Lüdemann“ mit langem ü. Wiederhole eine unsichere Zifferngruppe zum Abgleich.

## Zuhören und Unterbrechungen
Lass Anrufer Namen, Nummern und Korrekturen zu Ende sagen. Gib ihnen Zeit zum Nachdenken.
Bei „Moment“ unterbrich deine Erklärung und höre zu. Verwende danach die korrigierte Angabe.
Bitte vor einer Buchung um die ausdrückliche Bestätigung des konkreten Termins.

## Termine
Frage gezielt nach einem fehlenden Detail. Prüfe offene Termine über die verbundene Kalenderfunktion.
Biete passende zurückgemeldete Termine an. Bestätige die Buchung erst bei einem erfolgreichen Ergebnis.
Wird eine Buchung während der Anfrage geändert, prüfe ihren tatsächlichen Status vor einem weiteren Versuch.
```

When the caller chooses English, use equivalent behavior. For example, “Of course. Did you mean Wednesday at two thirty?” Keep the name and appointment details exactly as collected.

## Run a voice test

1. The caller requests Tuesday, pauses, and corrects it to Wednesday. Inspect the availability request for Wednesday.
2. As the assistant reads a time, the caller says “Moment” and asks for English. Listen for the assistant to yield and continue in English while preserving the chosen time and name.
3. The caller murmurs agreement while the date is incomplete. The test calendar receives no booking until the caller confirms the concrete slot.
4. Delay the test booking response. The assistant reports a confirmed appointment once after the successful result. In a separate test, return an uncertain status and check the calendar before any retry.

An audio preview shows the voice. These checks use actual voice input, captured output and the fixture's recorded tool calls. See [testing and evaluation](../testing-and-evaluation.md) and [voice prompting](../voice-prompting.md).
