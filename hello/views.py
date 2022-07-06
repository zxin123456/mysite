from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string


def hello_world(request):
    return HttpResponse('hello world')
    print(revers('hello_world'))
def hello_china(request):
    return HttpResponse('hello china')
def hello_html(request):
    html = """
    <html>
        <body>
            <h1 style="color:#f00">hello html</h1>>
        </body>
    </html>
    """

    return HttpResponse(html)

def article_list(request,month):
    return HttpResponse('article:{}'.format(month))

def search(request):

    name = request.GET.get('name',' ')
    print(name)
    return HttpResponse('查询成功')
def render_str(request):
    templ_name = 'hello/index.html'
    html = render_to_string(template_name=templ_name)
    return HttpResponse(html)

def render_html(request):

    return render(request, 'hello/index.html')

def http_request(request):
    print(request.method)
    headers = request.META
    print(headers)
    ua = request.META.get('HTTP_USER_AGENT',None)
    print(ua)
    print(request.headers)
    print(request.headers['User-Agent'])
    print(request.headers['user-agent'])

    name = request.GET.get('name','')
    print(name)
    return HttpResponse('响应')

def http_response(request):
    # resp = HttpResponse('响应内容',status=201)
    # resp.status_code = 204
    # print(resp.status_code)
    # return resp
    user_info = {
        'name': '张三',
        'age' : '34'
    }
    return JsonResponse(user_info)

def no_data_404(request):
    return HttpResponse('404')

def article_detail(request,article_id):
    if article_id < 1000:
        #return HttpResponseRedirect(reversed('no_data_404'))
        return redirect('no_data_404')
    return HttpResponse('文章{}的内容'.format(article_id))

def page_500(request):
    return HttpResponse('服务器正忙，请稍后重试')