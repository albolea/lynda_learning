from string import Template


def main():
    templ = Template("You are watching ${title} by ${author}")
    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)

    data = {
        "author": "Joe Marini",
        "title": "Advanced Python"
    }
    print(templ.substitute(data))


if __name__ == '__main__':
    main()
