<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# Endura 🎯

## Basic Details

### Team Name: Quackroach

### Team Members
- Member 1: Shreya Sajalan - Albertian Institute of Science and Technology
- Member 2: Elna Susan] - Albertian Institute of Science and Technology

### Hosted Project Link
[mention your project hosted link here]

### Project Description
Endura is a private, encrypted digital legacy platform that helps individuals securely store their financial assets, digital accounts, legal documents, and personal wishes — and ensures they're handed over to the right person at the right time, automatically.

### The Problem statement
In India, millions of families are left in chaos after an unexpected loss — bank accounts, LIC policies, PPF/EPF, and property documents remain unknown or inaccessible to loved ones. With no centralized record and no designated person to act, wealth disappears into paperwork and families are left with confusion instead of closure.

### The Solution
Endura gives users a secure, guided vault to document all their assets, accounts, and final wishes in one place. A trusted executor is assigned in advance but sees nothing while the user is alive. A smart check-in system monitors activity — and only upon verified death is the vault unlocked, delivering a structured PDF report, legacy letters, and a clear action checklist. No chaos. Just closure.

---

## Technical Details

### Technologies/Components Used

**For Software:**
- **Languages:** Python, JavaScript, HTML, CSS
- **Frameworks:** Django (backend), Vue.js (frontend)
- **Database:** SQLite3
- **Libraries:** Django REST Framework, Axios, Vue Router, Pinia, ReportLab (PDF generation)
- **Tools:** VS Code, Git, Postman, pip, npm
- **Security:** AES Encryption for all vault data, document-verified death confirmation

---

## Features

- Encrypted Vault: Store personal info, financial assets, digital accounts, physical assets, legacy letters, and dependent details — all AES encrypted.
- Executor System: Assign one trusted person who has zero vault access while you're alive. They're only notified and granted access after verified death.
- Smart Check-In: Automated 6-month email check-ins. If 3 consecutive reminders go unanswered over 30 days, the executor is alerted.
- Verified Handover: Executor uploads a death verification document. Once confirmed, they receive a structured PDF report, legacy letters, and a step-by-step action checklist.
- Completion Score: A live progress tracker shows users what's filled and what's still missing in their vault.

---

## Implementation

### For Software:

#### Installation
```
# Clone the repository
git clone https://github.com/your-username/endura.git
cd endura

# Backend setup
cd backend
pip install -r requirements.txt
python manage.py migrate

# Frontend setup
cd ../frontend
npm install
```

#### Run
```
# Start Django backend
cd backend
python manage.py runserver

# Start Vue.js frontend (separate terminal)
cd frontend
npm run dev
```

> Backend runs on `http://localhost:8000` | Frontend on `http://localhost:5173`

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

![Screenshot1](Add screenshot 1 here with proper name)
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
*Explain your system architecture - components, data flow, tech stack interaction*

**Application Workflow:**

![Workflow](docs/workflow.png)
*Add caption explaining your workflow*

---

#### Build Photos

![Team](Add photo of your team here)

![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `http://localhost:8000/api/`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/auth/register/` | Register a new user |
| `POST` | `/auth/login/` | Authenticate and receive token |
| `GET` | `/vault/` | Fetch the authenticated user's vault |
| `PUT` | `/vault/update/` | Update vault section data |
| `POST` | `/executor/assign/` | Assign a trusted executor |
| `POST` | `/checkin/` | Log a user check-in response |
| `POST` | `/executor/verify/` | Executor submits death verification document |
| `GET` | `/executor/handover/` | Retrieve unlocked vault report (post-verification) |

---
## Project Demo

### Video

https://github.com/user-attachments/assets/66205ea5-550b-4197-96cb-3369426b0d6f


### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Name 1]: [Specific contributions - e.g., Frontend development, API integration, etc.]
- [Name 2]: [Specific contributions - e.g., Backend development, Database design, etc.]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
