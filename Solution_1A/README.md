# Adobe - Connecting the Dots Challenge 1A

## How to Run

### Build Docker Image
```
docker build --platform linux/amd64 -t adobe-outline-extractor .
```

### Run the Solution
```
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none adobe-outline-extractor
```

### Input
Put your `.pdf` files in `/input`

### Output
Extracted outline will be in `/output` as `.json` files

## Output Format
```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Heading One", "page": 1 },
    { "level": "H2", "text": "Subheading", "page": 2 }
  ]
}
```
> This solution runs fully offline (no internet), uses CPU only, and meets all hackathon constraints.
