# Thread는 하나의 프로세스 안에서 여러개의 Thread를 나눠 연산하는 것
# Multiprocessing은 여러게의 프로세스를 통해 연산하는 작업을 말한다

# 마찬가지로 multiprocessing 패키지 불러오기
import multiprocessing
import time
import queue

def calculate_sum(start, end, q):
    total = sum(range(start, end + 1))
    q.put(total)
    
if __name__=='__main__':
    start_time = time.time()
    
    # 멀티프로세싱 queue 생성
    q = multiprocessing.Queue()
    
    # 두 개의 프로세스 생성
    process1 = multiprocessing.Process(target=calculate_sum, args=(1,50000000,q))
    process2 = multiprocessing.Process(target=calculate_sum, args=(50000001, 100000000,q))
    
    # 프로세스 시작
    process1.start()
    process2.start()
    
    # 프로세스 종료 대기
    process1.join()
    process2.join()
    
    # 결과값 저장
    sum1 = q.get()
    sum2 = q.get()
    
    # 결과값 통합
    total = sum1 + sum2
    
    # 코드 종료 시간 check
    end_time = time.time()
    
    # 코드 실행시간 
    codetime = end_time - start_time
    # 결과값과 코드 실행 시간 출력
    print('1부터 1억까지의 합 : {}'.format(total))
    print('코드 실행 시간 : {}초'.format(codetime))
    
    # Thread를 사용하는 것보다 좀 더 빠르다

