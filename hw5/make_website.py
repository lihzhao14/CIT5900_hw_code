import string

def read_from_file(file_name):
    """
    reads the file and stores it in memory as a list of lines
    """
    with open(file_name, 'r') as fin:
        # reads all lines in the file as a list
        contents = fin.readlines()
    return contents


def detect_name(contents):
    """
    Detect and return the name by extracting the first line.
    """
    name = contents[0]
    name = name.strip()
    if len(name) > 0:
        first_letter = name[0]
    else:
        return "Invalid Name"
    # if the first letter is the upper case
    if first_letter in string.ascii_letters.upper():
        return name
    else:
        return "Invalid Name"


def detect_email(contents):
    """
    Detect and return the email address by looking for a line that has the ‘@’ character.
    """
    # detect @ in all lines
    for line in contents:
        line = line.strip()
        if "@" in line:
            if line[-4:] != ".com" or ".edu":
                index = line.index("@")
                # if the letter after "@" is lower case
                if line[index + 1] in string.ascii_letters.lower():
                    for i in range(len(line)):
                        if line[i].isnumeric() or line[i].isdigit():
                            return ""
                    return line
    return ""


def detect_course(contents):
    """
    Detect and return the courses as a list by looking for the word “Courses” in the list and then extract the line
    that contains that word.
    """
    courses_list = ""
    # Extract the line that contains "Course"
    for line in contents:
        if "Course" in line:
            courses_list = line.strip()
            break

    start_index = len("Courses")
    if courses_list:
        # any random punctuation after the word “Courses” and before the first actual course needs to be ignored
        while courses_list[start_index] not in string.ascii_letters:
            start_index += 1
        courses_list = courses_list[start_index:]
        split_courses = courses_list.split(",")
        split_courses = [s.strip() for s in split_courses]
        return split_courses
    else:
        return ""

def detect_projects(contents):
    """
    Detect and return the projects as a list by looking for the word “Projects” in the list.
    """
    projects_list = []
    for line in contents:
        if "Projects" in line:
            index = contents.index(line)
            return index
        elif
    for line in



def surround_block(tag, text):
    """
    Surrounds the given text with the given html tag and returns the string.
    """

    # insert code
    pass


def create_email_link(email_address):
    """
    Creates an email link with the given email_address.
    To cut down on spammers harvesting the email address from the webpage,
    displays the email address with [aT] instead of @.

    Example: Given the email address: lbrandon@wharton.upenn.edu
    Generates the email link: <a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>

    Note: If, for some reason the email address does not contain @,
    use the email address as is and don't replace anything.
    """

    # insert code
    pass


def generate_html(txt_input_file, html_output_file):
    """
    Loads given txt_input_file,
    gets the name, email address, list of projects, and list of courses,
    then writes the info to the given html_output_file.

    # Hint(s):
    # call function(s) to load given txt_input_file
    # call function(s) to get name
    # call function(s) to get email address
    # call function(s) to get list of projects
    # call function(s) to get list of courses
    # call function(s) to write the name, email address, list of projects, and list of courses to the given html_output_file
    """

    # insert code
    pass


def main():
    # DO NOT REMOVE OR UPDATE THIS CODE
    # generate resume.html file from provided sample resume.txt
    generate_html('resume.txt', 'resume.html')
    contents = read_from_file("resume.txt")
    detect_name(contents)
    # DO NOT REMOVE OR UPDATE THIS CODE.
    # Uncomment each call to the generate_html function when you’re ready
    # to test how your program handles each additional test resume.txt file
    # generate_html('TestResumes/resume_bad_name_lowercase/resume.txt', 'TestResumes/resume_bad_name_lowercase/resume.html')
    # generate_html('TestResumes/resume_courses_w_whitespace/resume.txt', 'TestResumes/resume_courses_w_whitespace/resume.html')
    # generate_html('TestResumes/resume_courses_weird_punc/resume.txt', 'TestResumes/resume_courses_weird_punc/resume.html')
    # generate_html('TestResumes/resume_projects_w_whitespace/resume.txt', 'TestResumes/resume_projects_w_whitespace/resume.html')
    # generate_html('TestResumes/resume_projects_with_blanks/resume.txt', 'TestResumes/resume_projects_with_blanks/resume.html')
    # generate_html('TestResumes/resume_template_email_w_whitespace/resume.txt', 'TestResumes/resume_template_email_w_whitespace/resume.html')
    # generate_html('TestResumes/resume_wrong_email/resume.txt', 'TestResumes/resume_wrong_email/resume.html')

    # If you want to test additional resume files, call the generate_html function with the given .txt file
    # and desired name of output .html file


if __name__ == '__main__':
    main()
