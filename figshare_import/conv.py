import logging
import pyld

# from metapype.eml.exceptions import MetapypeRuleError
# import metapype.eml.names as names
# import metapype.eml.validate as validate
# from metapype.model.node import Node

from .defs import define_context, TEMP_ARTICLE


def from_scratch_eml():
    """
    This would be a way to generate EML from scratch.
    We are ignoring this for now in order to use the codemeta crosswalk method
    (https://github.com/codemeta/codemeta/).
    """

    eml = Node(names.EML)
    eml.add_attribute('packageId', 'edi.23.1')
    eml.add_attribute('system', 'metapype')

    access = Node(names.ACCESS, parent=eml)
    access.add_attribute('authSystem', 'pasta')
    access.add_attribute('order', 'allowFirst')
    eml.add_child(access)

    allow = Node(names.ALLOW, parent=access)
    access.add_child(allow)

    principal = Node(names.PRINCIPAL, parent=allow)
    principal.content = 'uid=gaucho,o=EDI,dc=edirepository,dc=org'
    allow.add_child(principal)

    permission = Node(names.PERMISSION, parent=allow)
    permission.content = 'all'
    allow.add_child(permission)

    dataset = Node(names.DATASET, parent=eml)
    eml.add_child(dataset)

    title = Node(names.TITLE, parent=dataset)
    title.content = 'Green sea turtle counts: Tortuga Island 20017'
    dataset.add_child(title)

    creator = Node(names.CREATOR, parent=dataset)
    dataset.add_child(creator)

    individualName_creator = Node(names.INDIVIDUALNAME, parent=creator)
    creator.add_child(individualName_creator)

    surName_creator = Node(names.SURNAME, parent=individualName_creator)
    surName_creator.content = 'Gaucho'
    individualName_creator.add_child(surName_creator)

    contact = Node(names.CONTACT, parent=dataset)
    dataset.add_child(contact)

    individualName_contact = Node(names.INDIVIDUALNAME, parent=contact)
    contact.add_child(individualName_contact)

    surName_contact = Node(names.SURNAME, parent=individualName_contact)
    surName_contact.content = 'Gaucho'
    individualName_contact.add_child(surName_contact)

    try:
        validate.tree(eml)
    except MetapypeRuleError as e:
        logging.error(e)
        
    return 0


def frame(jld: dict, context: dict=define_context()):
    """
    """
    return pyld.jsonld.frame(jld, frame=context)


def compact(jld: dict, context: dict=define_context()):
    """
    """
    return pyld.jsonld.compact(jld, ctx=context)


def expand(jld: dict):
    """
    """
    return pyld.jsonld.expand(jld)

def frame(article: dict=TEMP_ARTICLE, context: dict=define_context()):
    """
    """
    article['@context'] = context
    return pyld.jsonld.frame(article, frame=context)
