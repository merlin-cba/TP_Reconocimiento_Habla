import spacy

# Cargar el modelo de lenguaje en español de spaCy
nlp = spacy.load("es_core_news_sm")

def extract_named_entities(text):
    # Procesar el texto con el modelo de spaCy
    doc = nlp(text)
    
    # Extraer las entidades nombradas del texto
    named_entities = []
    for entity in doc.ents:
        named_entities.append((entity.text, entity.label_))
    
    return named_entities

def analyze_sentiment(text):
    # Procesar el texto con el modelo de spaCy
    doc = nlp(text)
    
    # Obtener el sentimiento general del texto
    sentiment = doc._.polarity
    
    return sentiment

# Texto de ejemplo para realizar el análisis
text = "Me encanta ir de vacaciones a la playa en verano."

# Extraer entidades nombradas del texto
entities = extract_named_entities(text)
print("Entidades nombradas:")
for entity, label in entities:
    print(f"- {entity} ({label})")

# Analizar el sentimiento del texto
sentiment = analyze_sentiment(text)
print("Sentimiento:", sentiment)
