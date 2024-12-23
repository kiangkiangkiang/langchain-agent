import base64
import io

from openai import OpenAI


def call_openai_with_image(input_text, image, system_prompt):
    client = OpenAI()

    # Read
    base64_images = []

    buffer = io.BytesIO()

    # 將影像儲存到 buffer 中，格式為 JPEG
    image.save(buffer, format="JPEG")

    # 取得 byte 資料
    byte_data = buffer.getvalue()

    base64_images = base64.b64encode(byte_data).decode("utf-8")

    # Transform
    request_obj = [
        {
            "type": "text",
            "text": input_text,
        }
    ]

    request_obj.append(
        {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{base64_images}"},
        }
    )

    # Call API
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": request_obj,
            },
        ],
    )
    return response.choices[0].message.content
