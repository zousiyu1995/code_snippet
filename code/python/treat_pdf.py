from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os


def get_designated_file_name(path, ext, out_file_name):
    for folder, subdirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == ext:
                if file == out_file_name:
                    print("跳过 %s" % out_file_name)
                    continue
                else:
                    yield os.path.join(folder, file)


current_path = os.path.split(os.path.abspath(__file__))[0]
out_file_name = 'out.pdf'
out_file_path = os.path.join(current_path, out_file_name)
file_name = list(get_designated_file_name(current_path, '.pdf', out_file_name))

# ===================================== #

# pdf_out = PdfFileWriter()
# if len(file_name) != 0:
#     for f in file_name:
#         print("正在处理 %s" %f)
#         pdf_input = PdfFileReader(open(f, 'rb'))
#         pdf_out.addPage(pdf_input.getPage(1))
#     pdf_out.write(open(out_file_path, 'wb'))
# else:
#     print("当前文件夹没有pdf文件！")

# ===================================== #

pdf_out = PdfFileMerger()
if len(file_name) != 0:
    for f in file_name:
        print("正在处理 %s" % f)
        pdf_out.append(f, pages=(1, 2))
    pdf_out.write(out_file_path)
else:
    print("当前文件夹没有pdf文件！")
