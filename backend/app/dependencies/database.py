def get_db():
    """FastAPI dependency for obtaining a database session."""
    db = None
    try:
        # Yield database session object
        yield db
    finally:
        pass
