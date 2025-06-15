# LDA Topic Modeling Web App

## Features:
- Upload `.csv` or `.xlsx` files
- Extracts `TI`, `AB`, `KW`, `PY` columns
- Runs LDA Topic Modeling with Gensim
- Returns top 5 topics with keywords

## How to Deploy

### Backend:
1. Push this repo to GitHub
2. Go to https://render.com
3. Create new Web Service
4. Connect GitHub repo
5. Set:
   - Runtime: Python
   - Start command: `gunicorn app:app`
6. Deploy and get live API URL

### Frontend:
1. Replace backend URL in `index.html`
2. Upload `index.html` to Hostinger File Manager > public_html