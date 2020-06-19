# TranslatorBOT

Web service to translate text

## Usage

This script is used to translate text into destination languages by using different translate engine.

For example:

```
from translator import translator
```

* translator_name: google, microsoft, bing, sogou, baidu, alibaba, tencent, youdao, deepl

```
t = translator(translator_name="google") 
```

```
print("result: "+t.translate_text(text="我是谁"))
```