from Tests.testCRUD import test_adauga_vanzare, test_sterge_vanzare
from Tests.testdomain import test_vanzare
from Tests.testfunctionalitate import test_vanzare_discount, test_modificare_gen


def run_all_test():
    test_vanzare()
    test_adauga_vanzare()
    test_sterge_vanzare()
    test_vanzare_discount()
    test_modificare_gen()