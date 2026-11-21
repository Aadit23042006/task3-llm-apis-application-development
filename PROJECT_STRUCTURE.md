# Project Structure

## Task 3 — LLM APIs & Application Development

This document maps the files in the repository and their roles.

```text
task3-llm-apis-application-development/
├── .streamlit/
│   └── config.toml
├── notebooks/
│   └── Task3_LLM_APIs_Application_Development.ipynb
├── src/
│   ├── __init__.py
│   ├── conversation.py
│   ├── demo.py
│   ├── llm_client.py
│   └── usage.py
├── tests/
│   ├── test_conversation.py
│   ├── test_demo.py
│   ├── test_llm_client_demo.py
│   └── test_usage.py
├── .env.example
├── .gitignore
├── app.py
├── DEPLOYMENT_GUIDE.md
├── README.md
├── linkedin_post.md
├── requirements.txt
└── test_rate_limit.py
```

## Root files

| File | Purpose |
|---|---|
| `app.py` | Streamlit application entry point and UI flow. |
| `requirements.txt` | Python dependencies for installation and deployment. |
| `.env.example` | Placeholder environment configuration; contains no real key. |
| `.gitignore` | Excludes secrets, local environments, caches, and generated files from Git. |
| `README.md` | Project overview, features, setup, tests, and links. |
| `DEPLOYMENT_GUIDE.md` | Deployment steps and cloud configuration notes. |
| `PROJECT_STRUCTURE.md` | Directory and module reference. |
| `linkedin_post.md` | Project announcement draft. |
| `test_rate_limit.py` | Additional retry/rate-limit test file. |

## Streamlit configuration — `.streamlit/`

| File | Purpose |
|---|---|
| `config.toml` | Streamlit UI/server configuration. |

## Source modules — `src/`

| File | Responsibility |
|---|---|
| `__init__.py` | Package initialization. |
| `conversation.py` | Conversation messages, history, and system instructions. |
| `demo.py` | Simulated responses for Demo Mode. |
| `llm_client.py` | Provider configuration, API calls, and request error handling. |
| `usage.py` | Token estimation, provider usage cost calculations, and cost formatting. |

## Notebook — `notebooks/`

`Task3_LLM_APIs_Application_Development.ipynb` demonstrates API configuration, LLM requests, message roles, JSON output, token usage normalization, cost estimation, safe errors, retry logic, and regression checks.

## Tests — `tests/`

| File | Scope |
|---|---|
| `test_conversation.py` | Conversation/message management. |
| `test_demo.py` | Demo response functionality. |
| `test_llm_client_demo.py` | Demo-mode client behavior. |
| `test_usage.py` | Usage and cost utilities. |

Run tests from the repository root:

```bash
pytest -q
```

## Application flow

```text
Streamlit UI (app.py)
   ├── Conversation state → src/conversation.py
   ├── LLM requests → src/llm_client.py
   ├── Demo responses → src/demo.py
   └── Usage/cost → src/usage.py
                 │
                 ▼
        OpenAI-compatible API
                 │
                 ▼
        Response displayed in UI
```

## Deployment

- Hosting: Streamlit Community Cloud
- GitHub repository: https://github.com/Aadit23042006/task3-llm-apis-application-development
- Branch: `main`
- Entry point: `app.py`
- Live URL: https://task3-llm-apis-application-development-5ruqmpmufgwkuerqduerld.streamlit.app

The URL is the deployment address. Confirm public access and Live API inference separately before reporting those checks as passed.
