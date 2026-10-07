---
title: Secure Groq API Key Demo
emoji: 🔐
colorFrom: blue
colorTo: purple
sdk: streamlit
app_file: app.py
pinned: false
---

# Secure Groq API Key Demo

A Streamlit application demonstrating secure Groq API key handling.

## Features

- Uses the Groq API
- Retrieves API keys from Streamlit Secrets
- Falls back to secure user input when no secret is configured
- Tests the Groq API connection

## Setup

### Streamlit Community Cloud

1. Deploy this repository using Streamlit Community Cloud.
2. Open the app settings.
3. Go to **Secrets**.
4. Add:

```toml
GROQ_API_KEY = "your-api-key-here"