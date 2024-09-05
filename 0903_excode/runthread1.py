import time

start_time = time.time()

sum_of_numbers = sum(range(1,100000001))

end_time = time.time()

print(f"1부터 100000000까지의 합: {sum_of_numbers}")
print(f"실행 시간: {end_time - start_time} 초")