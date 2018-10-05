import unittest
import sys
sys.path.append("..")
print(sys.path)
from src import Downloader_base
from src import Downloader_split_link

class Test_Downloader_split_link(unittest.TestCase):
    def setUp(self):
        print("\n[         setUp]")

    def tearDown(self):
        print("\n[tearDown      ]")
        
    def test_link1(self):
        test_src_link = "https://pl-p2p3.live.panda.tv/block/pandaTV/pl3.live.panda.tv/live_panda/91c800a81515aa8e3f3cdff9998675a2/5b97e6d9.wsv?type=0"
        dl = Downloader_split_link.DownloaderSplitLink(test_src_link)
        file_name1 = dl.get_next_file_name()
        print(file_name1)
        link1 = dl.get_next_link()
        print(link1)

if __name__ == '__main__':
    unittest.main()