def create_time_checker(max_time):
    def check_time(actual_time):
        if actual_time > max_time:
            print(f"Превышен лимит: {actual_time} > {max_time}")
            return False
        else:
            print(f"В пределах лимита: {actual_time} <= {max_time}")
            return True
    return check_time

check_fast = create_time_checker(1.5)
check_slow = create_time_checker(3.0)

check_fast(1.2)
check_fast(2.0)

check_slow(2.5)
check_slow(4.0)