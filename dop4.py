import subprocess
import time

def run_script(script_name):
    start_time = time.time()
    try:
        subprocess.run(['python3', script_name], check=True, capture_output=True)
        end_time = time.time()
        return end_time - start_time  # Возвращаем время выполнения
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении {script_name}: {e}")
        print(e.stderr)
        return None


number_of_executions = 100
script_name_1 = "must_have_task.py"
script_name_2 = "dop2.py"
script_name_3 = "dop1.py"

script1_time = 0
script2_time = 0
script3_time = 0
for x in range(number_of_executions):
    script1_time += run_script(script_name_1)
    script2_time += run_script(script_name_2)
    script3_time += run_script(script_name_3)

print("Конвертация json2yaml")
print(f"Количество запусков {number_of_executions}")
if script1_time is not None:
    print(f"Время выполнения {script_name_1} (своими силами): \n{script1_time:.4f} секунд")
if script2_time is not None:
    print(f"Время выполнения {script_name_2} (своими силами, но еще с regex): \n{script2_time:.4f} секунд")
if script3_time is not None:
    print(f"Время выполнения {script_name_3} (встроенные библиотеки): \n{script3_time:.4f} секунд")