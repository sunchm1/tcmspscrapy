# tcmspscrapy
tested in python>=3.8

所需的库：
requests
bs4
pandas

“scrapylib.py”——该爬虫的类库

“paqushuju.py” 顾名思义爬取数据，请自行修改源文件中的token，token从浏览器浏览tcmsp时的URL获得
如：https://www.tcmsp-e.com/tcmspsearch.php?qr=Citrus%20Reticulata&qsr=herb_en_name&token=f3bc803f0197f6cec27cf22f6b1adc01

“guolvshuju.py” 顾名思义过滤数据，得到OB>=0.3,dl>=0.18的成分，并修改相应的靶标数据

