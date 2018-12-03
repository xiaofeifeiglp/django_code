def my_middleware(get_response):
    print('init1被调用')
    def middleware(request):
        print('before request1被调用')
        response = get_response(request)
        print('after response1被调用')
        return response
    return middleware

def my_middleware2(get_response):
    print('init2被调用')
    def middleware(request):
        print('before request2 被调用')
        response = get_response(request)
        print('after response2 被调用')
        return response
    return middleware