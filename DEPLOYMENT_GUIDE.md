# Deployment Guide — AI Chat Lab

## 1. Overview

AI Chat Lab is a Streamlit application that uses an OpenAI-compatible chat-completions client to connect to an LLM provider. This guide describes deployment from GitHub to Streamlit Community Cloud.

- **GitHub:** https://github.com/Aadit23042006/task3-llm-apis-application-development
- **Live URL:** https://task3-llm-apis-application-development-5ruqmpmufgwkuerqduerld.streamlit.app
- **Main file:** `app.py`
- **Branch:** `main`
- **Dependencies:** `requirements.txt`

The URL above is the deployment address; verify public access and a prompt response before marking the hosted app as fully tested.

## 2. Prerequisites

- GitHub account and repository access
- Streamlit Community Cloud account connected to GitHub
- Project files in the repository root / expected folders
- API credentials only if Live API mode is required

## 3. Repository requirements

The repository should include:

- `app.py`
- `requirements.txt`
- `src/` application modules
- `.streamlit/config.toml` (if used)
- `.env.example`
- `README.md`
- `notebooks/` (assignment notebook)
- `tests/`
- documentation files

Do not commit `.env` or `.streamlit/secrets.toml`.

## 4. Deploy on Streamlit Community Cloud

1. Open https://share.streamlit.io/ and sign in with the GitHub account that owns or has access to the repository.
2. Click **Create app**.
3. Choose the option to deploy an existing app/repository.
4. Select repository `Aadit23042006/task3-llm-apis-application-development`.
5. Select branch `main`.
6. Set **Main file path** to `app.py`.
7. Optionally choose a custom app subdomain.
8. Open **Advanced settings** and select the supported Python version if needed.
9. Configure secrets as described below, if using Live API mode.
10. Click **Deploy** and wait for the build to finish.

Official instructions: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

## 5. Secrets and configuration

### Local environment

The app's configuration reads environment variables and loads `.env` for local development. Create `.env` locally (do not commit it):

```dotenv
DEMO_MODE=true
LLM_API_KEY=
LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
LLM_MODEL=gemini-2.5-flash
```

Set `DEMO_MODE=false` and supply a valid key to use Live API mode.

### Streamlit Community Cloud

In the app dashboard, open **Settings → Secrets** and enter TOML such as:

```toml
LLM_API_KEY = "replace_with_your_api_key"
LLM_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
LLM_MODEL = "gemini-2.5-flash"
DEMO_MODE = "false"
```

**Implementation note:** the current `src/llm_client.py` reads configuration using `os.getenv()` and the app calls `load_dotenv()`. Streamlit Cloud TOML secrets are accessed through `st.secrets`; they are not automatically made available as `os.environ` variables. To use these Cloud secrets in Live API mode, the application must explicitly read `st.secrets` or otherwise bridge the secrets into the configuration. Until that code is added and tested, leave Demo Mode enabled or treat hosted Live API mode as unverified.

Never paste an actual API key into README, this guide, source code, screenshots, or GitHub commits. If a key has been exposed, revoke it and generate a new one.

## 6. Demo Mode and Live API Mode

### Demo Mode

- No provider key required.
- Uses simulated responses from the demo module.
- Useful for verifying the UI and basic interaction.
- Does not represent live model inference.

### Live API Mode

Requires:
- valid provider API key
- correct API base URL
- model name available to the provider account
- configured quota/billing as required
- Cloud secrets correctly connected to the app configuration

Use a prompt and verify the provider-generated response before reporting Live API mode as tested.

## 7. Deployment verification checklist

After deployment, verify manually:

- [ ] App URL opens without access/authorization error
- [ ] App UI renders
- [ ] Chat input accepts a prompt
- [ ] Demo Mode returns a clearly simulated response
- [ ] Conversation history behaves as expected
- [ ] Clear conversation works
- [ ] System instructions and model parameters can be changed
- [ ] JSON mode works when supported
- [ ] Error messages do not expose secrets
- [ ] Usage/cost summary appears and is clearly identified as estimated where applicable
- [ ] Live API request succeeds, if configured
- [ ] API key is not visible in the UI or logs

Only check items that you actually tested.

## 8. Updating the deployment

Streamlit Community Cloud deploys from the connected GitHub repository. Commit and push changes to the selected branch; Cloud detects repository updates and redeploys the app. Dependency changes in `requirements.txt` may take longer because packages are reinstalled.

Official management documentation: https://docs.streamlit.io/deploy/streamlit-community-cloud/manage-your-app

## 9. Troubleshooting

| Issue | Likely cause | Suggested action |
|---|---|---|
| App access/does not exist message | Wrong app URL, account/workspace, or app sharing configuration | Confirm app appears in Streamlit workspace; verify URL and sharing settings |
| `ModuleNotFoundError` | Dependency missing | Add package to `requirements.txt` and redeploy |
| App fails to start | Wrong entrypoint or import/path issue | Confirm main file is `app.py`; review Cloud logs |
| Missing API key | Secret not loaded into app configuration | Verify secret name and code's secret/environment loading |
| Authentication error | Invalid/revoked key | Replace key in Cloud secrets; never print it |
| Rate limit/quota error | Provider limit reached | Check provider quota and retry later; retries cannot bypass exhausted quota |
| JSON response error | Provider/model may not support requested JSON mode or response invalid | Check model support and validate output |

## 10. Deployment record

- Repository: https://github.com/Aadit23042006/task3-llm-apis-application-development
- Live URL: https://task3-llm-apis-application-development-5ruqmpmufgwkuerqduerld.streamlit.app
- Platform: Streamlit Community Cloud
- Branch: `main`
- Entrypoint: `app.py`
- Hosted Live API inference: verify before marking as complete
