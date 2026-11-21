# Project Structure

## Task 3: LLM APIs & Application Development

This document provides an overview of the project directory structure, application components, source code organization, testing files, documentation, and deployment information for the **AI Chat Lab — API-Powered Conversational AI Application**.

---

## 1. Directory Structure

```text
Task3_LLM_APIs_Application_Development/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── config.toml
├── notebooks/
│   └── Task3_LLM_APIs_Application_Development.ipynb
├── tests/
│   └── test_app.py
├── DEPLOYMENT_GUIDE.md
├── PROJECT_STRUCTURE.md
└── linkedin_post.md
```

---

## 2. Root Directory Files

| File | Description |
|---|---|
| `README.md` | Project overview, features, installation instructions, usage, technology stack, and project documentation. |
| `PROJECT_STRUCTURE.md` | Documentation explaining the project directory structure and the responsibilities of its components. |
| `DEPLOYMENT_GUIDE.md` | Step-by-step instructions for deploying the application using Streamlit Community Cloud. |
| `requirements.txt` | Python dependencies required to install and run the application. |
| `.env.example` | Example environment variable configuration for API credentials and application settings. |
| `.gitignore` | Prevents sensitive files, virtual environments, cache files, and unnecessary generated files from being committed. |
| `app.py` | Main Streamlit application entry point. |
| `linkedin_post.md` | Prepared LinkedIn project announcement and internship task completion post. |

---

## 3. Streamlit Configuration

### `.streamlit/config.toml`

Contains Streamlit application configuration, including:

- Application theme
- UI configuration
- Server settings
- Hosting-related configuration

This file provides consistent application presentation and configuration across local development and deployment environments.

---

## 4. Source Code — `src/`

The `src/` directory contains the application's modular implementation.

| File | Responsibility |
|---|---|
| `__init__.py` | Initializes the Python source package. |
| `llm_client.py` | Handles LLM API configuration, request execution, provider integration, API errors, and transient-error retry logic. |
| `conversation.py` | Manages conversation messages, conversation history, system instructions, and message-related functionality. |
| `usage.py` | Provides token usage tracking and estimated API cost calculation utilities. |
| `demo.py` | Provides predefined demo responses and offline functionality without requiring live API credentials. |

### Architecture

The application separates its functionality into independent modules to improve maintainability, testing, and code organization.

```text
Streamlit User Interface
        │
        ▼
      app.py
        │
        ├── Conversation Management
        │       └── src/conversation.py
        │
        ├── LLM API Integration
        │       └── src/llm_client.py
        │
        ├── Token Usage & Cost Estimation
        │       └── src/usage.py
        │
        └── Demo Mode
                └── src/demo.py
```

---

## 5. Testing — `tests/`

The `tests/` directory contains unit tests for the application's core functionality.

| File | Testing Scope |
|---|---|
| `test_conversation.py` | Conversation history, message management, and system instructions. |
| `test_usage.py` | Token usage calculations and estimated API cost functionality. |
| `test_demo.py` | Demo mode functionality and sample response generation. |

Tests are designed to validate core components independently and help identify regressions during development.

---

## 6. Jupyter Notebook — `notebooks/`

### `Task3_LLM_APIs_Application_Development.ipynb`

The notebook provides an environment for experimenting with LLM API integration and understanding API-powered AI application development.

It includes:

- API configuration
- LLM API request examples
- Prompt and message handling
- Response generation
- API usage experimentation
- Error handling examples
- Google Colab compatibility

The notebook can be opened and executed using Google Colab or a compatible Jupyter Notebook environment.

---

## 7. Application Features

The AI Chat Lab application includes the following functionality:

- Interactive AI chat interface built using Streamlit.
- Integration with an LLM API using an OpenAI-compatible interface.
- Conversation history management.
- Customizable system instructions.
- Model configuration and generation parameter controls.
- Structured JSON response support and validation.
- API error handling.
- Retry handling for transient errors and rate limits.
- Token usage tracking.
- Approximate API cost estimation.
- Demo Mode for testing without API credentials.
- Modular Python architecture.
- Unit tests for core application components.

---

## 8. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application development and backend logic. |
| Streamlit | Interactive web application interface. |
| LLM APIs | AI-powered response generation. |
| REST APIs | Communication with the LLM provider. |
| Google Colab | API experimentation and notebook execution. |
| Git | Version control. |
| GitHub | Source code repository and project hosting. |
| Streamlit Community Cloud | Application deployment platform. |
| Pytest | Unit testing framework. |

---

## 9. Deployment Information

### Deployment Platform

**Platform:** Streamlit Community Cloud

**Application:** AI Chat Lab — API-Powered Conversational AI Application

**Deployment Source:** GitHub Repository

**Branch:** `main`

**Entry Point:** `app.py`

### Live Application URL

https://task3-llm-apis-application-development-7xpay5junqzq5ksypgpuyt.streamlit.app/

### Deployment Status

**Status: Public deployment verified in Demo Mode; Live API inference not verified.**

The public application URL was opened and tested. The interface rendered, a prompt was submitted, Demo Mode returned a simulated response, and the usage/cost summary displayed. Live API inference on the hosted application has not been verified.

---

## 10. GitHub Repository

**Repository Name:** `task3-llm-apis-application-development`

**Repository URL:**

https://github.com/aadit23042006/task3-llm-apis-application-development

The GitHub repository contains the project source code, application configuration, documentation, tests, and notebook.

---

## 11. Security and Configuration

The project follows basic security practices for API-powered applications:

- API credentials are configured through environment variables or platform secrets.
- Sensitive credentials are excluded from version control.
- `.env.example` provides configuration guidance without exposing actual secrets.
- `.gitignore` prevents sensitive configuration and unnecessary files from being committed.
- Demo Mode allows application testing without exposing API credentials.
- Deployment secrets are configured separately from the source code.

---

## 12. Project Deliverables

The completed project repository includes:

- Interactive Streamlit AI Chat Lab application.
- LLM API integration.
- Modular source code.
- Conversation management functionality.
- Token usage and cost estimation.
- Demo Mode.
- Unit tests.
- Google Colab notebook.
- README documentation.
- Project structure documentation.
- Deployment guide.
- `.env.example` configuration template.
- GitHub repository.
- Streamlit Community Cloud deployment URL.
- LinkedIn project announcement draft.

---

## 13. Project Completion Status

| Component | Status |
|---|---|
| Application Development | Completed |
| LLM API Integration | Implemented |
| Conversation Management | Implemented |
| Demo Mode | Implemented |
| Token Usage Tracking | Implemented |
| Cost Estimation | Implemented |
| Error Handling | Implemented |
| Unit Tests | Implemented |
| Google Colab Notebook | Prepared |
| GitHub Repository | Available |
| Project Documentation | Completed |
| Deployment Guide | Prepared |
| Streamlit Deployment | Public URL and Demo Mode verified |
| Live API Inference | Not verified |
| LinkedIn Announcement | Prepared |

---

## 14. Conclusion

The project demonstrates practical implementation of Large Language Model APIs within an interactive web application.

Its modular architecture, API integration, conversation management, token usage tracking, error handling, demo functionality, testing structure, and deployment documentation provide a foundation for developing and deploying API-powered AI applications.

The project is organized to support maintainability, experimentation, testing, and future improvements in Generative AI application development.

**Project:** AI Chat Lab — API-Powered Conversational AI Application  
**Task:** Task 3 — LLM APIs & Application Development  
**Repository:** GitHub  
**Deployment Platform:** Streamlit Community Cloud


> **Repository accuracy note:** The directory tree above follows the uploaded README. Confirm it against the current GitHub file listing before submitting; this document does not independently inspect the live repository contents.
