# Software Requirements Specification (SRS)

## Project Title
SecurePass: Web-Based Password Security Analysis Toolkit

## Version
1.0

## Prepared By
Farah Tanveer

## Date
March 25, 2026

---

# 1. Introduction

## 1.1 Purpose

The purpose of this document is to define the software requirements for the **SecurePass: Web-Based Password Security Analysis Toolkit**.

SecurePass is a web-based password security analysis system designed to help users evaluate the strength and security of their passwords. The system performs password strength evaluation, entropy calculation, detection of commonly used passwords, and secure hash generation through a web-based graphical user interface.

The system uses **Python with Flask** as the backend and **HTML, CSS, and JavaScript** for the frontend interface.

This document serves as a reference for developers, testers, instructors, and users to understand the expected behavior and functionality of the system.

---

## 1.2 Scope

SecurePass is a **web-based application** that runs locally using a Flask server and is accessed through a web browser.

The system allows users to:

- Enter passwords through a web interface
- Evaluate password strength
- Calculate password entropy
- Detect commonly used weak passwords
- Generate password hashes
- Receive password security feedback

The application processes passwords locally and does **not store passwords**, ensuring privacy and security.

---

## 1.3 Definitions, Acronyms, and Abbreviations

| Term | Description |
|------|-------------|
| GUI | Graphical User Interface |
| SRS | Software Requirements Specification |
| API | Application Programming Interface |
| SHA | Secure Hash Algorithm |
| MD5 | Message Digest Algorithm 5 |
| Entropy | Measurement of password randomness |
| Hash | Encoded representation of data |
| HTTP | Hypertext Transfer Protocol |

---

## 1.4 Intended Audience

This document is intended for:

- Software developers
- Project reviewers
- Instructors
- End users
- Software testers

---

## 1.5 Overview

This document describes:

- System overview
- Functional requirements
- Non-functional requirements
- External interface requirements
- System features
- Future enhancements

---

# 2. Overall Description

## 2.1 Product Perspective

SecurePass is a **web-based password security system** that operates through a web browser.

The system architecture includes:

- Frontend Interface (HTML, CSS, JavaScript)
- Backend Server (Python Flask)
- Password Security Processing Modules
- Data Module (Common Password List)

The frontend communicates with the backend using HTTP requests, and the backend processes password analysis using Python logic modules.

---

## 2.2 Product Functions

The major functions of SecurePass include:

1. Accept password input from user
2. Analyze password strength
3. Calculate password entropy
4. Detect commonly used passwords
5. Generate secure password hashes
6. Display results on the web interface
7. Provide password security feedback

---

## 2.3 User Characteristics

Target users include:

- Students
- Developers
- General computer users
- Individuals interested in password security

User knowledge level:

- Basic computer knowledge required
- No advanced cybersecurity knowledge required

---

## 2.4 Operating Environment

SecurePass will run on:

- Operating System:
  - Windows
  - Linux
  - macOS

- Programming Language:
  - Python 3.x

- Backend Framework:
  - Flask

- Frontend Technologies:
  - HTML
  - CSS
  - JavaScript

- Web Browser:
  - Google Chrome
  - Mozilla Firefox
  - Microsoft Edge

- Hardware:
  - Standard desktop or laptop

---

## 2.5 Design Constraints

The system must:

- Be developed using Python and Flask
- Use HTML, CSS, and JavaScript for frontend
- Operate through a web browser
- Not store passwords
- Maintain modular backend design
- Use HTTP requests between frontend and backend

---

## 2.6 Assumptions and Dependencies

### Assumptions

- Python 3.x is installed
- Flask is installed
- A modern web browser is available
- Users input valid password text

### Dependencies

- Python Standard Libraries
- Flask Framework
- hashlib Library
- JavaScript Fetch API

---

# 3. System Features

---

## 3.1 Password Strength Evaluation

### Description

The system evaluates the strength of a password based on character composition and length.

### Functional Requirements

FR1.1 The system shall accept password input from the user.

FR1.2 The system shall check password length.

FR1.3 The system shall detect:

- Uppercase letters  
- Lowercase letters  
- Numbers  
- Symbols  

FR1.4 The system shall classify password strength as:

- Weak  
- Medium  
- Strong  

FR1.5 The system shall display the strength result on the interface.

---

## 3.2 Password Entropy Calculation

### Description

The system calculates password entropy to measure password randomness.

### Functional Requirements

FR2.1 The system shall calculate password entropy.

FR2.2 The system shall estimate password cracking time.

FR2.3 The system shall display entropy value.

---

## 3.3 Common Password Detection

### Description

The system checks whether the entered password exists in a list of commonly used passwords.

### Functional Requirements

FR3.1 The system shall compare password against stored weak password list.

FR3.2 The system shall display a warning if password is weak.

FR3.3 The system shall notify if password is safe.

---

## 3.4 Password Hash Generation

### Description

The system generates cryptographic hashes of the password.

### Functional Requirements

FR4.1 The system shall generate MD5 hash.

FR4.2 The system shall generate SHA-256 hash.

FR4.3 The system shall display generated hashes.

---

## 3.5 Web-Based Graphical User Interface

### Description

The system provides a browser-based graphical interface for user interaction.

### Functional Requirements

FR5.1 The system shall provide password input field.

FR5.2 The system shall provide buttons for:

- Analyze Password  
- Generate Hash  
- Clear Input  

FR5.3 The system shall display analysis results visually.

FR5.4 The system shall display messages clearly to the user.

---

# 4. External Interface Requirements

---

## 4.1 User Interface

The system provides a **web-based user interface** accessible through a browser.

The interface shall include:

- Password input textbox
- Analyze button
- Generate Hash button
- Clear button
- Output display section
- Status message area

The interface shall be:

- Simple
- User-friendly
- Responsive

---

## 4.2 Hardware Interface

No special hardware required.

The system runs on standard computers.

---

## 4.3 Software Interface

The system interacts with:

- Python Standard Libraries
- Flask Web Framework
- hashlib module
- JavaScript Fetch API
- Web Browser

---

## 4.4 Communication Interface

Communication between frontend and backend shall occur using:

- HTTP Requests
- Flask API Endpoints
- JavaScript Fetch API

All communication occurs locally between browser and Flask server.

---

# 5. Non-Functional Requirements

---

## 5.1 Performance Requirements

The system shall:

- Process password analysis within 1 second
- Provide fast response time

---

## 5.2 Security Requirements

The system shall:

- Not store passwords
- Process passwords locally
- Prevent data leakage
- Handle password data securely

---

## 5.3 Usability Requirements

The system shall:

- Provide simple navigation
- Use readable fonts
- Display results clearly

---

## 5.4 Reliability Requirements

The system shall:

- Handle invalid input
- Prevent unexpected crashes
- Provide meaningful error messages

---

## 5.5 Maintainability Requirements

The system shall:

- Use modular code structure
- Separate frontend and backend logic
- Allow easy updates and modifications

---

# 6. Future Enhancements

Possible future upgrades include:

- Password suggestion generator
- Dark mode interface
- Password history analysis
- Integration with password breach databases
- Multi-language support
- Advanced encryption visualization

---

# 7. Appendix

## Tools Used

- Python 3.x
- Flask Framework
- HTML
- CSS
- JavaScript
- GitHub
- VS Code

---

**End of Document**