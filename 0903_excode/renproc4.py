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

    # 프로세스 개수 설정
    num_processes = 4

    # 프로세스 생성 및 시작
    processes = []
    for i in range(num_processes):
        start = i * (100000000 // num_processes) + 1
        end = (i + 1) * (100000000 // num_processes)
        process = multiprocessing.Process(target=calculate_sum, args=(start, end, queue))
        processes.append(process)
        process.start()

    # 모든 프로세스 종료 대기
    for process in processes:
        process.join()

    # Queue에서 결과 가져와서 합산
    total_sum = 0
    while not queue.empty():
        total_sum += queue.get()

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"1부터 1억까지의 합: {total_sum}")
    print(f"실행 시간: {execution_time}초")