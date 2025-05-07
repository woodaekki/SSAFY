from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Stocks

from selenium import webdriver as wb 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('headless') # 창 띄우지 않는 옵션 설정

def search(request) : 
    keyword = request.GET.get('query')
    stocks = Stocks.objects.filter(CompanyName = keyword)
    stocks.delete()
    driver = wb.Chrome(options=options)
    url = 'https://tossinvest.com/'
    driver.get(url)
    driver.find_element(By.CSS_SELECTOR , "span.tw-1r5dc8g0").click()
    driver.find_element(By.CSS_SELECTOR , 'input._1x1gpvi6').send_keys(keyword,Keys.ENTER)
    time.sleep(1)
    url = driver.current_url[0:-6] + '/community'
    driver.get(url)
    time.sleep(1)
    StockCode = driver.find_element(By.CSS_SELECTOR , "#__next > div.ho2myi0 > div.ho2myi1 > main > div > div > div > div.njzdl30 > div > div._1sivumi0 > div:nth-child(1) > span:nth-child(2)")
    CompanyName = driver.find_element(By.CSS_SELECTOR , "#__next > div.ho2myi0 > div.ho2myi1 > main > div > div > div > div.njzdl30 > div > div._1sivumi0 > div:nth-child(1) > span:nth-child(1)")
    for i in range(5) : 
        Comments = driver.find_element(By.CSS_SELECTOR , f"#stock-content > div > div > section > section > ul > div > div:nth-child({3+i}) > article > div > a > span:nth-child(2) > span")
        print(Comments)
        print('l')
        stock = Stocks(StockCode = StockCode.text, CompanyName = CompanyName.text, Comments = Comments.text)
        stock.save()
    return redirect('crawlings:search_page', CompanyName.text)

# Create your views here.
def index(request):
    # if request.method == "POST" : 
    #     stocks = Stocks.objects.filter()
    # context = {
    #     'stocks' : stocks, 
    # }
    return render(request, 'crawlings/index.html/')

def search_page(request, keyword):
    stocks = Stocks.objects.filter(CompanyName=keyword)
    context = {
        'stocks': stocks,
    }
    return render(request, 'crawlings/index.html', context)


def delete_comment(request):
    stock_id = request.POST.get('stock_id')
    stock = get_object_or_404(Stocks, id=stock_id)
    company_name = stock.CompanyName  # 삭제 전에 회사명을 저장
    stock.delete()
    return redirect('crawlings:search_page', company_name)
