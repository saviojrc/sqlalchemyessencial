from pathlib import Path
from typing import Optional

import sqlalchemy as sa
from sqlalchemy.future.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from models.model_base import ModelBase

__engine: Optional[Engine] = None


def create_engine(sqlite: bool = False) -> Engine:
    """Create and return a SQLAlchemy engine.
    Args:
        sqlite (bool): If True, create a SQLite engine; otherwise, create a PostgreSQL engine.
    Returns:
        Engine: A SQLAlchemy engine instance.
    """

    global __engine

    if __engine:
        return __engine

    if sqlite:
        arquivo_db = f'../db/picoles.db'
        folder = Path(arquivo_db).parent
        folder.mkdir(parents=True, exist_ok=True)

        conn_str = f'sqlite:///{arquivo_db}'
        __engine = sa.create_engine(conn_str, echo=False, connect_args={"check_same_thread": False})
    else:
        conn_str = f'postgresql://geek:university@localhost:5432/picoles'
        __engine = sa.create_engine(conn_str, echo=False)

    return __engine


def create_session() -> Session:
    """Create a new SQLAlchemy session.

    Returns:
        Session: A new SQLAlchemy session object.
    """

    global __engine

    if not __engine:
        create_engine(True)

    __session = sessionmaker(bind=__engine, expire_on_commit=False, class_=Session)
    session: Session = __session()

    return session


def create_tables():
    """Create all tables in the database using the ModelBase metadata."""
    global __engine

    if not __engine:
        create_engine(True)

    ## Importa tudo o que tem em models.__all_models.py
    from models import __all_models  # noqa: F401

    ModelBase.metadata.create_all(__engine)
    ModelBase.metadata.create_all(__engine)
