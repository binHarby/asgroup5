import logging

import azure.functions as func
from modules.library_finder import *

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        req_body = req.get_json()
        logging.info(f'Request body: {req_body}')
    except:
        return func.HttpResponse('Failed to load json request')
    try:
        text = req_body.get('text').lower()
        library_df=''

        if ('man' in text) or ('?' in text):
             library_df = manual()
             return func.HttpResponse(f'```   \n {library_df}')
        

        elif 'info' in text:
             data = text.replace('info','')
             library_df = info1(data.strip())
             return func.HttpResponse(f'```   \n {library_df.to_string()}')
        elif 'news' in text:
             data = text.replace('news','')
             library_df = news(data.strip())
             return func.HttpResponse(f'```   \n {library_df.to_string()}')
        elif 'check' in text:
             data = text.replace('check','')
             alist=data.split(" ")
             city,center='',''
             if len(alist)==3:
                 city=str(alist[0])+str(alist[1])
                 center=str(alist[2])
             elif len(alist)==2:
                 city=str(alist[0])
                 center=str(alist[1])
             else:
                 return func.HttpResponse(f'```   \n Please pass a valid command in the request text')
             library_df = imgg(city.strip(),center.strip())
             return func.HttpResponse(f'```   \n {library_df.to_string()}')

        elif 'available' in text:
            city = text.replace('available','')
            library_df = available(city.strip())
            return func.HttpResponse(f'```   \n {library_df.to_string()}')

        else:
            return func.HttpResponse(
                "Please pass a valid command in the request text"+f'```   \n {library_df.to_string()}'
            )
    except Exception as e:
        return func.HttpResponse('Json in request was not in the correct format \nError: '+f'{e}```   \n {library_df.to_string()}')