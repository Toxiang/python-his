from aip import AipOcr
import configparser
class baidu_api:
    def __init__(self,filePath):
        #实例化
        target=configparser.ConfigParser()
        target.read(filePath)
        app_id=target.get('工单密码','APP_ID')
        api_key=target.get('工单密码','API_KEY')
        secret_key=target.get('工单密码','secret_key')
        print(app_id,api_key,secret_key)
        APP_ID=app_id
        API_KEY=api_key
        SECRET_KEY=secret_key
        self.client=AipOcr(APP_ID,API_KEY,SECRET_KEY)

    def picturetonum(self,filePath):
        image=self.getfileContent(filePath)
        numbers=self.client.basicGeneral(image)
        # try:
        print(numbers)
        numberlist=list(map(lambda x:int(x),list(numbers['words_result'][0]['words'])))
        print(numberlist)
        # except:
        #     print('识别结果错误')
        #装饰器 静态方法
    # @staticmethod
    # def getfileContent(filePath):
    #     with open(filePath,'rb') as fp:
    #         return fp.read()
    @classmethod
    def getfileContent(cls,filePath):
        with open(filePath,'rb') as fp:
            return fp.read()

if __name__ == '__main__':
    baidu=baidu_api(r'C:\Users\wangz\Desktop\password.ini')
    baidu.picturetonum(r'C:\Users\wangz\Desktop\2.jpg')