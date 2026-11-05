# 16. "the cat the dog the bird" → 词频字典，必须用 dict.get(w,0)+1，不许用 Counter
# 17. 上题结果按 value 降序取前 3，输出 [('the',3),...]
# 28. safe_div(a,b)、get_score(d,name)：除零提示“除数不能为 0”，KeyError 提示“没有这个学生”，禁止裸 except
# 29. read_lines(path)：逐行读、去行尾 \n、跳过空行返回列表；文件不存在返回 [] 并提示“文件不存在”
# 导入内置csv模块，用来写入csv表格文件
import csv
# 导入jieba分词库，用于中文分词
import jieba


def load_stopwords(stop_file: str = "stopwords.txt") -> set:
    """加载停用词，文件不存在返回空集合
    stop_file: 停用词文件路径，默认 stopwords.txt
    返回值：set集合（查找速度快，用来判断词语是不是停用词）
    """
    # 初始化空集合存放停用词，集合自动去重
    stop_words = set()
    try:
        # 打开停用词文件，只读r，utf-8编码
        with open(stop_file, "r", encoding="utf-8") as f:
            # 循环读取文件每一行
            for line in f:
                # strip() 去掉每行首尾换行、空格
                word = line.strip()
                # 如果处理后不是空字符串，就加入停用词集合
                if word:
                    stop_words.add(word)
    # 捕获【文件找不到】的异常：stopwords.txt不存在的时候触发
    except FileNotFoundError:
        print(f"【提示】停用词文件 {stop_file} 未找到，不使用停用词过滤")
    # 捕获其他未知异常
    except Exception as e:
        print(f"【警告】读取停用词异常：{str(e)}")
    # 返回停用词集合给外面调用
    return stop_words


def count_word_frequency(text: str, stop_words: set, min_len: int = 2) -> dict:
    """
    分词 + 词频统计
    :param text: 原始长文本字符串
    :param stop_words: 停用词集合
    :param min_len: 词语最小长度，默认2（过滤单字，比如“我、的”）
    返回：排序好的词频字典 {词语:次数}
    """
    # 新建空字典，key=词语，value=出现次数
    word_count = {}
    # jieba.lcut() 精确模式分词，返回分词后的列表
    words = jieba.lcut(text)
    # 遍历每一个分词结果
    for w in words:
        # 清理词语两边空白
        w = w.strip()
        # 如果词语长度小于设定最小值，跳过这个词
        if len(w) < min_len:
            continue
        # 如果这个词在停用词里面，跳过
        if w in stop_words:
            continue
        # 统计计数：有这个词就+1，没有默认0再加1
        word_count[w] = word_count.get(w, 0) + 1
    # sorted排序：按词频（x[1]）降序 reverse=True，频次高放前面
    # 转成字典，得到排序后的词频
    word_count = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))
    return word_count


def save_to_csv(word_dict: dict, out_csv: str = "word_freq.csv"):
    """词频字典写入csv文件
    word_dict：统计好的词频字典
    out_csv：输出csv文件名，默认 word_freq.csv
    """
    try:
        # w 写入模式；utf-8-sig 兼容Excel打开不乱码；newline="" 去掉csv多余空行
        with open(out_csv, "w", encoding="utf-8-sig", newline="") as f:
            # 创建csv写入器
            writer = csv.writer(f)
            # 写入表头第一行：词语、频次
            writer.writerow(["词语", "频次"])
            # 循环字典里每一组词和次数，逐行写入
            for k, v in word_dict.items():
                writer.writerow([k, v])
        print(f"✅ 成功输出至：{out_csv}")
    # 捕获权限异常：csv正在被Excel打开占用，无法写入
    except PermissionError:
        print(f"❌ 写入失败：没有权限，请关闭 {out_csv} 再试！")
    # 捕获其他写入异常
    except Exception as e:
        print(f"❌ 保存CSV异常：{str(e)}")


def read_text_from_txt(txt_path: str) -> str:
    """读取txt文本
    txt_path：要读取的txt文件路径
    返回读取到的文本字符串；出错返回空字符串 ""
    """
    try:
        # 只读模式打开文本，utf-8编码读取
        with open(txt_path, "r", encoding="utf-8") as f:
            # 一次性读取全部内容返回
            return f.read()
    # 文件不存在
    except FileNotFoundError:
        print(f"❌ 文本文件 {txt_path} 不存在！")
        return ""
    # 编码错误：文件不是utf-8（比如GBK），读取乱码报错
    except UnicodeDecodeError:
        print(f"❌ 文件编码错误！请用 utf-8 保存 {txt_path}")
        return ""
    # 其余读取异常
    except Exception as e:
        print(f"❌ 读取文本异常：{str(e)}")
        return ""


# 程序入口：只有直接运行这个py文件时，下面代码才执行；被import导入时不执行
if __name__ == "__main__":
    # ========== 配置区，按需修改 ==========
    INPUT_TXT = "article.txt"    # 待统计文本文件
    STOP_FILE = "stopwords.txt"   # 停用词文件
    OUTPUT_CSV = "word_freq.csv"  # 输出csv
    MIN_WORD_LEN = 2              # 最小词长，1=允许单字
    # =====================================

    print("===== 词频统计程序开始 =====")
    # 调用函数加载停用词
    stop_set = load_stopwords(STOP_FILE)
    # 调用函数读取原始文本
    raw_text = read_text_from_txt(INPUT_TXT)

    # 判断：去掉首尾空白之后文本为空
    if not raw_text.strip():
        print("⚠️ 文本内容为空，终止运行")
    else:
        # 调用统计函数，得到词频结果
        freq_result = count_word_frequency(raw_text, stop_set, MIN_WORD_LEN)
        # 判断有没有筛选出有效词语
        if not freq_result:
            print("⚠️ 没有统计到有效词语")
        else:
            # 写入csv
            save_to_csv(freq_result, OUTPUT_CSV)
    print("===== 程序结束 =====")
