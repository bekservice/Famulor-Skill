# Knowledge Bases API operations

Reviewed 2026-10-27. 31 public operations. [All areas](index.md) · [Execution guide](../api-and-sdk.md)

Paths are relative to `https://app.famulor.io/api/v1`. Each operation ID is also the typed SDK method `client.api.<operationId>`. Look up its exact request contract with the bundled `find-operation.py`; CLI help reflects the installed version.

Hidden CLI operations require an interactive/browser flow or `famulor api` where appropriate; do not assume the displayed generated name is an available command.

| Operation ID / SDK method suffix | HTTP endpoint | CLI command | Purpose |
| --- | --- | --- | --- |
| `addKnowledgeDocument` | `POST /knowledge-bases/{id}/documents` | `famulor add-knowledge-document` | [Add or retry a document](https://docs.famulor.io/api-reference/knowledge-bases/add-or-retry-a-document) |
| `createCrawlSource` | `POST /knowledge-bases/{id}/crawl-sources` | `famulor create-crawl-source` | [Create a crawl source](https://docs.famulor.io/api-reference/knowledge-bases/create-a-crawl-source) |
| `createDriveSource` | `POST /knowledge-bases/{id}/drive-sources` | `famulor create-drive-source` | [Create a cloud drive source](https://docs.famulor.io/api-reference/knowledge-bases/create-a-cloud-drive-source) |
| `createKnowledgeBase` | `POST /knowledge-bases` | `famulor create-knowledge-base` | [Create a knowledge base](https://docs.famulor.io/api-reference/knowledge-bases/create-a-knowledge-base) |
| `createKnowledgeBaseFaq` | `POST /knowledge-bases/{id}/faqs` | `famulor create-knowledge-base-faq` | [Create and publish an FAQ entry](https://docs.famulor.io/api-reference/knowledge-bases/create-and-publish-an-faq-entry) |
| `deleteCrawlSource` | `DELETE /knowledge-bases/{id}/crawl-sources/{sourceId}` | `famulor delete-crawl-source` | [Delete a crawl source](https://docs.famulor.io/api-reference/knowledge-bases/delete-a-crawl-source) |
| `deleteDriveSource` | `DELETE /knowledge-bases/{id}/drive-sources/{sourceId}` | `famulor delete-drive-source` | [Delete a cloud drive source](https://docs.famulor.io/api-reference/knowledge-bases/delete-a-cloud-drive-source) |
| `deleteKnowledgeBase` | `DELETE /knowledge-bases/{id}` | `famulor delete-knowledge-base` | [Delete a knowledge base](https://docs.famulor.io/api-reference/knowledge-bases/delete-a-knowledge-base) |
| `deleteKnowledgeBaseDocument` | `DELETE /knowledge-bases/{id}/documents/{docId}` | `famulor delete-knowledge-base-document` | [Delete a document](https://docs.famulor.io/api-reference/knowledge-bases/delete-a-document) |
| `deleteKnowledgeBaseDocuments` | `POST /knowledge-bases/{id}/documents/delete` | `famulor delete-knowledge-base-documents` | [Delete documents in bulk](https://docs.famulor.io/api-reference/knowledge-bases/delete-documents-in-bulk) |
| `deleteKnowledgeBaseFaq` | `DELETE /knowledge-bases/{id}/faqs/{faqId}` | `famulor delete-knowledge-base-faq` | [Delete an FAQ entry](https://docs.famulor.io/api-reference/knowledge-bases/delete-an-faq-entry) |
| `discoverCrawlSourcePaths` | `POST /knowledge-bases/{id}/crawl-sources/discover` | `famulor discover-crawl-source-paths` | [Discover website crawl paths](https://docs.famulor.io/api-reference/knowledge-bases/discover-website-crawl-paths) |
| `getCrawlSource` | `GET /knowledge-bases/{id}/crawl-sources/{sourceId}` | `famulor get-crawl-source` | [Get a crawl source](https://docs.famulor.io/api-reference/knowledge-bases/get-a-crawl-source) |
| `getDriveSource` | `GET /knowledge-bases/{id}/drive-sources/{sourceId}` | `famulor get-drive-source` | [Get a cloud drive source](https://docs.famulor.io/api-reference/knowledge-bases/get-a-cloud-drive-source) |
| `getKnowledgeBase` | `GET /knowledge-bases/{id}` | `famulor get-knowledge-base` | [Get a knowledge base](https://docs.famulor.io/api-reference/knowledge-bases/get-a-knowledge-base) |
| `getKnowledgeBaseFaq` | `GET /knowledge-bases/{id}/faqs/{faqId}` | `famulor get-knowledge-base-faq` | [Get an FAQ entry](https://docs.famulor.io/api-reference/knowledge-bases/get-an-faq-entry) |
| `listCrawlSourcePages` | `GET /knowledge-bases/{id}/crawl-sources/{sourceId}/pages` | `famulor list-crawl-source-pages` | [List indexed crawl-source pages](https://docs.famulor.io/api-reference/knowledge-bases/list-indexed-crawl-source-pages) |
| `listCrawlSources` | `GET /knowledge-bases/{id}/crawl-sources` | `famulor list-crawl-sources` | [List crawl sources](https://docs.famulor.io/api-reference/knowledge-bases/list-crawl-sources) |
| `listDriveSources` | `GET /knowledge-bases/{id}/drive-sources` | `famulor list-drive-sources` | [List cloud drive sources](https://docs.famulor.io/api-reference/knowledge-bases/list-cloud-drive-sources) |
| `listKnowledgeBaseAssistants` | `GET /knowledge-bases/{id}/assistants` | `famulor list-knowledge-base-assistants` | [List assistants using a knowledge base](https://docs.famulor.io/api-reference/knowledge-bases/list-assistants-using-a-knowledge-base) |
| `listKnowledgeBaseDocuments` | `GET /knowledge-bases/{id}/documents` | `famulor list-knowledge-base-documents` | [List documents](https://docs.famulor.io/api-reference/knowledge-bases/list-documents) |
| `listKnowledgeBaseFaqs` | `GET /knowledge-bases/{id}/faqs` | `famulor list-knowledge-base-faqs` | [List FAQ entries and knowledge gaps](https://docs.famulor.io/api-reference/knowledge-bases/list-faq-entries-and-knowledge-gaps) |
| `listKnowledgeBases` | `GET /knowledge-bases` | `famulor list-knowledge-bases` | [List knowledge bases](https://docs.famulor.io/api-reference/knowledge-bases/list-knowledge-bases) |
| `listKnowledgeDocumentChunks` | `GET /knowledge-bases/{id}/documents/{docId}/chunks` | `famulor list-knowledge-document-chunks` | [List document chunks](https://docs.famulor.io/api-reference/knowledge-bases/list-document-chunks) |
| `runCrawlSource` | `POST /knowledge-bases/{id}/crawl-sources/{sourceId}/run` | `famulor run-crawl-source` | [Run a crawl now](https://docs.famulor.io/api-reference/knowledge-bases/run-a-crawl-now) |
| `runDriveSource` | `POST /knowledge-bases/{id}/drive-sources/{sourceId}/run` | `famulor run-drive-source` | [Run a cloud drive sync now](https://docs.famulor.io/api-reference/knowledge-bases/run-a-cloud-drive-sync-now) |
| `searchKnowledgeBase` | `POST /knowledge-bases/{id}/search` | `famulor search-knowledge-base` | [Search knowledge or query a table](https://docs.famulor.io/api-reference/knowledge-bases/search-knowledge-or-query-a-table) |
| `setKnowledgeBaseAssistants` | `PUT /knowledge-bases/{id}/assistants` | `famulor set-knowledge-base-assistants` | [Replace assistants using a knowledge base](https://docs.famulor.io/api-reference/knowledge-bases/replace-assistants-using-a-knowledge-base) |
| `updateCrawlSource` | `PATCH /knowledge-bases/{id}/crawl-sources/{sourceId}` | `famulor update-crawl-source` | [Update a crawl source](https://docs.famulor.io/api-reference/knowledge-bases/update-a-crawl-source) |
| `updateDriveSource` | `PATCH /knowledge-bases/{id}/drive-sources/{sourceId}` | `famulor update-drive-source` | [Update a cloud drive source](https://docs.famulor.io/api-reference/knowledge-bases/update-a-cloud-drive-source) |
| `updateKnowledgeBaseFaq` | `PATCH /knowledge-bases/{id}/faqs/{faqId}` | `famulor update-knowledge-base-faq` | [Review or update an FAQ entry](https://docs.famulor.io/api-reference/knowledge-bases/review-or-update-an-faq-entry) |
