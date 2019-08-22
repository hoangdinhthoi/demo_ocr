from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser
from django.http import JsonResponse
from api.form import OcrForm
from api.image_processing import prepare_image
from api import tf_sering
import numpy as np
import itertools
import ast
from ocr_demo.settings import OCR_CHARACTER_MAPPING
from ocr_demo.settings import EMPTY_TEXT


class OcrView(APIView):
    parser_classes = (MultiPartParser, JSONParser)

    def json_response(self, data=None, status=200):
        response = JsonResponse({'data': data}, status=status)
        return response


    def post(self, request):
        form = OcrForm(request.POST)
        if not form.is_valid():
            return self.json_response(status=500)
        image_base64 = form.cleaned_data.get('image')
        location = form.cleaned_data.get('location')
        image = prepare_image(image_base64)
        print (image)
        if image is None:
            return self.json_response(status=500)
        ocr_result = np.squeeze(tf_sering.call(image))
        location = ast.literal_eval(location)
        print(location)
        # text = self.process_ocr_result(ocr_result)
        # data = {'text': text}
        data = 1
        return self.json_response(data=data)


    def process_ocr_result(self, ocr_result):
        def label_to_text(label):
            text = ''
            for l in label:
                if l < len(OCR_CHARACTER_MAPPING):
                    text += OCR_CHARACTER_MAPPING[l]
            return text
        if len(ocr_result.shape) < 2:
            return EMPTY_TEXT
        ocr_result = np.argmax(ocr_result, axis=-1)
        ocr_result = [k for k, _ in itertools.groupby(ocr_result)]
        recognized_text = label_to_text(ocr_result)
        return recognized_text
