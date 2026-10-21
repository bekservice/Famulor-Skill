# Billing API operations

Reviewed 2026-10-21. 15 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `cancelAddonTrial` | `DELETE /billing/addon-trials` | `famulor cancel-addon-trial` | [Cancel add-on trial renewal](https://docs.famulor.io/api-reference/billing/cancel-add-on-trial-renewal) |
| `confirmSubscriptionPaymentChange` | `POST /billing/subscription-change/confirm` | `famulor confirm-subscription-payment-change` | [Confirm subscription change](https://docs.famulor.io/api-reference/billing/confirm-subscription-change) |
| `createBillingPortalLink` | `POST /billing/portal` | `famulor create-billing-portal-link` | [Create billing management link](https://docs.famulor.io/api-reference/billing/create-billing-management-link) |
| `createInvoicePaymentLink` | `POST /billing/invoice-payment` | `famulor create-invoice-payment-link` | [Create invoice payment link](https://docs.famulor.io/api-reference/billing/create-invoice-payment-link) |
| `getBalance` | `GET /balance` | `famulor get-balance` | [Get balance](https://docs.famulor.io/api-reference/billing/get-balance) |
| `getPaymentStatus` | `GET /billing/payment-status` | `famulor get-payment-status` | [Get workspace payment status](https://docs.famulor.io/api-reference/billing/get-workspace-payment-status) |
| `getReferrals` | `GET /referrals` | `famulor get-referrals` | [Get referrals](https://docs.famulor.io/api-reference/billing/get-referrals) |
| `getSmsRegistrationBilling` | `GET /billing/sms-registration` | `famulor get-sms-registration-billing` | [Get workspace SMS registration billing](https://docs.famulor.io/api-reference/billing/get-workspace-sms-registration-billing) |
| `getTelephonyUsageRates` | `GET /usage/telephony-rates` | `famulor get-telephony-usage-rates` | [Estimate assistant or Loop phone rates](https://docs.famulor.io/api-reference/billing/estimate-assistant-or-loop-phone-rates) |
| `getWorkspaceUsageRates` | `GET /usage/rates` | `famulor get-workspace-usage-rates` | [Get workspace usage rates](https://docs.famulor.io/api-reference/billing/get-workspace-usage-rates) |
| `listAddonTrials` | `GET /billing/addon-trials` | `famulor list-addon-trials` | [List add-on trials](https://docs.famulor.io/api-reference/billing/list-add-on-trials) |
| `listTransactions` | `GET /transactions` | `famulor list-transactions` | [List transactions](https://docs.famulor.io/api-reference/billing/list-transactions) |
| `manageSmsRegistrationBilling` | `POST /billing/sms-registration` | `famulor manage-sms-registration-billing` | [Pay for or cancel SMS registration](https://docs.famulor.io/api-reference/billing/pay-for-or-cancel-sms-registration) |
| `reviewSubscriptionPaymentChange` | `POST /billing/subscription-change/review` | `famulor review-subscription-payment-change` | [Review subscription change](https://docs.famulor.io/api-reference/billing/review-subscription-change) |
| `startAddonTrial` | `POST /billing/addon-trials` | `famulor start-addon-trial` | [Start add-on trial checkout](https://docs.famulor.io/api-reference/billing/start-add-on-trial-checkout) |
