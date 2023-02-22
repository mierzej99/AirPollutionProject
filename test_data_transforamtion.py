import data_transofrmation
import pytest

@pytest.mark.parametrize("list_of_yeras_from_different_sources,res", [([], []), ([['12','13','14'],['12']], ['12'])])
def test_find_common_years(list_of_yeras_from_different_sources, res):
    assert data_transofrmation.find_common_years(list_of_yeras_from_different_sources) == res