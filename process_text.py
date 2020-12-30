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
    lemmas = [ent.lemma_ for ent in ents]
    entrs = [getEntries(lem) for lem in lemmas]
    # print(entrs[0])

    for entr in entrs:
        print(entr['searchinfo']['search'])
        for s in entr['search']:
            if 'description' in s:
                print("  " + s['description'])
            elif 'title' in s:
                print("  " + s['title'])
            else:
                print("  __other")

processText(example_text)
