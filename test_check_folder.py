import unittest 
from check_folder import Check_Folder
from os import walk

class Test_Check_Me(unittest.TestCase):

    def setUp(self):
        self.check = Check_Folder()

    def tearDown(self):
        pass 

    def test_check_if_strings_in_file(self):
        check = ['ali']
        directory_loc= "./test_for_looking/one" 
        answer = self.check.check_if_list_in_files(check, directory_loc)
        self.assertDictEqual(
            answer, 
            {'ali': {'files': ['./test_for_looking/one/hello.py']}})

    def test_check_if_strings_in_file_2(self):
        check = ['check', 'the', 'mic']
        directory_loc= "./test_for_looking/two" 
        answer = self.check.check_if_list_in_files(check, directory_loc)
    
        expected_answer = {
            'the': {
                'files': [
                    './test_for_looking/two/umm_2.py', 
                    './test_for_looking/two/umm_1.py']
                }, 
            'check': {
                'files': [
                    './test_for_looking/two/umm_2.py', 
                    './test_for_looking/two/umm_1.py']
                }, 
            'mic': {
                'files': [
                    './test_for_looking/two/umm_2.py', 
                    './test_for_looking/two/umm_1.py']
                }
        }
        self.assertDictEqual(answer, expected_answer) 

if __name__ == "__main__":
    unittest.main()
