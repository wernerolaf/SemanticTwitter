from pywikibot.data import api
import pywikibot
import pprint

def getItems(site, itemtitle):
    params = { 'action' :'wbsearchentities' , 'format' : 'json' , 'language' : 'en', 'type' : 'item', 'search': itemtitle}
    request = api.Request(site=site, parameters=params)
    return request.submit()

def getItem(site, wdItem, token):
    request = api.Request(site=site,
                          action='wbgetentities',
                          format='json',
                          ids=wdItem)    
    return request.submit()

def prettyPrint(variable):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(variable)

# Login to wikidata
site = pywikibot.Site("wikidata", "wikidata")
#repo = site.data_repository()
#token = repo.token(pywikibot.Page(repo, 'Main Page'), 'edit')
wikidataEntries = getItems(site, "Google")
# Print the different Wikidata entries to the screen
prettyPrint(wikidataEntries)

# Print each wikidata entry as an object
#for wdEntry in wikidataEntries["search"]:
#   prettyPrint(getItem(site, wdEntry["id"], token))
