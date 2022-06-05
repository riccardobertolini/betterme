
from unittest import mock
import pandas as pd

from login import get_password



@mock.patch('login.sqlite3')
def test_sql_query(read_sql_query_mock):
    read_sql_query_mock.return_value = pd.DataFrame("tessdt")
    assert get_password("tesst").to_dict(orient='list') == "tesst"

test_sql_query()