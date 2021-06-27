# 圖片轉換成文字

## 程式碼

```
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = Image.open('test2.png')
text = pytesseract.image_to_string(img, lang='eng')
print(text)

```

## 說明

### OCR 與 Tesseract

OCR 為光學文字識別的縮寫（Optical Character Recognition，OCR），白話一點就是將圖片翻譯為文字。而 Tesseract 是一個 OCR 模組，目前由 Google 贊助。Tesseract 已經有 30 年歷史，一開始它是惠普實驗室的一款專利軟體，於 2005 年開源，從 2006 年後由 Google 贊助進行後續的開發和維護， Tesseract 也是目前公認最優秀、最精準的開源 OCR 系統。

##

[img](https://github.com/hongyu101094/ai109b/blob/main/HW4/test1.jpg)

## 參考資料

[參考資料](https://medium.com/codingbar/%E4%B8%8D%E6%83%B3%E6%89%93%E5%AD%97-%E7%94%A8-python-%E6%8A%8A%E5%9C%96%E7%89%87%E8%AE%8A%E6%96%87%E5%AD%97-ff1be7f9efef)
