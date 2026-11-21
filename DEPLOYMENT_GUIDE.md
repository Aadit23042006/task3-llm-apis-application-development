# Deployment Guide — Live Website

## 1. Project Overview

This project is a deployable Streamlit web application developed as part of the **LLM APIs & Application Development** task.

The application provides an interactive AI chat interface with support for:

- Large Language Model (LLM) API integration.
- Interactive chat conversations.
- Conversation history.
- Custom system instructions.
- Model configuration and parameters.
- JSON-formatted responses.
- API error handling.
- Rate-limit handling and retry logic.
- Token usage tracking.
- API cost estimation.
- Demo Mode for testing without an API key.

The project source code and deployment configuration are included in the GitHub repository.

**Deployment Status:** The public application has been opened and verified in Demo Mode. The interface loaded, a prompt was submitted, a simulated response appeared, and the usage/cost summary displayed. Live API inference on the hosted application remains unverified.

---

## 2. Deployment Platform

| Component | Platform |
|---|---|
| Application Framework | Streamlit |
| Source Code Repository | GitHub |
| Hosting Platform | Streamlit Community Cloud |
| Application Entry Point | `app.py` |
| Dependency Management | `requirements.txt` |
| Deployment Branch | `main` |
| Application URL | Streamlit-generated public URL |

### Live Application URL

https://task3-llm-apis-application-development-7xpay5junqzq5ksypgpuyt.streamlit.app/

---

## 3. Prerequisites

Before deploying the application, ensure the following are available:

1. A GitHub account.
2. A GitHub repository containing the project source code.
3. Streamlit Community Cloud access.
4. The required project files.
5. An LLM API key, if Live API Mode is required.

### Required Project Files

The repository root should contain the following files:

```text
Task3_LLM_APIs_Application_Development/
│
├── app.py
├── requirements.txt
├── README.md
├── DEPLOYMENT_GUIDE.md
├── .gitignore
├── linkedin_post.md
│
├── notebooks/
│   └── Task3_LLM_APIs_Application_Development.ipynb
│
└── Additional application modules and configuration files
```

The exact folder structure may vary depending on the final project implementation.

**Important:** `app.py` and `requirements.txt` must be available at the repository root if that is the application path configured during deployment.

---

## 4. GitHub Repository Setup

### Step 1: Create a GitHub Repository

1. Sign in to GitHub.
2. Click **New repository**.
3. Enter the repository name.
4. Add a project description.
5. Select Public or Private according to the submission requirements.
6. Create the repository.

### Step 2: Upload the Project

Upload the complete project contents to the repository.

Ensure the repository contains:

- `app.py`
- `requirements.txt`
- `README.md`
- `DEPLOYMENT_GUIDE.md`
- `.gitignore`
- Required source code modules
- The project notebook, if required for submission
- Supporting documentation

### Step 3: Verify the Repository

Confirm the following:

- The application source code is available.
- The required dependencies are listed.
- The deployment guide is included.
- No API keys or private credentials are committed.
- The main application file is located at the expected path.
- The repository contains the latest project version.

---

## 5. Deploy to Streamlit Community Cloud

### Step 1: Open Streamlit Community Cloud

Visit:

https://share.streamlit.io/

Sign in using your GitHub account.

### Step 2: Create a New Application

Select:

**Create app → Deploy an app**

The interface may use slightly different wording depending on the current Streamlit dashboard.

### Step 3: Configure the Application

Configure the deployment settings:

| Setting | Value |
|---|---|
| Repository | Task 3 GitHub repository |
| Branch | `main` |
| Main file path | `app.py` |
| App URL | Streamlit-generated URL |
| Python dependencies | `requirements.txt` |

Ensure the repository and branch contain the latest application code.

### Step 4: Deploy

Click **Deploy**.

Streamlit Community Cloud will:

1. Retrieve the application from GitHub.
2. Install dependencies from `requirements.txt`.
3. Configure the application environment.
4. Start the Streamlit application.
5. Generate or activate the public application URL if deployment succeeds.

The initial deployment may take several minutes.

---

## 6. Configure Application Secrets

Application secrets must be configured through the hosting platform's secret-management interface.

Never commit API keys, passwords, or private credentials to GitHub.

### Configure Secrets

Open the deployed application settings.

Navigate to:

**Settings → Secrets**

Add the configuration required by the application.

### Example Configuration

The following example is for an OpenAI-compatible LLM provider:

```toml
LLM_API_KEY = "your-provider-api-key"
LLM_BASE_URL = "https://api.openai.com/v1"
LLM_MODEL = "gpt-4o-mini"

DEMO_MODE = "false"

INPUT_COST_PER_1K = "0.00015"
OUTPUT_COST_PER_1K = "0.00060"
```

Replace the example values with the configuration supported by your selected provider and application.

### Security Requirements

- Never use a real API key in documentation.
- Never commit `.env` files.
- Never expose API keys in screenshots.
- Never display secrets in application logs.
- Configure secrets through the hosting platform.
- Use the correct provider endpoint and model.
- Verify API access and account quota before enabling Live API Mode.

If the application is deployed without an API key, Demo Mode should remain enabled.

---

## 7. Demo Mode

Demo Mode allows the application to be tested without a live LLM API connection.

### Benefits

- No API key is required.
- No external API charges are incurred.
- The application interface can be tested.
- Chat interactions can be demonstrated.
- Application features can be verified.
- Deployment can be checked independently of API availability.

### Configuration

Use the application's Demo Mode setting or the appropriate deployment configuration.

If the application supports environment-based configuration, use the setting expected by the application implementation.

**Demo Mode responses are simulated and should not be represented as genuine LLM-generated responses.**

---

## 8. Live LLM API Mode

Live API Mode enables the application to communicate with an actual LLM provider.

### Requirements

- A valid API key.
- A supported API endpoint.
- A model accessible to the API account.
- Sufficient account quota or billing balance.
- Correct application secrets.
- A working internet connection from the hosting environment.

### Verification

After configuring the secrets:

1. Open the deployed application.
2. Confirm Demo Mode is disabled.
3. Enter a test prompt.
4. Submit the prompt.
5. Verify that the response is generated by the configured provider.
6. Check token usage, if available.
7. Check the estimated API cost.
8. Verify that the API key is not displayed.

Provider availability, model access, account quotas, and pricing may change.

---

## 9. Verify the Deployed Website

After deployment, perform the following verification checks.

| Test | Expected Result |
|---|---|
| Application URL | Opens successfully |
| Application interface | Loads without errors |
| Chat input | Accepts user prompts |
| Demo Mode | Returns simulated responses |
| Live API Mode | Returns genuine provider responses when configured |
| Conversation history | Maintains messages during the session |
| Clear conversation | Resets the conversation |
| System instructions | Can be customized |
| Model parameters | Available according to implementation |
| JSON response mode | Produces valid JSON when requested |
| Error handling | Displays appropriate error messages |
| Rate-limit handling | Handles provider rate limits gracefully |
| Token usage | Displays usage when supported |
| Cost estimation | Displays estimated API costs |
| Secrets security | API credentials are not exposed |
| Refresh | Application reloads successfully |

Only mark a test as passed after it has been verified on the deployed application.

---

## 10. Obtain and Document the Live URL

Streamlit Community Cloud generates or activates the public URL associated with the application deployment.

The URL generally follows this format:

```text
https://your-app-name.streamlit.app/
```

The above URL is an example only.

### Actual Project URL

https://task3-llm-apis-application-development-7xpay5junqzq5ksypgpuyt.streamlit.app/

### Update the README

The README should contain the actual application URL and the current deployment status.

### Current README Status

```markdown
## Live Application

**Deployment Platform:** Streamlit Community Cloud

**Deployment Status:** Pending deployment verification.

**Live URL:**

https://task3-llm-apis-application-development-7xpay5junqzq5ksypgpuyt.streamlit.app/
```

After deployment succeeds and the application has been tested, update the status to:

```markdown
## Live Application

**Deployment Platform:** Streamlit Community Cloud

**Deployment Status:** Successfully deployed and verified.

**Live URL:**

https://task3-llm-apis-application-development-7xpay5junqzq5ksypgpuyt.streamlit.app/
```

Replace or update the deployment status only after actual verification.

Do not claim successful deployment or verification before testing the public application.

---

## 11. Troubleshooting

### Application Build Failure

Possible causes:

- Missing dependencies.
- Incorrect `requirements.txt`.
- Incorrect main file path.
- Incompatible Python package versions.
- Incorrect repository structure.

Solutions:

1. Verify `requirements.txt`.
2. Confirm `app.py` exists at the configured path.
3. Review the Streamlit deployment logs.
4. Correct dependency errors.
5. Redeploy.

### API Authentication Error

Possible causes:

- Incorrect API key.
- Missing secrets.
- Incorrect provider endpoint.
- Invalid model name.
- API account restrictions.

Solutions:

1. Verify the secret names.
2. Verify the API key privately with the provider.
3. Check model availability.
4. Confirm endpoint compatibility.
5. Review the application logs without exposing credentials.

### Rate Limit Error

Possible causes:

- API quota exhausted.
- Requests submitted too frequently.
- Provider rate limits exceeded.

Solutions:

1. Check the provider's usage dashboard.
2. Verify available quota.
3. Reduce unnecessary requests.
4. Allow retry logic to handle temporary failures.
5. Use Demo Mode when live API access is unavailable.

### Application Does Not Start

Possible causes:

- Python dependency errors.
- Missing modules.
- Incorrect configuration.
- Application startup exceptions.

Solutions:

1. Review the Streamlit logs.
2. Verify the dependencies.
3. Check the application entry point.
4. Confirm the configuration values.
5. Fix the error and redeploy.

### Application URL Is Unavailable

Possible causes:

- Deployment is still running.
- Build failed.
- Application crashed.
- Hosting service temporarily unavailable.
- Application access or deployment configuration issue.

Solutions:

1. Check deployment status.
2. Review the build logs.
3. Restart or redeploy if necessary.
4. Verify the GitHub repository connection.
5. Check application access settings.
6. Open the application URL again after successful deployment.

---

## 12. Security and Privacy

The following security practices must be followed:

- API keys must not be committed to GitHub.
- Secrets must be configured using the hosting platform's secrets manager.
- `.env` files must be excluded using `.gitignore`.
- `.streamlit/secrets.toml` must not be committed.
- Credentials must not be included in screenshots.
- Error messages must not expose private credentials.
- API keys must not be embedded in frontend code.
- Only necessary application configuration should be exposed publicly.
- API usage and cost must be monitored when Live API Mode is enabled.

---

## 13. Deployment Status

Deployment status must be updated based on actual verification.

### Current Deployment Status

```text
Deployment Status: Public deployment verified in Demo Mode

Platform: Streamlit Community Cloud

Application: Task 3 - LLM APIs & Application Development

Live URL:
https://task3-llm-apis-application-development-7xpay5junqzq5ksypgpuyt.streamlit.app/

GitHub Repository: Connected

Application Registration: Completed

Deployment Build: Public app opened and interface rendered

Public Accessibility: Verified

Application Functionality: Demo Mode prompt/response and usage display verified
```

### Before Successful Verification

For full deployment verification, confirm the following additional items as applicable:

- The Streamlit deployment/build succeeds.
- The public application URL opens.
- The application interface loads.
- Chat functionality is tested.
- Demo Mode is verified.
- The application does not expose secrets.

### After Successful Deployment

Update the status to:

```text
Deployment Status: Successfully deployed and verified

Platform: Streamlit Community Cloud

Application: Task 3 - LLM APIs & Application Development

Live URL:
https://task3-llm-apis-application-development-7xpay5junqzq5ksypgpuyt.streamlit.app/

Deployment Build: Successful

Public Accessibility: Verified

Application Functionality: Verified
```

Do not use the successful deployment status until the application has been deployed and tested.

---

## 14. Final Deployment Checklist

### Project Files

- [ ] Application source code uploaded to GitHub.
- [ ] Repository contains `app.py`.
- [ ] Repository contains `requirements.txt`.
- [ ] Repository contains `README.md`.
- [ ] Repository contains `DEPLOYMENT_GUIDE.md`.
- [ ] `.gitignore` configured correctly.
- [ ] No API keys or credentials committed.
- [ ] Project notebook included, if required.

### GitHub

- [ ] GitHub repository verified.
- [ ] Latest code uploaded.
- [ ] Correct branch selected.
- [ ] Required files available.
- [ ] Repository access configured appropriately.

### Streamlit Community Cloud

- [ ] Streamlit Community Cloud connected to GitHub.
- [ ] Correct repository selected.
- [ ] Correct branch selected.
- [ ] Correct application entry point configured.
- [ ] Dependencies installed successfully.
- [ ] Deployment completed successfully.
- [ ] Public application URL generated.

### Application Testing

- [ ] Public URL opened and tested.
- [ ] Application interface loads.
- [ ] Demo Mode verified.
- [ ] Live API Mode verified, if configured.
- [ ] Chat input tested.
- [ ] Chat responses verified.
- [ ] Conversation history verified.
- [ ] Clear conversation verified.
- [ ] Custom system instructions verified.
- [ ] JSON response mode verified.
- [ ] Error handling verified.
- [ ] Rate-limit handling verified.
- [ ] Token usage verified, if supported.
- [ ] Cost estimation verified, if supported.
- [ ] Application refresh verified.

### Security

- [ ] Secrets security verified.
- [ ] No credentials exposed.
- [ ] API key not present in repository.
- [ ] API key not present in screenshots.
- [ ] Secrets configured securely.

### Documentation and Submission

- [ ] README updated with the actual Live URL.
- [ ] Deployment status accurately documented.
- [ ] Deployment screenshots saved.
- [ ] GitHub repository link prepared for submission.
- [ ] Live application link prepared for submission.
- [ ] Deployment verification completed.

---

## 15. Deliverables

The documented deployment deliverables include:

1. GitHub repository containing the application source code.
2. `README.md` containing the project overview and setup instructions.
3. `DEPLOYMENT_GUIDE.md` containing deployment instructions.
4. `requirements.txt` containing application dependencies.
5. Google Colab notebook, if required by the task.
6. Public Streamlit application URL after successful deployment.
7. Screenshots demonstrating the deployed application.
8. Verification of the deployed application features.

---

## Conclusion

The application is designed to be deployed using Streamlit Community Cloud.

The GitHub repository contains the source code and deployment configuration required to host the application.

The public Streamlit application has been opened and verified in Demo Mode. The interface, prompt submission, simulated response, and usage/cost summary were checked. Live API inference and any feature not explicitly listed as verified remain unverified. Demo Mode does not represent genuine LLM inference.
