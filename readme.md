# AWS Learning Repository

Welcome to my AWS learning journey! 🚀  
This repository documents my hands-on experience and learnings with various **AWS services**, using **Infrastructure as Code (IaC)** through **AWS CloudFormation**.

---

## 📁 Project Structure
```
.
├── .env                  # Environment configuration (ignored by Git)
├── .venv/                # Python virtual environment (ignored by Git)
├── .vscode/              # VSCode settings (ignored by Git)
├── plan                  # Optional plan/config file (ignored by Git)
├── readme.md             # This file
├── run.py                # Entry point script for automation (if any)
├── scripts/              # Custom helper or deployment scripts
├── templates/            # Common CloudFormation templates or partials
├── utils/                # Utility functions/modules
└── stacks/               # 💡 Main directory containing CFTs for learned services
```

---

## 📦 What You'll Find

- ✅ Hands-on examples of AWS services like EC2, S3, IAM, VPC, ALB, Auto Scaling, etc.
- 🧩 CloudFormation templates to automate the deployment of AWS infrastructure
- 🛠 Scripts and utilities to support testing and deployment
- 📚 Notes, learnings, and experiments as I progress through AWS

---

## 📂 `stacks/` Folder

The `stacks/` directory contains individual **CloudFormation templates** for different AWS services I've learned. Each stack is tested and deployed using the AWS Management Console or AWS CLI.

---

## 🚀 How to Use

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/aws-learning.git
   cd aws-learning
