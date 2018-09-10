# coding=utf-8
import matplotlib.pyplot as plt
import imageio


def read_document(docx_file_path):
    """
    获取文档(docx)对象，将文档内容按段落读入，并存入doc中
    """
    import docx

    file_content = docx.Document(docx_file_path)
    doc = ""
    for para in file_content.paragraphs:
        doc = doc + para.text
    return doc


def read_text_utf8(text_utf8_path):
    """
    获取text(utf8)内容，并返回
    """
    import codecs
    text_from_file_with_path = codecs.open(text_utf8_path, 'r', 'utf-8').read()
    return text_from_file_with_path


def get_wordcloud(content_from_file):
    """
    获取词云对象
    """
    from wordcloud import WordCloud
    import jieba

    wordlist_after_jieba = jieba.cut(content_from_file, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)

    my_wordcloud = WordCloud(
        font_path=r'./Fonts/simhei.ttf',
        background_color="white",
        width=2000, height=1500, margin=5,
        # mask=bg_pic,
        stopwords=stopwordset
    )
    my_wordcloud.generate(wl_space_split)
    return my_wordcloud


docx_file = "./党的十九大报告全文.docx"
bg_pic = imageio.imread('./pic/04.jpg')
text_from_file = read_document(docx_file)
stopwordset = set()
stopwordset.update(["国特", "会主", "国人", "主义", "社会"])

my_wordcloud = get_wordcloud(text_from_file)
plt.imshow(my_wordcloud)
# 是否显示x轴、y轴下标
plt.axis("off")
# 显示词云图
plt.show()
