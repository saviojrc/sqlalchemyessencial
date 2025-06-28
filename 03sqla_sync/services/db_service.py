from sqlalchemy.orm import Session
from conf.db_session import create_session

class DBService:
    """
    Manages the lifecycle of a SQLAlchemy session.
    """

    def __init__(self):
        self._session: Session | None = None

    @property
    def session(self) -> Session:
        """
        Returns an active session, creating one if necessary.
        """
        if self._session is None or not self._session.is_active:
            self._session = create_session()
        return self._session

    def close_session(self) -> None:
        """
        Closes the current session if it exists.
        """
        if self._session is not None:
            self._session.close()
            self._session = None