# 데이터 전처리 : 수집된 데이터를 정리 후 분석에 용이하게 가공


import re
raw_text = "<p>Hello, <strong>world</strong>!</p>"
clean_text = re.sub(r"<.*?>", "", raw_text)  # 텍스트 정제: HTML 태그 제거, 특수문자 제거 등
print(clean_text)

# 데이터 저장
import json
import os

# C 드라이브에 output 폴더 생성
output_path = "C:/output"
if not os.path.exists(output_path):
    os.makedirs(output_path)
    
# 샘플 데이터
data = [
{"title": "Example 1", "link": "https://example.com/1", "description": "This is example 1"},
{"title": "Example 2", "link": "https://example.com/2", "description": "This is example 2"},
]

# 저장 함수 정의
def save_data(data, format_type, output_file):
    if format_type.lower() == "json": # JSON 형식으로 저장
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data saved in JSON format: {output_file}")
        
        
    elif format_type.lower() == "html": # HTML 형식으로 저장
        html_content = "<html><body>\n"
        html_content += "<h1>Data</h1>\n<ul>\n"
        for item in data:
            html_content += f"<li><strong>{item['title']}</strong>: <a href='{item['link']}'>{item['link']}</a><br>{item['description']}</li>\n"
            html_content += "</ul>\n</body></html>"
            
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Data saved in HTML format: {output_file}")
        

    elif format_type.lower() == "markdown": # Markdown 형식으로 저장
        markdown_content = "# Data\n\n"
        for item in data:
            markdown_content += f"## {item['title']}\n"
            markdown_content += f"{item['link']}\n\n"
            markdown_content += f"{item['description']}\n\n---\n"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"Data saved in Markdown format: {output_file}")

    else:
        print("Unsupported format. Please use 'json', 'html', or 'markdown'.")

# 파일 저장 경로 설정 및 실행
json_file = os.path.join(output_path, "data.json")
html_file = os.path.join(output_path, "data.html")
markdown_file = os.path.join(output_path, "data.md")

# 데이터 저장
save_data(data, "json", json_file)      # JSON 형식으로 저장
save_data(data, "html", html_file)      # HTML 형식으로 저장
save_data(data, "markdown", markdown_file)   # Markdown 형식으로 저장




