# Persona-Driven Document Intelligence (Adobe Hackathon - Challenge 1B)

This project is a sophisticated solution for Challenge 1B of the Adobe India Hackathon. It implements an advanced Retrieval-Augmented Generation (RAG) pipeline to analyze multiple document collections and extract relevant, persona-driven insights.

---

## Key Features

Our solution goes beyond simple semantic search to deliver highly accurate and user-centric results.

*   **Advanced Two-Stage Retrieval:** To solve the critical "negative constraint" problem (e.g., finding "vegetarian" recipes), we use a two-stage pipeline.
    1.  **Keyword Filtering:** First, it filters out irrelevant content based on keywords (like removing non-vegetarian items).
    2.  **Semantic Ranking:** Then, it applies a powerful sentence-transformer model to rank the remaining "safe" content.
*   **AI-Powered Title Generation:** Instead of using unreliable heuristics, the system uses a local generative model (`google/flan-t5-base`) to create clean, concise, and human-readable titles for each extracted section.
*   **Global Ranking:** The pipeline pools content from all documents in a collection and ranks them globally, ensuring the final output contains the absolute best results from the entire set.
*   **Unified & Configurable Architecture:** A single, robust Python script (`run_analysis.py`) handles all collections, configured via command-line arguments for professional and scalable execution.
*   **Completely Offline & CPU-Only:**  
    Runs in Docker with **no internet** (`--network none`), model size <1GB, and only CPU required.  
    All models are **already cached inside the image** for strict hackathon compliance.

---

## How to Run the Project

1. **Docker Build**
    ```bash
    docker build --platform linux/amd64 -t adobe1b .
    ```

2. **Docker Run (Offline/No Internet)**
    ```bash
    docker run --rm ^
      -v "%cd%\Collection_1:/app/collection" ^
      -v "%cd%\output:/app/output" ^
      --network none ^
      adobe1b /app/collection
    ```
    - Replace `Collection_1` with your target collection.
    - Output JSON (`challenge1b_output.json`) will be saved in the output directory.

---

## Input / Output Format

### 1. **Input**

- Place **3–10 PDFs** in:  
(e.g., `Collection_1/PDFs/`)

- Add persona + job in:  

### 2. **Output**

- The solution will generate:  
in your chosen output folder (e.g., `/output/` if you use the run command above).


- **Output JSON Structure:**
  ```json
  {
    "metadata": { ... },
    "sections": [
      {
        "document": "doc1.pdf",
        "page": 3,
        "title": "Best Practices for Travel",
        "importance_rank": 1
      }
    ],
    "subsections": [
      {
        "document": "doc1.pdf",
        "page": 3,
        "text": "Relevant excerpt here...",
        "importance_rank": 1
      }
    ]
  }
  ```
## Project Structure

adobe-hackathon-challenge1b-master/
├── Collection_1/
│   ├── PDFs/
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── Collection_2/
│   ├── PDFs/
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── Collection_3/
│   ├── PDFs/
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── output/
├── Scripts/
│   ├── dumppdf.py
│   ├── pdf2txt.py
│   ├── (other .exe, .py, .exe, etc.)
├── approach_explanation.md
├── Dockerfile
├── README.md
├── requirements.txt
└── run_analysis.py

