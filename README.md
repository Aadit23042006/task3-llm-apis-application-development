# Task 3 — LLM APIs & Application Development

## AI Chat Lab — API-Powered Conversational AI Application

An interactive Streamlit application that demonstrates how to integrate Large Language Models (LLMs) into real-world applications using APIs. The project provides a conversational AI interface with configurable model settings, conversation history, custom system instructions, structured JSON responses, API error handling, token usage tracking, cost estimation, and an offline demo mode.

---

## Project Overview

This project was developed as part of the **LLM APIs & Application Development** assignment.

The application demonstrates how an AI-powered product can communicate with an LLM through an API, manage conversation context, configure model parameters, handle errors gracefully, and provide a user-friendly interface for interacting with AI models.

The application supports both live API mode and demo mode, making it usable even without API credentials.

---

## Key Features

### 1. LLM API Integration
- Integration with OpenAI-compatible chat completion APIs.
- Configurable API endpoint.
- Configurable model name.
- Secure API key configuration through environment variables.
- Support for compatible providers.

### 2. Interactive AI Chat Interface
- Chat-based user interface built with Streamlit.
- User and assistant message display.
- Conversation history maintained during the session.
- Context-aware responses using previous messages.
- Clear conversation functionality.

### 3. Custom System Instructions
- Configure the AI assistant's behavior.
- Customize response tone, style, and role.
- Set instructions for specific use cases.
- Support for beginner-friendly, technical, concise, and creative responses.

### 4. Model Configuration
Adjust model parameters through the interface:

- **Temperature:** Controls response creativity.
- **Maximum output tokens:** Controls response length.
- **Model selection:** Configure the model used for API requests.
- **Custom instructions:** Define the assistant's behavior.

### 5. Structured JSON Responses
- Generate structured responses using JSON mode where supported.
- Validate generated JSON responses.
- Display formatted JSON output.
- Handle invalid structured responses gracefully.

### 6. Conversation Management
- Maintain conversation context.
- Store messages with appropriate roles.
- Support system, user, and assistant messages.
- Reset conversation history when required.

### 7. Error Handling
The application includes handling for common API errors, including:

- Authentication errors.
- Invalid API configuration.
- Connection failures.
- API request errors.
- Rate limits.
- Quota exhaustion.
- Invalid responses.
- Unexpected exceptions.

Error messages are designed to provide useful troubleshooting information without exposing sensitive credentials.

### 8. Token Usage & Cost Estimation
- Track reported prompt tokens.
- Track reported completion tokens.
- Calculate normalized total token usage.
- Detect inconsistencies in provider-reported token totals.
- Estimate API request costs using configurable example pricing.
- Display token usage information for API requests.

**Note:** Token counts and estimated costs depend on provider reporting and the pricing rates configured in the application. Estimates are not billing statements.

### 9. Rate-Limit Handling
- Bounded retry attempts.
- Exponential backoff.
- Random jitter to reduce repeated request collisions.
- Support for retry delays where applicable.
- Graceful handling of exhausted quotas and rate limits.

Retries cannot overcome a permanently exhausted API quota or provider restrictions.

### 10. Demo Mode
- Runs without an API key.
- Provides sample AI responses.
- Allows users to explore the application's functionality.
- Useful for demonstrations, testing, and development.

### 11. Google Colab Notebook
The project includes a Jupyter notebook demonstrating LLM API integration independently from the Streamlit application.

The notebook includes:

- API configuration.
- Secure API key input.
- Gemini API integration through an OpenAI-compatible endpoint.
- Conversation messages and roles.
- Live API requests.
- JSON response generation.
- Token usage normalization.
- Cost estimation.
- Error handling.
- Retry backoff.
- Regression checks.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web interface |
| OpenAI Python SDK | OpenAI-compatible API client |
| Google Gemini API | LLM inference provider |
| Jupyter Notebook | API experimentation and demonstration |
| JSON | Structured AI responses |
| Python dotenv | Environment configuration |
| Pytest | Automated testing |
| Git | Version control |
| GitHub | Source code hosting |
| Streamlit Community Cloud | Application deployment |

---

## Project Architecture

```text
User
 |
 v
Streamlit Chat Interface
 |
 +-- Chat Input
 +-- Conversation History
 +-- System Instructions
 +-- Model Configuration
 +-- JSON Response Mode
 |
 v
Application Logic
 |
 +-- API Configuration
 +-- Message Management
 +-- Request Validation
 +-- Error Handling
 +-- Retry Logic
 +-- Token Usage Normalization
 +-- Cost Estimation
 |
 v
LLM API Provider
 |
 v
AI Model Response
 |
 v
Streamlit Interface
```

---

## Project Structure

```text
Task3_LLM_APIs_Application_Development/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── .streamlit/
│   └── config.toml
│
├── notebooks/
│   └── Task3_LLM_APIs_Application_Development.ipynb
│
├── tests/
│   └── test_app.py
│
├── DEPLOYMENT_GUIDE.md
├── PROJECT_STRUCTURE.md
└── linkedin_post.md
```

*The actual repository structure may contain additional files depending on the final implementation.*

---

## Requirements

- Python 3.10 or newer (recommended)
- pip
- Git
- Internet connection for live API requests
- An API key for live mode
- Streamlit-compatible hosting for deployment

Demo mode does not require an API key.

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Aadit23042006/task3-llm-apis-application-development.git
```

Navigate to the project directory:

```bash
cd task3-llm-apis-application-development
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root for local development.

Example:

```env
DEMO_MODE=false
LLM_API_KEY=your_api_key_here
LLM_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/
LLM_MODEL=gemini-2.5-flash
```

Replace the placeholder API key with your own valid API key.

**Never commit your `.env` file or API credentials to GitHub.**

The application should be configured to use demo mode when credentials are unavailable.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will normally open in your browser at:

```text
http://localhost:8501
```

---

## Demo Mode vs Live API Mode

### Demo Mode

Demo mode allows the application to run without API credentials.

Features available in demo mode may include:

- Chat interface.
- Sample responses.
- Conversation management.
- UI configuration.
- Demonstration of application workflows.

Demo responses are simulated and are not generated by a live LLM provider.

### Live API Mode

Live API mode connects the application to a configured LLM provider.

Required configuration:

| Variable | Description |
|---|---|
| `LLM_API_KEY` | API authentication key |
| `LLM_BASE_URL` | API endpoint |
| `LLM_MODEL` | Model identifier |
| `DEMO_MODE` | Set to `false` for live API mode |

Provider availability, model access, quotas, rate limits, and pricing may vary.

---

## Google Colab Notebook

The project includes a notebook for testing LLM APIs and application development concepts independently.

### Notebook Location

```text
notebooks/Task3_LLM_APIs_Application_Development.ipynb
```

### How to Run

1. Open [Google Colab](https://colab.research.google.com/).
2. Upload the project's notebook.
3. Configure your API key through Colab Secrets or secure runtime input.
4. Run the notebook cells sequentially.
5. Review the live responses and test outputs.

The notebook is designed to avoid displaying API credentials.

---

## Testing

Run the automated tests from the project root:

```bash
pytest -q
```

Tests may cover:

- Application functionality.
- API configuration.
- Error handling.
- Token usage calculations.
- Cost estimation.
- JSON validation.
- Retry logic.
- Demo mode behavior.

### Verification Status

| Check | Status | Evidence / Scope |
|---|---|---|
| Public application URL opens | Verified | Hosted URL opened successfully |
| Interface loads | Verified | AI Chat Lab interface rendered |
| Prompt submission | Verified | Test prompt submitted |
| Demo Mode response | Verified | Simulated response displayed; not live LLM inference |
| Usage summary | Verified | Demo usage and estimated cost displayed |
| Live API inference on hosted app | Not verified | Requires valid provider credentials and an actual hosted request |
| Other feature-level manual checks | Not individually verified in this deployment session | Do not treat as hosted verification |

---

## Deployment

The application is designed to be deployable using Streamlit Community Cloud.

### Deployment Overview

1. Push the project to a GitHub repository.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub account.
4. Select the project repository.
5. Select `app.py` as the main application file.
6. Configure required secrets in the deployment settings.
7. Deploy the application.
8. Test the deployed application.

### Deployment Secrets

Configure API credentials through the hosting platform's secret-management system.

Example configuration:

```toml
LLM_API_KEY = "your_api_key"
LLM_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
LLM_MODEL = "gemini-2.5-flash"
DEMO_MODE = "false"
```

Do not store secrets directly in source code.

For complete instructions, refer to:

```text
DEPLOYMENT_GUIDE.md
```

### Live Application

**Deployment Status:** Public deployment verified in Demo Mode. Live API inference has not been verified on the hosted application.

**Live URL:** task3-llm-apis-application-development-7xpay5junqzq5ksypgpuyt.streamlit.app

The public application URL is available and has been opened and tested. The interface loaded, prompt submission worked, Demo Mode returned a simulated response, and the usage/cost summary displayed. Live API inference has not been verified on the hosted application.

---

## API Usage & Cost Management

The application includes basic token usage and cost-estimation functionality.

The estimated cost is calculated using configurable input and output token rates.

Example calculation:

```text
Estimated Cost =
(Input Tokens × Input Rate)
+
(Output Tokens × Output Rate)
```

Rates configured in the application are illustrative unless verified against the provider's current pricing documentation.

Actual billing may differ due to:

- Model pricing changes.
- Provider-specific token accounting.
- Cached tokens.
- Additional API features.
- Different billing units.
- Provider-reported usage discrepancies.

Always verify current provider pricing and quota information before using cost estimates for financial decisions.

---

## Security

Security considerations implemented or intended in the application:

- API keys are configured through environment variables or hosting secrets.
- Secrets are excluded from Git using `.gitignore`.
- API credentials are not intentionally displayed in the interface.
- Error handling avoids exposing sensitive configuration.
- Demo mode allows testing without credentials.
- Notebook credentials use secure input or platform secrets.

Before publishing the repository, verify that no API keys, private credentials, `.env` files, or personal information are committed.

---

## Limitations

- Live API functionality depends on provider availability.
- API requests require valid credentials in live mode.
- Rate limits and quotas are controlled by the API provider.
- Retry logic cannot bypass exhausted quotas.
- Cost calculations are estimates.
- Demo mode does not represent actual LLM inference.
- JSON response mode may depend on provider and model support.
- Deployment requires appropriate hosting configuration.
- The project does not guarantee uninterrupted API availability.

---

## Company Assignment Deliverables

| Deliverable | Location |
|---|---|
| Source code | GitHub repository |
| Streamlit application | `app.py` |
| Dependencies | `requirements.txt` |
| Google Colab notebook | `notebooks/` |
| Documentation | `README.md` |
| Deployment guide | `DEPLOYMENT_GUIDE.md` |
| Project structure | `PROJECT_STRUCTURE.md` |
| LinkedIn post draft | `linkedin_post.md` |
| Live application | Deployment URL, after successful deployment |

---

## Future Improvements

- Support additional LLM providers.
- Add persistent conversation storage.
- Add conversation export.
- Add authentication.
- Add advanced model selection.
- Improve provider-specific usage tracking.
- Add monitoring and logging.
- Add automated deployment.
- Add more comprehensive integration tests.
- Add configurable rate-limit policies.

---

## Author

**Aadit Choudhary**

B.Tech — Artificial Intelligence & Data Science

Rajasthan Institute of Engineering and Technology, Jaipur

---

## Acknowledgements

Developed as part of the **LLM APIs & Application Development** assignment, focusing on practical API integration, conversational AI, application development, testing, error handling, and deployment readiness.

---

## License

This project was developed for educational and internship-assignment purposes. Add an appropriate license file if redistribution or reuse is intended.
