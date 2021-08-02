from old_file import get_doc_shelf, get_doc_owner_name, get_all_doc_owners_names,\
    show_all_docs_info, add_new_doc, delete_doc, move_doc_to_shelf ,add_new_shelf

from old_file import documents, directories


class Test_dir:

        def setup(self):
                print("method setup")

        def teardown(self):
                print("method teardowmn")

        def owner_name_Gena(self):
                assert get_doc_owner_name("11-2") == "Геннадий Покемонов"

        uniq_users = get_all_doc_owners_names()

        show_all_docs_info()

        directory_number = get_doc_shelf()

        new_doc_shelf_number = add_new_doc()

        doc_number, deleted = delete_doc()

        move_doc_to_shelf()

        shelf_number, added = add_new_shelf()
