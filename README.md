# 🛡️ Campus Backend

A robust backend system for modern campus security and administration, orchestrating real-time facial recognition, license plate detection, and campus surveillance—all built for extensibility, security, and seamless integration with diverse campus management solutions.

## 📖 Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Repository Structure](#repository-structure)
4. [Getting Started](#getting-started)
5. [Core Modules & Components](#core-modules--components)
6. [Tech Stack](#tech-stack)
7. [Configuration](#configuration)
8. [Contributing](#contributing)
9. [License](#license)
10. [Support & Contact](#support--contact)
11. [Acknowledgements](#acknowledgements)

## Project Overview

**Campus Backend** powers campus-wide security by providing APIs and services for:

- Automated **Face Recognition** for access control and attendance
- **Vehicle License Plate Detection** for entry/exit logging
- Support for smart surveillance and event monitoring
- Integration with campus management platforms

Designed to be the backbone of next-gen smart campuses, it leverages state-of-the-art computer vision models, Python-driven automation, and modular architecture for easy extensibility.

## Features

| Category                    | Description                                                               |
|-----------------------------|---------------------------------------------------------------------------|
| Facial Recognition          | Detect and authenticate registered individuals at campus access points     |
| License Plate Detection     | Track vehicle movement through automated number plate recognition          |
| Modular Design              | Clear separation for decoupled security, detection, and data pipelines    |
| RESTful APIs                | External systems can fetch, post, and manage security records             |
| Logging & Auditing          | Track all campus entry/exit and incident events for compliance            |
| Deployment Ready            | Runs on local servers or cloud (compatible with containerized workflows)  |
| Platform Integration        | Tailored for integration with custom campus, admin, or third-party apps   |

## Repository Structure

```
Campus_backend/
│
├── Car-Number-Plates-Detection-main/           # Vehicle plate detection module
│   ├── ...                                    # Python scripts, models, configs
│
├── Face-recognition/                          # Face authentication module
│   ├── ...                                    # Image processing, ML scripts
│
├── campus-guardian-be/                        # Main backend logic (API, DB, auth)
│
├── campus-guardian-shield-main/               # Enhanced security & event layer
│
├── myproject/                                 # Supporting/experimental work
│
├── Car-Number-Plates-Detection-main.zip       # Archive version
├── Face-recognition.zip                       # Archive version
├── campus-guardian-shield-main.zip            # Archive version
└── ... (project metadata, configs, etc.)
```

## Getting Started

### Prerequisites

- **Python 3.8+**
- pip / conda (for dependency management)
- (Optional) Docker for containerized deployment

### Installation

```bash
# Clone the repository
git clone https://github.com/puli-pro/Campus_backend.git
cd Campus_backend

# Enter the core modules as needed
cd Car-Number-Plates-Detection-main
pip install -r requirements.txt

cd ../Face-recognition
pip install -r requirements.txt

# (For all-in-one builds, set up virtual environments as appropriate)
```

### Run Key Modules

```bash
# Example: Start vehicle plate detection
python main.py  # (in Car-Number-Plates-Detection-main/)

# Example: Start facial recognition server
python app.py   # (in Face-recognition/)
```

> Refer to in-module README or help comments for module-specific settings.

## Core Modules & Components

### 1. Car-Number-Plates-Detection-main/
- **Goal:** Real-time vehicle plate reading from webcam, images, or video streams
- **Core files:** Python/OpenCV scripts, pre-trained models, API integration

### 2. Face-recognition/
- **Goal:** Detect, match, and authenticate faces for attendance, access, or alerts
- **Core files:** Python face recognition models, API endpoints, camera utilities

### 3. campus-guardian-be/
- **Goal:** Backend API logic, data storage (student/vehicle/event records), authentication
- **Likely Tools:** FastAPI or Flask (Python web frameworks), SQLite/MySQL, REST interfaces

### 4. campus-guardian-shield-main/
- **Goal:** Security orchestrator for advanced event detection, logging, and escalation workflows

### 5. myproject/
- **Goal:** Staging/experimental scripts, possibly for integration, auxiliary services, or new features

## Tech Stack

| Layer           | Technology          |
|-----------------|--------------------|
| Core Language   | Python             |
| CV & AI         | OpenCV, face_recognition, TensorFlow/PyTorch (as needed) |
| Web/API         | Flask or FastAPI   |
| Data Storage    | SQLite, CSV, MySQL (varies by module) |
| Web Frontend    | (Optional, for admin dashboard) TypeScript, React |
| Scripting/Utils | Bash, Shell        |

> Some submodules may use HTML/JS, CSS, or Jupyter Notebook for rapid prototyping or reporting.

## Configuration

- **Environment Files:** Modules might use `.env` or `config.py` for specifying database URIs, secret keys, port numbers, or camera sources.
- **Custom Settings:** Adjust paths to pre-trained models, video source urls, or admin credentials in respective config files.
- **Dataset Dependencies:** Face and plate models might require uploading reference images or training data to specific folders before first launch.

## Contributing

1. Fork the repository and create a feature branch (`feat/`)
2. Follow Python PEP8 and module-specific code conventions
3. Add docstrings and in-line comments for clarity
4. For new vision models: document dependencies and provide demo/test assets
5. Submit a pull request describing your changes, testing approach, and screenshots (if UI)

## License

Distributed under the **MIT License**—see `LICENSE` file for details.

## Support & Contact

- **Issues:** Use the [GitHub Issues](https://github.com/puli-pro/Campus_backend/issues) page for bug reports or feature requests
- **Email**: [pulipavan696@gmail.com](mailto:pulipavan696@gmail.com)
- **LinkedIn**: [Solige Pullaiah](https://www.linkedin.com/in/solige-pullaiah-478462270/)
  

## Acknowledgements

- Core vision algorithms powered by Open Source libraries (OpenCV, face_recognition, etc.)
- Thanks to the community for ongoing improvements in AI-based campus security


 <p align="center"> <em>Building safer, smarter campuses—powered by AI and open source</em> </p>
---
