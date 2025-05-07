# 주식 댓글 크롤링 웹 서비스 결과 보고서

## 📌 프로젝트 개요
토스증권 웹사이트에서 특정 회사의 주식 커뮤니티 댓글을 Selenium을 이용하여 크롤링하고, Django 웹 애플리케이션을 통해 결과를 검색 및 관리할 수 있도록 구현했습니다.

## 🔍 구현 기능 및 상세 내용

### 1. 크롤링 기능
- **도구 및 기술**: Selenium, ChromeDriver
- **기능 설명**:
  - 사용자가 입력한 회사명을 토스증권에서 검색하여 댓글 데이터를 크롤링
  - 댓글은 상위 5개를 가져와 Django 모델(Stocks)에 저장
- **주요 함수**:
  - `search(request)`: Selenium으로 웹사이트 접속 및 데이터 크롤링, DB 저장

```python
def search(request):
    keyword = request.GET.get('query')
    stocks = Stocks.objects.filter(CompanyName=keyword)
    stocks.delete()
    driver = wb.Chrome(options=options)
    url = 'https://tossinvest.com/'
    driver.get(url)
    driver.find_element(By.CSS_SELECTOR, "span.tw-1r5dc8g0").click()
    driver.find_element(By.CSS_SELECTOR, 'input._1x1gpvi6').send_keys(keyword, Keys.ENTER)
    time.sleep(1)
    url = driver.current_url[0:-6] + '/community'
    driver.get(url)
    time.sleep(1)
    StockCode = driver.find_element(By.CSS_SELECTOR, "#__next > div.ho2myi0 > div.ho2myi1 > main > div > div > div > div.njzdl30 > div > div._1sivumi0 > div:nth-child(1) > span:nth-child(2)")
    CompanyName = driver.find_element(By.CSS_SELECTOR, "#__next > div.ho2myi0 > div.ho2myi1 > main > div > div > div > div.njzdl30 > div > div._1sivumi0 > div:nth-child(1) > span:nth-child(1)")
    for i in range(5):
        Comments = driver.find_element(By.CSS_SELECTOR, f"#stock-content > div > div > section > section > ul > div > div:nth-child({3+i}) > article > div > a > span:nth-child(2) > span")
        stock = Stocks(StockCode=StockCode.text, CompanyName=CompanyName.text, Comments=Comments.text)
        stock.save()
    return redirect('crawlings:search_page', CompanyName.text)
```

### 2. 검색 기능
- **기술 스택**: Django ORM
- **기능 설명**:
  - 사용자가 입력한 회사명으로 Stocks 데이터베이스에서 기존 데이터를 삭제 후 크롤링한 최신 데이터를 저장
  - DB에서 회사명으로 저장된 댓글 데이터를 조회하여 화면에 출력
- **주요 함수**:
  - `search_page(request, keyword)`: DB 조회 후 결과 화면 출력

```python
def search_page(request, keyword):
    stocks = Stocks.objects.filter(CompanyName=keyword)
    context = {'stocks': stocks}
    return render(request, 'crawlings/index.html', context)
```

### 3. 화면 구현
- **기술 스택**: HTML, CSS, Bootstrap
- **화면 구성**:
  - 메인 페이지(index.html): 회사명 입력 후 검색 버튼 제공
  - 결과 페이지:
    - 검색된 회사명과 주식 코드 표시
    - 저장된 댓글 목록 출력
    - 댓글 전체 삭제 버튼 제공 (개별 삭제가 목표였으므로 수정 필요함)

(HTML 코드 생략)

### 4. 삭제 기능
- **기술 스택**: Django ORM
- **기능 설명**:
  - 각 댓글 옆의 '삭제' 버튼을 클릭하면 해당 댓글을 DB에서 삭제하고, 나머지 댓글 목록을 다시 출력
- **주요 함수**:
  - `delete_comment(request)`: 특정 댓글 삭제 후 페이지 리다이렉트

```python
def delete_comment(request):
    stock_id = request.POST.get('stock_id')
    stock = get_object_or_404(Stocks, id=stock_id)
    company_name = stock.CompanyName
    stock.delete()
    return redirect('crawlings:search_page', company_name)
```

---

