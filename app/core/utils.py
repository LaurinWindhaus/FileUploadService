import os
import base64
import uuid
import mimetypes

def save_file_to_storage(base64str: str) -> dict:
    folder = "uploaded_files"
    try:
        if ',' in base64str:
            header, encoded_str = base64str.split(",", 1)
            filetype = header.split(';')[0].split(':')[1].split('/')[1]
        else:
            encoded_str = base64str
            filetype = 'application/octet-stream'

        file_data = base64.b64decode(encoded_str)
        filename = f"{uuid.uuid4()}.{filetype}"

        filepath = os.path.join(folder, filename)
        
        os.makedirs(folder, exist_ok=True)

        with open(filepath, 'wb') as f:
            f.write(file_data)
        
        size = len(file_data)
        url = f"/fileservice/{folder}/{filename}"

        return {"filename": filename, "filetype": filetype, "size": size, "url": url}
    except Exception as e:
        return {"error": str(e)}
    

def delete_file_from_storage(filename: str) -> dict:
    filepath = os.path.join("uploaded_files", filename)
    try:
        os.remove(filepath)
        return {"message": "File deleted successfully"}
    except Exception as e:
        return {"error": str(e)}
    

def file_to_base64_with_mime(filepath: str) -> str:
    mime_type, _ = mimetypes.guess_type(filepath)
    if mime_type is None:
        mime_type = "application/octet-stream"

    with open(filepath, "rb") as file:
        file_content = file.read()

    base64_encoded_content = base64.b64encode(file_content).decode("utf-8")
    base64_string_with_mime = f"data:{mime_type};base64,{base64_encoded_content}"

    return base64_string_with_mime
    

# base64_str = file_to_base64_with_mime("C:\\Development\\FileUploadService\\app\core\\test.pdf")
# print(base64_str)
# save_result = save_file_to_storage(base64_str)
# print(save_result)