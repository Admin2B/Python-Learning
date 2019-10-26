from pdfminer.pdfparser import  PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator

#获取文档对象
fp=open('1.pdf','rb')

#创建与文档关联的分析器
parser=PDFParser(fp)

#PDF文档的对象
doc=PDFDocument()

#连接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

#初始化
doc.initialize('')

#创建PDF资源管理器
resource=PDFResourceManager()

#参数分析器
laparam=LAParams()

#创建聚合器
device=PDFPageAggregator(resource,laparams=laparam)

#创建页面解释器
interpreter=PDFPageInterpreter(resource,device)

#使用文档对象从页面读取内容
for page in doc.get_pages():
    #使用页面解释器读取
    interpreter.process_page(page)

    #使用聚合器来获得内容
    layout=device.get_result()

    for out in layout:
        if hasattr(out,'get_text'):
            print(out.get_text())




