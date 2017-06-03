#coding-utf-8
import re,sys
from bs4 import BeautifulSoup
import time
from util import getUrl

sys.setrecursionlimit(1000000) 
baseUrlList = [
"http://yuyi0479.tumblr.com",
"http://bishihuiyi.tumblr.com",
"http://dream-wets.tumblr.com",
"http://xiaowanzi-tang.tumblr.com",
"http://qplovecr.tumblr.com",
"http://zaixialvbu.tumblr.com",
"http://stockingbaby.tumblr.com",
"http://xhzxgz.tumblr.com",
"http://keri-011.tumblr.com",
"http://suegn-8471.tumblr.com",
"http://390950355.tumblr.com",
"http://yemao53113.tumblr.com",
"http://nuanliu.tumblr.com",
"http://xxgreenfrogxx.tumblr.com",
"http://trainerofrose.tumblr.com",
"http://szql123.tumblr.com",
"http://greenhat1314.tumblr.com",
"http://jingcexiatian.tumblr.com",
"http://teenagedelusionparadise.tumblr.com",
"http://jack07452.tumblr.com",
"http://vx-wliu910123.tumblr.com",
"http://weazcola1.tumblr.com",
"http://vvvvvlbb.tumblr.com",
"http://fuckwq.tumblr.com",
"http://monkeygiraffe767.tumblr.com",
"http://loo-ooo.tumblr.com",
"http://itshopefulperfectionbouquetblog.tumblr.com",
"http://nvxing.tumblr.com",
"http://y2011803.tumblr.com",
"http://abang1990.tumblr.com",
"http://chinaoutdoors.tumblr.com",
"http://833244.tumblr.com",
"http://kkinaw3.tumblr.com",
"https://redsexbitch.tumblr.com",
"http://girlllfriend.tumblr.com",
"http://masteranddoglead.tumblr.com",
"http://sara-00-sara.tumblr.com",
"http://zero-ppp.tumblr.com",
"http://asura-anger.tumblr.com",
"http://nanrenfengcai.tumblr.com",
"http://missyourselfagain.tumblr.com",
"http://tecnos96.tumblr.com",
"http://landiskey.tumblr.com",
"http://bellebodys.tumblr.com",
"http://sweetlyman.tumblr.com",
"http://qwd758.tumblr.com",
"https://venustrap1910.tumblr.com",
"http://matrix097.tumblr.com",
"http://saotunnannan.tumblr.com",
"http://shuimuqingfeng.tumblr.com",
"http://chenge124.tumblr.com",
"http://qi-c-c.tumblr.com",
"http://lovely-annie.tumblr.com",
"http://lovely-tracy.tumblr.com",
"http://loveobedientlybitch1399.tumblr.com",
"http://parrotblood.tumblr.com",
"http://e1225815.tumblr.com",
"http://pussynah.tumblr.com",
"http://hesayiammiracler.tumblr.com",
"http://kirkykirk.tumblr.com",
"http://secret599.tumblr.com",
"http://doubleher.tumblr.com",
"https://subjugatecouple.tumblr.com",
"http://xiaoxiaobai12138.tumblr.com",
"http://yaoyaomei.tumblr.com",
"http://yinqi-ntr.tumblr.com",
"http://yinwoqi.tumblr.com",
"http://yiyi2016kink.tumblr.com",
"http://yohomiao.tumblr.com",
"http://zhling1994.tumblr.com",
"http://zhuchangan.tumblr.com",
"http://xiaogougou.tumblr.com",
"http://xiaokonglaoshi.tumblr.com",
"http://xavieml.tumblr.com",
"http://wlovelw0816.tumblr.com",
"http://viewpro.tumblr.com",
"http://soulwaiting.tumblr.com",
"http://tiffanypang16.tumblr.com",
"http://soratum.tumblr.com",
"http://saosaoqiuai.tumblr.com",
"http://sexyyc.tumblr.com",
"http://russy555.tumblr.com",
"http://queenwen.tumblr.com",
"http://queendanmo.tumblr.com",
"https://qiqimeijiqi.tumblr.com",
"http://pennysexy.tumblr.com",
"http://pangxiaonuoyaogege.tumblr.com",
"http://niexiaoxin.tumblr.com",
"http://nuoer.tumblr.com",
"http://ntr1234.tumblr.com",
"http://maomao1069.tumblr.com",
"http://lonelypatients025.tumblr.com",
"http://lgwwl7777.tumblr.com",
"http://ll0202.tumblr.com",
"https://mypaperbagslut.tumblr.com",
"http://wakaya1213.tumblr.com",
"http://s721s721s721.tumblr.com",
"http://nami0716.tumblr.com",
"http://exposure-to-wife.tumblr.com",
"http://xy730.tumblr.com",
"http://yazu-sao.tumblr.com",
"http://11122ppp.tumblr.com",
"http://chengshaobin.tumblr.com",
"https://littlesexroom.tumblr.com",
"http://shijian99570.tumblr.com",
"http://konstantine30.tumblr.com",
"http://jsg-qi.tumblr.com",
"http://ivanyao.tumblr.com",
"http://huoer.tumblr.com",
"http://catherinefe.tumblr.com",
"https://htl69.tumblr.com",
"http://hongwuye.tumblr.com",
"http://hongjizhifeng.tumblr.com",
"https://hlmmbaby.tumblr.com",
"http://unasit.tumblr.com",
"http://heisarah94.tumblr.com",
"http://liliko99.tumblr.com",
"http://half9999.tumblr.com",
"http://ganodermabitch.tumblr.com",
"https://fuckwife.tumblr.com",
"http://frosty-land.tumblr.com",
"http://dusadoggy.tumblr.com",
"http://conanhomles.tumblr.com",
"http://coco9669.tumblr.com",
"http://cmizico.tumblr.com",
"http://chinkogirl.tumblr.com",
"http://chinatin.tumblr.com",
"http://cc198704.tumblr.com",
"http://cainv.tumblr.com",
"http://blueskybjbj.tumblr.com",
"http://ar-carcass.tumblr.com",
"http://miaomiaof.tumblr.com",
"http://akane88.tumblr.com",
"http://albee0820.tumblr.com",
"http://karenllover.tumblr.com",
"http://ailuoli666.tumblr.com",
"http://naiyinboby.tumblr.com",
"http://pocky-girl.tumblr.com",
"http://a-dirty.tumblr.com",
"https://51lookatme.tumblr.com",
"http://2368736283.tumblr.com",
"http://applem9.tumblr.com",
"http://mengquan1zhi.tumblr.com",
"http://puppyjiangzhaozhuren.tumblr.com",
"http://ellystrikesback.tumblr.com",
"http://3023969727.tumblr.com",
"http://tjsaoshuanghhh.tumblr.com",
"http://cainongsinacom.tumblr.com",
"http://hanyou322.tumblr.com",
"http://dainifei.tumblr.com",
"http://anmengmeng.tumblr.com",
"http://woshiqinweia.tumblr.com",
"http://lu-lunie.tumblr.com",
"http://hahahaha13579.tumblr.com",
"http://lovenanalin.tumblr.com",
"http://reblogking1.tumblr.com",
"http://madkinggg.tumblr.com",
"http://kitty0020092009.tumblr.com",
"http://ningbocouples.tumblr.com",
"http://nvbao.tumblr.com",
"http://grosserboss.tumblr.com",
"http://angelskyjack.tumblr.com",
"http://feiermm.tumblr.com",
"http://bigpenis236.tumblr.com",
"http://mxdwusi.tumblr.com",
"http://hdhhbwj.tumblr.com",
"http://jiaoqi900202.tumblr.com",
"http://yzralbus.tumblr.com",
"http://bunbunmylove.tumblr.com",
"http://charlieweng.tumblr.com",
"http://nudebatgirl.tumblr.com",
"http://djbgsn520.tumblr.com",
"http://huxudagua.tumblr.com",
"http://318taotao.tumblr.com",
"http://yanguoliang.tumblr.com",
"http://johnny280.tumblr.com",
"http://tony0103.tumblr.com",
"http://lilovez.tumblr.com",
"http://greyforesthu.tumblr.com",
"http://mellowfesttriumph.tumblr.com",
"http://livehaha.tumblr.com",
"http://aq1903693296.tumblr.com",
"http://chnaqi.tumblr.com",
"http://kovkdmoo.tumblr.com",
"http://sexiaomin.tumblr.com",
"http://lovejinerfan.tumblr.com",
"http://naiyayingzi-queen.tumblr.com",
"http://2379399169.tumblr.com",
"http://fuktwgirl.tumblr.com",
"http://slutty-asian-hotwife.tumblr.com",
"https://lovewifeforcrazy.tumblr.com",
"http://gogoylj.tumblr.com",
"http://asdbit.tumblr.com",
"http://subinpapa.tumblr.com",
"http://saodiandian.tumblr.com",
"http://xzxbxx.tumblr.com",
"http://showtimecc.tumblr.com",
"http://chenqin.tumblr.com",
"http://2592532122.tumblr.com",
"http://yayasez.tumblr.com",
"http://cz10160000.tumblr.com",
"https://nancymeng.tumblr.com",
"http://cherryboomh.tumblr.com",
"http://xbx123.tumblr.com",
"http://asianbreeding.tumblr.com",
"http://cnkeyes666.tumblr.com",
"http://asianfiona.tumblr.com",
"http://asiancuckoldlover.tumblr.com",
"http://niceaaaaaa.tumblr.com",
"http://yuyuxiaoxiao.tumblr.com",
"http://deepsleepl.tumblr.com",
"http://frgyhhhhh.tumblr.com",
"http://sexrapesex20162016.tumblr.com",
"http://panduolazazhi.tumblr.com",
"http://shike-suzhi-88.tumblr.com",
"http://cctv91porn.tumblr.com",
"http://tianli2015.tumblr.com",
"http://ccdjb.tumblr.com",
"http://omnibusrrr.tumblr.com",
"http://caoyuanbazhu.tumblr.com",
"http://91ajiuajiu.tumblr.com",
"http://nzzg.tumblr.com",
"http://xnandly.tumblr.com",
"http://luckystarjay.tumblr.com",
"http://pangpang1987.tumblr.com",
"http://bensonwoo.tumblr.com",
"http://azhua.tumblr.com",
"http://yusx3563.tumblr.com",
"http://vindiamond.tumblr.com",
"http://lelenvwang.tumblr.com",
"http://clyl1024.tumblr.com",
"http://leo1000000.tumblr.com",
"http://keainanbaobao.tumblr.com",
"http://nelochan.tumblr.com",
"http://lao47.tumblr.com",
"http://acccc09.tumblr.com",
"https://mizhichasao.tumblr.com",
"http://naughtykaoru.tumblr.com",
"http://bally2.tumblr.com",
"http://yourfavrose-deactivated20161122.tumblr.com",
"http://xiaomiaomiao.tumblr.com",
"http://masteroneyuan.tumblr.com",
"http://biyangla.tumblr.com",
"http://samsayy.tumblr.com",
"http://slowlycolorfulengineer.tumblr.com",
"http://gwnetori.tumblr.com",
"http://yinniqi.tumblr.com",
"http://ordinary12345.tumblr.com",
"http://chxixi.tumblr.com",
"https://moregoin.tumblr.com",
"http://srlive.tumblr.com",
"http://1684550354.tumblr.com",
"http://lyiren.tumblr.com",
"http://yin-wa.tumblr.com",
"http://8haidaowang8.tumblr.com",
"http://yeyeahyeah.tumblr.com",
"http://hisashi1976.tumblr.com",
"http://sexladyyyy.tumblr.com",
"http://kissmango.tumblr.com",
"http://lixiaoyumm.tumblr.com",
"http://zhiniminmin.tumblr.com",
"https://saolulu.tumblr.com",
"http://apple69699.tumblr.com",
"http://baixiaowen.tumblr.com",
"http://yoursweetslovegirlworld.tumblr.com",
"http://jinsefengbao.tumblr.com",
"http://prinece879.tumblr.com",
"http://sharon0415.tumblr.com",
"http://mike-233.tumblr.com",
"http://pnbcfakes.tumblr.com",
"http://celebfakes27.tumblr.com",
"http://maxx315.tumblr.com",
"http://weiweiqiuai.tumblr.com",
"http://moyra12.tumblr.com",
"http://lsaobi.tumblr.com",
"http://bcgg.tumblr.com",
"http://d53471.tumblr.com",
"http://dashan666.tumblr.com",
"http://freeyun.tumblr.com",
"http://eva5201314.tumblr.com",
"https://redwei.tumblr.com",
"http://akasakaandaya.tumblr.com",
"http://matureslavewife.tumblr.com",
"http://xiaoming-xiaotiandi.tumblr.com",
"http://yourpussylover123456789.tumblr.com",
"http://hdfrt.tumblr.com",
"http://lovebabyzoz.tumblr.com",
"http://raped-doll.tumblr.com",
"http://mannmannmannmannmann.tumblr.com",
"http://yuciii.tumblr.com",
"http://asd7789789dsa.tumblr.com",
"https://tutucindy.tumblr.com",
"http://mengyi945.tumblr.com",
"http://dirtytalk1105.tumblr.com",
"http://sunrise668.tumblr.com",
"http://sexyasdfgh1200.tumblr.com",
"http://eyebrow7.tumblr.com",
"http://bmwsl55.tumblr.com",
"http://samsue2628.tumblr.com",
"http://kk11511.tumblr.com",
"http://rp-mij.tumblr.com",
"http://skykid520.tumblr.com",
"http://anny1221.tumblr.com",
"http://moduxiaopaowang.tumblr.com",
"http://littlepumpkinbb.tumblr.com",
"http://easybabyeloue.tumblr.com",
"http://fy518fy.tumblr.com",
"http://xinfenxj.tumblr.com",
"http://thetoys.tumblr.com",
"http://thecitynme.tumblr.com",
"http://sasaw99.tumblr.com",
"http://coolover.tumblr.com",
"http://zzghns.tumblr.com",
"http://crazyambro.tumblr.com",
"http://dggniuv.tumblr.com",
"http://exposebitch.tumblr.com",
"http://manjessss.tumblr.com",
"http://cbrivers.tumblr.com",
"http://publicwifebutterfly.tumblr.com",
"http://skymonk-s.tumblr.com",
"http://yourwifeswetpussy.tumblr.com",
"http://bigcake2012.tumblr.com",
"http://tatalin323.tumblr.com",
"http://exactlycoralchaos.tumblr.com",
"http://nycwait4u.tumblr.com",
"http://glaciergr.tumblr.com",
"http://temuermm.tumblr.com",
"http://mingtoux.tumblr.com",
"http://adrianyang00.tumblr.com",
"http://david1604927.tumblr.com",
"http://hardkingdominternet.tumblr.com",
"http://singer-m.tumblr.com",
"http://xiaosaomugou.tumblr.com",
"http://the-lovingangelcollection.tumblr.com",
"http://baihuweitongwen.tumblr.com",
"http://cold-sundae.tumblr.com",
"http://tiantian695.tumblr.com",
"http://goodbitch1.tumblr.com",
"http://atomchen1.tumblr.com",
"http://bersih76.tumblr.com",
"http://bear4sex.tumblr.com",
"http://nicaiwoainime.tumblr.com",
"http://iamsoeasytocum.tumblr.com",
"http://sexteamate.tumblr.com",
"http://sexyfuckmeee.tumblr.com",
"http://cuckold鈥搇over.tumblr.com",
"http://lsaia30678.tumblr.com",
"http://oreocool.tumblr.com",
"http://yinjianfuqi.tumblr.com",
"http://doridorijam.tumblr.com",
"http://aco520.tumblr.com",
"http://lolicornpop.tumblr.com",
"http://jdjdhhdjdmd.tumblr.com",
"http://zbtdbta485278.tumblr.com",
"http://rixingqianli.tumblr.com",
"http://chaojikaishen.tumblr.com",
"http://chenyenhung.tumblr.com",
"http://michelleslutworld.tumblr.com",
"http://crazyengineerdonut.tumblr.com",
"https://aa20120909.tumblr.com",
"http://nude-vodka.tumblr.com",
"http://yanhong.tumblr.com",
"http://saopoi.tumblr.com",
"http://sonyalai.tumblr.com",
"http://slutgirl355033.tumblr.com",
"http://comet633.tumblr.com",
"http://meimeiyaoyao.tumblr.com",
"http://buhuidjd.tumblr.com",
"http://valiantlygli33tterysheep.tumblr.com",
"http://noahy5843.tumblr.com",
"http://mycharmingwife.tumblr.com",
"http://51851878.tumblr.com",
"http://x-sigmund-freud.tumblr.com",
"http://wing-hkgirl2017.tumblr.com",
"http://sasor1111.tumblr.com",
"http://jocol.tumblr.com",
"http://mastergangbang.tumblr.com",
"http://moon123311.tumblr.com",
"https://humiliatemeplz.tumblr.com",
"http://233333333333333333333333.tumblr.com",
"http://higher059874.tumblr.com",
"http://siyaltsing.tumblr.com",
"http://shigold.tumblr.com",
"http://mrs1985.tumblr.com",
"http://mixcouple.tumblr.com",
"http://wife-hunter.tumblr.com",
"http://zjdcj.tumblr.com",
"http://tuatu.tumblr.com",
"http://xxwife.tumblr.com",
"https://thedesirediary.tumblr.com",
"http://rtyfhre.tumblr.com",
"http://xxoo8181.tumblr.com",
"http://humbleboy.tumblr.com",
"http://duplicitie.tumblr.com",
"http://sm-nanzhu.tumblr.com",
"http://ggxiansheng.tumblr.com",
"http://uuuseee.tumblr.com",
"http://beautyshaw.tumblr.com",
"http://fzzzin.tumblr.com",
"http://vikingtyou.tumblr.com",
"http://ohhh-my-deer.tumblr.com",
"http://76039.tumblr.com",
"http://xiaobaiaisheying.tumblr.com",
"http://whiteeeehana.tumblr.com",
"http://wypgm.tumblr.com",
"http://r65270.tumblr.com",
"http://thesexykatsy.tumblr.com",
"https://sweetie0909.tumblr.com",
"http://aoooo1992.tumblr.com",
"http://bb480.tumblr.com",
"http://polarbear6ice.tumblr.com",
"http://tenkokoko.tumblr.com",
"http://zmziyo.tumblr.com",
"http://zimindoudong.tumblr.com",
"http://zhuhuiln150306.tumblr.com",
"http://xusaobim.tumblr.com",
"http://saomeitingting.tumblr.com",
"http://xingnumugou.tumblr.com",
"http://sluttybitch3068.tumblr.com",
"http://masterkama.tumblr.com",
"http://scarcrowjunk.tumblr.com",
"http://sherrynotthewine.tumblr.com",
"http://yesnakedbutterfly.tumblr.com",
"http://kandedaocaobudao.tumblr.com",
"http://llvoehotwife.tumblr.com",
"http://xifu.tumblr.com",
"http://s-hoooooo.tumblr.com",
"http://yuanweimugou.tumblr.com",
"http://shanghaisexygirl.tumblr.com",
"http://kool17.tumblr.com",
"http://chenyuhan.tumblr.com",
"http://mygirlfrienddaily.tumblr.com",
"http://mugousissi.tumblr.com",
"http://woshijugen.tumblr.com",
"http://xiner.tumblr.com",
"http://luziga456.tumblr.com",
"http://bjqlbo.tumblr.com",
"http://zhangjiayinqi.tumblr.com",
"http://lamapartyx.tumblr.com"
    ]

firstUrl = baseUrlList[-1]

secondUrl=firstUrl+"/page/"
startPage = 1
endPage = 10
result = {
    "img_list" : [],
    "video_list" : []
    }

def tumblrDownHtml():
    currentPage = startPage
    while currentPage <= endPage:
        print('第%d页\n'%(currentPage))
        if currentPage == 1:
            url = firstUrl
        else:
            url = secondUrl+str(currentPage)
        downLoader(url);
        currentPage = currentPage + 1

def downLoader(url):
    while True:
        try:
            get_url = getUrl(url)
            break
        except Exception:    
            time.sleep(1)
            continue
    codingTypr = get_url.encoding
    soup = BeautifulSoup(get_url.text,"html5lib")
    postList = soup.find_all("section", class_="post")
    #Analysis direct img link
    for i in postList:
        imgList = i.find_all("img")
        for j in imgList:
            imgLink = j["src"].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore')
            if not imgLink.endswith(".png"):
                print(imgLink)
                result["img_list"].append(imgLink)
    #Analysis iframe img link   
    for i in postList:
        iframeLink = i.find_all("iframe")      
        for j in  iframeLink:
            print("find a iframe")
            if j["src"].startswith("http"):
                urlLink = j["src"]
            elif j["src"].startswith("//"):
                urlLink = "https:"+j["src"]
            else:
                urlLink = firstUrl+j["src"]
            print(urlLink)    
            downIframe(urlLink)   

def downIframe(url):
    isVideo = False
    while True:
        try:
            get_url = getUrl(url)
            break
        except Exception:    
            time.sleep(1)
            continue
    codingTypr = get_url.encoding
    soup = BeautifulSoup(get_url.text,"html5lib")
    if not url.find("instagram") == -1:
        try:
            videoLink = soup.find_all("div", class_="EmbedFrame EmbedMedia")
            videoLink1 = videoLink[0]
            videoLink2 = videoLink1.a
            handleInsLink('https://www.instagram.com'+videoLink2['href'])
        except IndexError as e:  
            print(e)    
        return
    videoList = soup.find_all("video")        
    for i in videoList:
        try:
            print(i["src"].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))
            result["video_list"].append(i["src"].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))  
        except KeyError:
            sourceLink = i.source
            print(sourceLink["src"].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))   
            result["video_list"].append(sourceLink["src"].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))      
        isVideo = True
        
    if isVideo == False:    
        imgList = soup.find_all("img")
        for j in imgList:
            imgLink = j["src"].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore')
            if not imgLink.endswith(".png"):
                print(imgLink)
                result["img_list"].append(imgLink)

def handleInsLink(url):
    print("handleInsLink: "+url)
    while True:
        try:
            get_url = getUrl(url)
            break
        except Exception:    
            time.sleep(1)
            continue
    codingTypr = get_url.encoding
    soup = BeautifulSoup(get_url.text,"html5lib")
    link = soup.find_all("meta")
    for i in link:
        try:
            if i['property'] == 'og:video:secure_url':
                print(i['content'].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))
                result["video_list"].append(i['content'].encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore'))
        except KeyError:
            continue

if __name__=="__main__":
    totalNum = len(baseUrlList)
    currentNum = 0
    for ilink in baseUrlList:
        print("######start now is %dth link, total number is %d, is %f%%"%(currentNum, totalNum, currentNum*100/totalNum))
        print("link: "+ilink)
        firstUrl = ilink
        tumblrDownHtml()
        p = re.compile("[^\w]*")
        fileName = p.sub('', firstUrl)
        fpath = 'D:\\3333\\'+fileName+'.txt'
        try:
            with open(fpath, 'w') as f:
                f.write('')
            with open(fpath, 'a') as f:
                f.write('result:\n')
                f.write('img:\n')
                for i in result["img_list"]:
                    f.write(i+'\n')
                f.write('video:\n')    
                for i in result["video_list"]:
                    f.write(i+'\n')  
        except OSError as e:
            print(e)
        print('done') 
        currentNum = currentNum + 1    
        result["img_list"] = []
        result["video_list"] = []
        
        
        
        
        
        
        
        
        