@staticmethod
def llog(message):
    """Lazy Logger for trouble shooting
    """
    import os
    path = os.path.dirname(os.path.realpath(__file__))
    with open("{}/log.txt".format(path), "a") as f:
        f.write("{}\n".format(message))