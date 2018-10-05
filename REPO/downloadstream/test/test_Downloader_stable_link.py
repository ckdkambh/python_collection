import unittest
import sys
sys.path.append("..")
print(sys.path)
from src import Downloader_base
from src import Downloader_stable_link
import time

class Test_Downloader_stable_link(unittest.TestCase):
    def setUp(self):
        print("\n[         setUp]")

    def tearDown(self):
        print("\n[tearDown      ]")
        
    def test_link1(self):
        test_src_link = "https://3grauymtt8rzdnqb1fahdn.ourdvsss.com/pl3.live.panda.8686c.com/live_panda/e900b5f1420886d08fe60acb82d6cec7_4000.flv?sign=fcd87c307001eb7fe60a8f47d236791f&ts=5b894f55&rid=27836296&add_index_info=1&wshc_tag=0&wsts_tag=5b894f59&wsid_tag=72f4bb6a&wsiphost=ipdbm"
        dl = Downloader_stable_link.DownloaderStableLink(test_src_link)
        link = dl.get_next_link()
        self.assertEqual(link, test_src_link)
        file_name = dl.get_next_file_name()
        self.assertEqual(True, file_name.startswith('D:\\MY_DownLoad'))
        self.assertEqual(True, file_name.endswith('flv'))
        self.assertNotEqual(-1, file_name.find('e900b5f1420886d08fe60acb82d6cec7'))
        file_name2 = dl.get_next_file_name()
        self.assertEqual(True, file_name2.startswith('D:\\MY_DownLoad'))
        self.assertEqual(True, file_name2.endswith('flv'))
        self.assertNotEqual(-1, file_name2.find('e900b5f1420886d08fe60acb82d6cec7'))
        self.assertNotEqual(file_name2,file_name)
        
        
    def test_link2(self):
        test_src_link = "https://flv-live-ws.xingyan.panda.tv/panda-xingyan/722c94a07a91fde51a318de3223a47e8.flv"
        dl = Downloader_stable_link.DownloaderStableLink(test_src_link)
        link = dl.get_next_link()
        self.assertEqual(link, test_src_link)
        file_name = dl.get_next_file_name() 
        self.assertEqual(True, file_name.startswith('D:\\MY_DownLoad'))
        self.assertEqual(True, file_name.endswith('flv'))
        self.assertNotEqual(-1, file_name.find('722c94a07a91fde51a318de3223a47e8'))
        file_name2 = dl.get_next_file_name()
        self.assertEqual(True, file_name2.startswith('D:\\MY_DownLoad'))
        self.assertEqual(True, file_name2.endswith('flv'))
        self.assertNotEqual(-1, file_name2.find('722c94a07a91fde51a318de3223a47e8'))
        self.assertNotEqual(file_name2,file_name)
        
        
    def test_link3(self):
        test_src_link = "https://flv-live-ws.xingxiu.panda.tv/panda-xingxiu/202cd4e68db2553f2f6a9c90bf65c16d.flv?0.5197100099176168"
        dl = Downloader_stable_link.DownloaderStableLink(test_src_link)
        link = dl.get_next_link()
        self.assertEqual(link, test_src_link)
        file_name = dl.get_next_file_name() 
        self.assertEqual(True, file_name.startswith('D:\\MY_DownLoad'))
        self.assertEqual(True, file_name.endswith('flv'))
        self.assertNotEqual(-1, file_name.find('202cd4e68db2553f2f6a9c90bf65c16d'))
        file_name2 = dl.get_next_file_name()
        self.assertEqual(True, file_name2.startswith('D:\\MY_DownLoad'))
        self.assertEqual(True, file_name2.endswith('flv'))
        self.assertNotEqual(-1, file_name2.find('202cd4e68db2553f2f6a9c90bf65c16d'))
        self.assertNotEqual(file_name2,file_name)
        
    def test_link4(self):
        test_src_link = "https://ws.p2p.huya.com/huyalive/85956800-2559586022-10993338255788736512-2883629200-10057-A-0-1_420_0.slice?wsSecret=c7d348a0b13ec2a6e83ea51485ef54cc&wsTime=5b896beb&ex1=0&baseIndex=0&quickTime=2000&timeStamp=2018-09-01_00:25:39.601&u=-1327849161&t=100&sv=1808301533"
        dl = Downloader_stable_link.DownloaderStableLink(test_src_link)
        link = dl.get_next_link()
        self.assertEqual(link, test_src_link)
        file_name = dl.get_next_file_name() 
        self.assertEqual(True, file_name.startswith('D:\\MY_DownLoad'))
        self.assertEqual(True, file_name.endswith('flv'))
        self.assertNotEqual(-1, file_name.find('85956800-2559586022-10993338255788736512-2883629200'))
        file_name2 = dl.get_next_file_name() 
        self.assertEqual(True, file_name2.startswith('D:\\MY_DownLoad'))
        self.assertEqual(True, file_name2.endswith('flv'))
        self.assertNotEqual(-1, file_name2.find('85956800-2559586022-10993338255788736512-2883629200'))
        self.assertNotEqual(file_name2,file_name)
        
    def test_link5(self):
        test_src_link = "http://124.165.216.84/hdl0901.plures.net/onlive/67c3434ebf454429819c33806fc85b14.flv?wsSecret=d4fa274267f6b5bef58bbf6e744ad124&wsTime=5b896ca3&wshc_tag=0&wsts_tag=5b896cbb&wsid_tag=72f4bb6a&wsiphost=ipdbm"
        dl = Downloader_stable_link.DownloaderStableLink(test_src_link)
        link = dl.get_next_link()
        self.assertEqual(link, test_src_link)
        file_name = dl.get_next_file_name() 
        self.assertEqual(True, file_name.startswith('D:\\MY_DownLoad'))
        self.assertEqual(True, file_name.endswith('flv'))
        self.assertNotEqual(-1, file_name.find('67c3434ebf454429819c33806fc85b14'))
        file_name2 = dl.get_next_file_name() 
        self.assertEqual(True, file_name2.startswith('D:\\MY_DownLoad'))
        self.assertEqual(True, file_name2.endswith('flv'))
        self.assertNotEqual(-1, file_name2.find('67c3434ebf454429819c33806fc85b14'))
        self.assertNotEqual(file_name2,file_name)

if __name__ == '__main__':
    unittest.main()