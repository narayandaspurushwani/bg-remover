# app.py

import os
from flask import Flask, request, send_file
from rembg import remove
import io

app = Flask(__name__)

# यह endpoint background को हटाता है
@app.route('/remove_bg', methods=['POST'])
def remove_background():
    # जाँच करें कि रिक्वेस्ट में 'image' नाम की फ़ाइल है या नहीं
    if 'image' not in request.files:
        return 'No image file uploaded', 400

    image_file = request.files['image']
    input_bytes = image_file.read()

    # rembg का उपयोग करके background हटाएँ
    output_bytes = remove(input_bytes)

    # प्रोसेस्ड इमेज को रिस्पॉन्स के लिए तैयार करें
    output_buffer = io.BytesIO(output_bytes)
    output_buffer.seek(0)

    # इमेज को 'image/png' टाइप के साथ वापस भेजें
    return send_file(output_buffer, mimetype='image/png')

# यह कोड Render पर सही पोर्ट पर चलने के लिए ज़रूरी है
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
