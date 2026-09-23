# ElderAssist 🤝
> **A Simple, Modern, Responsive Web Application Empowering Elderly People with Everyday Digital Tasks**

ElderAssist connects senior citizens with compassionate community volunteers for guided assistance with digital payments, doctor appointments, online government forms, video calling family, and smartphone configuration.

Designed from the ground up with elderly accessibility in mind, ElderAssist features large touch targets, high contrast vision modes, adjustable text scaling, integrated voice reading (Text-to-Speech), simple step-by-step digital guides, live request status tracking, safe in-app messaging, reviews, and an administrator dashboard.

---

## 🌟 Key Features

### 👵 1. Elderly Experience
- **5 Core Help Categories**:
  - **💳 Digital Payments**: Pay electricity, water, gas, or broadband bills; QR code & UPI assistance; credit/debit card support.
  - **📅 Appointments**: Book doctor clinic visits, lab test sample pickups, and hospital checkups.
  - **📝 Online Forms**: Senior pension certificates, health card renewal, and transit concession passes.
  - **📹 Video Calls**: Set up WhatsApp, Zoom, or Google Meet calls to see children and grandchildren.
  - **📱 Smartphone Use**: Make fonts larger, clear "Storage Full" warnings, configure Wi-Fi and Bluetooth.
- **1-Tap Preset Suggestions**: Seniors don't need to type lengthy descriptions; tapping chips like *"Help me pay electricity bill"* autofills the request.
- **Visual Status Pipeline**: Clear 4-step progress tracker: `Submitted ➔ Assigned ➔ In Progress ➔ Finished`.
- **In-App Messaging**: Senior-tailored chat interface with 1-tap quick replies (*"I am ready now"*, *"Could you explain that step again?"*, *"Thank you so much!"*).
- **Ratings & Compliment Tags**: Seniors can rate volunteers with 5 stars and select heartfelt tags like *"Very Patient"*, *"Explained Clearly"*, and *"Warm & Friendly"*.

### 🤝 2. Volunteer Experience
- **Impact & Recognition**: Live tracker for seniors helped, hours volunteered, star rating (e.g. 4.9★), and badges (*"Kind Listener"*, *"Payment Wizard"*).
- **Available Requests Board**: Filter requests by category and urgency (*Need Help Today*, *In 1-2 Days*, *Flexible*).
- **1-Click Accept**: Volunteers can review details and immediately accept a task.
- **Active Task Management**: Chat with the senior, add helper notes, mark tasks *In Progress*, and resolve them when completed.

### 🛡️ 3. Admin Dashboard
- **Live Platform Metrics**: Real-time counters for Total Requests, Completed Tasks, Active Volunteers, Seniors Registered, and Community Satisfaction Rating.
- **Request Moderation**: Inspect all requests, reassign volunteers, update status, or delete expired requests.
- **User Directory**: View registered seniors and volunteers, inspect contact methods, and toggle role permissions.
- **Digital Guides Manager**: View, preview, and publish new interactive step-by-step guides.
- **Feedback Stream**: Review all comments and compliment tags submitted by seniors.

### 👁️ 4. Elderly-First Accessibility
- **🔤 Font Resizing Toolbar**: Instantly switch between **Normal (18px)**, **Large (22px)**, and **Extra Large (26px)** text with persistent preference.
- **🌓 High Contrast Mode**: One-click toggle for high contrast black/gold/cyan theme adhering to WCAG AAA standards for seniors with cataracts or low vision.
- **🔊 Voice Narration (Text-to-Speech)**: Built-in voice reader powered by the Web Speech API reads instructions, status updates, and guides aloud at a gentle, clear pace.
- **👆 Huge Touch Targets**: All interactive buttons are at least 52px–68px high with generous padding and prominent focus outlines.

---

## ⚡ Supabase Backend & Database

ElderAssist supports **both real-world Supabase backend integration AND an offline Interactive Demo Mode**:

### Dual-Mode Architecture
1. **Interactive Demo Mode (Default)**: Runs seamlessly out of the box with zero setup required. Uses browser `localStorage` to persist requests, messages, guides, profiles, and reviews.
2. **Supabase Production Mode**: Connects directly to Supabase Authentication and PostgreSQL database with Row Level Security (RLS).

### Setting up Supabase:
1. Create a free project at [supabase.com](https://supabase.com).
2. Go to your project's **SQL Editor**.
3. Open `supabase/schema.sql` from this repository, paste the contents into the SQL Editor, and click **Run**.
4. Retrieve your **Project URL** and **Anon Public Key** from *Project Settings ➔ API*.
5. In the ElderAssist web app:
   - Click the **⚡ Interactive Demo Mode** badge in the top accessibility bar.
   - Enter your `Project URL` and `Anon Key`.
   - Click **Save & Connect**. The badge will switch to green: **● Connected to Supabase**.

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8+ (already available on most systems)

### Running the Application Locally
1. Open a terminal or PowerShell in the project directory:
   ```bash
   python server.py
   ```
2. Open your web browser and navigate to:
   ```
   http://localhost:8000
   ```

### Running Automated Verification Tests
To run the automated test suite verifying files, schema, HTML accessibility, and server responses:
```bash
python test_app.py
```

---

## 📁 Project Structure

```
Elderassist/
├── index.html                   # Semantic, accessible single-page web app
├── css/
│   └── styles.css               # Elderly design system, high contrast mode, responsive layout
├── js/
│   ├── config.js                # App constants, categories, presets, and seed guides
│   ├── supabase-client.js       # Supabase client wrapper & local storage demo engine
│   ├── accessibility.js         # Font size scaler, high contrast toggle, Web Speech TTS
│   └── app.js                   # Application state, role routing, modals, and event handling
├── supabase/
│   └── schema.sql               # Full PostgreSQL DDL, RLS policies, and seed data
├── server.py                    # Lightweight Python 3 HTTP server with CORS & MIME support
├── test_app.py                  # Automated test verification suite
└── README.md                    # Project documentation & user guide
```

---

## 👥 Persona Switching for Demonstration

Use the pill switcher at the top of the page to easily test the application from any perspective:
- **👵 Senior (Margaret Jenkins)**: Post requests, test "Read Aloud", follow guides, chat with David, and leave a review.
- **🤝 Volunteer (David Chen)**: Browse open requests, accept Margaret's or Bob's tasks, send quick messages, and complete requests.
- **🛡️ Admin (Sarah Connor)**: Monitor KPIs, moderate requests, manage users, and author new guides.
