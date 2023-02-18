def cleanup(session, engine_container):
    """
    This method cleans up the session object and also closes the connection pool using the dispose method.
    """

    session.close()
    engine_container.dispose()