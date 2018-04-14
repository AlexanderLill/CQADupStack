
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import unittest
import query_cqadupstack as cqa

import os
import tempfile
import shutil

from zipfile import ZipFile

_TEST_FORUM_NAME = 'testforumf'

def setUpModule():
    """
    Creates a zip fil which mimics the structure of subforum archive. 
    The zip is stored in tmp folder.
    """
    
    zip_file_path, zip_file_folder_path = _get_zip_file_path()
        
    _remove_zip_file(zip_file_path)
    
    if not os.path.exists(zip_file_folder_path):
        os.makedirs(zip_file_folder_path)
    
    with ZipFile(zip_file_path, 'w') as zipFile:
        zipFile.writestr(('%s/%s_answers.json' % (_TEST_FORUM_NAME, _TEST_FORUM_NAME)), '{}')
        zipFile.writestr(('%s/%s_comments.json' % (_TEST_FORUM_NAME, _TEST_FORUM_NAME)), '{}')
        zipFile.writestr(('%s/%s_questions.json' % (_TEST_FORUM_NAME, _TEST_FORUM_NAME)), '{}')
        zipFile.writestr(('%s/%s_users.json' % (_TEST_FORUM_NAME, _TEST_FORUM_NAME)), '{}')

def tearDownModule():
    zip_file_path, _ = _get_zip_file_path()
    _remove_zip_file(zip_file_path)

class SubforumUnzipTestCase(unittest.TestCase):
    
    def test_unzip_current_dir(self):
        # arrange
        zip_file_path, _ = _get_zip_file_path()        
        unziped_forum_path = self._get_cwd_foum_path()
        if os.path.exists(unziped_forum_path):
            shutil.rmtree(unziped_forum_path)

        # act
        self.subforum = cqa.Subforum(zip_file_path)

        # assert
        is_forum_unziped = os.path.exists(unziped_forum_path)
        self.assertTrue(is_forum_unziped, ('Forum archive expected to be unzipped to "%s" ', unziped_forum_path))
        
        shutil.rmtree(unziped_forum_path)
    
    def test_unzip_custom_dir(self):
        # arrange
        zip_file_path, tmp_dir_path = _get_zip_file_path()        
        unziped_forum_path = self._get_forum_path(tmp_dir_path)
        
        # act
        self.subforum = cqa.Subforum(zip_file_path, unziped_forum_path)

        # assert
        is_forum_unziped = os.path.exists(unziped_forum_path)
        self.assertTrue(is_forum_unziped, ('Forum archive expected to be unzipped to "%s" ', unziped_forum_path))
    
    def _get_cwd_foum_path(self):
        return self._get_forum_path(os.getcwd())
        
    def _get_forum_path(self, folder_path):
        unziped_forum_path = os.path.join(folder_path, _TEST_FORUM_NAME)
        return unziped_forum_path


def _remove_zip_file(zip_file_path):
    if os.path.exists(zip_file_path):
        os.remove(zip_file_path)

def _get_zip_file_path():
    tmp_dir = tempfile.gettempdir()
    zip_file_folder_path = os.path.join(tmp_dir, 'python_tests', 'cqa')
    zip_file_path = os.path.join(zip_file_folder_path, ('%s.zip' % _TEST_FORUM_NAME))

    return zip_file_path, zip_file_folder_path

if __name__ == '__main__':
    unittest.main()