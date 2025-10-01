import streamlit as st
import spacy
import subprocess
import sys

st.title("Named Entity Recognition")

# Load spaCy model, install automatically if missing
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

text = st.text_area("Enter text here:", "Type something to extract entities…")

if st.button("Extract Entities"):
    doc = nlp(text)
    if doc.ents:
        st.write("### Entities Found:")
        for ent in doc.ents:
            st.write(f"{ent.text} — {ent.label_}")
    else:
        st.write("No entities found.")