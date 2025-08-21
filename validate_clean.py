def clean_data(data):
    data = data.strip()
    return data


def validate_domain(email_address):
    domains = ['.org', '.com', '.scot', '.co.uk']

    for domain in domains:
        if domain in email_address:
            return True
    return False

def check_student(student,cohort):
    check = False
    #print("student = ", student)
    for item in cohort:
      if ( item.Moodle_Email == student.Moodle_Email 
        #and item.full_name.upper() == student.full_name.upper() 
        and item.postcode == student.postcode ):
        check = True
        break
    #print("check = ", check)
    return check

def remove_duplicates(valid):
    seen = []
    duplicates = []
    non_duplicates = []

    #print("valid:", valid)

    i = 1
    for sub in valid:
      if i == 1:
        seen.append(sub)
        non_duplicates.append(sub)
        #print("\n")
        #print(i)
        #print("non_duplicates = ", non_duplicates)
        #print("duplicates = ", duplicates)
        #print("seen = ", seen)
        i = i + 1
      else:
        dup = True
        #print("\n")
        #print(i)
        #print("sub = ", sub)
        for item in seen:
          #print("seen item = ", item)
          if ( sub.Moodle_Email == item.Moodle_Email
            and item.full_name.upper() in sub.full_name.upper()
            and sub.postcode == item.postcode ):
            #non_duplicates.remove(item)
            duplicates.append(sub)
            duplicates.append(item)
            #seen.remove(item)
            dup = False
            break
          i = i + 1

        if dup:
          non_duplicates.append(sub)
          seen.append(sub)

    #print("\n")
    #print("non_duplicates = ", non_duplicates)
    #print("duplicates = ", duplicates)

    return non_duplicates

