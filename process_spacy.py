import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

def exampleDoc():
    # Process whole documents
    text1 = ("When Sebastian Thrun started working on self-driving cars at "
            "Google in 2007, few people outside of the company took him "
            "seriously. “I can tell you very senior CEOs of major American "
            "car companies would shake my hand and turn away because I wasn’t "
            "worth talking to,” said Thrun, in an interview with Recode earlier "
            "this week.")
    return nlp(text1)


def analyzeDoc(doc):
    # Analyze syntax
    print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

    #  Find named entities, phrases and concepts
    for entity in doc.ents:
        print(entity.text, entity.label_)


def getEntities(text):
    doc = nlp(text)
    return doc.ents
