import multiprocessing
import time

def calculate_sum(start, end, queue):
    """주어진 범위의 숫자 합을 계산하여 Queue에 저장하는 함수"""
    local_sum = 0
    for i in range(start, end + 1):
        local_sum += i
    queue.put(local_sum)

if __name__ == '__main__':
    start_time = time.time()

    # 멀티프로세싱 Queue 생성
    queue = multiprocessing.Queue()

    # 두 개의 프로세스 생성
    process1 = multiprocessing.Process(target=calculate_sum, args=(1, 50000000, queue))
    process2 = multiprocessing.Process(target=calculate_sum, args=(50000001, 100000000, queue))

    # 프로세스 시작
    process1.start()
    process2.start()

    # 프로세스 종료 대기
    process1.join()
    process2.join()

    # Queue에서 결과 가져오기
    sum1 = queue.get()
    sum2 = queue.get()

    # 두 프로세스의 결과 합산
    total_sum = sum1 + sum2

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"1부터 1억까지의 합: {total_sum}")
    print(f"실행 시간: {execution_time}초")