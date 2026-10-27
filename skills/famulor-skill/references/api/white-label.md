# White Label API operations

Reviewed 2026-10-27. 29 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `cancelPlatformUserPlan` | `DELETE /platform/users/{user_id}/plan` | `famulor cancel-platform-user-plan` | [End a customer managed plan](https://docs.famulor.io/api-reference/white-label/end-a-customer-managed-plan) |
| `createPlatformCustomPayment` | `POST /platform/users/{user_id}/custom-payments` | `famulor create-platform-custom-payment` | [Create a custom payment for a customer](https://docs.famulor.io/api-reference/introduction) |
| `createPlatformUserToken` | `POST /platform/users/{user_id}/token` | `famulor create-platform-user-token` | [Create a platform user token](https://docs.famulor.io/api-reference/white-label/create-a-platform-user-token) |
| `createResellerTaxRegistration` | `POST /reseller/tax/registrations` | `famulor create-reseller-tax-registration` | [Create reseller tax registration](https://docs.famulor.io/api-reference/introduction) |
| `getPlatformCustomPayment` | `GET /platform/custom-payments/{payment_id}` | `famulor get-platform-custom-payment` | [Get a custom payment](https://docs.famulor.io/api-reference/introduction) |
| `getPlatformDefaultLimits` | `GET /platform/default-limits` | `famulor get-platform-default-limits` | [Get platform registration and prepaid defaults](https://docs.famulor.io/api-reference/white-label/get-platform-registration-and-prepaid-defaults) |
| `getPlatformUser` | `GET /platform/users/{user_id}` | `famulor get-platform-user` | [Get a platform user](https://docs.famulor.io/api-reference/white-label/get-a-platform-user) |
| `getPlatformUserPasswordAccess` | `GET /platform/users/{user_id}/password` | `famulor get-platform-user-password-access` | [Get customer password permissions](https://docs.famulor.io/api-reference/white-label/get-customer-password-permissions) |
| `getPlatformUserPlan` | `GET /platform/users/{user_id}/plan` | `famulor get-platform-user-plan` | [Review a customer managed plan](https://docs.famulor.io/api-reference/white-label/review-a-customer-managed-plan) |
| `getPlatformWelcomeCredits` | `GET /platform/welcome-credits` | `famulor get-platform-welcome-credits` | [Get platform welcome-credit settings](https://docs.famulor.io/api-reference/white-label/get-platform-welcome-credit-settings) |
| `getResellerBilling` | `GET /reseller/billing` | `famulor get-reseller-billing` | [Get reseller financial overview or activity](https://docs.famulor.io/api-reference/white-label/get-reseller-financial-overview-or-activity) |
| `getResellerTaxSettings` | `GET /reseller/tax/settings` | `famulor get-reseller-tax-settings` | [Get reseller tax settings](https://docs.famulor.io/api-reference/introduction) |
| `listPlatformCustomPayments` | `GET /platform/custom-payments` | `famulor list-platform-custom-payments` | [List custom payments across your customers](https://docs.famulor.io/api-reference/introduction) |
| `listPlatformUserCustomPayments` | `GET /platform/users/{user_id}/custom-payments` | `famulor list-platform-user-custom-payments` | [List a customer's custom payments](https://docs.famulor.io/api-reference/introduction) |
| `listPlatformUsers` | `GET /platform/users` | `famulor list-platform-users` | [List platform users](https://docs.famulor.io/api-reference/white-label/list-platform-users) |
| `listResellerPlans` | `GET /reseller/plans` | `famulor list-reseller-plans` | [List customer plans and inclusions](https://docs.famulor.io/api-reference/white-label/list-customer-plans-and-inclusions) |
| `loginPlatformUser` | `POST /platform/users/login` | Browser flow / raw API | [Log in a platform user](https://docs.famulor.io/api-reference/white-label/log-in-a-platform-user) |
| `logoutPlatformUser` | `POST /platform/users/{user_id}/logout` | `famulor logout-platform-user` | [Log out a platform user](https://docs.famulor.io/api-reference/white-label/log-out-a-platform-user) |
| `managePlatformUserPassword` | `POST /platform/users/{user_id}/password` | `famulor manage-platform-user-password` | [Set a customer password or send a reset email](https://docs.famulor.io/api-reference/white-label/set-a-customer-password-or-send-a-reset-email) |
| `registerPlatformUser` | `POST /platform/users` | `famulor register-platform-user` | [Register a platform user](https://docs.famulor.io/api-reference/white-label/register-a-platform-user) |
| `runPlatformCustomPaymentAction` | `POST /platform/custom-payments/{payment_id}` | `famulor run-platform-custom-payment-action` | [Run an action on a custom payment](https://docs.famulor.io/api-reference/introduction) |
| `savePlatformUserPlan` | `PUT /platform/users/{user_id}/plan` | `famulor save-platform-user-plan` | [Assign a customer managed plan or update renewal settings](https://docs.famulor.io/api-reference/white-label/assign-a-customer-managed-plan-or-update-renewal-settings) |
| `transferPlatformUserBalance` | `POST /platform/users/{user_id}/balance` | `famulor transfer-platform-user-balance` | [Transfer credits to or from a platform user](https://docs.famulor.io/api-reference/white-label/transfer-credits-to-or-from-a-platform-user) |
| `updatePlatformDefaultLimits` | `PATCH /platform/default-limits` | `famulor update-platform-default-limits` | [Update platform registration and prepaid defaults](https://docs.famulor.io/api-reference/white-label/update-platform-registration-and-prepaid-defaults) |
| `updatePlatformWelcomeCredits` | `PATCH /platform/welcome-credits` | `famulor update-platform-welcome-credits` | [Update platform welcome-credit settings](https://docs.famulor.io/api-reference/white-label/update-platform-welcome-credit-settings) |
| `updateResellerPlanInclusions` | `PUT /reseller/plans/{id}/inclusions` | `famulor update-reseller-plan-inclusions` | [Update included plan services](https://docs.famulor.io/api-reference/white-label/update-included-plan-services) |
| `updateResellerPlanKnowledgeSources` | `PATCH /reseller/plans/{id}/knowledge-sources` | `famulor update-reseller-plan-knowledge-sources` | [Update plan knowledge source access](https://docs.famulor.io/api-reference/white-label/update-plan-knowledge-source-access) |
| `updateResellerTaxRegistration` | `PATCH /reseller/tax/registrations` | `famulor update-reseller-tax-registration` | [Update reseller tax registration](https://docs.famulor.io/api-reference/introduction) |
| `updateResellerTaxSettings` | `PUT /reseller/tax/settings` | `famulor update-reseller-tax-settings` | [Update reseller tax settings](https://docs.famulor.io/api-reference/introduction) |
