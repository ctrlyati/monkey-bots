#TapTitans
#####bot เพื่อการศึกษา
เอาไว้ศึกษาการทำ Test บน Android นะครับ

##System Requirements
- ต้องมี AndroidSDK ซึ่งสามารถ Download ได้ที่
http://developer.android.com/sdk/installing/index.html?pkg=tools โดยเวอร์ชั่นใหม่สุดขณะเขียนสามารถ download ได้ตามลิงค์ด้านล่าง
 - Windows : http://dl.google.com/android/android-sdk_r24.0.2-windows.zip
 - Mac : http://dl.google.com/android/android-sdk_r24.0.2-macosx.zip
 - Linux : http://dl.google.com/android/android-sdk_r24.0.2-linux.tgz
- ต้องมีไฟล์ jython เวอร์ชั่นใหม่ล่าสุด ซึ่งจะ download ได้ที่ http://www.jython.org/downloads.html (ให้ download เวอร์ชั่น 2.5.4rc1 หรือใหม่กว่าเท่านั้น)
และเมื่อ download เสร็จแล้ว ให้นำไปวางไว้ที่ `/tools/lib` โดยเราจะต้องนำไฟล์ jython-standalone เวอร์ชั่นเก่าออกด้วย (โดยการลบ หรือ backup ไว้ที่อื่น การแก้ชื่อไฟล์ไม่ได้ผล)

##Download
สามารถ download ไฟล์ได้ที่ https://github.com/ctrlyati/monkey-bots


##Installation
ให้นำไฟล์ที่อยู่ภายใน sdk ออกมาแล้วทำการแก้ไขชื่อ Directory จาก `android-sdk-*` เป็น `android-sdk` แล้วจากนั้นให้นำไฟล์ที่จะ download ต่อไปนี้ วางไว้ใน Dicrectory เดียวกันกับ `android-sdk` แล้วจะได้ผลลัพท์คือทั้งสามไฟล์ด้านล่างอยู่ใน Directory เดียวกัน
```
android-sdk
monkeyScript
TapTitans.bat
README.md
```

##Usage
ให้เปิดเกมให้เสร็จ แล้วรัน TapTitans.bat ที่เหลือ อ่านเอาข้างในแล้วกัน