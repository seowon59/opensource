import os
import json

FILE_NAME = "todo_data.json"

def load_task_list():
    if os.path.isfile(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_task_list(task_list):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(task_list, f, ensure_ascii=False, indent=2)

def print_tasks(task_list):
    print("\n현재 등록된 할 일들")
    if not task_list:
        print(" - 아직 아무것도 없음.")
    else:
        for idx, item in enumerate(task_list):
            state = "완료" if item["done"] else "진행 중"
            print(f"{idx + 1}. [{state}] {item['title']}")
    print()

def add_new_task(task_list):
    task_name = input("새 할 일 입력: ").strip()
    if task_name:
        task_list.append({"title": task_name, "done": False})
        print(" - 추가 완료")

def mark_task_done(task_list):
    print_tasks(task_list)
    try:
        sel = int(input("완료한 항목 번호: ")) - 1
        if 0 <= sel < len(task_list):
            task_list[sel]["done"] = True
            print(" - 완료로 표시함.")
        else:
            print(" - 유효한 번호가 아님.")
    except ValueError:
        print(" - 숫자를 입력해야 함.")

def delete_task(task_list):
    print_tasks(task_list)
    try:
        sel = int(input("삭제할 항목 번호: ")) - 1
        if 0 <= sel < len(task_list):
            deleted = task_list.pop(sel)
            print(f" - '{deleted['title']}' 삭제 완료.")
        else:
            print(" - 번호가 잘못되었음.")
    except ValueError:
        print(" - 숫자로 입력해야 함.")

def run_task_manager():
    tasks = load_task_list()

    while True:
        print("\n===== 할 일 관리 프로그램 =====")
        print("1. 할 일 목록 보기")
        print("2. 할 일 추가")
        print("3. 완료 체크")
        print("4. 항목 삭제")
        print("5. 저장 후 종료")

        user_input = input("번호를 선택하세요 ")

        if user_input == "1":
            print_tasks(tasks)
        elif user_input == "2":
            add_new_task(tasks)
        elif user_input == "3":
            mark_task_done(tasks)
        elif user_input == "4":
            delete_task(tasks)
        elif user_input == "5":
            save_task_list(tasks)
            print("저장되었음.")
            break
        else:
            print(" - 1부터 5까지 중에서 선택해야함.")

if __name__ == "__main__":
    run_task_manager()

