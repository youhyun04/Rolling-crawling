import mysql.connector
import json

class MySQLStorage:
    def __init__(self, host, user, password, database):
        # MySQL 연결 설정
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def save_data(self, data, data_type):
        # 데이터 저장 SQL 쿼리
        insert_query = """
        INSERT INTO data_storage (data_type, content) VALUES (%s, %s)
        """
        self.cursor.execute(insert_query, (data_type, data))
        self.connection.commit()

    def save_bulk_data(self, data_list):
        # 대용량 데이터 삽입 (배치 처리)
        insert_query = """
        INSERT INTO data_storage (data_type, content) VALUES (%s, %s)
        """
        self.cursor.executemany(insert_query, data_list)
        self.connection.commit()

    def close(self):
        # MySQL 연결 종료
        self.cursor.close()
        self.connection.close()


def process_and_store_data(storage, data, format_type):
    if format_type.lower() == "json":
        # JSON 데이터 저장
        content = json.dumps(data, ensure_ascii=False, indent=4)
        storage.save_data(content, "json")
    elif format_type.lower() == "html":
        # HTML 데이터 저장
        storage.save_data(data, "html")
    elif format_type.lower() == "markdown":
        # Markdown 데이터 저장
        storage.save_data(data, "markdown")
    else:
        print("Unsupported format type. Use 'json', 'html', or 'markdown'.")


def process_and_store_bulk_data(storage, data_list):
    bulk_data = []
    for item in data_list:
        format_type = item.get("format_type")
        data = item.get("data")

        if not format_type or not data:
            print(f"Invalid data item: {item}")
            continue

        if format_type.lower() == "json":
            content = json.dumps(data, ensure_ascii=False, indent=4)
            bulk_data.append(("json", content))
        elif format_type.lower() == "html":
            bulk_data.append(("html", data))
        elif format_type.lower() == "markdown":
            bulk_data.append(("markdown", data))
        else:
            print(f"Unsupported format type: {format_type}")
            continue

    storage.save_bulk_data(bulk_data)


# 실행 예시
try:
    # MySQL 저장 모듈 초기화
    storage = MySQLStorage(host="localhost", user="root", password="new_password", database="my_database")

    # JSON 데이터 저장
    json_data = {"title": "Example", "description": "This is a JSON example"}
    process_and_store_data(storage, json_data, "json")

    # HTML 데이터 저장
    html_data = "<p>This is an HTML example</p>"
    process_and_store_data(storage, html_data, "html")

    # Markdown 데이터 저장
    markdown_data = "## Markdown Example\n\nThis is an example."
    process_and_store_data(storage, markdown_data, "markdown")

    # 대량 데이터
    bulk_data = [
        {"format_type": "json", "data": {"title": "Bulk 1", "description": "This is bulk JSON 1"}},
        {"format_type": "html", "data": "<p>This is bulk HTML 1</p>"},
        {"format_type": "markdown", "data": "## Bulk Markdown 1\n\nThis is bulk markdown 1"},
    ]

    process_and_store_bulk_data(storage, bulk_data)

    # 연결 종료
    storage.close()

except mysql.connector.Error as err:
    print(f"MySQL Error: {err}")




