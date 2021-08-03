from app import get_doc_shelf, get_doc_owner_name, get_all_doc_owners_names,\
    show_all_docs_info, add_new_doc, delete_doc, move_doc_to_shelf ,add_new_shelf

class TestDirApp:

        def setup(self):
                print("method setup")

        def teardown(self):
                print("method teardowmn")

        def test_owner_name_Gena(self):
                assert get_doc_owner_name("11-2") == "Геннадий Покемонов"

        def test_get_all(self):
                assert get_all_doc_owners_names() != []

        def test_show_all(self):
                assert show_all_docs_info() is True

        def test_get_2_shelf(self):
                assert get_doc_shelf('10006') == '2'

        def test_add_new(self):
                assert add_new_doc('12315','паспорт','Человек Разумный','4') == '4'

        def test_delete_hommo(self):
                assert delete_doc('12315') == ('12315', True)

        def test_move_hommo(self):
                assert move_doc_to_shelf('10006','3') == True

        def test_add_shelf(self):
                assert add_new_shelf('5') == '5'

