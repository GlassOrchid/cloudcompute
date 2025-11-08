# ☁️ CloudBase

**A developer-centric, transparent, and scalable cloud file backup system powered by Google Cloud and Kubernetes.**

---

##  Abstract

Mainstream cloud storage platforms like Google Drive, Dropbox, and iCloud are highly reliable and user-friendly, but they are designed for general use. For developers, creators, and advanced users seeking **more control, transparency, and flexibility**, these platforms often fall short due to API and commercial limitations.

**CloudBase** aims to bridge this gap by providing a **scalable, secure, and customizable cloud-based file backup system** built on **Google Cloud Engine** and **Kubernetes**. It empowers users to:

- Securely upload and manage files through a Virtual Private Cloud (VPC)
- Gain real-time insights and analytics into storage usage
- Access developer-friendly APIs for automation and integration
- Maintain full transparency on resource usage and system performance

Unlike traditional cloud services, CloudBase provides complete visibility into storage behavior and resource utilization — ideal for users who want to *build upon*, not just *use*, their cloud storage.

---

## Features

- **Secure Uploads via VPC**
- **Usage Statistics & Storage Analytics**
- **Developer-Friendly APIs**
- **Scalable Infrastructure with Kubernetes**
- **Transparent Resource Monitoring**
- **Dashboard for Data Insights**

---

## Tech Stack

| Component | Technology |
|------------|-------------|
| Cloud Platform | Google Cloud Platform (GCP) |
| Compute | Google Kubernetes Engine (GKE) |
| Containerization | Docker |
| Database | Cloud SQL (PostgreSQL / MySQL) |
| Storage | Google Cloud Storage |
| Website | Flask |
| Analytics | GCP Monitoring, Custom APIs |

---

##  Installation (Prototype Setup)

```bash
# Clone the repository
git clone https://github.com/your-username/cloudbase.git
cd cloudbase

# Build Docker image
docker build -t cloudbase .
```
The application will be available at http://localhost:8000.