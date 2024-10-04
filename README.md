# AI-Driven Natural Language to SQL Converter Using Langchain

## Overview

This project simplifies database interaction by converting natural language queries into SQL, allowing non-technical users to easily access and retrieve data from a MySQL database. Using AI technologies like Langchain and OpenAI embeddings, the system ensures accurate and efficient data querying.

## Key Features

- **Natural Language Queries**: Allows users to input queries in plain language.
- **SQL Conversion**: Converts natural language into SQL to retrieve data.
- **Improved Query Accuracy**: Utilizes few-shot learning and OpenAI embeddings for better understanding and response over time.

## Tech Stack

- **Langchain**: Natural language processing to SQL conversion.
- **OpenAI embeddings**: Enhances semantic understanding.
- **ChromaDB**: Vector store for efficient data retrieval.
- **Streamlit**: Provides a user-friendly interface.
- **MySQL**: The database system used for data storage and retrieval.

## End Result

This solution empowers both technical and non-technical users:

- **Non-technical users** can interact with databases without learning SQL.
- **Technical users** benefit from time-saving automation in query writing.

The project is highly adaptable, scalable, and valuable across various business domains, promoting ease of access to critical data.

## Installation and Usage

To run the application:

1. Clone the repository.
2. Set up the necessary environment and install dependencies.
3. Launch the Streamlit app to start querying your MySQL database using natural language.

```bash
git clone [repository-url]
cd project-directory
pip install -r requirements.txt
streamlit run app.py
```
