# Thread를 활용하여 연산 속도를 줄여보자

# Thread를 만들기 위한 패키지와 코드 실행 시간을 측정할 time 패키지 불러오기
# Thread에서는 result를 사용할 수 없기 때문에
# queue를 사용해 q값에 결과값을 저장할 수 있게 만듦
import threading
import time
import queue

# Thread 함수 정의
def calculate_sum(start, end, q):
    total_sum = sum(range(start, end + 1))
    # return이 아니라 q.get을 사용하여 함수 결과값을 저장
    q.put(total_sum)
    
    
# 시작 시간 기록
start_time = time.time()

# Queue 생성
q = queue.Queue()

# Thread 생성 및 시작
# 두개의 Thread를 생성하고, 첫번째 thread에선 1~5천만, 두번째 thread에선 5천만1~1억까지 연산
# 해당 연산이 끝날 때 까지 대시
thread1 = threading.Thread(target=calculate_sum, args=(1, 50000000,q))
thread2 = threading.Thread(target=calculate_sum, args=(50000001, 100000000,q))
thread1.start()
thread2.start()

# 각 Thread가 연산을 끝내기 까지 대기
thread1.join()
thread2.join()

# 각 Thread의 결과를 가져온 뒤 합산
total_sum = q.get() + q.get()

# 연산 종료, 종료시간 측정, 코드 실행 시간 측정
end_time = time.time()
code_time = end_time - start_time

# 결과 출력
print('1부터 1억까지의 합 : {}'.format(total_sum))
print('코드 실행 시간 : {}초'.format(code_time))

# 1부터 1억까지 연산 정도는 간단한 편이라
# thread를 사용하지 않는게 좀 더 빠르게 보일 지 몰라도
# 좀 더 복잡한 연산 혹은 아예 분리에서 작업을 해야 하는 경우
# thread를 나눠 연산하는게 효율적이다.