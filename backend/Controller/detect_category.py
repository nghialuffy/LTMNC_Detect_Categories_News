from flask.globals import request
from flask_restful import Resource, abort
from Controller import nb_model, label_encode
import requests
from core import text_preprocess
from newspaper import Article

class DetectCategory(Resource):
    def post(self):
        try:
            res = {}
            url = request.json.get("url")
            article = Article(url)
            article.download()
            article.parse()
            document = article.text
            document = text_preprocess(document)
            # print(document)
            label_predict_index = nb_model.predict([document])
            res["category"] = str(label_encode[int(label_predict_index)])
            res["context"] = document
            return res
        except Exception as exc:
            print("Error in DetectCategory", exc)
            return abort(401)
