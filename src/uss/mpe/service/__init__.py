from src.uss.mpe.service.bmi import Bmi
from src.uss.mpe.service.contacts import Contacts
from src.uss.mpe.service.grade import Grade
from src.uss.mpe.service.person import Person
from src.cmm.service.common import Common

ls = []
while True:
    menu = Common.menu(["종료", "BMI", "주소록", "성적", "개인정보"])
    if menu == '0':
        print("프로그램을 종료합니다.")
        break
    elif menu == '1':
        submenu = Common.menu(["종료", "BMI 등록", "BMI 출력", "BMI 삭제"])
        if submenu == '0':
            print("프로그램을 종료합니다")
            break
        elif submenu == '1':
            data = Bmi.get_data()
            ls.append(data)
        elif submenu == '2':
            Bmi.print_info(ls)
        elif submenu == '3':
            Bmi.del_bmi(ls, input("이름 : "))
        else:
            print("다시 입력 해 주세요.")
    elif menu == '2':
        submenu = Common.menu(["종료", "주소록 등록", "주소록 출력", "주소록 삭제"])
        if submenu == '0':
            print("작업을 종료합니다.")
            break
        elif submenu == '1':
            ls.append(Contacts.get_data())
        elif submenu == '2':
            Contacts.print_info(ls)
        elif submenu == '3':
            Contacts.del_contacts(ls, input("이름 : "))
        else:
            print("다시 입력 해 주세요.")
    elif menu == '3':
        submenu = Common.menu(["종료", "성적 등록", "성적 출력", "성적 삭제"])
        if submenu == '0':
            print("작업을 종료합니다.")
            break
        elif submenu == '1':
            ls.append(Grade.get_data())
        elif submenu == '2':
            Grade.print_grade(ls)
        elif submenu == '3':
            Grade.del_grade(ls, input("이름 : "))
        else:
            print("다시 입력 해 주세요.")
    elif menu == '4':
        submenu = Common.menu(["종료", "개인정보 등록", "개인정보 출력", "개인정보 삭제"])
        if submenu == '0':
            print("프로그램을 종료합니다.")
            break
        elif submenu == '1':
            ls.append(Person.get_data())
        elif submenu == '2':
            Person.print_info(ls)
        elif submenu == '3':
            Person.del_person(ls, input("삭제할 사람 : "))
        else:
            print("다시 입력 해 주세요.")
    else:
        print("다시 입력 해 주세요.")
