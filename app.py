from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from gensim import corpora, models
from gensim.parsing.preprocessing import preprocess_string

app = Flask(__name__)
CORS(app)

@app.route('/lda', methods=['POST'])
def lda_api():
    file = request.files['file']
    df = pd.read_csv(file) if file.filename.endswith('.csv') else pd.read_excel(file)

    if not all(col in df.columns for col in ['TI', 'AB', 'KW', 'PY']):
        return jsonify({'error': 'Columns TI, AB, KW, PY required'}), 400

    texts = (df['TI'].fillna('') + ' ' + df['AB'].fillna('') + ' ' + df['KW'].fillna('')).tolist()
    processed = [preprocess_string(t) for t in texts]
    dictionary = corpora.Dictionary(processed)
    corpus = [dictionary.doc2bow(text) for text in processed]

    lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=10)
    topics = [{'id': i, 'keywords': [w for w, _ in lda_model.show_topic(i)]} for i in range(5)]

    return jsonify({'topics': topics})