import signal


def handler(signum, frame):
    # 定义一个信号处理函数，当超时发生时，触发该函数。
    raise TimeoutError("Function call timed out.")


# def set_timeout(func,arr_list, timeout):
#     # 使用signal模块注册信号处理函数，当超时出现时，触发handler函数。
#     signal.signal(signal.SIGALRM, handler)
#     # 设置超时时间
#     signal.alarm(timeout)
#
#     try:
#         # 执行函数调用
#         result = func(arr_list[0],arr_list[1])
#         # 取消信号的设置
#         signal.alarm(0)
#         return result
#     except TimeoutError as te:
#         raise te
#     except Exception:
#         # 其他异常处理
#         signal.alarm(0)
#         raise

def set_timeout(func, timeout):
    # 使用signal模块注册信号处理函数，当超时出现时，触发handler函数。
    signal.signal(signal.SIGALRM, handler)
    # 设置超时时间
    signal.alarm(timeout)

    try:
        # 执行函数调用
        result = func()
        # 取消信号的设置
        signal.alarm(0)
        return result
    except TimeoutError as te:
        raise te
    except Exception:
        # 其他异常处理
        signal.alarm(0)
        raise
