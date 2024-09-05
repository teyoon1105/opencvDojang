import threading
import time

# 공유 자원 설정
sum_lock = threading.Lock()
total_sum = 0

# 스레드 함수 정의
def calculate_sum(start, end):
    global total_sum
    local_sum = 0
    for i in range(start, end + 1):
        local_sum += i
    
    with sum_lock:
        total_sum += local_sum

# 시작 시간 기록
start_time = time.time()

# 스레드 생성 및 시작
thread1 = threading.Thread(target=calculate_sum, args=(1, 50000000))
thread2 = threading.Thread(target=calculate_sum, args=(50000001, 100000000))
thread1.start()
thread2.start()

# 스레드 종료 대기
thread1.join()
thread2.join()

# 종료 시간 기록 및 실행 시간 계산
end_time = time.time()
execution_time = end_time - start_time

# 결과 출력
print(f"1부터 1억까지의 합: {total_sum}")
print(f"실행 시간: {execution_time}초")