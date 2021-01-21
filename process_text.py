from process_pwbot import getEntries
from process_spacy import getEntities


example_text = ("Governor @BrianKempGA and his puppet @GeoffDuncanGA, together with the Secretary of State of Georgia, "
    "are very slow on Signature Verification, and won’t allow Fulton County to be examined. What are these "
    "RINOS hiding? We will easily win Presidential State race. @KLoeffler and"
    "@sendavidperdue will not be able to win on January 5th. unless these people allow Signature Verification in presidential race."
    "K & D need it for their race also, & Georgia spirit will rise to such a high that they will easily bring home a great victory. Move fast @BrianKempGA")

def processText(text):
    print(text + "\n")
    ents = getEntities(text)
    ents_metas = {ent: get_meta(ent) for ent in ents}
    ents_metas = {k: v for k, v in ents_metas.items() if v is not None}
    return ents_metas


def get_meta(entity):
    lemma = entity.lemma_
    entr = getEntries(lemma)

    wiki_results = [] ## multiple wiki results (like Georgia state and Georgia country)
    print(entr['searchinfo']['search'])
    for s in entr['search']:
        wiki_results.append(s)
        if 'description' in s:
            print("  " + s['description'])
        elif 'title' in s:
            print("  " + s['title'])
        else:
            print("  __other")
        # return s # single wiki result
    return wiki_results


processText(example_text)
