from ..setup import index

def fetch_products_vector(tempid):
    response = index.fetch(ids=tempid)
    return