# Contribution Rules for DataWhiz

This document outlines the required standards for anyone submitting Pull Requests (PRs) to the DataWhiz repository. Contributions that do not follow these rules will be rejected.


## Feature and Code Requirements

### 1. Verify All Features
Any features you modify or add must be:
- Fully functional in both CLI and GUI modes
- Complete and not partially implemented or broken

### 2. Source Code Only
Only modify the source code files:
- DataWhiz_CLI.py
- DataWhiz_GUI.py

Do not edit or reverse-engineer the precompiled binaries.

### 3. Keep API Code Untouched
The following line must remain unchanged:

    _cr_u = API_ENDPOINT = "REDACTED_FOR_PUBLIC_RELEASE_CONTACT_X_@AnonKryptiQuz"

You are not required to implement or use a working API endpoint. This part can be skipped during testing.

### 4. Testing Required
Your changes must be tested on at least one Linux distribution. In your PR description, mention:
- The name and version of the Linux distribution used
- The Python version used during testing

### 5. Clear Documentation in Pull Request
Your PR description must clearly explain:
- What was changed
- Why the change was necessary
- Any known limitations or edge cases
- The environment where the code was tested

### 6. Respect Original Design
You must maintain the current structure, naming conventions, and user experience flow. Do not introduce large design changes without prior discussion. If your changes significantly affect the UX or UI, open a GitHub issue first.


## Security, Scope, and Code Integrity

### 7. No Malicious Code
Submitted code must not include:
- Data collection or telemetry features
- Shell injections or unauthorized system access
- Suspicious or obfuscated behavior

Violations will lead to permanent bans and GitHub reporting.

### 8. Do Not Obfuscate Code
All contributions must be:
- Readable
- Well-commented
- Free from encryption or code minimization

Obfuscated or unreadable code will be rejected.

### 9. No Rebranding or Fork-Washing
You may fork the repository for personal or educational use, but public forks must:
- Retain attribution to the original project
- Avoid rebranding or misleading repackaging

Permission is required for any public releases under a different name or appearance.

### 10. Respect API Rate Limits
If testing with a real API (after receiving access), avoid automated spamming or abuse. Violations may result in API bans and PR rejection.

### 11. No Major UI Redesigns Without Approval
Significant changes to GUI layout or functionality must first be proposed via an issue. Wait for maintainer approval before submission.

### 12. Maintain CLI/GUI Compatibility
Ensure that any changes are reflected in both the CLI and GUI versions if applicable. Avoid introducing functionality that only works in one mode unless discussed.

### 13. Avoid Dependency Bloat
Do not add new libraries or external dependencies without discussion. Stick to existing tech stack unless absolutely required.


## AI-Generated Code

If using AI assistance such as ChatGPT, Copilot, or Gemini:
- You are responsible for understanding and validating the generated code
- Optionally mention AI usage in your PR for transparency
- Blindly pasted, untested AI code will be rejected


## Final Notes

These rules are in place to maintain code quality, prevent misuse, and ensure maintainability. If anything is unclear or if your contribution falls outside these rules, open a GitHub issue first to discuss it with the maintainer.

