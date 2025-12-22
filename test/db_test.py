import pytest

from db.db_manager import DBManager


class TestDBManager:
    @pytest.fixture
    def db(self):
        db = DBManager(":memory:")
        yield db
        db.close()
