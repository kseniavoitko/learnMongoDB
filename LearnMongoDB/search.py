import connect
from models import Authors, Qoutes


def print_result(qoutes):
    for qoute in qoutes:
        print(qoute.to_mongo().to_dict())


if __name__ == "__main__":
    while True:
        comand = input("Give me comand field:value\n")

        try:
            field, value = comand.split(":")
        except ValueError:
            field = comand

        if field == "name":
            authors = Authors.objects(fullname=value)
            qoutes = Qoutes.objects(author__in=authors)
        elif field == "tag":
            qoutes = Qoutes.objects(tags=value)
        elif field == "tags":
            qoutes = Qoutes.objects(tags__in=value.split(","))
        elif field == "exit":
            break
        else:
            print('Wrong comand!')

        print_result(qoutes)
