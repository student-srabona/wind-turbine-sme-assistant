# 🌬️ Wind Turbine GenAI SME Assistant

> An AI-powered Subject Matter Expert (SME) assistant for wind turbine operations, maintenance, and troubleshooting, built using **AWS API Gateway**, **AWS Lambda**, **Amazon Bedrock (Nova Pro)**, and **Streamlit**.

## 📖 Overview

The **Wind Turbine GenAI SME Assistant** is an intelligent chatbot designed to help engineers, technicians, students, and renewable energy professionals quickly access reliable information about wind turbine systems.

Instead of searching through lengthy technical manuals, users can ask natural language questions and receive AI-generated responses powered by Amazon Bedrock.

---

## ✨ Features

* 🤖 AI-powered technical assistant for wind turbine knowledge
* 💬 Natural language question answering
* ⚡ Serverless backend using AWS Lambda
* 🌐 REST API exposed through AWS API Gateway
* 🧠 Powered by Amazon Bedrock Nova Pro
* 🖥️ Interactive Streamlit web interface
* 🔒 Secure cloud-based architecture
* 📈 Scalable and cost-efficient deployment

---

## 🏗️ Solution Architecture

```
                User
                  │
                  ▼
        Streamlit Frontend
                  │
                  ▼
          AWS API Gateway
                  │
                  ▼
            AWS Lambda
                  │
                  ▼
      Amazon Bedrock (Nova Pro)
                  │
                  ▼
          AI Generated Response
```

---

## 🛠️ Tech Stack

| Technology      | Purpose                  |
| --------------- | ------------------------ |
| Python          | Backend development      |
| Streamlit       | User Interface           |
| AWS Lambda      | Serverless compute       |
| AWS API Gateway | REST API                 |
| Amazon Bedrock  | Foundation Model Service |
| Amazon Nova Pro | Large Language Model     |
| Boto3           | AWS SDK                  |

---

## 📂 Project Structure

```
Wind-Turbine-SME-Assistant/
│
├── frontend/
│   └── app.py
│
├── backend/
│   └── lambda_function.py
│
├── requirements.txt
├── README.md
└── architecture.png
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/wind-turbine-sme-assistant.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure AWS

Create an AWS credentials profile:

```bash
aws configure
```

Ensure your IAM user has access to:

* Amazon Bedrock
* AWS Lambda
* API Gateway

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will launch in your browser.

---

## 🔗 API Flow

1. User submits a question from the Streamlit UI.
2. The frontend sends a POST request to AWS API Gateway.
3. API Gateway invokes an AWS Lambda function.
4. Lambda sends the prompt to Amazon Bedrock (Nova Pro).
5. Bedrock generates a response.
6. Lambda returns the answer through API Gateway.
7. Streamlit displays the AI-generated response.

---

## 💡 Example Questions

* What causes gearbox failure in wind turbines?
* Explain pitch control systems.
* How often should turbine blades be inspected?
* What are common SCADA alarms?
* Describe preventive maintenance procedures.
* What is the function of the nacelle?
* How does a yaw system work?

---

## 🎯 Future Enhancements

* RAG with turbine maintenance manuals
* PDF document upload
* Conversation memory
* Voice interaction
* Image-based fault diagnosis
* Multi-language support
* User authentication
* Chat history storage

---

## 👩‍💻 Author

**Srabona Bose**

Computer Science Engineering Student | AI & Cloud Enthusiast

* AWS Cloud
* Generative AI
* Machine Learning
* Python
* Serverless Applications

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project helpful

Please consider giving this repository a **Star ⭐** on GitHub to support the project.
