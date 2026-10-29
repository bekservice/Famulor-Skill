# Phone Numbers API operations

Reviewed 2026-10-29. 15 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `buyPhoneNumber` | `POST /phone-numbers` | `famulor buy-phone-number` | [Buy a phone number](https://docs.famulor.io/api-reference/phone-numbers/buy-a-phone-number) |
| `deletePhoneNumberVerification` | `DELETE /phone-numbers/verifications/{id}` | `famulor delete-phone-number-verification` | [Delete regulatory number verification](https://docs.famulor.io/api-reference/introduction) |
| `getPhoneNumber` | `GET /phone-numbers/{id}` | `famulor get-phone-number` | [Get a phone number](https://docs.famulor.io/api-reference/phone-numbers/get-a-phone-number) |
| `getPhoneNumberVerification` | `GET /phone-numbers/verifications/{id}` | `famulor get-phone-number-verification` | [Get regulatory number verification](https://docs.famulor.io/api-reference/phone-numbers/get-regulatory-number-verification) |
| `getPhoneNumberVerificationRequirements` | `GET /phone-numbers/verifications/requirements` | `famulor get-phone-number-verification-requirements` | [Get number verification requirements](https://docs.famulor.io/api-reference/phone-numbers/get-number-verification-requirements) |
| `getPhoneNumberVerificationSubmission` | `GET /phone-numbers/verifications/{id}/submission` | `famulor get-phone-number-verification-submission` | [Get the last submitted verification details](https://docs.famulor.io/api-reference/introduction) |
| `getSmsRegistration` | `GET /phone-numbers/{id}/sms-registration` | `famulor get-sms-registration` | [Get SMS registration](https://docs.famulor.io/api-reference/phone-numbers/get-sms-registration) |
| `listPhoneNumberVerificationCatalog` | `GET /phone-numbers/verifications/catalog` | `famulor list-phone-number-verification-catalog` | [List countries requiring number verification](https://docs.famulor.io/api-reference/phone-numbers/list-countries-requiring-number-verification) |
| `listPhoneNumberVerifications` | `GET /phone-numbers/verifications` | `famulor list-phone-number-verifications` | [List regulatory number verifications](https://docs.famulor.io/api-reference/phone-numbers/list-regulatory-number-verifications) |
| `listPhoneNumbers` | `GET /phone-numbers` | `famulor list-phone-numbers` | [List phone numbers](https://docs.famulor.io/api-reference/phone-numbers/list-phone-numbers) |
| `manageSmsRegistration` | `POST /phone-numbers/{id}/sms-registration` | `famulor manage-sms-registration` | [Prepare, check, correct or attach SMS registration](https://docs.famulor.io/api-reference/phone-numbers/prepare-check-correct-or-attach-sms-registration) |
| `releasePhoneNumber` | `DELETE /phone-numbers/{id}` | `famulor release-phone-number` | [Release or delete a phone number](https://docs.famulor.io/api-reference/phone-numbers/release-or-delete-a-phone-number) |
| `searchAvailablePhoneNumbers` | `GET /phone-numbers/available` | `famulor search-available-phone-numbers` | [Search purchasable numbers](https://docs.famulor.io/api-reference/phone-numbers/search-purchasable-numbers) |
| `submitPhoneNumberVerification` | `POST /phone-numbers/verifications` | `famulor submit-phone-number-verification` | [Submit regulatory number verification](https://docs.famulor.io/api-reference/phone-numbers/submit-regulatory-number-verification) |
| `updatePhoneNumber` | `PATCH /phone-numbers/{id}` | `famulor update-phone-number` | [Update a phone number](https://docs.famulor.io/api-reference/phone-numbers/update-a-phone-number) |
